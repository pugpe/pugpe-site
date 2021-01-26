from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import TimeStampedModel


class Profile(TimeStampedModel):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile",
        verbose_name=_("user"),
    )
    full_name = models.CharField(_("full name"), max_length=128, blank=False)
    about_me = models.TextField(_("about me"), blank=True)
    telegram_user = models.CharField(_("telegram user"), max_length=64, blank=True)

    def __str__(self):
        if not self.full_name:
            return self.user.email

        splitted_name = self.full_name.split(" ")

        if len(splitted_name) >= 2:
            first_name = splitted_name[0]
            last_name = splitted_name[-1]
            return first_name + " " + last_name

        first_name = splitted_name[0]
        return first_name
