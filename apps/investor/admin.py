from django.contrib import admin
from apps.investor.models import Investor, Country

admin.site.register((Investor, Country))
