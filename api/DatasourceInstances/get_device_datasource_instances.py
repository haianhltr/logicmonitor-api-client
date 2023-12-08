from utils.api_utils import create_api_instance, save_response_to_file, save_array_to_file, handle_api_exception, \
    fetch_paginated_data
from logicmonitor_sdk.rest import ApiException
from pprint import pprint


def get_device_datasource_instance_by_id(deviceId, hdsId, instanceId):
    api_instance = create_api_instance()
    try:
        api_response = api_instance.get_device_datasource_instance_by_id(deviceId, hdsId, instanceId)
        pprint(api_response)
        save_response_to_file(api_response, 'getDeviceDatasourceInstanceById.json')
    except ApiException as e:
        handle_api_exception(e)

