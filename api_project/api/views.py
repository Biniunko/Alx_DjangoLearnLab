from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetch all book entries from the database
    serializer_class = BookSerializer  # Use the BookSerializer to convert model data into JSON

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Get all book records
    serializer_class = BookSerializer  # Use the BookSerializer for serialization
