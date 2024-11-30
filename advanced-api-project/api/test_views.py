from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    """Test suite for Book model API endpoints."""
    
    def setUp(self):
        """Set up test data."""
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )
        self.client = APIClient()
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_list_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('1984', str(response.data))

    def test_retrieve_book_detail(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    def test_create_book(self):
        """Test creating a new book."""
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Test updating an existing book."""
        data = {
            'title': 'Nineteen Eighty-Four',
            'publication_year': 1949,
            'author': self.author.id
        }
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Nineteen Eighty-Four')

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        """Test filtering books by author name."""
        response = self.cli
     def test_test_database_is_used(self):
        """Verify that tests use a separate database."""
        # The database should start empty except for objects created in setUp
        self.assertEqual(User.objects.count(), 1)  # Only test user exists
        self.assertEqual(Book.objects.count(), 1)  # Only one book exists
