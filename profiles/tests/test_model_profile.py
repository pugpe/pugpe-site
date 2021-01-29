from django.contrib.auth import get_user_model
from django.test import TestCase

from model_bakery import baker

from common.models import TimeStampedModel

from ..models import Profile


User = get_user_model()


class ProfileModelTest(TestCase):
    def test_can_create_a_profile(self):
        profile_data = {
            "user": baker.make(User),
            "full_name": "Meu Nome Completo",
            "about_me": "Minha mini bio",
            "telegram_user": "marcusgabrields",
        }
        Profile.objects.create(**profile_data)

        self.assertTrue(Profile.objects.exists())

    def test_if_a_profile_is_time_stamped(self):
        """Should raises KeyError if `created_at` and `updated_at` not in `fields`."""
        Profile._meta.get_field("created_at")
        Profile._meta.get_field("updated_at")

        self.assertTrue(issubclass(Profile, TimeStampedModel))

    def test_can_create_a_profile_without_optional_fields(self):
        profile_data = {
            "user": baker.make(User),
            "full_name": "Meu Nome Completo",
        }
        Profile.objects.create(**profile_data)

        self.assertTrue(Profile.objects.exists())

    def test_profile_str_with_multiple_names(self):
        profile_data = {
            "user": baker.make(User),
            "full_name": "Meu Nome Completo",
        }
        profile = Profile.objects.create(**profile_data)

        expected_result = "Meu Completo" + " - " + profile.user.email
        self.assertEqual(expected_result, str(profile))

    def test_profile_str_with_two_names(self):
        profile_data = {
            "user": baker.make(User),
            "full_name": "Meu Completo",
        }
        profile = Profile.objects.create(**profile_data)

        expected_result = "Meu Completo" + " - " + profile.user.email
        self.assertEqual(expected_result, str(profile))

    def test_profile_str_with_one_name(self):
        profile_data = {
            "user": baker.make(User),
            "full_name": "Meu",
        }
        profile = Profile.objects.create(**profile_data)

        expected_result = "Meu" + " - " + profile.user.email
        self.assertEqual(expected_result, str(profile))

    def test_profile_str_without_full_name(self):
        user = baker.make(User)
        profile_data = {
            "user": user,
        }
        profile = Profile.objects.create(**profile_data)

        self.assertEqual(user.email, str(profile))
