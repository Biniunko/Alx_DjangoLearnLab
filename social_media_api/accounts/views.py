from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
@api_view(["POST"])
def register(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    return Response(
        {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return Response({'message': f'Now following {user_to_follow.username}'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({'message': f'Unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
# accounts/views.py



# Example: List of all users (CustomUser)
class UserListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request, *args, **kwargs):
        users = User.objects.all()  # Query all users (CustomUser)
        serializer = UserSerializer(users, many=True)  # Serialize the data
        return Response(serializer.data)  # Return the serialized data

class CustomUserListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()  # Query all CustomUser objects
        serializer = CustomUserSerializer(users, many=True)  # Serialize the data
        return Response(serializer.data)  # Return the serialized data
