from django.urls import path
from . import views
from blog.views import (
    home,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # Authentication URLs
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    # Home URL
    path("", home, name="home"),  # Root path to home view
    # Blog Post URLs
    path("posts/", PostListView.as_view(), name="post-list"),  # List of all blog posts
    path(
        "posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"
    ),  # View individual post details
    path("posts/new/", PostCreateView.as_view(), name="post-create"),  # Create new post
    path(
        "posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"
    ),  # Edit existing post
    path(
        "posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"
    ),  # Delete a post
    # blog/urls.py

    path('post/new/', views.create_post, name='create_post'),  # For creating a new post
    path('post/<int:pk>/update/', views.update_post, name='update_post'),  # For updating an existing post
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),  # For deleting a post

]

urlpatterns = [
    path("comments/<int:pk>/edit/", views.edit_comment, name="edit_comment"),
    path("comments/<int:pk>/delete/", views.delete_comment, name="delete_comment"),
]

urlpatterns = [
    path("search/", views.search, name="search"),
    path("tags/<str:tag_name>/", views.posts_by_tag, name="posts_by_tag"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
]
