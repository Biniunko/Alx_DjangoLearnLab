# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Tag, Comment
from django.db.models import Q
from django.http import Http404


# User Registration View
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})


# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect("profile")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})


# User Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")


# User Profile View
@login_required
def profile(request):
    if request.method == "POST":
        user = request.user
        email = request.POST.get("email")
        user.email = email
        user.save()
        messages.success(request, "Profile updated successfully.")
    return render(request, "blog/profile.html")

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list_by_tag.html'  # Template for rendering posts by tag
    context_object_name = 'posts'
    
    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')  # Get tag slug from URL
        tag = get_object_or_404(Tag, slug=tag_slug)  # Fetch the tag by slug
        return Post.objects.filter(tags=tag)
# List view to display all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


# Detail view to display a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


# Create view to create a new post (only for authenticated users)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content", "tags"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        # Handle tag creation if they are not in the database
        tags = form.cleaned_data["tags"]
        for tag in tags:
            if not Tag.objects.filter(name=tag).exists():
                Tag.objects.create(name=tag)

        return response


# Update view to edit a post (only the author can edit)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can edit

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.pk})


# Delete view to delete a post (only the author can delete)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can delete


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=post.pk)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "comment_form": comment_form},
    )


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        raise Http404

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/edit_comment.html", {"form": form})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        raise Http404

    if request.method == "POST":
        comment.delete()
        return redirect("post_detail", pk=comment.post.pk)

    return render(request, "blog/delete_comment.html", {"comment": comment})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()

            # Handle tag creation if they are not in the database
            tags = form.cleaned_data["tags"]
            for tag in tags:
                if not Tag.objects.filter(name=tag).exists():
                    Tag.objects.create(name=tag)

            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})


def search(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()

    return render(request, "blog/search_results.html", {"posts": posts, "query": query})


def posts_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()
    return render(
        request, "blog/posts_by_tag.html", {"posts": posts, "tag_name": tag_name}
    )


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = (
        "blog/comment_form.html"  # This is a separate template for comment creation
    )

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])  # Post ID passed in URL
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["pk"]})


# Update view to edit a comment (only the author can edit)
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = (
        "blog/comment_form.html"  # Use the same form template as create view
    )

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only the author can edit

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.pk})


# Delete view to delete a comment (only the author can delete)
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = (
        "blog/comment_confirm_delete.html"  # A confirmation page for deleting comments
    )
    success_url = reverse_lazy("post_list")

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only the author can delete


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=post.pk)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "comment_form": comment_form},
    )


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        raise Http404

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/edit_comment.html", {"form": form})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.author:
        raise Http404

    if request.method == "POST":
        comment.delete()
        return redirect("post_detail", pk=comment.post.pk)

    return render(request, "blog/delete_comment.html", {"comment": comment})
