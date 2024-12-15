from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.decorators import action


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.create_user(
                username=serializer.validated_data["username"],
                email=serializer.validated_data["email"],
                password=request.data["password"],
            )
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class FollowUnfollowView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk=None, action_type=None):
        try:
            target_user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if action_type == "follow":
            if target_user == request.user:
                return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
            if target_user in request.user.following.all():
                return Response({"error": "You are already following this user."}, status=status.HTTP_400_BAD_REQUEST)
            request.user.following.add(target_user)
            return Response({"status": "following"}, status=status.HTTP_200_OK)

        elif action_type == "unfollow":
            if target_user == request.user:
                return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
            if target_user not in request.user.following.all():
                return Response({"error": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)
            request.user.following.remove(target_user)
            return Response({"status": "unfollowing"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid action type."}, status=status.HTTP_400_BAD_REQUEST)
