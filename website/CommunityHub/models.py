from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserSurvey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isNYCHA = models.BooleanField()
    building = models.CharField(max_length=100)
    referredBy = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class WasteTracking(models.Model):
    #Workers username
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    volunteer = models.CharField(max_length = 100)
    wasteWeight = models.IntegerField()

class VolunteerTracking(models.Model):
    #Workers username
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    volunteer = models.CharField(max_length = 100)
    VolunteerTime = models.IntegerField()