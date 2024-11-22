from django.urls import path
from .views import BookList
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("books/", BookList.as_view(), name="book-list"),  # Maps to the BookList view
]
# Create the router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Include the router's URL patterns
    path('', include(router.urls)),  # Automatically includes all CRUD routes
]


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Token retrieval endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Include the router's URL patterns
    path('', include(router.urls)),  # Automatically includes all CRUD routes for books
]
