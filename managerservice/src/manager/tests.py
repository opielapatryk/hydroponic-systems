from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import System


class SystemViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")
        self.system = System.objects.create(
            name="Test System",
            system_type="NFT",
            capacity=100.0,
            owner_id=self.user.id,
        )
        self.token = self.get_token_for_user(self.user)

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_get_systems(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.get("/api/v1/system/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Test System")
