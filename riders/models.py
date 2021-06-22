from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rider(models.Model):
    riderFullName = models.CharField(max_length=255, db_index=True)
    phone = models.PositiveSmallIntegerField(primary_key=True)
    rider = models.ForeignKey(User, on_delete=models.CASCADE)
    billingAddress = models.CharField(max_length=255, null=True, blank=True)
    isActive = models.BooleanField(default=True)
    lat = models.SmallIntegerField()
    lon = models.SmallIntegerField()

    @property
    def getLocation(self):
        if self.lat and self.lon:
            return (self.lat, self.lon)
        return (0, 0)