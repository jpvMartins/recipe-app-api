"""
Testes for models.
"""
from django.test import TestCase # base class for tests
from django.contrib.auth import get_user_model # helper function : get the user model


class ModelTests(TestCase):
    """
    Test cases for models.
    """

    def test_create_user_with_email_successful(self):
        """
        Test creating a user with email is successful.
        """
        email = "test@exemple.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalized.
        """
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TESTE3@EXAMPLE.COM', 'TESTE3@example.com'],
            ['test4@example.com', 'test4@example.com'],
        ]
        for email,expected in sample_emails:
            user = get_user_model().objects.create_user(email=email, password='sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """
        Test creating user without email raises error.
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','test123')