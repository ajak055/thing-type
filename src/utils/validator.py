from utils.error import *
from utils.constants import *
import utils.env_constants as const

class Validator:
    def __init__(self, logger) -> None:
        self.logger = logger
        pass

    def validateThingType(self, data, db_handler):
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
        
        category = self.getThingCategory(db_handler)
        catgoryCompare = all(ele in category['category'] for ele in data['category'])

        if not catgoryCompare:
            self.logger.error("Category has invalid value")
            raise BusinessValidationError("Category has invalid value, supported are {data}".format(data=category['category']))

        if not 'model' in data:
            self.logger.error("model is required")
            raise BusinessValidationError("model is required")
        
        models = self.getThingModels(db_handler)
        if data['model'] not in models["models"]:
            self.logger.error("given model is not available")
            raise BusinessValidationError("given model is not available, supported models are {data}".format(data=models["models"]))
                
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
    
    def validateModelRequest(self, data):
        self.logger.info("validateModelRequest invoked")
        if not isinstance(data['models'], list):
            raise BusinessValidationError("model should of type list")
        self.logger.info("validateModelRequest exited")

    def validateCategoryRequest(self, data):
        self.logger.info("validateCategoryRequest invoked")
        if not isinstance(data['category'], list):
            raise BusinessValidationError("categpry should of type list")
        self.logger.info("validateCategoryRequest exited")
  
    def getThingModels(self, db_handler):
        self.logger.info("getThingModels invoked")
        query = { "selector": {"name" : {"$eq": "thingModel"}}}
        queryResponse = db_handler.findModelDocument(const.MODEL_DB_NAME, query, self.logger)
        if len(queryResponse) == 0:
            raise NotFoundError("Model doesnt exists")
        del queryResponse[0]['_id']
        del queryResponse[0]['_rev']
        del queryResponse[0]['name']
        self.logger.info("getThingModels exited")
        return queryResponse[0]

    def getThingCategory(self, db_handler):
        self.logger.info("getThingCategory invoked")
        query = { "selector": {"name" : {"$eq": "thingCategory"}}}
        queryResponse = db_handler.findModelDocument(const.CATEGORY_DATABASE_NAME, query, self.logger)
        if len(queryResponse) == 0:
            raise NotFoundError("Category doesnt exists")
        del queryResponse[0]['_id']
        del queryResponse[0]['_rev']
        del queryResponse[0]['name']
        self.logger.info("getThingCategory exited")
        return queryResponse[0]
