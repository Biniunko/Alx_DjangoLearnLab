# Delete the book instance in python code
from bookshelf.models import Book
book.delete()

# Confirm deletion
all_books = Book.objects.all()
print(list(all_books))

# delete.md

# Command:
book.delete()

# Confirm deletion
all_books = Book.objects.all()
print(list(all_books))

# Expected Output:
[]
