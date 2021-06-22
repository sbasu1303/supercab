from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from cabs.constants import CabStatus


class Cab(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    driverFullName = models.CharField(max_length=254, db_index=True)
    registrationNumber = models.CharField(max_length=20, primary_key=True)
    phone = models.PositiveSmallIntegerField()
    email = models.EmailField()
    IsActive = models.BooleanField(default=True)
    status = models.CharField(max_length=30, default=CabStatus.FREE)
    lat = models.SmallIntegerField()
    lon = models.SmallIntegerField()

    @property
    def getLocation(self):
        if self.lat and self.lon:
            return (self.lat, self.lon)
        return (0,0)

