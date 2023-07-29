from django.contrib import admin

from apps.b2b_meeting.models import Meeting


class MeetingAdmin(admin.ModelAdmin):
    list_display = ['inviter', 'invited', 'start', 'end', 'status', 'answer']
    list_filter = ('start', 'end', 'status', 'answer')


admin.site.register(Meeting, MeetingAdmin)
