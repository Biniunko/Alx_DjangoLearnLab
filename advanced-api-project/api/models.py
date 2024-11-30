from django.db import models

# Create your models here.


class Author(models.Model):
    """
    Represents an author entity with a name field.
    Each author can be linked to multiple books (one-to-many relationship).
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book entity with a title, publication year, and author.
    Links to an author using a foreign key.
    """

    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
