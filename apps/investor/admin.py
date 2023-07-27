from django.contrib import admin
from apps.investor.models import Investor, Country , Organizer, Sponsors

admin.site.register((Investor, Country,Organizer, Sponsors))
