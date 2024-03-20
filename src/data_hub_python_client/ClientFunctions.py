import json
import requests
from src.BearerAuth import BearerAuth


class ClientFunctions:
    def __init__(self, opts: dict):
        """
        Functions for interaction with the RNV data hub API.
        :param opts: options which contain the main parameters for the requests, usually loaded from .env file.
        """
        self.opts = opts

    def request_access_token(self) -> dict:
        """
        Requesting an access token from the oauth2 authorization server.
        :return: access token message body
        """
        rq_body = (f"grant_type = client_credentials&client_id={self.opts['CLIENT_ID']}"
                   f"&client_secret={self.opts['CLIENT_SECRET']}&resource={self.opts['RESOURCE_ID']}")
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        x = requests.post(self.opts['OAUTH_URL'], headers=headers, data=rq_body)
        return json.loads(x.text)

    def request_query_response(self, query: str, at_response: dict) -> dict:
        """
        Do graphql query in a POST request and obtain the response from
        Data Hub API.
        :param query: graphql query to datahub api as string (i.e. Constants.EXAMPLE_QUERIES.stations)
        :param at_response: access token message body
        :return: query response message body
        """
        post_data = {
            'query': query
        }

        post_data_str = json.dumps(post_data)
        headers = {
            'Authorization': f'Bearer {at_response['access_token']}',
            'Content-Type': 'application/json',
            'Content-Length': str(len(post_data_str))
        }

        x = requests.post(self.opts['CLIENT_API_URL'], headers=headers, data=post_data_str)
        return json.loads(x.text)

    def request_query_response_with_auth(self, query: str, at_response: dict) -> dict:
        """
        Basically the same as request_query_response, just with an auth class.
        This is rather a coding example, how to do request in alternative way.
        :param query: access token message body
        :param at_response: access token message body
        :return: query response message body
        """
        post_data = {
            'query': query
        }

        post_data_str = json.dumps(post_data)
        headers = {
            'Content-Type': 'application/json',
            'Content-Length': str(len(post_data_str))
        }

        x = requests.post(self.opts['CLIENT_API_URL'], headers=headers, data=post_data_str,
                          auth=BearerAuth(at_response['access_token']))
        return json.loads(x.text)
