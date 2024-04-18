import utils.env_constants as const
from utils.prepare_thingtype import PrepareDocument
from utils.validator import Validator
import datetime
import uuid

class ThingType:
    """
    ThingType class manages CRUD functionality
    """

    def __init__(self, db_object, logger) -> None:
        self.logger = logger
        self.db_handler = db_object
    
    @PrepareDocument()
    def createThingType(self, data):
        self.logger.info("createThingType invoked")
        typeValidator = Validator(self.logger)
        typeValidator.validateThingType(data)
        typeValidator.validateIfNameExists(self.db_handler, data)
        self.db_handler.insertDocument(const.DB_NAME, data, self.logger)
        self.logger.info("createThingType exited")
        return {"message" : "thing type create successfully", "resource": "/v1/type/{id}".format(id=data['id'])}

    def fetchThingTypeById(self, id):
        self.logger.info("fetchThingTypeById invoked")
        query =  { "selector": {"id" : {"$eq": id}}}
        response = self.db_handler.findSingleDocument(const.DB_NAME, query, self.logger)
        del response['_id']
        del response['_rev']
        self.logger.info("fetchThingTypeById exited")
        return response

    def fetchAllThingType(self, params):
        self.logger.info("fetchAllThingType invoked")
        query = self.__prepare_query(params)
        response = self.db_handler.findDocument(const.DB_NAME, query, self.logger)
        self.logger.info("fetchAllThingType exited")
        return {"thingTypes" : response}
        
    def updateThingType(self, id, data):
        self.logger.info("updateThingType invoked")
        typeValidator = Validator(self.logger)
        typeValidator.validateThingType(data)
        document = typeValidator.validateUpdateThingTypeRequest(self.db_handler, id, data)
        updateDocument = self.__updateType_query(data, document)
        self.db_handler.updateDocument(const.DB_NAME, updateDocument, self.logger)
        return {"message" : "thing type updated successfully", "resource": "/v1/type/{id}".format(id=data['id'])}

    def deleteThingType(self, id):
        self.logger.info("deleteThingType invoked")
        typeValidator = Validator(self.logger)
        document = typeValidator.validateIfIdExists(self.db_handler, id)
        self.db_handler.deleteDocument(const.DB_NAME, document, self.logger)
        return {"message": "resource delete for given id"}

    def __prepare_query(self, data):
        fetch_query = { "selector": {}}
        if "name" in data:
            fetch_query['selector']['name'] = {"$eq": data['name']}
        if "category" in data:
            fetch_query['selector']['category'] = {"$eq": data['category']}
        if "location" in data:
            fetch_query['selector']['model'] = {"$eq": data['location']}
        if "limit" in data:
            fetch_query['limit'] = int(data["limit"])
        if "skip" in data:
            fetch_query['skip'] = int(data["skip"])
        return fetch_query
    
    def __updateType_query(self, request, result):
        etag = uuid.uuid4()
        result["name"] = request["name"]
        result["category"] = request["category"]
        result["model"] = request["model"]
        result["description"] = request["description"]
        result["createDate"] = request["createDate"]
        result["id"] = request["id"]
        result["etag"] = str(etag)
        result["modifiedDate"] = datetime.datetime.now().isoformat()
        return result
