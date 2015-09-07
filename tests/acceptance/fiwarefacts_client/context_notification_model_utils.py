

def create_context_element_attribute(name, type, value):
    """
    Function to create a context attribute body
    :param name (string): Name of the attribute
    :param type (string): Type of the attribute
    :param value (string): Value of the attribute
    :return (dict): Contest attribute body. The attribute in JSON will be like this:
            {
                "name" : "temperature",
                "type" : "float",
                "value" : "23"
            }
    """

    return {"name": name,
            "type": type,
            "value": value}


def _create_context_element(type=None, is_pattern=None, id=None, attribute_list=None):
    """
    Function to create a context server body with the given attribute_list param.
    :param type (String): Context type
    :param is_pattern (Bool): Value of 'isPattern' attribute
    :param id (String): The id of the entity.
    :param attribute_list (list of dicts): All atribute values
            [{"name": "temperature", "type": "float", "value": "23"}, ...]
    :return (dict) Context element body. The contextElement in JSON will be like this:
            "contextElement" : {
                "type" : "Room",
                "isPattern" : "false",
                "id" : "Room1",
                "attributes" : [
                {
                    "name" : "temperature",
                    "type" : "float",
                    "value" : "23"
                }
                ]
            }
    """

    return {"attributes": attribute_list,
            "type": type,
            "isPatter": is_pattern,
            "id": id}


def _create_context_status_code(status_code=None, details=None, reason=None):
    """
    Function to build the status code model
    :param status_code: Numerical status code generated from context server
    :param details: Details regarding the context
    :param reason: Information about the context
    :return (dict) Status code model. The statusCode in JSON will be like this:
            "statusCode" : {
                "code" : "200",
                "reasonPhrase" : "OK"
            }
    """

    return {"code": status_code,
            "reasonPhrase": reason,
            "details": details}


def _create_context_response(context_el, status_code):
    """
    Function to build the context response model
    :param context_el: JSON including the context element attributes
    :param status_code: status code received from context manager
    :return (dict) Context response mode. The contextResponse in JSON will be like this:
        {
            "contextResponses" : [
                {
                    "contextElement" : {
                        "type" : "Room",
                        "isPattern" : "false",
                        "id" : "Room1",
                        "attributes" : [
                        {
                            "name" : "temperature",
                            "type" : "float",
                            "value" : "23"
                        }
                        ]
                    },
                    "statusCode" : {
                        "code" : "200",
                        "reasonPhrase" : "OK"
                    }
                }
            ]
        }

    """

    return {"contextElement": context_el,
            "statusCode": status_code}


def _create_context_notification(context_responses=None, originator=None, subscription_id=None):

    """
    Function to create the context notification model
    :param context_responses: List with all context responses from server
    :param originator: String with the originator identifier
    :param subscription_id: OpenStack subscription unique identifier
    :return (dict): The context notification request model. The request in JSON will be like this:
        {
            "subscriptionId" : "552f7481983d79a38fbd5a74",
            "originator" : "localhost",
            "contextResponses" : [
                {
                    "contextElement" : {
                        "type" : "Room",
                        "isPattern" : "false",
                        "id" : "Room1",
                        "attributes" : [
                        {
                            "name" : "temperature",
                            "type" : "float",
                            "value" : "23"
                        }
                        ]
                    },
                    "statusCode" : {
                        "code" : "200",
                        "reasonPhrase" : "OK"
                    }
                }
            ]
        }
    """

    return {"subscriptionId": subscription_id,
            "originator": originator,
            "contextResponses": context_responses}


def create_context_notification_model(subscription_id=None, originator=None,
                                      status_code=None, details=None, reason=None,
                                      type=None, is_pattern=None, id=None, attribute_list=None):
    """
    HELPER. Create a context notification with the given params (described in previous private functions).
    """

    context_element = _create_context_element(type, is_pattern, id, attribute_list)
    context_status = _create_context_status_code(status_code, details, reason)
    context_responses = _create_context_response(context_element,context_status)

    return _create_context_notification(context_responses, originator, subscription_id)

