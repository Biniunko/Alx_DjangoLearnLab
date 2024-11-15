from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name).first()
    if author:
        return Book.objects.filter(author=author)
    return None

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name).first()
    if library:
        return library.books.all()
    return None

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name).first()
    if library:
        return library.librarian
    return None
