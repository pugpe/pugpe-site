from django.contrib import admin

from .models import Meeting, MeetingEvent


admin.site.register(Meeting)
admin.site.register(MeetingEvent)
