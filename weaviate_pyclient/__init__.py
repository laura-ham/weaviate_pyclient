#!/usr/bin/env python
""" Module to create connection with weaviate and data import scripts """

from .swagger_client import ApiClient


class ToWeaviate():
    """
    This class serves as a intermediate step between data import scripts and doing queries to the Weaviate instance.
    The methods define correct formats for doing queries.
    """

    def __init__(self, config):
        self.weaviate_config = config
        self.weaviate_client = ApiClient(
            self.weaviate_config["token"],
            self.weaviate_config["location"])
        self.location_url = self.weaviate_config["urlport"]

    # returns schema for property when value is cross reference
    def get_cref_schema(self, uuid):
        cref_schema = {}
        cref_schema["locationUrl"] = self.location_url
        cref_schema["type"] = "Thing"
        cref_schema["$cref"] = uuid
        return cref_schema

    # find uuid of thing based on class and one given property
    def get_uuid(self, class_name, property_name, property_value):
        body = {
            "query": "{listThings(first:1 schema:\"" +
                     property_name +
                     ":" +
                     str(property_value) +
                     "\", class:\"" +
                     class_name +
                     "\") {things {uuid}}}"}
        response = self.weaviate_client.weaviate_graphql_post(body)
        things = response["data"]["listThings"]["things"]
        # if thing exists: return uuid
        if things is not None and things:
            uuid = things[0]["uuid"]
            return uuid
        # if thing doesn't exists: return None
        return None

    def post_thing(self, class_name, schema):
        # how to check if thing already exists?

        body = {}
        body["@context"] = "http://dbpedia.org"
        body["@class"] = class_name
        body["schema"] = schema

        # post thing to weaviate and get a result when posted succesfully
        response = self.weaviate_client.weaviate_things_create(body)

        # return uuid if successfully posted thing
        uuid = response["thingId"]
        return uuid

    def update_thing(self, uuid, operation, path, value):
        body = {}
        body["op"] = operation
        body["path"] = path
        body["value"] = value

        # patch thing to weaviate and get a result when patch was succesful
        self.weaviate_client.weaviate_things_patch(uuid, [body])
        return

    def update_thing_schema(self, uuid, schema):
        body = {}
        body["op"] = "replace"
        body["path"] = "/schema"
        body["value"] = schema

        # patch thing to weaviate and get a result when patch was succesful
        self.weaviate_client.weaviate_things_patch(uuid, [body])
        return
