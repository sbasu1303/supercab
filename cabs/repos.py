from cabs.message import CabMessage
from cabs.models import Cab
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class CabRepo(object):
    def _allCabs(self):
        return Cab.objects.all()

    def createNewCab(self, cabMessage: CabMessage):
        user = User.objects.create_user(username=cabMessage.email)
        logger.info("User created successfully")
        c = Cab()
        c.driver = user
        c.registrationNumber = cabMessage.registrationNumber
        c.driverFullName = cabMessage.driverFullName
        c.email = cabMessage.email
        c.phone = cabMessage.phone
        c.IsActive = cabMessage.IsActive
        c.status = cabMessage.status
        c.lat = cabMessage.lat
        c.lon = cabMessage.lon

        c.save()
        logger.info("Cab created successfully {}".format(cabMessage.str()))
        return c


cabRepo = CabRepo()