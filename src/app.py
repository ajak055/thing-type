from flask import Flask, request, jsonify
from utils.logger import Logger
from utils.response import success_response, failure_response
from controller.ThingType import ThingType
from controller.Models import Models
from data.db import CouchDB
import utils.env_constants as const

app = Flask(__name__)

db_handler = CouchDB(const.URL, const.USERNAME, const.PASSWORD, 5984)
db_handler.connect()

@app.route("/v1/type", methods = ['POST'])
def CreateThingType():
   try:
      logger = Logger("thing-type")
      logger.info("API: create thing type invoked")
      input = request.get_json()
      createType = ThingType(db_handler, logger)
      response = createType.createThingType(input)
      return success_response(response, 201)
   except Exception as e:
      return failure_response(e)

@app.route("/v1/type/<id>", methods = ['GET'])
def fetchThingById(id):
   try:
      logger = Logger("thing-type")
      logger.info("API: fetchThingById invoked")
      fetchThingTypeId = ThingType(db_handler, logger)
      response = fetchThingTypeId.fetchThingTypeById(id)
      logger.info("API: fetchThingById exited")
      return success_response(response)
   except Exception as e:
      return failure_response(e)

@app.route("/v1/type", methods = ['GET'])
def fetchThingType():
   try:
      logger = Logger("thing-type")
      logger.info("API: fetchThingType invoked")
      fetchThingType = ThingType(db_handler, logger)
      response = fetchThingType.fetchAllThingType(request.args.to_dict())
      logger.info("API: fetchThingType exited")
      return success_response(response)
   except Exception as e:
      return failure_response(e)
   
@app.route("/v1/type/<id>", methods = ['DELETE'])
def deleteThingType(id):
   try:
      logger = Logger("thing-type")
      logger.info("API: deleteThingType invoked")
      deleteThingType = ThingType(db_handler, logger)
      response = deleteThingType.deleteThingType(id)
      logger.info("API: deleteThingType exited")
      return success_response(response)
   except Exception as e:
      return failure_response(e)

@app.route("/v1/type/<id>", methods = ['PUT'])
def updateThingType(id):
   try:
      logger = Logger("thing-type")
      logger.info("API: updateThingType invoked")
      updateThingType = ThingType(db_handler, logger)
      input = request.get_json()
      response = updateThingType.updateThingType(id, input)
      logger.info("API: updateThingType exited")
      return success_response(response)
   except Exception as e:
      return failure_response(e)
   
@app.route("/v1/type/model", methods = ["PUT"])
def addModels():
   try:
      logger = Logger("thing-type")
      logger.info("API: addModels invoked")
      addThingModel = Models(db_handler, logger)
      input = request.get_json()
      response = addThingModel.addModel(input)
      logger.info("API: addModels exited")
      return success_response(response)
   except Exception as e:
      return failure_response(e)  

@app.route("/v1/type/model", methods = ["GET"])
def fetchModels():
   try:
      logger = Logger("thing-type")
      logger.info("API: fetchModels invoked")
      fetchThingModel = Models(db_handler, logger)
      response = fetchThingModel.fetchModel()
      logger.info("API: fetchModels exited")
      return success_response(response)
   except Exception as e:
      return failure_response(e)  

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port=8000, debug=False)