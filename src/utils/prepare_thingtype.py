
import uuid
import datetime

class PrepareDocument:

    def __init__(self) -> None:
        pass
    
    def __call__(self, function):
        def wrapper(self, data):
            id = uuid.uuid4()
            date = datetime.datetime.now()
            
            document = {
                "id": str(id),
                "name": data['name'],
                "category": data['category'],
                "model": data['model'],
                "description": "thing type service" if data['description'] is not None else "no data",
                "createDate": date.isoformat(),
                "modifiedDate" : date.isoformat(),
                "etag" : str(uuid.uuid4())
            }
            return function(self, document)
            #return document
        return wrapper