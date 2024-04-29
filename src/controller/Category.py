from utils.validator import Validator
import utils.env_constants as const
from utils.error import *

class Category:

    def __init__(self, db_object, logger) -> None:
        self.logger = logger
        self.db_handler = db_object

    def addCategory(self, data):
        self.logger.info("addCategory invoked")
        modelValidator = Validator(self.logger)
        modelValidator.validateCategoryRequest(data)
        query = { "selector": {"name" : {"$eq": "thingCategory"}}}
        queryResponse = self.db_handler.findModelDocument(const.CATEGORY_DATABASE_NAME, query, self.logger)
        if len(queryResponse) == 0:
            self.logger.info("inserting catgeory")
            self.db_handler.insertDocument(const.CATEGORY_DATABASE_NAME, { "name": "thingCategory", "category" : data['category']}, self.logger)
        else:
            self.logger.info("adding new category to model array")
            resultData = self.__data(data, queryResponse[0])
            self.db_handler.updateDocument(const.CATEGORY_DATABASE_NAME, resultData, self.logger)
        return {"message": "category updated"}


    def removeCategory(self, id):
        self.logger.info("removeCategory invoked")
        query = { "selector": {"name" : {"$eq": "thingCategory"}}}
        queryResponse = self.db_handler.findModelDocument(const.CATEGORY_DATABASE_NAME, query, self.logger)
        try:
            queryResponse[0]['category'].remove(id)
            self.db_handler.updateDocument(const.CATEGORY_DATABASE_NAME, queryResponse[0], self.logger)
            return {"message": "category removed successfully"}
        except Exception as err:
            raise NotFoundError("Given category doesnt exist") 

    def fetchCategory(self):
        query = { "selector": {"name" : {"$eq": "thingCategory"}}}
        queryResponse = self.db_handler.findModelDocument(const.CATEGORY_DATABASE_NAME, query, self.logger)
        if len(queryResponse) == 0:
            raise NotFoundError("Category doesnt exists")
        del queryResponse[0]['_id']
        del queryResponse[0]['_rev']
        del queryResponse[0]['name']
        return queryResponse[0]
    
    def __data(self, request, dbData):
        self.logger.info("creating data for category update invoked")
        existingDataList = dbData['category']
        requestDataList = request['category']
        set1 = set(existingDataList)
        set2 = set(requestDataList)
        dbData["name"] = "thingCategory"
        dbData["category"] = list(set1.union(set2))
        self.logger.info("creating data for category update exited")
        return dbData
