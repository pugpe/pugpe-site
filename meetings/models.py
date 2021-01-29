from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import TimeStampedModel

from .event_helpers import check_required_fields_for_a_valid_event


class Meeting(TimeStampedModel):

    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), blank=True)
    start_date = models.DateTimeField(_("start date"), null=True)
    end_date = models.DateTimeField(_("end date"), null=True)
    is_online = models.BooleanField(_("is online"), blank=True, default=False)
    is_draft = models.BooleanField(_("is draft"), blank=True, default=True)

    def __str__(self):
        return self.title

    def publish(self):
        check_required_fields_for_a_valid_event(self)
        self.is_draft = False
        self.save()


class MeetingEvent(TimeStampedModel):
    class TypeChoices(models.TextChoices):
        TALK = "TALK", _("talk")
        LIGHTNING_TALK = "lightning_talk", _("lightning_talk")
        DOJO = "DOJO", _("dojo")
        PYPUDINHOS = "PYPUDINHOS", _("pypudinhos")
        INTERVAL = "INTERVAL", _("interval")

    meeting = models.ForeignKey(
        "meetings.Meeting",
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name=_("meeting"),
    )
    title = models.CharField(_("title"), max_length=255, blank=True)
    description = models.TextField(blank=True)
    typee = models.CharField(_("type"), max_length=20, choices=TypeChoices.choices)
    hosts = models.ManyToManyField(
        "profiles.Profile",
        related_name="events",
        verbose_name=_("hosts"),
        blank=True,
    )
    starts_at = models.DateTimeField(_("starts at"))
    ends_at = models.DateTimeField(_("ends at"))

    def __str__(self):
        meeting = str(self.meeting)
        return self.title + " - " + meeting
