from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class FollowUnfollowTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.user2 = User.objects.create_user(username="user2", password="password123")
        self.client.login(username="user1", password="password123")

    def test_follow_user(self):
        response = self.client.post(f'/follow/{self.user2.username}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user2, self.user1.following.all())

    def test_unfollow_user(self):
        self.user1.following.add(self.user2)
        response = self.client.post(f'/unfollow/{self.user2.username}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn(self.user2, self.user1.following.all())

    def test_follow_self(self):
        response = self.client.post(f'/follow/{self.user1.username}/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

