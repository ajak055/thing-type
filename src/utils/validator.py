from utils.error import *
from utils.constants import *
import utils.env_constants as const

class Validator:
    def __init__(self, logger) -> None:
        self.logger = logger
        pass

    def validateThingType(self, data):
        self.logger.info("validateThingType invoked")
        if not 'name' in data:
              self.logger.error("Error : Name is required field")
              raise BusinessValidationError("Name is required field")
        
        if len(data['name']) < 3:
            self.logger.error("Minimum length of name is 3 chars")
            raise BusinessValidationError("Minimum length of name is 3 chars")

        if not 'category' in data:
            self.logger.error("Category is required")
            raise BusinessValidationError("Category is required")
        
        if not isinstance(data['category'], list):
            self.logger.error("Category has to be of type list")
            raise BusinessValidationError("Category has to be of type list")
        catgoryCompare = all(ele in Constants.category() for ele in data['category'])
        if not catgoryCompare:
            self.logger.error("Category has invalid value")
            raise BusinessValidationError("Category has invalid value, supported are {data}".format(data=Constants.category()))

        if not 'model' in data:
            self.logger.error("model is required")
            raise BusinessValidationError("model is required")
        
        if data['model'] not in Constants.models():
            self.logger.error("given model is not available")
            raise BusinessValidationError("given model is not available, supported models are {data}".format(data=Constants.models()))
                
        self.logger.info("validateThingType exited")

    def validateIfNameExists(self, db_handler, data):
        self.logger.info("validateIfNameExists invoked")
        query = { "selector": {"name" : {"$eq": data['name']}}}
        queryResponse = db_handler.findDocument(const.DB_NAME, query, self.logger)
        if len(queryResponse) != 0:
            raise BusinessValidationError("given name already exists")
        
    def validateIfIdExists(self, db_handler, id):
        self.logger.info("validateIfIdExists invoked")
        query = { "selector": {"id" : {"$eq": id}}}
        return db_handler.findSingleDocument(const.DB_NAME, query, self.logger)
    
    def validateUpdateThingTypeRequest(self, db_handler, id, data):
        self.logger.info("validateUpdateThingTypeRequest invoked")
        query = { "selector": {"id" : {"$eq": id}}}
        queryResponse = db_handler.findSingleDocument(const.DB_NAME, query, self.logger)
        print(queryResponse)
        nameQuery = { "selector": {"name" : {"$eq": data['name']}}}
        validateName = db_handler.findDocument(const.DB_NAME, nameQuery, self.logger)
        if queryResponse['etag'] != data['etag']:
            raise BusinessValidationError("etag mismatch, please pull latest record and update")
        if len(validateName) !=0:
            idList = [ dbData['id'] for dbData in validateName if dbData['name'] == data['name'] and dbData['id'] != id]
            if len(idList) !=0:
                raise BusinessValidationError("given name already exists")
        self.logger.info("validateUpdateThingTypeRequest exited")
        return {"_id": queryResponse['_id'], "_rev" : queryResponse['_rev']}