

"""
Testes for models.
"""
from decimal import Decimal


from django.test import TestCase   # base class for tests
from django.contrib.auth import get_user_model
# helper function : get the user model

from core import models

def create_user(email='user@example.com',password='test123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email,password)

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
            email=email,
            password=password,
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
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password='sample123'
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """
        Test creating user without email raises error.
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """
        Test creating a superuser.
        """
        user = get_user_model().objects.create_superuser(
            'test@exemple.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """
        Test creating a recipe is successful.
        """
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample Recipe',
            time_minutes=5,
            price=Decimal('5.50'),
            description='A simple recipe for testing.',
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating a teg is successful."""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Tag1')

        self.assertEqual(str(tag),tag.name)

    def test_create_Igredient(self):
        """Test creating an Igredient Successful."""
        user = create_user()
        ingredient = models.Ingredient.objects.create(user=user,name="Ingredient1")

        self.assertEqual(str(ingredient),'Ingredient1')