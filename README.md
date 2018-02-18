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


### *class* weaviate_pyclient.ToWeaviate(config)

**get_cref_schema**(*uuid*)

```
Return the schema for property when value is cross reference
param uuid:	uuid of the thing
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
```

**post_thing**(*class_name, schema*)

```
Post a thing to Weaviate instance given its schema and class
param class_name:
 	Class
param schema:	Thing schema
```

**update_thing**(*uuid, operation, path, value*)

```
Update thing by json patch
param uuid:	uuid of the Thing
param operation:
 	Update operation. E.g. “replace”
param path:	Path
param value:	New value
```

**update_thing_schema**(*uuid, schema*)

```
Patch the schema of a Thing
param uuid:	uuid of the Thing
param schema:	new schema of the thing
```