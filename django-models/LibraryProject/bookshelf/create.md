from bookshelf.models import Book

# Create a new book instance in pyhton code
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
 
# create.md

# Command:
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Expected Output:
1984 by George Orwell (1949)
