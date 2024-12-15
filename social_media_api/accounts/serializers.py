from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.bio = validated_data.get('bio', '')
        user.profile_picture = validated_data.get('profile_picture', None)
        user.save()
        return user
class MySerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

