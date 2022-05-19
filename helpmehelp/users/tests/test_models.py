from django.test import TestCase

from helpmehelp.users.models import User
from helpmehelp.users.services import create_user


class UserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_user(
            username="moazsamy99",
            name="Moaz Samy",
            email="admin@example.com",
            password="difficult21",
            age="22",
            blood="O-",
            phone="01001001001",
            address="12 at example street",
            nat_ID="28703211203257",
        )

    def test_name_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("name").max_length
        self.assertEqual(max_length, 155)

    def test_user_get_absolute_url(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.get_absolute_url(), "/users/1/")

    def test_username(self):
        user = User.objects.get(id=1)
        expected_name = user.username
        self.assertEqual(str(user), expected_name)

    def test_is_verified_default_false(self):
        user = User.objects.get(id=1)
        self.assertFalse(user.is_verified)
