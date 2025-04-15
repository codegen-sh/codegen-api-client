# openapi_client.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_run_v1_organizations_org_id_agent_run_post**](AgentsApi.md#create_agent_run_v1_organizations_org_id_agent_run_post) | **POST** /v1/organizations/{org_id}/agent/run | Create Agent Run
[**create_agent_run_v1_organizations_org_id_agent_run_post_0**](AgentsApi.md#create_agent_run_v1_organizations_org_id_agent_run_post_0) | **POST** /v1/organizations/{org_id}/agent/run | Create Agent Run
[**create_agent_run_v1_organizations_org_id_agent_run_post_1**](AgentsApi.md#create_agent_run_v1_organizations_org_id_agent_run_post_1) | **POST** /v1/organizations/{org_id}/agent/run | Create Agent Run
[**get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get**](AgentsApi.md#get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get) | **GET** /v1/organizations/{org_id}/agent/run/{agent_run_id} | Get Agent Run
[**get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0**](AgentsApi.md#get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0) | **GET** /v1/organizations/{org_id}/agent/run/{agent_run_id} | Get Agent Run
[**get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1**](AgentsApi.md#get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1) | **GET** /v1/organizations/{org_id}/agent/run/{agent_run_id} | Get Agent Run


# **create_agent_run_v1_organizations_org_id_agent_run_post**
> AgentRunResponse create_agent_run_v1_organizations_org_id_agent_run_post(org_id, create_agent_run_input, authorization=authorization)

Create Agent Run

Create a new agent run.

Creates and initiates a long-running agent process based on the provided prompt.
The process will complete asynchronously, and the response contains the agent run ID
which can be used to check the status later. The requesting user must be a member
of the specified organization.

### Example


```python
import openapi_client
from openapi_client.models.agent_run_response import AgentRunResponse
from openapi_client.models.create_agent_run_input import CreateAgentRunInput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AgentsApi(api_client)
    org_id = 56 # int | 
    create_agent_run_input = openapi_client.CreateAgentRunInput() # CreateAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Create Agent Run
        api_response = api_instance.create_agent_run_v1_organizations_org_id_agent_run_post(org_id, create_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->create_agent_run_v1_organizations_org_id_agent_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->create_agent_run_v1_organizations_org_id_agent_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **create_agent_run_input** | [**CreateAgentRunInput**](CreateAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**AgentRunResponse**](AgentRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_run_v1_organizations_org_id_agent_run_post_0**
> AgentRunResponse create_agent_run_v1_organizations_org_id_agent_run_post_0(org_id, create_agent_run_input, authorization=authorization)

Create Agent Run

Create a new agent run.

Creates and initiates a long-running agent process based on the provided prompt.
The process will complete asynchronously, and the response contains the agent run ID
which can be used to check the status later. The requesting user must be a member
of the specified organization.

### Example


```python
import openapi_client
from openapi_client.models.agent_run_response import AgentRunResponse
from openapi_client.models.create_agent_run_input import CreateAgentRunInput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AgentsApi(api_client)
    org_id = 56 # int | 
    create_agent_run_input = openapi_client.CreateAgentRunInput() # CreateAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Create Agent Run
        api_response = api_instance.create_agent_run_v1_organizations_org_id_agent_run_post_0(org_id, create_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->create_agent_run_v1_organizations_org_id_agent_run_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->create_agent_run_v1_organizations_org_id_agent_run_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **create_agent_run_input** | [**CreateAgentRunInput**](CreateAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**AgentRunResponse**](AgentRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_run_v1_organizations_org_id_agent_run_post_1**
> AgentRunResponse create_agent_run_v1_organizations_org_id_agent_run_post_1(org_id, create_agent_run_input, authorization=authorization)

Create Agent Run

Create a new agent run.

Creates and initiates a long-running agent process based on the provided prompt.
The process will complete asynchronously, and the response contains the agent run ID
which can be used to check the status later. The requesting user must be a member
of the specified organization.

### Example


```python
import openapi_client
from openapi_client.models.agent_run_response import AgentRunResponse
from openapi_client.models.create_agent_run_input import CreateAgentRunInput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AgentsApi(api_client)
    org_id = 56 # int | 
    create_agent_run_input = openapi_client.CreateAgentRunInput() # CreateAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Create Agent Run
        api_response = api_instance.create_agent_run_v1_organizations_org_id_agent_run_post_1(org_id, create_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->create_agent_run_v1_organizations_org_id_agent_run_post_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->create_agent_run_v1_organizations_org_id_agent_run_post_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **create_agent_run_input** | [**CreateAgentRunInput**](CreateAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**AgentRunResponse**](AgentRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get**
> AgentRunResponse get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get(agent_run_id, org_id, authorization=authorization)

Get Agent Run

Retrieve the status and result of an agent run.

Returns the current status, progress, and any available results for the specified agent run.
The agent run must belong to the specified organization. If the agent run is still in progress,
this endpoint can be polled to check for completion.

### Example


```python
import openapi_client
from openapi_client.models.agent_run_response import AgentRunResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AgentsApi(api_client)
    agent_run_id = 56 # int | 
    org_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Agent Run
        api_response = api_instance.get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get(agent_run_id, org_id, authorization=authorization)
        print("The response of AgentsApi->get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_run_id** | **int**|  | 
 **org_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**AgentRunResponse**](AgentRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0**
> AgentRunResponse get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0(agent_run_id, org_id, authorization=authorization)

Get Agent Run

Retrieve the status and result of an agent run.

Returns the current status, progress, and any available results for the specified agent run.
The agent run must belong to the specified organization. If the agent run is still in progress,
this endpoint can be polled to check for completion.

### Example


```python
import openapi_client
from openapi_client.models.agent_run_response import AgentRunResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AgentsApi(api_client)
    agent_run_id = 56 # int | 
    org_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Agent Run
        api_response = api_instance.get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0(agent_run_id, org_id, authorization=authorization)
        print("The response of AgentsApi->get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_run_id** | **int**|  | 
 **org_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**AgentRunResponse**](AgentRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1**
> AgentRunResponse get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1(agent_run_id, org_id, authorization=authorization)

Get Agent Run

Retrieve the status and result of an agent run.

Returns the current status, progress, and any available results for the specified agent run.
The agent run must belong to the specified organization. If the agent run is still in progress,
this endpoint can be polled to check for completion.

### Example


```python
import openapi_client
from openapi_client.models.agent_run_response import AgentRunResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AgentsApi(api_client)
    agent_run_id = 56 # int | 
    org_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Agent Run
        api_response = api_instance.get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1(agent_run_id, org_id, authorization=authorization)
        print("The response of AgentsApi->get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_run_id** | **int**|  | 
 **org_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**AgentRunResponse**](AgentRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

