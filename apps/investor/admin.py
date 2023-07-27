from django.contrib import admin
<<<<<<< HEAD

from apps.investor.models import Investor, Country
=======
from apps.investor.models import Investor, Country , Organizer, Sponsors
>>>>>>> 5eb36137c99492841360ea843c19737cfdbd3369

admin.site.register((Investor, Country,Organizer, Sponsors))
