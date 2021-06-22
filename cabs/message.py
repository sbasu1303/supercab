
class CabMessage(object):
    def __init__(self):
        self.driver = None
        self.driverFullName = None
        self.registrationNumber = None
        self.phone = None
        self.email = None
        self.IsActive = None
        self.status = None
        self.lat = None
        self.lon = None

    def str(self):
        return "{}-{}".format(self.driverFullName, self.registrationNumber)

    def dataDict(self):
        return self.__dict__

    def validate(self):
        return True