from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book


class BookAPITests(APITestCase):
    """Test suite for Book model API endpoints."""

    def setUp(self):
        """Set up test data and authentication."""
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
        # Create an author and a book
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        # Create API client and login the test user
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")  # Login the user

        # Define URLs
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_authenticated_user_can_create_book(self):
        """Test authenticated user can create a new book."""
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_unauthenticated_user_cannot_create_book(self):
        """Test unauthenticated user cannot create a book."""
        self.client.logout()  # Logout the user
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_update_book(self):
        """Test authenticated user can update an existing book."""
        data = {
            'title': 'Nineteen Eighty-Four',
            'publication_year': 1949,
            'author': self.author.id
        }
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Nineteen Eighty-Four')

    def test_unauthenticated_user_cannot_update_book(self):
        """Test unauthenticated user cannot update a book."""
        self.client.logout()  # Logout the user
        data = {
            'title': 'Nineteen Eighty-Four',
            'publication_year': 1949,
            'author': self.author.id
        }
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
