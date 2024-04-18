import couchdb
from utils.error import *
class CouchDB:

    def __init__(self, url, username, password, port=5984) -> None:
        self.url = url
        self.port = port
        self.username = username
        self.password = password
        self.dbObject = None

    def connect(self):
        db_url = "http://{user}:{pwd}@{host}:{dbport}/".format(user=self.username, pwd=self.password, host=self.url, dbport=self.port)
        self.dbObject = couchdb.Server(db_url)
    
    def createDb(self, dbname):
        self.dbObject(dbname)

    def insertDocument(self, dbname, document, logger):
        logger.info("Data: insertDocument invoked")
        db = self.dbObject[dbname]
        db.save(document)
        logger.info("Data: insertDocument exited")
    
    def findDocument(self, dbname, query, logger):
        logger.info("Data: findDocument invoked")
        query_response = []
        db = self.dbObject[dbname]
        result = db.find(query)
        for i in result:
            del i['_id']
            del i['_rev']
            query_response.append(i)
        logger.info("Data: findDocument exited")
        return query_response
    
    def findSingleDocument(self, dbname, query, logger):
        logger.info("Data: findSingleDocument invoked")
        query_response = []
        db = self.dbObject[dbname]
        result = db.find(query)
        for i in result:
            query_response.append(i)
        logger.info("Data: findSingleDocument exited")
        if len(query_response) == 0:
            raise NotFoundError("Data doesn't exists for given Id")
        return query_response[0]
    
    def deleteDocument(self, dbname, document, logger):
        logger.info("Data: deleteDocument invoked")
        db = self.dbObject[dbname]
        db.delete(document)
        logger.info("Data: deleteDocument exited")
    
    def updateDocument(self, dbname, document, logger):
        logger.info("Data: updateDocument invoked")
        db = self.dbObject[dbname]
        db.save(document)
        logger.info("Data: updateDocument exited")
