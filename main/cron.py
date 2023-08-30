import requests

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

import django
from django.conf import settings

if not settings.configured:
    django.setup()

from apps.ticket.models import Ticket


def ticket_delete():
    tickets = Ticket.objects.filter(status=1)
    tickets.delete()


ticket_delete()
