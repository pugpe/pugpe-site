from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from model_bakery import baker

from common.models import TimeStampedModel

from ..models import MeetingEvent


class MeetingEventModelTest(TestCase):
    def setUp(self):
        self.meeting_event_data = {
            "meeting": baker.make("meetings.Meeting", title="34º Encontro PUGPE"),
            "title": "Talk sobre python",
            "description": "Vamos falar sobre python.",
            "typee": "talk",
            "starts_at": timezone.now(),
            "ends_at": timezone.now() + timedelta(hours=1),
        }

    def test_can_create_a_meeting_event(self):
        meeting_event = MeetingEvent.objects.create(**self.meeting_event_data)
        meeting_event.hosts.set(baker.make("profiles.Profile", _quantity=5))

        self.assertTrue(MeetingEvent.objects.exists())

    def test_if_a_meeting_is_time_stamped(self):
        """Should raises KeyError if `created_at` and `updated_at` not in `fields`."""
        MeetingEvent._meta.get_field("created_at")
        MeetingEvent._meta.get_field("updated_at")

        self.assertTrue(issubclass(MeetingEvent, TimeStampedModel))

    def test_meeting_related_name(self):
        meeting_event = MeetingEvent.objects.create(**self.meeting_event_data)
        meeting_event.hosts.set(baker.make("profiles.Profile", _quantity=1))

        meeting = self.meeting_event_data["meeting"]

        self.assertEqual(meeting_event, meeting.events.first())

    def test_hosts_related_name(self):
        meeting_event = MeetingEvent.objects.create(**self.meeting_event_data)
        host = baker.make("profiles.Profile")
        meeting_event.hosts.add(host)

        self.assertEqual(meeting_event, host.events.first())

    def test_str(self):
        meeting_event = MeetingEvent.objects.create(**self.meeting_event_data)
        meeting_event.hosts.set(baker.make("profiles.Profile", _quantity=5))

        self.assertEqual("Talk sobre python - 34º Encontro PUGPE", str(meeting_event))
