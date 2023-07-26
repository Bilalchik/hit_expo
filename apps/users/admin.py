from django.contrib import admin

from .models import User, UserSMI, Expert, Visitor, GosUser


admin.site.register(User)
admin.site.register(UserSMI)
admin.site.register(Expert)
admin.site.register(Visitor)
admin.site.register(GosUser)