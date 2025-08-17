# codegen_api_client.ToolsApi

All URIs are relative to *https://api.codegen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_tool_v1_organizations_org_id_tools_execute_post**](ToolsApi.md#execute_tool_v1_organizations_org_id_tools_execute_post) | **POST** /v1/organizations/{org_id}/tools/execute | Execute Tool
[**execute_tool_v1_organizations_org_id_tools_execute_post_0**](ToolsApi.md#execute_tool_v1_organizations_org_id_tools_execute_post_0) | **POST** /v1/organizations/{org_id}/tools/execute | Execute Tool
[**execute_tool_v1_organizations_org_id_tools_execute_post_1**](ToolsApi.md#execute_tool_v1_organizations_org_id_tools_execute_post_1) | **POST** /v1/organizations/{org_id}/tools/execute | Execute Tool
[**get_available_tools_v1_organizations_org_id_tools_get**](ToolsApi.md#get_available_tools_v1_organizations_org_id_tools_get) | **GET** /v1/organizations/{org_id}/tools | Get Available Tools
[**get_available_tools_v1_organizations_org_id_tools_get_0**](ToolsApi.md#get_available_tools_v1_organizations_org_id_tools_get_0) | **GET** /v1/organizations/{org_id}/tools | Get Available Tools
[**get_available_tools_v1_organizations_org_id_tools_get_1**](ToolsApi.md#get_available_tools_v1_organizations_org_id_tools_get_1) | **GET** /v1/organizations/{org_id}/tools | Get Available Tools


# **execute_tool_v1_organizations_org_id_tools_execute_post**
> ToolExecutionResponse execute_tool_v1_organizations_org_id_tools_execute_post(org_id, tool_execution_request, authorization=authorization)

Execute Tool

Execute a specific tool with the provided arguments.

This endpoint allows direct execution of available tools by providing the tool name
and arguments as JSON. The tool will be executed in the context of the authenticated
user's organization and permissions.

The tool execution happens with the same permissions and context as if the tool
were called by an agent, ensuring proper security and access control.

Rate limit: 30 requests per minute.

### Example


```python
import codegen_api_client
from codegen_api_client.models.tool_execution_request import ToolExecutionRequest
from codegen_api_client.models.tool_execution_response import ToolExecutionResponse
from codegen_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.codegen.com
# See configuration.py for a list of all supported configuration parameters.
configuration = codegen_api_client.Configuration(
    host = "https://api.codegen.com"
)


# Enter a context with an instance of the API client
with codegen_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codegen_api_client.ToolsApi(api_client)
    org_id = 56 # int | 
    tool_execution_request = codegen_api_client.ToolExecutionRequest() # ToolExecutionRequest | 
    authorization = None # object |  (optional)

    try:
        # Execute Tool
        api_response = api_instance.execute_tool_v1_organizations_org_id_tools_execute_post(org_id, tool_execution_request, authorization=authorization)
        print("The response of ToolsApi->execute_tool_v1_organizations_org_id_tools_execute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->execute_tool_v1_organizations_org_id_tools_execute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **tool_execution_request** | [**ToolExecutionRequest**](ToolExecutionRequest.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**ToolExecutionResponse**](ToolExecutionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_tool_v1_organizations_org_id_tools_execute_post_0**
> ToolExecutionResponse execute_tool_v1_organizations_org_id_tools_execute_post_0(org_id, tool_execution_request, authorization=authorization)

Execute Tool

Execute a specific tool with the provided arguments.

This endpoint allows direct execution of available tools by providing the tool name
and arguments as JSON. The tool will be executed in the context of the authenticated
user's organization and permissions.

The tool execution happens with the same permissions and context as if the tool
were called by an agent, ensuring proper security and access control.

Rate limit: 30 requests per minute.

### Example


```python
import codegen_api_client
from codegen_api_client.models.tool_execution_request import ToolExecutionRequest
from codegen_api_client.models.tool_execution_response import ToolExecutionResponse
from codegen_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.codegen.com
# See configuration.py for a list of all supported configuration parameters.
configuration = codegen_api_client.Configuration(
    host = "https://api.codegen.com"
)


# Enter a context with an instance of the API client
with codegen_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codegen_api_client.ToolsApi(api_client)
    org_id = 56 # int | 
    tool_execution_request = codegen_api_client.ToolExecutionRequest() # ToolExecutionRequest | 
    authorization = None # object |  (optional)

    try:
        # Execute Tool
        api_response = api_instance.execute_tool_v1_organizations_org_id_tools_execute_post_0(org_id, tool_execution_request, authorization=authorization)
        print("The response of ToolsApi->execute_tool_v1_organizations_org_id_tools_execute_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->execute_tool_v1_organizations_org_id_tools_execute_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **tool_execution_request** | [**ToolExecutionRequest**](ToolExecutionRequest.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**ToolExecutionResponse**](ToolExecutionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_tool_v1_organizations_org_id_tools_execute_post_1**
> ToolExecutionResponse execute_tool_v1_organizations_org_id_tools_execute_post_1(org_id, tool_execution_request, authorization=authorization)

Execute Tool

Execute a specific tool with the provided arguments.

This endpoint allows direct execution of available tools by providing the tool name
and arguments as JSON. The tool will be executed in the context of the authenticated
user's organization and permissions.

The tool execution happens with the same permissions and context as if the tool
were called by an agent, ensuring proper security and access control.

Rate limit: 30 requests per minute.

### Example


```python
import codegen_api_client
from codegen_api_client.models.tool_execution_request import ToolExecutionRequest
from codegen_api_client.models.tool_execution_response import ToolExecutionResponse
from codegen_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.codegen.com
# See configuration.py for a list of all supported configuration parameters.
configuration = codegen_api_client.Configuration(
    host = "https://api.codegen.com"
)


# Enter a context with an instance of the API client
with codegen_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codegen_api_client.ToolsApi(api_client)
    org_id = 56 # int | 
    tool_execution_request = codegen_api_client.ToolExecutionRequest() # ToolExecutionRequest | 
    authorization = None # object |  (optional)

    try:
        # Execute Tool
        api_response = api_instance.execute_tool_v1_organizations_org_id_tools_execute_post_1(org_id, tool_execution_request, authorization=authorization)
        print("The response of ToolsApi->execute_tool_v1_organizations_org_id_tools_execute_post_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->execute_tool_v1_organizations_org_id_tools_execute_post_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **tool_execution_request** | [**ToolExecutionRequest**](ToolExecutionRequest.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**ToolExecutionResponse**](ToolExecutionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_tools_v1_organizations_org_id_tools_get**
> Dict[str, object] get_available_tools_v1_organizations_org_id_tools_get(org_id, repo_id=repo_id, authorization=authorization)

Get Available Tools

Get a list of all available tools for the given API token and organization.

Returns a comprehensive list of tools that can be used with the current API token,
including their names, descriptions, and parameter specifications. Tools are filtered
based on the organization's permissions and enabled integrations.

The response includes tool schemas that can be used to understand:
- Tool name and description
- Required and optional parameters
- Parameter types and constraints
- Default values where applicable

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.codegen.com
# See configuration.py for a list of all supported configuration parameters.
configuration = codegen_api_client.Configuration(
    host = "https://api.codegen.com"
)


# Enter a context with an instance of the API client
with codegen_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codegen_api_client.ToolsApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | Optional repository ID to filter tools for specific repository context (optional)
    authorization = None # object |  (optional)

    try:
        # Get Available Tools
        api_response = api_instance.get_available_tools_v1_organizations_org_id_tools_get(org_id, repo_id=repo_id, authorization=authorization)
        print("The response of ToolsApi->get_available_tools_v1_organizations_org_id_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_available_tools_v1_organizations_org_id_tools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**| Optional repository ID to filter tools for specific repository context | [optional] 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_tools_v1_organizations_org_id_tools_get_0**
> Dict[str, object] get_available_tools_v1_organizations_org_id_tools_get_0(org_id, repo_id=repo_id, authorization=authorization)

Get Available Tools

Get a list of all available tools for the given API token and organization.

Returns a comprehensive list of tools that can be used with the current API token,
including their names, descriptions, and parameter specifications. Tools are filtered
based on the organization's permissions and enabled integrations.

The response includes tool schemas that can be used to understand:
- Tool name and description
- Required and optional parameters
- Parameter types and constraints
- Default values where applicable

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.codegen.com
# See configuration.py for a list of all supported configuration parameters.
configuration = codegen_api_client.Configuration(
    host = "https://api.codegen.com"
)


# Enter a context with an instance of the API client
with codegen_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codegen_api_client.ToolsApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | Optional repository ID to filter tools for specific repository context (optional)
    authorization = None # object |  (optional)

    try:
        # Get Available Tools
        api_response = api_instance.get_available_tools_v1_organizations_org_id_tools_get_0(org_id, repo_id=repo_id, authorization=authorization)
        print("The response of ToolsApi->get_available_tools_v1_organizations_org_id_tools_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_available_tools_v1_organizations_org_id_tools_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**| Optional repository ID to filter tools for specific repository context | [optional] 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_tools_v1_organizations_org_id_tools_get_1**
> Dict[str, object] get_available_tools_v1_organizations_org_id_tools_get_1(org_id, repo_id=repo_id, authorization=authorization)

Get Available Tools

Get a list of all available tools for the given API token and organization.

Returns a comprehensive list of tools that can be used with the current API token,
including their names, descriptions, and parameter specifications. Tools are filtered
based on the organization's permissions and enabled integrations.

The response includes tool schemas that can be used to understand:
- Tool name and description
- Required and optional parameters
- Parameter types and constraints
- Default values where applicable

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.codegen.com
# See configuration.py for a list of all supported configuration parameters.
configuration = codegen_api_client.Configuration(
    host = "https://api.codegen.com"
)


# Enter a context with an instance of the API client
with codegen_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = codegen_api_client.ToolsApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | Optional repository ID to filter tools for specific repository context (optional)
    authorization = None # object |  (optional)

    try:
        # Get Available Tools
        api_response = api_instance.get_available_tools_v1_organizations_org_id_tools_get_1(org_id, repo_id=repo_id, authorization=authorization)
        print("The response of ToolsApi->get_available_tools_v1_organizations_org_id_tools_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_available_tools_v1_organizations_org_id_tools_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**| Optional repository ID to filter tools for specific repository context | [optional] 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

