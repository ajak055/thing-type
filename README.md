# Thing-Type

The purpose of thing-type microservice is to provide a blue print of thing. Thing consists of category and model, category is of type which describes measruements that are recorded by thing such as temperature, lux, flow pressure etc.
Model describes what type of thing it is, thing can be controller based or processor based. models such as raspberry pi, esp32 etc.

thing-type consists 11 Api's in total.
1. Thing type crud APIs
2. Model APIs
3. Category APIs

Thing type uses couchdb as data store. The deployment of this repo consists for both thing-type and couchdb. If user wants to use seperate instance of their own.
Databases to be created for new installation.
1.  models
2.  category
3.  thing_type

## Schema
thing type API schema
```json
{
    "name": "irrigation", //type of thing, such as for which its things are mapped
    "category": ["lux", "sensor"],  //category is an array of sensor types which are integrated to thing
    "model": "pi4", // type of SoC as thing
    "description": "creating thing type"
}
```
model schema
```json
{
    "models": [
        "esp32",
        "rpi-picow",
        "rpi3",
        "nodemcu",
        "pi4"
    ]
}
```

Category schema
```json
{
 "category": ["mcu", "sensor", "moisture", "temperature", "water flow", "solenoid", "lux"]
}
```
## Deployment

## API Specs
Api specs provides  request, response for thing-type, model and category

### Create thing type
```sh
API: URL:8081/v1/type
METHOD: POST
REQUEST BODY:
{
    "name": "string",
    "category": ["string", "string"],
    "model": "string",
    "description": "string"
}
RESPONSE: 201 CREATED
{
    "message": "thing type create successfully",
    "resource": "/v1/type/d29e991a-a268-4285-9f30-48fb9ee8701d"
}
RESPONSE: 400 BAD REQUEST
{
    "message": "given name already exists"
}
RESPONSE: 400 BAD REQUEST
{
    "message": "Category has invalid value, supported are ['mcu', 'sensor', 'moisture', 'temperature', 'water flow', 'solenoid', 'lux']"
}
RESPONSE: 400 BAD REQUEST
{
    "message": "given model is not available, supported models are ['esp32', 'rpi-picow', 'rpi3', 'nodemcu', 'pi4']"
}
```
### Fetch thing type
```sh
API: URL:8081/v1/type
METHOD: GET
QUERY PARAMS:
  name : string
  model: string
  limit: string
  category: string
  skip: string
RESPONSE: 200 OK
{
    "thingTypes": [
        {
            "category": [
                "lux",
                "sensor"
            ],
            "createDate": "2024-04-23T17:27:53.860957",
            "description": "thing type service",
            "etag": "a337fa31-953a-4004-9099-f12a357b676a",
            "id": "d29e991a-a268-4285-9f30-48fb9ee8701d",
            "model": "pi4",
            "modifiedDate": "2024-04-23T17:27:53.860957",
            "name": "irrigation"
        }
    ]
}
```
### Fetch thing type by Id
```sh
API: URL:8081/v1/type/{id}
METHOD: GET
RESPONSE BODY: 200 OK
{
    "category": [
        "lux",
        "sensor"
    ],
    "createDate": "2024-04-23T17:27:53.860957",
    "description": "thing type service",
    "etag": "a337fa31-953a-4004-9099-f12a357b676a",
    "id": "d29e991a-a268-4285-9f30-48fb9ee8701d",
    "model": "pi4",
    "modifiedDate": "2024-04-23T17:27:53.860957",
    "name": "irrigation"
}
RESPONSE: 404 NOT FOUND
{
    "message": "Data doesn't exists for given Id"
}
```
### Update thing type
```sh
API: URL:8081/v1/type/{id}
METHOD: PUT
REQUEST BODY:
{
    "category": [
        "lux",
        "sensor"
    ],
    "createDate": "2024-04-23T17:27:53.860957",
    "description": "thing type service",
    "etag": "a337fa31-953a-4004-9099-f12a357b676a",
    "id": "d29e991a-a268-4285-9f30-48fb9ee8701d",
    "model": "pi4",
    "modifiedDate": "2024-04-23T17:27:53.860957",
    "name": "irrigation"
}
RESPONSE: 200 OK
{
    "message": "thing type updated successfully",
    "resource": "/v1/type/d29e991a-a268-4285-9f30-48fb9ee8701d"
}
```
### Delete thing type
```sh
API: URL:8081/v1/type/{id}
METHOD: DELETE
RESPONSE: 200 OK
{
    "message": "resource delete for given id"
}
RESPONSE: 404 NoT FOUND
{
    "message": "Data doesn't exists for given Id"
}
```
### Add models
```sh
API: URL:8081/v1/type/model
METHOD: PUT
REQUEST BODY:
{
    "models": [
        "esp32",
        "rpi-picow",
        "rpi3",
        "nodemcu",
        "pi4"
    ]
}
RESPONSE: 200 OK
{
    "message": "model updated"
}
```
### Fetch model
```sh
API: URL:8081/v1/type/model
METHOD: GET
RESPONSE: 200 OK
{
    "models": [
        "nodemcu",
        "esp32",
        "pi4",
        "rpi-picow",
        "rpi3"
    ]
}
```
### Delete model
```sh
API: URL:8081/v1/type/model/{model}
METHOD: DELETE
RESPONSE: 200 OK
{
    "message": "model removed successfully"
}
RESPONSE: 404 NOT FOUND
{
    "message": "Given model doesnt exist"
}
```
### Add Category
```sh
API: URL:8081/v1/type/category
METHOD: PUT
REQUEST BODY:
{
    "category": [
        "mcu",
        "sensor",
        "moisture",
        "temperature",
        "water flow",
        "solenoid",
        "lux"
    ]
}
RESPONSE: 200 OK
{
    "message": "category updated"
}
```

### Fetch category
```sh
API: URL:8081/v1/type/category
METHOD: GET
RESPONSE: 200 OK
{
    "category": [
        "mcu",
        "sensor",
        "moisture",
        "temperature",
        "water flow",
        "solenoid",
        "lux"
    ]
}
```
### Delete category
```sh
API: URL:8081/v1/type/category/{category}
METHOD: DELETE
RESPONSE: 200 OK
{
    "message": "category removed successfully"
}
RESPONSE: 404 NOT FOUND
{
    "message": "Given category doesnt exist"
}
```