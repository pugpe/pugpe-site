from datetime import datetime

from django.forms import ValidationError
from django.test import TestCase

from common.models import TimeStampedModel

from ..models import Event


class EventModelTest(TestCase):
    def test_can_create_a_event(self):
        event_data = {
            "title": "67º Encontro do PUG-PE",
            "description": "PugPE",
            "date": datetime.now(),
            "is_online": True,
            "is_draft": True,
        }
        Event.objects.create(**event_data)

        self.assertTrue(Event.objects.exists())

    def test_if_a_event_is_time_stamped(self):
        """Should raises KeyError if `created_at` and `updated_at` not in `fields`."""
        Event._meta.get_field("created_at")
        Event._meta.get_field("updated_at")

        self.assertTrue(issubclass(Event, TimeStampedModel))

    def test_can_create_a_event_without_not_required_fields(self):
        event_data = {"title": "67º Encontro do PUG-PE"}
        Event.objects.create(**event_data)

        self.assertTrue(Event.objects.exists())

    def test_publish_a_valid_event(self):
        event_data = {
            "title": "67º Encontro do PUG-PE",
            "description": "PugPE",
            "date": datetime.now(),
            "is_online": True,
            "is_draft": True,
        }
        event = Event.objects.create(**event_data)
        event.publish()
        event.refresh_from_db()
        self.assertFalse(event.is_draft)

    def test_publish_a_event_without_str_field(self):
        event_data = {
            "title": "",
            "description": "PugPE",
            "date": datetime.now(),
            "is_online": True,
            "is_draft": True,
        }
        event = Event.objects.create(**event_data)

        with self.assertRaises(ValidationError):
            event.publish()

        event.refresh_from_db()
        self.assertTrue(event.is_draft)

    def test_publish_a_event_without_date_field(self):
        event_data = {
            "title": "67º Encontro do PUG-PE",
            "description": "PugPE",
            "date": None,
            "is_online": True,
            "is_draft": True,
        }
        event = Event.objects.create(**event_data)

        with self.assertRaises(ValidationError):
            event.publish()

        event.refresh_from_db()
        self.assertTrue(event.is_draft)
