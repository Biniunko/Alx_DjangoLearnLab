from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    # Using Book.objects.all() to fetch all book entries
    books = Book.objects.all()
    # Rendering the template 'relationship_app/list_books.html'
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Points to 'relationship_app/library_detail.html'
    context_object_name = 'library'  # The name used in the template context
