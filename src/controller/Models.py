from utils.validator import Validator
import utils.env_constants as const
from utils.error import *

class Models:

    def __init__(self, db_object, logger) -> None:
        self.logger = logger
        self.db_handler = db_object

    def addModel(self, data):
        self.logger.info("addModel invoked")
        modelValidator = Validator(self.logger)
        modelValidator.validateModelRequest(data)
        query = { "selector": {"name" : {"$eq": "thingModel"}}}
        queryResponse = self.db_handler.findModelDocument(const.MODEL_DB_NAME, query, self.logger)
        if len(queryResponse) == 0:
            self.logger.info("inserting model")
            self.db_handler.insertDocument(const.MODEL_DB_NAME, { "name": "thingModel", "models" : data['models']}, self.logger)
        else:
            self.logger.info("adding new model to model array")
            resultData = self.__data(data, queryResponse[0])
            self.db_handler.updateDocument(const.MODEL_DB_NAME, resultData, self.logger)
        return {"message": "model updated"}
           

    def fetchModel(self):
        query = { "selector": {"name" : {"$eq": "thingModel"}}}
        queryResponse = self.db_handler.findModelDocument(const.MODEL_DB_NAME, query, self.logger)
        if len(queryResponse) == 0:
            raise NotFoundError("Model doesnt exists")
        del queryResponse[0]['_id']
        del queryResponse[0]['_rev']
        del queryResponse[0]['name']
        return queryResponse[0]


    def removeModel(self, id):
        query = { "selector": {"name" : {"$eq": "thingModel"}}}
        queryResponse = self.db_handler.findModelDocument(const.MODEL_DB_NAME, query, self.logger)
        try:
            queryResponse[0]['models'].remove(id)
            self.db_handler.updateDocument(const.MODEL_DB_NAME, queryResponse[0], self.logger)
            return {"message": "model removed successfully"}
        except Exception as err:
            raise NotFoundError("Given model doesnt exist")            
        

    def __data(self, request, dbData):
        self.logger.info("creating data for model update invoked")
        existingDataList = dbData['models']
        requestDataList = request['models']
        set1 = set(existingDataList)
        set2 = set(requestDataList)
        dbData["name"] = "thingModel"
        dbData["models"] = list(set1.union(set2))
        self.logger.info("creating data for model update exited")
        return dbData