from django.contrib import admin

from .models import User, UserSMI, Expert, Visitor, GosUser, Participant


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',)
    search_fields = ('username', 'email', 'first_name', 'last_name')


admin.site.register(UserSMI, UserAdmin)
admin.site.register(Expert, UserAdmin)
admin.site.register(Visitor, UserAdmin)
admin.site.register(GosUser, UserAdmin)
admin.site.register(Participant, UserAdmin)