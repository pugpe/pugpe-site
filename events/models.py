from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import TimeStampedModel

from .event_helpers import check_required_fields_for_a_valid_event


class Event(TimeStampedModel):

    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), blank=True)
    date = models.DateField(_("date"), null=True)
    is_online = models.BooleanField(_("is online"), blank=True, default=False)
    is_draft = models.BooleanField(_("is draft"), blank=True, default=True)

    def __str__(self):
        return self.title

    def publish(self):
        check_required_fields_for_a_valid_event(self)
        self.is_draft = False
        self.save()
