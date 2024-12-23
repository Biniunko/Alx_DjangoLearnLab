from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # Function-based view
    path(
        "library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"
    ),  # Class-based view
]
# urls.py


urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
]


urlpatterns = [
    path("admin/", views.admin_view, name="admin_view"),
    path("librarian/", views.librarian_view, name="librarian_view"),
    path("member/", views.member_view, name="member_view"),
]


urlpatterns = [
    path('add/', views.add_book, name='add_book/'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book/'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # Function-based view
    path(
        "library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"
    ),  # Class-based view
]

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
