import logging
import uuid
import json

class Logger:
    """
    Logger class provides info, debug and error function to log all service information
    """

    def __init__(self, service, correlationId=None) -> None:
        if(correlationId is None):
            self.correlationId = uuid.uuid4()
        else:
            self.correlationId = correlationId
        self.service = service
        logging.basicConfig(format='%(asctime)s-%(name)s:%(levelname)s: %(message)s', level=logging.DEBUG)
        self.logger = logging.getLogger(self.service)

    
    def info(self, message, data=None):
        if data:
            self.logger.info({"message": message, "data": json.dumps(data), "correlationId" : str(self.correlationId)})
        else:
            self.logger.info({"message": message, "correlationId" : str(self.correlationId)})
    
    def debug(self, message, data=None):
        if data:
            self.logger.debug({"message": message, "data": json.dumps(data), "correlationId" : str(self.correlationId)})
        else:
            self.logger.debug({"message": message, "correlationId" : str(self.correlationId)})
    
    def error(self, message, data=None):
        if data:
            self.logger.error({"message": message, "data": json.dumps(data), "correlationId" : str(self.correlationId)})
        else:
            self.logger.error({"message": message, "correlationId" : str(self.correlationId)})