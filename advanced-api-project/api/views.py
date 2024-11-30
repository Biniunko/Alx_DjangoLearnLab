from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Accessible by unauthenticated users.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Open access


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    Accessible by unauthenticated users.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Open access


class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated access only


class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update an existing book.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated access only


class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated access only


class BookListView(generics.ListAPIView):
    """
    Retrieves a list of books with filtering, searching, and ordering capabilities.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filtering options
    filterset_fields = ["title", "author__name", "publication_year"]

    # Search options
    search_fields = ["title", "author__name"]

    # Ordering options
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]  # Default ordering
