from cabs.message import CabMessage
from rest_framework.exceptions import NotAcceptable
from cabs.repos import cabRepo
from cabs.constants import CabStatus
import logging
from abc import ABC

logger = logging.getLogger(__name__)

class CabServices(object):
    def createNewCab(self, payload):
        cabMessage = CabMessage()
        cabMessage.registrationNumber = payload['registrationNumbe']
        cabMessage.driverFullName = payload['driverFullName']
        cabMessage.email = payload['email']
        cabMessage.phone = payload['phone']
        cabMessage.IsActive = payload['IsActive'] or True
        cabMessage.status = payload['status'] or CabStatus.OFFHOURS
        cabMessage.lat = payload['lat']
        cabMessage.lon = payload['lon']
        if not cabMessage.validate():
            raise NotAcceptable
        try:
            cab = cabRepo.createNewCab(cabMessage)
            return cab
        except Exception as ex:
            return Exception("Failed to create a cab - {}".format(ex.__str__()))
        return None

    def findCab(self, slat, slon):
        pass




