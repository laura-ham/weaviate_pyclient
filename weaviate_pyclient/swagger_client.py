#!/usr/bin/env python
""" Client library module for connecting to weaviate instance API"""

import sys
import json
import requests

# A client class for accessing Weaviate data by querying the RESTful API


class ApiClient:
    def __init__(self, api_token, ip_adres):
        self.api_token = api_token
        self.ip_adres = ip_adres
        self.default_url = 'http://' + self.ip_adres + ':8070//weaviate/v1'
        self.headers = {
            'X-API-KEY': self.api_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'}

    # Print error and exit if query was not successful
    def error_message(self, query, response):
        sys.exit("Error: query " + query + "returned the following: " +
                 str(response.status_code) + ": " + response.reason)

    # Queries: Things

    # Get a list of things related to this key.
    def weaviate_things_list(self, max_results=None, page=None):
        # define url
        url = self.default_url + '/things'
        if max_results is not None:
            if isinstance(max_results, int):
                url += "?maxResults=" + str(max_results)
            else:
                sys.exit(
                    "The maxResults argument " +
                    max_results +
                    " you entered is not an integer")
                # error maxresults is not an integer
        else:
            url += "?maxResults=0"

        if page is not None:
            if isinstance(page, int):
                if max_results in url:
                    url += "&page=" + str(page)
            else:
                sys.exit(
                    "The page argument " +
                    max_results +
                    " you entered is not an integer")
                # error page is not an integer
        else:
            url += "&page=0"

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            result = json.loads(response.content.decode('utf-8'))
            return result
        else:
            self.error_message(url, response)

    # Create a new thing based on a thing template related to this key
    def weaviate_things_create(self, body):
        url = self.default_url + '/things'
        response = requests.post(url, headers=self.headers, json=body)
        if response.status_code == 202:
            result = json.loads(response.content.decode('utf-8'))
            return result
        else:
            self.error_message((url + str(body)), response)

    # Validate Things schema
    def weaviate_things_validate(self, body):
        url = self.default_url + '/things/validate'
        response = requests.post(url, headers=self.headers, json=body)
        if response.status_code == 200:
            return True
        else:
            self.error_message((url + str(body)), response)

    # Delete a thing based on its uui related to this key and return True if
    # Thing successfully deleted
    def weaviate_things_delete(self, thing_id):
        url = self.default_url + '/things/' + thing_id
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            return True
        else:
            self.error_message(("delete" + url), response)

    # Get a thing based on its uuid related to this key
    def weaviate_things_get(self, thing_id):
        url = self.default_url + '/things/' + thing_id
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            result = json.loads(response.content.decode('utf-8'))
            return result
        else:
            self.error_message(("get" + url), response)

    # Update a thing based on its uuid (using patch semantics) related to this
    # key
    def weaviate_things_patch(self, thing_id, body):
        url = self.default_url + '/things/' + thing_id
        response = requests.patch(url, headers=self.headers, json=body)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            self.error_message(("patch" + url + str(body)), response)

    # Update a thing based on its uud related to this key
    def weaviate_things_put(self, thing_id, body):
        url = self.default_url + '/things/' + thing_id
        response = requests.put(url, headers=self.headers, json=body)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            self.error_message(("put" + url + str(body)), response)

    # Get a thing based on its uuid related to this thing. Alse available as
    # MQTT
    def weaviate_things_actions_list(self, thing_id, body):
        url = self.default_url + '/things/' + thing_id + '/actions'
        response = requests.get(url, headers=self.headers, json=body)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            self.error_message((url + str(body)), response)

    # Queries: Actions

    # Create actions between two things (object and subject)
    def weaviate_actions_create(self, body):
        url = self.default_url + '/actions'
        response = requests.post(url, headers=self.headers, json=body)
        if response.status_code == 202:
            result = json.loads(response.content.decode('utf-8'))
            return result
        else:
            self.error_message(("post" + url + str(body)), response)

    # Delete an action based on its uuid related to this key
    def weaviate_actions_delete(self, action_id):
        url = self.default_url + '/actions/' + action_id
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            return True
        else:
            self.error_message(("delete" + url), response)

    # Get a specific action based on its uuid and a thing uuid related to this
    # key.
    def weaviate_actions_get(self, action_id):
        url = self.default_url + '/actions/' + action_id
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            result = json.loads(response.content.decode('utf-8'))
            return result
        else:
            self.error_message(("get" + url), response)

    # Update an action based on its uud (using patch semantics) related to
    # this key.
    def weaviate_actions_patch(self, action_id, body):
        url = self.default_url + '/action/' + action_id
        response = requests.patch(url, headers=self.headers, json=body)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            self.error_message(("patch" + url + str(body)), response)

    # Validate an action based on a schema.
    def weaviate_actions_validate(self, body):
        url = self.default_url + '/actions/validate'
        response = requests.post(url, headers=self.headers, json=body)
        if response.status_code == 200:
            return True
        else:
            self.error_message((url + str(body)), response)

    # Queries: GraphQL

    # Get a json response based on GraphQL
    def weaviate_graphql_post(self, body):
        url = self.default_url + '/graphql'
        response = requests.post(url, headers=self.headers, json=body)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            self.error_message((url + str(body)), response)

    # Get the uuid of the first result of the json response based on GraphQL
    # should be more efficient by querying only 1
    def weaviate_graphql_post_get_first_uuid(self, body):
        url = self.default_url + '/graphql'
        response = requests.post(url, headers=self.headers, json=body)
        if response.status_code == 200:
            result = json.loads(response.content.decode('utf-8'))
            if result["data"]["listThings"]["things"]:
                # return uuid of first thing in result
                return result["data"]["listThings"]["things"][0]["uuid"]
            return None
        else:
            self.error_message((url + str(body)), response)

    # Get all things of the json response based on GraphQL
    def weaviate_graphql_post_get_all_things(self, body):
        url = self.default_url + '/graphql'
        response = requests.post(url, headers=self.headers, json=body)
        if response.status_code == 200:
            result = json.loads(response.content.decode('utf-8'))
            if result["data"]["listThings"]["things"]:
                # return uuid of first thing in result
                return result["data"]["listThings"]["things"]
            return None
        else:
            self.error_message((url + str(body)), response)

    # Meta

    # Get meta information of the current Weaviate instance
    def weaviate_get_meta(self):
        url = self.default_url + '/meta'
        response = requests.post(url, headers=self.headers)
        if response.status_code == 200:
            result = json.loads(response.content.decode('utf-8'))
            return result
        else:
            self.error_message(url, response)

    # Keys

    # Create a new key related to this key
    def weaviate_create_key(self, body):
        url = self.default_url + '/keys'
        response = requests.post(url, headers=self.headers, json=body)
        if response.status_code == 202:
            return json.loads(response.content.decode('utf-8'))
        else:
            self.error_message((url + str(body)), response)

    # Delete a key based on its uuid related to this key
    def weaviate_delete_key(self, key_id):
        url = self.default_url + '/keys/' + key_id
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            return True
        else:
            self.error_message(("delete" + url), response)

    # Get a key based on its uuid related to this key
    def weaviate_get_key(self, key_id):
        url = self.default_url + '/keys/' + key_id
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            self.error_message(url, response)

    # Get an object of this keys' children related to this key
    def weaviate_get_keys_children(self, key_id):
        url = self.default_url + '/keys/' + key_id + '/children'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            self.error_message(url, response)

    # Get a key based on the key used to do the request
    def weaviate_get_mykey(self):
        url = self.default_url + '/keys/me'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            self.error_message(url, response)

    # Get an object of this keys' children related to th ekey used for request
    def weaviate_get_mykeys_children(self):
        url = self.default_url + '/keys/me/children'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            self.error_message(url, response)
