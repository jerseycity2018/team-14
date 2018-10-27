from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserSurvey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isNYCHA = models.BooleanField()
    building = models.CharField(max_length=100)
    referredBy = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name

class WasteTracking(models.Model):
    #Workers username
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    volunteer = models.CharField(max_length = 100)
    wasteWeight = models.IntegerField()

    def __str__(self):
        return self.volunteer

class VolunteerTracking(models.Model):
    #Workers username
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    volunteer = models.CharField(max_length = 100)
    VolunteerTime = models.IntegerField()

    def __str__(self):
        return self.volunteer