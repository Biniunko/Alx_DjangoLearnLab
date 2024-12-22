from django.shortcuts import render
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework import generics  # Importing GenericAPIView

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

class UserViewSet(generics.GenericAPIView, viewsets.ReadOnlyModelViewSet):  # Adding GenericAPIView
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"], url_path="follow")
    def follow_user(self, request, pk=None):
        user_to_follow = self.get_object()
        request.user.following.add(user_to_follow)
        return Response({"status": "following"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], url_path="unfollow")
    def unfollow_user(self, request, pk=None):
        user_to_unfollow = self.get_object()
        request.user.following.remove(user_to_unfollow)
        return Response({"status": "unfollowing"}, status=status.HTTP_200_OK)
