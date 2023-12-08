# utils/api_utils.py
from __future__ import print_function
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from config import app_config
import json
import logging

# Initialize a logger
logger = logging.getLogger(__name__)

def create_api_instance():
    """
    Create and return an API instance.
    """
    configuration = logicmonitor_sdk.Configuration()
    configuration.company = app_config.company
    configuration.access_id = app_config.access_id
    configuration.access_key = app_config.access_key

    api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
    return api_instance

def fetch_paginated_data(api_instance, fetch_function, page_size=500):
    """
    Fetch paginated data from the API using the specified fetch function.

    :param api_instance: The API instance.
    :param fetch_function: The function for fetching data.
    :param page_size: The page size for each request.
    :return: A list of fetched items.
    """
    result = []

    try:
        response = fetch_function(api_instance, page_size, offset=0)
        response_dict = response.to_dict()
        total = response_dict.get('total')
        result += response_dict['items']

        offset = page_size
        while offset < total:
            response = fetch_function(api_instance, page_size, offset)
            response_dict = response.to_dict()
            result += response_dict['items']
            offset += page_size

        return result
    except ApiException as e:
        logger.error(f"API Error: {str(e)}")

def handle_api_exception(e):
    """
    Handle API exceptions and log errors.

    :param e: The ApiException instance.
    """
    logger.error(f"API Error: {str(e)}")

def save_response_to_file(response, filename):
    """
    Save the API response to a JSON file.

    :param response: The API response.
    :param filename: The output filename.
    """
    response_dict = response.to_dict()
    with open(filename, 'w') as f:
        json.dump(response_dict, f, indent=4)

def save_array_to_file(arr, filename):
    """
    Save a Python list to a JSON file.

    :param arr: The list to be saved.
    :param filename: The output filename.
    """
    with open(filename, 'w') as f:
        json.dump(arr, f, indent=4)