# Thing-Type

## The purpose of thing-type microservice is to provide an blue print of thing, which model and category thing belongs to. 

thing-type consists 11 Api's in total.
1. thing type crud APIs
2. model APIs
3. category APIs

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