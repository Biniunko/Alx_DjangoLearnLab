from django.shortcuts import render
from .forms import ExampleForm
# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        # Logic to create a book
        pass
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # Logic to edit a book
        pass
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        # Redirect after deletion
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
from .forms import SearchForm


def search_books(request):
    """
    View for searching books safely.
    """
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            # Using ORM to prevent SQL injection
            books = Book.objects.filter(title__icontains=query)
            return render(request, "bookshelf/book_list.html", {"books": books})
    else:
        form = SearchForm()
    return render(request, "bookshelf/book_list.html", {"form": form})
