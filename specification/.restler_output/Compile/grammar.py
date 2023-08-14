""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name = dependencies.DynamicVariable("_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name")

_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_tags = dependencies.DynamicVariable("_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_tags")

def parse_subscriptionssubscriptionIdresourceGroupsresourceGroupNameprovidersMicrosoftAnalysisServicesserversserverNameput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None
    temp_8173 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8173 = str(data["tags"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262 or temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name", temp_7262)
    if temp_8173:
        dependencies.set_variable("_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_tags", temp_8173)

req_collection = requests.RequestCollection([])
# Endpoint: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourceGroups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourceGroups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("serverName"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "properties":
        {
            "asAdministrators":
                {
                    "members":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["azsdktest@microsoft.com"]),
    primitives.restler_static_string(""",
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["azsdktest2@microsoft.com"]),
    primitives.restler_static_string("""
                    ]
                }
        }
    ,
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["West US"]),
    primitives.restler_static_string(""",
    "sku":
        {
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["S1"]),
    primitives.restler_static_string(""",
            "tier":"""),
    primitives.restler_fuzzable_group("tier", ['Development','Basic','Standard']  ,quoted=True, examples=["Standard"]),
    primitives.restler_static_string(""",
            "capacity":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("""
        }
    ,
    "tags":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"testKey\":\"testValue\"}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_subscriptionssubscriptionIdresourceGroupsresourceGroupNameprovidersMicrosoftAnalysisServicesserversserverNameput,
            'dependencies':
            [
                _subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name.writer(),
                _subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_tags.writer()
            ]
        }

    },

],
requestId="/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourceGroups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourceGroups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "sku":
        {
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["S1"]),
    primitives.restler_static_string(""",
            "tier":"""),
    primitives.restler_fuzzable_group("tier", ['Development','Basic','Standard']  ,quoted=True, examples=["Standard"]),
    primitives.restler_static_string(""",
            "capacity":"""),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("""
        }
    ,
    "tags":"""),
    primitives.restler_static_string(_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_tags.reader(), quoted=False),
    primitives.restler_static_string(""",
    "properties":
        {
            "asAdministrators":
                {
                    "members":
                    [
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["azsdktest@microsoft.com"]),
    primitives.restler_static_string(""",
                        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["azsdktest2@microsoft.com"]),
    primitives.restler_static_string("""
                    ]
                }
        }
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/suspend, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourceGroups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("suspend"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/suspend"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/resume, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourceGroups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resume"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/resume"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourceGroups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/servers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/servers"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/skus, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("skus"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/skus"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/skus, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourceGroups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("skus"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/skus"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/listGatewayStatus, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourceGroups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("listGatewayStatus"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/listGatewayStatus"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/dissociateGateway, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourceGroups"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("servers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_subscriptions__subscriptionId__resourceGroups__resourceGroupName__providers_Microsoft_AnalysisServices_servers__serverName__put_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dissociateGateway"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/dissociateGateway"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/checkNameAvailability, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("checkNameAvailability"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["azsdktest"]),
    primitives.restler_static_string(""",
    "type":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Microsoft.AnalysisServices/servers"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/checkNameAvailability"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/operationresults/{operationId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("operationresults"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/operationresults/{operationId}"
)
req_collection.add_request(request)

# Endpoint: /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/operationstatuses/{operationId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("locations"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("operationstatuses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2017-08-01"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/operationstatuses/{operationId}"
)
req_collection.add_request(request)

# Endpoint: /providers/Microsoft.AnalysisServices/operations, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("providers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Microsoft.AnalysisServices"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("operations"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("api-version="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: management.azure.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/providers/Microsoft.AnalysisServices/operations"
)
req_collection.add_request(request)
