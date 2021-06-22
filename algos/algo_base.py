from abc import ABC
from abc import ABCMeta
from abc import abstractmethod
import logging

logger = logging.getLogger(__name__)

def generateFivePartKey():
    pass

class CabFinder(ABC):
    __metaclass__ = ABCMeta

    def setProperties(self, properties):
        self.algoRunId = generateFivePartKey()
        self.properties = properties #Algo details and class name
        extra = {'algoRunId': self.algoRunId}
        logger = logging.getLogger(properties.class_name)
        self.logger = logging.LoggerAdapter(logger, extra)

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
