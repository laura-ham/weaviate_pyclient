# weaviate_pyclient

This package is a python client library, which can be used for efficient requests on your Weaviate instance.

## Getting started

Install the library by running:
` $ pip install weaviate_pyclient `

Then, you can include this module by importing it in your Python scripts:
` import weaviate_pyclient `

## How to use

You can use this package for making requests to Weaviate instances. Initiate connection to Weaviate by calling 

``` python
to_weaviate = weaviate_pyclient.ToWeaviate(config) 
```

where ` config ` contains the correct credentials and location of your instance in the following format: 

``` json
{
	"location": "localhost",
	"urlport" : "localhost:8070",
	"token_header": "X-API-KEY",
	"token": "xxxx-xxxx-xxxx-xxxx"
}
```

Then, the variable `to_weaviate` can be used for requests.

Note that using functions of this class are using the Swagger API client of Weaviate, to make data synchronisation with your Weaviate instance in python scripts easier and more structured. Not all functions of the Weaviate API are used in this class. If you want to use other REST API or GraphQL functions, these can be used by `to_weaviate.weaviate_client.[function]`, where the available functions can be found in [this script](https://raw.githubusercontent.com/laura-ham/weaviate_pyclient/master/weaviate_pyclient/swagger_client.py). (documentation will be added later.)


## Documentation

### *class* weaviate_pyclient.ToWeaviate(config)

**get_cref_schema**(*uuid*)

```
Return the schema for property when value is cross reference
param uuid:	uuid of the thing

Returns the cref schema of the Thing in json format.
```

**get_uuid**(*class_name, property_name, property_value*)

```
Return the uuid of a thing based on class and one property
param class_name:
 	Class name
param property_name:
 	Property name
param property_value:
 	Property value

Returns the uuid when the Thing is found, returns None if no Thing was found.
```

**post_thing**(*class_name, schema*)

```
Post a thing to Weaviate instance given its schema and class
param class_name:
 	Class
param schema:	Thing schema

Returns the uuid of the Thing which is created and posted to Weaviate.
```

**update_thing**(*uuid, operation, path, value*)

```
Update thing by json patch
param uuid:	uuid of the Thing
param operation:
 	Update operation. E.g. “replace”
param path:	Path
param value:	New value

Returns nothing.
```

**update_thing_schema**(*uuid, schema*)

```
Patch the schema of a Thing
param uuid:	uuid of the Thing
param schema:	new schema of the thing

Returns nothing.
```