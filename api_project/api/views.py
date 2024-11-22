from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all() 
    serializer_class = BookSerializer  

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 

    def get_permissions(self):
        # Custom permission logic
        if self.action == 'destroy':
            self.permission_classes = [IsAdminUser]  
        return super().get_permissions()
