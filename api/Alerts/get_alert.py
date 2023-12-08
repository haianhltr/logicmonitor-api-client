from utils.api_utils import create_api_instance, save_response_to_file, save_array_to_file, handle_api_exception, \
    fetch_paginated_data
from logicmonitor_sdk.rest import ApiException
from pprint import pprint


def get_alert_rule_by_id(alert_id):
    api_instance = create_api_instance()
    try:
        api_response = api_instance.get_alert_by_id(alert_id)
        pprint(api_response)
        save_response_to_file(api_response, 'getAlertById.json')
    except ApiException as e:
        handle_api_exception(e)


def get_alert_list():
    api_instance = create_api_instance()
    try:
        result = fetch_paginated_data(api_instance, api_instance.get_alert_list, page_size=500)
        save_array_to_file(result, 'getAlertRuleList.json')
    except ApiException as e:
        handle_api_exception(e)
