from datetime import datetime

from django.forms import ValidationError
from django.test import TestCase

from common.models import TimeStampedModel

from ..models import Meeting


class MeetingModelTest(TestCase):
    def test_can_create_a_meeting(self):
        meeting_data = {
            "title": "67º Encontro do PUG-PE",
            "description": "PugPE",
            "date": datetime.now(),
            "is_online": True,
            "is_draft": True,
        }
        Meeting.objects.create(**meeting_data)

        self.assertTrue(Meeting.objects.exists())

    def test_if_a_meeting_is_time_stamped(self):
        """Should raises KeyError if `created_at` and `updated_at` not in `fields`."""
        Meeting._meta.get_field("created_at")
        Meeting._meta.get_field("updated_at")

        self.assertTrue(issubclass(Meeting, TimeStampedModel))

    def test_can_create_a_meeting_without_not_required_fields(self):
        meeting_data = {"title": "67º Encontro do PUG-PE"}
        Meeting.objects.create(**meeting_data)

        self.assertTrue(Meeting.objects.exists())

    def test_publish_a_valid_meeting(self):
        meeting_data = {
            "title": "67º Encontro do PUG-PE",
            "description": "PugPE",
            "date": datetime.now(),
            "is_online": True,
            "is_draft": True,
        }
        meeting = Meeting.objects.create(**meeting_data)
        meeting.publish()
        meeting.refresh_from_db()
        self.assertFalse(meeting.is_draft)

    def test_publish_a_meeting_without_str_field(self):
        meeting_data = {
            "title": "",
            "description": "PugPE",
            "date": datetime.now(),
            "is_online": True,
            "is_draft": True,
        }
        meeting = Meeting.objects.create(**meeting_data)

        with self.assertRaises(ValidationError):
            meeting.publish()

        meeting.refresh_from_db()
        self.assertTrue(meeting.is_draft)

    def test_publish_a_meeting_without_date_field(self):
        meeting_data = {
            "title": "67º Encontro do PUG-PE",
            "description": "PugPE",
            "date": None,
            "is_online": True,
            "is_draft": True,
        }
        meeting = Meeting.objects.create(**meeting_data)

        with self.assertRaises(ValidationError):
            meeting.publish()

        meeting.refresh_from_db()
        self.assertTrue(meeting.is_draft)
