from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
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
    Lists all books with filtering, searching, and ordering capabilities.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define fields for filtering
    filterset_fields = ['author__name', 'publication_year']

    # Define fields for searching
    search_fields = ['title', 'author__name']

    # Define fields for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves details of a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
