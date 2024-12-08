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
 
    
    path('post/new/', views.create_post, name='create_post'),  # For creating a new post
    path('post/<int:pk>/update/', views.update_post, name='update_post'),  # For updating an existing post
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),  # For deleting a post

]

urlpatterns = [
    path("search/", views.search, name="search"),
    path("tags/<str:tag_name>/", views.posts_by_tag, name="posts_by_tag"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
]

urlpatterns = [
    # URL for viewing all posts
    path('posts/', views.PostListView.as_view(), name='post_list'),

    # URL for viewing a single post's details, including comments
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # URL for creating a new post
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),

    # URL for editing a post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),

    # URL for deleting a post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # URL for creating a comment on a post
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),

    # URL for updating a comment
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),

    # URL for deleting a comment
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    # URL for searching posts
    path('search/', views.search, name='search'),

    # URL for viewing posts by a specific tag
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
]

