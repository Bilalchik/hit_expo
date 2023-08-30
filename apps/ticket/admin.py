from django.contrib import admin
from apps.ticket.models import Industry, Stand, Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'zone', 'place_status', 'status', 'created_date')
    list_filter = ('zone', 'place_status', 'status', 'created_date')
    search_fields = ('user', )
    list_display_links = list_display


admin.site.register(Industry)
admin.site.register(Stand)
admin.site.register(Ticket, TicketAdmin)
