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
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to homepage after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# User Logout View
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')


from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

# Check if the user has the 'Admin' role
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user has the 'Librarian' role
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user has the 'Member' role
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view - accessible only by Admins
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian view - accessible only by Librarians
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member view - accessible only by Members
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
