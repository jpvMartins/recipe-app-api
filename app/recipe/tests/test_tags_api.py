"""
    Test for the tags API.
"""

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework import APIClient

from core.models import Tag

from recipe.serializers import TagSerializer

TAGS_URL =  reverse('recipe:tag-list')

def create_user(email='user@examplee.com',password='test123'):
    """Create and return a user with given parameters."""
    return get_user_model().objects.create_user(email=email,password=password)


class PublicTagsApiTests(TestCase):
    """Test unauthenticated API resquets."""

    def setUp(self):
        self.client = APIClient()

    def test_uth_required(self):
        """Test auth is required for retrieving tags."""

        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsAPITest(TestCase):
    """Test authenticated API resquests."""

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        Tag.objects.create(user=self.user,name="Vegan")
        Tag.objects.create(user=self.user,name="Dessert")

        res = self.client.get(TAGS_URL)

        tags= Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)

        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.data,serializer.data)

    def t