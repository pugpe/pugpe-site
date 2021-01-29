from django.test import TestCase

from ..models import User


class UserModelTestCase(TestCase):
    def test_if_can_add_a_email_based_user(self):
        user = User(email="my_email@email.com")
        user.set_password("my_password")
        user.save()

        self.assertTrue(User.objects.exists())
