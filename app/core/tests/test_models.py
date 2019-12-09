from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='me@jc.com', password='1234567890'):
    """Create a simple user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_creat_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "MohammadAliMalekie@gmail.com"
        password = "passis!@#"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password)

    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = 'test@JOHHNYWCAGE.COM'
        password = 'passis!@#'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123!@#qwe')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@john.com',
            password='123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""

        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
