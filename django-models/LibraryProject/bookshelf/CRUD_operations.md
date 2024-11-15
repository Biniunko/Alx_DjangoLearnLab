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


# Retrieve the book instance in python code
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# retrieve.md

# Command:
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Expected Output:
1984 George Orwell 1949


# Update the book title in python code
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

# update.md

# Command:
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

# Expected Output:
Nineteen Eighty-Four



# Delete the book instance in python code
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
