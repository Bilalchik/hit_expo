from django.contrib import admin

from apps.other.models import Expectation, Partner, SMI, B2B, News


admin.site.register((Expectation, Partner, SMI, B2B, News))
