
class Constants:

    def __init__(self) -> None:
        self.__http_codes = {
            "BAD_REQUEST": 400,
            "SUCCESS": 200,
            "CREATED": 201,
            "ACCEPTED": 204,
            "NOT_FOUND": 404,
            "FORBIDDEN": 403,
            "UNAUTHORISED" : 401,
            "UNKNOWN_ERROR" : 500
        }
        self.__query_constants = {
            "LIMIT" : 10,
            "SKIP" : 0
        }
    
    def httpConstants(self, type: str)-> dict:
        if type in self.__http_codes:
            return self.__http_codes[type]
        else:
            return self.__http_codes['UNKNOWN_ERROR']
    
    def queryConstants(self, input):
        return self.__query_constants[input]
    
    @classmethod
    def models(cls):
        return ["esp32", "picow", "pi3", "pi4", "arduino", "nodemcu"]
    
    @classmethod
    def category(cls):
        return ["mcu", "sensor", "moisture", "temperature", "water flow", "solenoid", "lux"]
