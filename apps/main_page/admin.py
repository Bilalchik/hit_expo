from django.contrib import admin
from apps.main_page.models import (PageOne, Place, PlaceOffice,
                                    Partners, Members, Forum, 
                                    Ellipse, Video, Organizers,
                                    Target, Tasks, Sectors,
                                    Sponsors, Speakers, Socials)

admin.site.register((PageOne, Place, PlaceOffice,
                    Partners, Members, Forum, 
                    Ellipse, Video, Organizers,
                    Target, Tasks, Sectors,
                    Sponsors, Speakers, Socials))
