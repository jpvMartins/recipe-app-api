"""
Tests for the Django admin interface.
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client


class AdminSiteTests(TestCase):
    """
    Tests for the Django admin interface.
    """

    def setUp(self):
        """
        Create user and client for testing.
        """
        self.client = Client()  # Allow the client to make requests
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='password123',
            name='Test User'
        )

    def test_users_list(self):
        """
        Test that the users list page is accessible and displays users.
        """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """
        Test that the edit user page works.
        """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """
        Test that the create user page works.
        """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
