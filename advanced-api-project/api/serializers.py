from rest_framework import serializers
from .models import Author, Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes the Book model. Includes custom validation for publication_year.
    """

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        """
        Ensure publication year is not in the future.
        """
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model. Includes a nested representation of related books.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
