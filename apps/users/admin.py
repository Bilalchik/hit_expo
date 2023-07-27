from django.contrib import admin

from .models import Participant, UserSMI, Expert, Visitor, GosUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',) 

admin.site.register(Participant)
admin.site.register(UserSMI)
admin.site.register(Expert)
admin.site.register(Visitor)
admin.site.register(GosUser)