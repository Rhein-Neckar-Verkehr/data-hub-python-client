from dotenv import load_dotenv
import os

from data_hub_python_client.ClientFunctions import ClientFunctions
from data_hub_python_client.Constants import EXAMPLE_QUERIES


def load_options() -> dict:
    """
    Loads options from .env file into dictionary
    :return: dictionary with options
    """
    load_dotenv()
    options = {
        "CLIENT_API_URL" : os.environ.get("CLIENT_API_URL"),
        "OAUTH_URL": os.environ.get("OAUTH_URL"),
        "CLIENT_ID": os.environ.get("CLIENT_ID"),
        "CLIENT_SECRET": os.environ.get("CLIENT_SECRET"),
        "RESOURCE_ID": os.environ.get("RESOURCE_ID")
    }
    return options


opts = load_options()
print(f"CLIENT_API_URL: {opts['CLIENT_API_URL']}")
cf = ClientFunctions(opts)
at_info = cf.request_access_token()
q_res1 = cf.request_query_response(EXAMPLE_QUERIES.stations, at_info)
# alternative way of doing query
q_res2 = cf.request_query_response_with_auth(EXAMPLE_QUERIES.stations, at_info)

print(f"Response header auth: {str(q_res1)[:100]}")
print(f"Response bearer auth: {str(q_res2)[:100]}")





