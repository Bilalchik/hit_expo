from django.contrib import admin

from .models import Participant, UserSMI, Expert, Visitor, GosUser


admin.site.register(Participant)
admin.site.register(UserSMI)
admin.site.register(Expert)
admin.site.register(Visitor)
admin.site.register(GosUser)