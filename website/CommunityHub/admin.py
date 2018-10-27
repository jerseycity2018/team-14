from django.contrib import admin
from .models import UserSurvey, WasteTracking, VolunteerTracking

# Register your models here.
admin.site.register(UserSurvey)
admin.site.register(WasteTracking)
admin.site.register(VolunteerTracking)