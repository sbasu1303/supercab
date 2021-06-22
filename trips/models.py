from django.db import models
from cabs.models import Cab
from riders.models import Rider
# Create your models here.

class TripStatus(object):
    YET_TO_START = 'Yet To Start'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'COMPLETED'

class Trip(models.Model):
    tripId = models.UUIDField(db_index=True)
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default=TripStatus.YET_TO_START)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    startTime = models.DateTimeField(null=True, blank=True)
    endTime = models.DateTimeField(null=True, blank=True)
    pickupLocation = models.JSONField()
    dropLocation = models.JSONField()
    distance = models.SmallIntegerField(null=True, blank=True)