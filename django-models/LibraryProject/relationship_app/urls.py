from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # Function-based view
    path(
        "library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"
    ),  # Class-based view
]
# urls.py

LogoutView.as_view(template_name=", "LoginView.as_view(template_name=
urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
]
