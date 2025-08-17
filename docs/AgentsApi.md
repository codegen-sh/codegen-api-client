# codegen_api_client.AgentsApi

All URIs are relative to *https://api.codegen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post**](AgentsApi.md#ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post) | **POST** /v1/organizations/{org_id}/agent/run/ban | Ban All Checks For Agent Run
[**ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_0**](AgentsApi.md#ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_0) | **POST** /v1/organizations/{org_id}/agent/run/ban | Ban All Checks For Agent Run
[**ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_1**](AgentsApi.md#ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_1) | **POST** /v1/organizations/{org_id}/agent/run/ban | Ban All Checks For Agent Run
[**create_agent_run_v1_organizations_org_id_agent_run_post**](AgentsApi.md#create_agent_run_v1_organizations_org_id_agent_run_post) | **POST** /v1/organizations/{org_id}/agent/run | Create Agent Run
[**create_agent_run_v1_organizations_org_id_agent_run_post_0**](AgentsApi.md#create_agent_run_v1_organizations_org_id_agent_run_post_0) | **POST** /v1/organizations/{org_id}/agent/run | Create Agent Run
[**create_agent_run_v1_organizations_org_id_agent_run_post_1**](AgentsApi.md#create_agent_run_v1_organizations_org_id_agent_run_post_1) | **POST** /v1/organizations/{org_id}/agent/run | Create Agent Run
[**get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get**](AgentsApi.md#get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get) | **GET** /v1/organizations/{org_id}/agent/run/{agent_run_id} | Get Agent Run
[**get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0**](AgentsApi.md#get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0) | **GET** /v1/organizations/{org_id}/agent/run/{agent_run_id} | Get Agent Run
[**get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1**](AgentsApi.md#get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1) | **GET** /v1/organizations/{org_id}/agent/run/{agent_run_id} | Get Agent Run
[**list_agent_runs_v1_organizations_org_id_agent_runs_get**](AgentsApi.md#list_agent_runs_v1_organizations_org_id_agent_runs_get) | **GET** /v1/organizations/{org_id}/agent/runs | List Agent Runs
[**list_agent_runs_v1_organizations_org_id_agent_runs_get_0**](AgentsApi.md#list_agent_runs_v1_organizations_org_id_agent_runs_get_0) | **GET** /v1/organizations/{org_id}/agent/runs | List Agent Runs
[**list_agent_runs_v1_organizations_org_id_agent_runs_get_1**](AgentsApi.md#list_agent_runs_v1_organizations_org_id_agent_runs_get_1) | **GET** /v1/organizations/{org_id}/agent/runs | List Agent Runs
[**remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post**](AgentsApi.md#remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post) | **POST** /v1/organizations/{org_id}/agent/run/remove-from-pr | Remove Codegen From Pr
[**remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_0**](AgentsApi.md#remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_0) | **POST** /v1/organizations/{org_id}/agent/run/remove-from-pr | Remove Codegen From Pr
[**remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_1**](AgentsApi.md#remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_1) | **POST** /v1/organizations/{org_id}/agent/run/remove-from-pr | Remove Codegen From Pr
[**resume_agent_run_v1_organizations_org_id_agent_run_resume_post**](AgentsApi.md#resume_agent_run_v1_organizations_org_id_agent_run_resume_post) | **POST** /v1/organizations/{org_id}/agent/run/resume | Resume Agent Run
[**resume_agent_run_v1_organizations_org_id_agent_run_resume_post_0**](AgentsApi.md#resume_agent_run_v1_organizations_org_id_agent_run_resume_post_0) | **POST** /v1/organizations/{org_id}/agent/run/resume | Resume Agent Run
[**resume_agent_run_v1_organizations_org_id_agent_run_resume_post_1**](AgentsApi.md#resume_agent_run_v1_organizations_org_id_agent_run_resume_post_1) | **POST** /v1/organizations/{org_id}/agent/run/resume | Resume Agent Run
[**unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post**](AgentsApi.md#unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post) | **POST** /v1/organizations/{org_id}/agent/run/unban | Unban All Checks For Agent Run
[**unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_0**](AgentsApi.md#unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_0) | **POST** /v1/organizations/{org_id}/agent/run/unban | Unban All Checks For Agent Run
[**unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_1**](AgentsApi.md#unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_1) | **POST** /v1/organizations/{org_id}/agent/run/unban | Unban All Checks For Agent Run


# **ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post**
> object ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post(org_id, stop_agent_run_input, authorization=authorization)

Ban All Checks For Agent Run

Ban all checks for a PR and stop all related agents.

This endpoint:
1. Flags the PR to prevent future CI/CD check suite events from being processed
2. Stops all current agents for that PR

### Example


```python
import codegen_api_client
from codegen_api_client.models.stop_agent_run_input import StopAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    stop_agent_run_input = codegen_api_client.StopAgentRunInput() # StopAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Ban All Checks For Agent Run
        api_response = api_instance.ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post(org_id, stop_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **stop_agent_run_input** | [**StopAgentRunInput**](StopAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_0**
> object ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_0(org_id, stop_agent_run_input, authorization=authorization)

Ban All Checks For Agent Run

Ban all checks for a PR and stop all related agents.

This endpoint:
1. Flags the PR to prevent future CI/CD check suite events from being processed
2. Stops all current agents for that PR

### Example


```python
import codegen_api_client
from codegen_api_client.models.stop_agent_run_input import StopAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    stop_agent_run_input = codegen_api_client.StopAgentRunInput() # StopAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Ban All Checks For Agent Run
        api_response = api_instance.ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_0(org_id, stop_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **stop_agent_run_input** | [**StopAgentRunInput**](StopAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_1**
> object ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_1(org_id, stop_agent_run_input, authorization=authorization)

Ban All Checks For Agent Run

Ban all checks for a PR and stop all related agents.

This endpoint:
1. Flags the PR to prevent future CI/CD check suite events from being processed
2. Stops all current agents for that PR

### Example


```python
import codegen_api_client
from codegen_api_client.models.stop_agent_run_input import StopAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    stop_agent_run_input = codegen_api_client.StopAgentRunInput() # StopAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Ban All Checks For Agent Run
        api_response = api_instance.ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_1(org_id, stop_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->ban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_ban_post_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **stop_agent_run_input** | [**StopAgentRunInput**](StopAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_run_v1_organizations_org_id_agent_run_post**
> AgentRunResponse create_agent_run_v1_organizations_org_id_agent_run_post(org_id, create_agent_run_input, authorization=authorization)

Create Agent Run

Create a new agent run.

Creates and initiates a long-running agent process based on the provided prompt.
The process will complete asynchronously, and the response contains the agent run ID
which can be used to check the status later. The requesting user must be a member
of the specified organization.

This endpoint accepts both a text prompt and an optional image file upload.

Rate limit: 10 requests per minute.

### Example


```python
import codegen_api_client
from codegen_api_client.models.agent_run_response import AgentRunResponse
from codegen_api_client.models.create_agent_run_input import CreateAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    create_agent_run_input = codegen_api_client.CreateAgentRunInput() # CreateAgentRunInput | 
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
**429** | Too Many Requests |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_run_v1_organizations_org_id_agent_run_post_0**
> AgentRunResponse create_agent_run_v1_organizations_org_id_agent_run_post_0(org_id, create_agent_run_input, authorization=authorization)

Create Agent Run

Create a new agent run.

Creates and initiates a long-running agent process based on the provided prompt.
The process will complete asynchronously, and the response contains the agent run ID
which can be used to check the status later. The requesting user must be a member
of the specified organization.

This endpoint accepts both a text prompt and an optional image file upload.

Rate limit: 10 requests per minute.

### Example


```python
import codegen_api_client
from codegen_api_client.models.agent_run_response import AgentRunResponse
from codegen_api_client.models.create_agent_run_input import CreateAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    create_agent_run_input = codegen_api_client.CreateAgentRunInput() # CreateAgentRunInput | 
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
**429** | Too Many Requests |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_run_v1_organizations_org_id_agent_run_post_1**
> AgentRunResponse create_agent_run_v1_organizations_org_id_agent_run_post_1(org_id, create_agent_run_input, authorization=authorization)

Create Agent Run

Create a new agent run.

Creates and initiates a long-running agent process based on the provided prompt.
The process will complete asynchronously, and the response contains the agent run ID
which can be used to check the status later. The requesting user must be a member
of the specified organization.

This endpoint accepts both a text prompt and an optional image file upload.

Rate limit: 10 requests per minute.

### Example


```python
import codegen_api_client
from codegen_api_client.models.agent_run_response import AgentRunResponse
from codegen_api_client.models.create_agent_run_input import CreateAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    create_agent_run_input = codegen_api_client.CreateAgentRunInput() # CreateAgentRunInput | 
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
**429** | Too Many Requests |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get**
> AgentRunResponse get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get(agent_run_id, org_id, authorization=authorization)

Get Agent Run

Retrieve the status and result of an agent run.

Returns the current status, progress, and any available results for the specified agent run.
The agent run must belong to the specified organization. If the agent run is still in progress,
this endpoint can be polled to check for completion.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.agent_run_response import AgentRunResponse
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
    api_instance = codegen_api_client.AgentsApi(api_client)
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0**
> AgentRunResponse get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_0(agent_run_id, org_id, authorization=authorization)

Get Agent Run

Retrieve the status and result of an agent run.

Returns the current status, progress, and any available results for the specified agent run.
The agent run must belong to the specified organization. If the agent run is still in progress,
this endpoint can be polled to check for completion.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.agent_run_response import AgentRunResponse
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
    api_instance = codegen_api_client.AgentsApi(api_client)
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1**
> AgentRunResponse get_agent_run_v1_organizations_org_id_agent_run_agent_run_id_get_1(agent_run_id, org_id, authorization=authorization)

Get Agent Run

Retrieve the status and result of an agent run.

Returns the current status, progress, and any available results for the specified agent run.
The agent run must belong to the specified organization. If the agent run is still in progress,
this endpoint can be polled to check for completion.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.agent_run_response import AgentRunResponse
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
    api_instance = codegen_api_client.AgentsApi(api_client)
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agent_runs_v1_organizations_org_id_agent_runs_get**
> PageAgentRunResponse list_agent_runs_v1_organizations_org_id_agent_runs_get(org_id, user_id=user_id, source_type=source_type, skip=skip, limit=limit, authorization=authorization)

List Agent Runs

List agent runs for an organization with optional user filtering.

Returns a paginated list of agent runs for the specified organization.
Optionally filter by user_id to get only agent runs initiated by a specific user.
Results are ordered by creation date (newest first).

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.api_agent_run_source_type import ApiAgentRunSourceType
from codegen_api_client.models.page_agent_run_response import PageAgentRunResponse
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    user_id = 56 # int | Filter by user ID who initiated the agent runs (optional)
    source_type = codegen_api_client.ApiAgentRunSourceType() # ApiAgentRunSourceType | Filter by source type of the agent runs (optional)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # List Agent Runs
        api_response = api_instance.list_agent_runs_v1_organizations_org_id_agent_runs_get(org_id, user_id=user_id, source_type=source_type, skip=skip, limit=limit, authorization=authorization)
        print("The response of AgentsApi->list_agent_runs_v1_organizations_org_id_agent_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_agent_runs_v1_organizations_org_id_agent_runs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **user_id** | **int**| Filter by user ID who initiated the agent runs | [optional] 
 **source_type** | [**ApiAgentRunSourceType**](.md)| Filter by source type of the agent runs | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageAgentRunResponse**](PageAgentRunResponse.md)

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

# **list_agent_runs_v1_organizations_org_id_agent_runs_get_0**
> PageAgentRunResponse list_agent_runs_v1_organizations_org_id_agent_runs_get_0(org_id, user_id=user_id, source_type=source_type, skip=skip, limit=limit, authorization=authorization)

List Agent Runs

List agent runs for an organization with optional user filtering.

Returns a paginated list of agent runs for the specified organization.
Optionally filter by user_id to get only agent runs initiated by a specific user.
Results are ordered by creation date (newest first).

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.api_agent_run_source_type import ApiAgentRunSourceType
from codegen_api_client.models.page_agent_run_response import PageAgentRunResponse
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    user_id = 56 # int | Filter by user ID who initiated the agent runs (optional)
    source_type = codegen_api_client.ApiAgentRunSourceType() # ApiAgentRunSourceType | Filter by source type of the agent runs (optional)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # List Agent Runs
        api_response = api_instance.list_agent_runs_v1_organizations_org_id_agent_runs_get_0(org_id, user_id=user_id, source_type=source_type, skip=skip, limit=limit, authorization=authorization)
        print("The response of AgentsApi->list_agent_runs_v1_organizations_org_id_agent_runs_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_agent_runs_v1_organizations_org_id_agent_runs_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **user_id** | **int**| Filter by user ID who initiated the agent runs | [optional] 
 **source_type** | [**ApiAgentRunSourceType**](.md)| Filter by source type of the agent runs | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageAgentRunResponse**](PageAgentRunResponse.md)

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

# **list_agent_runs_v1_organizations_org_id_agent_runs_get_1**
> PageAgentRunResponse list_agent_runs_v1_organizations_org_id_agent_runs_get_1(org_id, user_id=user_id, source_type=source_type, skip=skip, limit=limit, authorization=authorization)

List Agent Runs

List agent runs for an organization with optional user filtering.

Returns a paginated list of agent runs for the specified organization.
Optionally filter by user_id to get only agent runs initiated by a specific user.
Results are ordered by creation date (newest first).

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.api_agent_run_source_type import ApiAgentRunSourceType
from codegen_api_client.models.page_agent_run_response import PageAgentRunResponse
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    user_id = 56 # int | Filter by user ID who initiated the agent runs (optional)
    source_type = codegen_api_client.ApiAgentRunSourceType() # ApiAgentRunSourceType | Filter by source type of the agent runs (optional)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # List Agent Runs
        api_response = api_instance.list_agent_runs_v1_organizations_org_id_agent_runs_get_1(org_id, user_id=user_id, source_type=source_type, skip=skip, limit=limit, authorization=authorization)
        print("The response of AgentsApi->list_agent_runs_v1_organizations_org_id_agent_runs_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_agent_runs_v1_organizations_org_id_agent_runs_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **user_id** | **int**| Filter by user ID who initiated the agent runs | [optional] 
 **source_type** | [**ApiAgentRunSourceType**](.md)| Filter by source type of the agent runs | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageAgentRunResponse**](PageAgentRunResponse.md)

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

# **remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post**
> object remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post(org_id, stop_agent_run_input, authorization=authorization)

Remove Codegen From Pr

Remove Codegen from a PR.

This endpoint performs the same action as banning all checks but with more user-friendly naming.
It:
1. Flags the PR to prevent future CI/CD check suite events from being processed
2. Stops all current agents for that PR

### Example


```python
import codegen_api_client
from codegen_api_client.models.stop_agent_run_input import StopAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    stop_agent_run_input = codegen_api_client.StopAgentRunInput() # StopAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Remove Codegen From Pr
        api_response = api_instance.remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post(org_id, stop_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **stop_agent_run_input** | [**StopAgentRunInput**](StopAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_0**
> object remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_0(org_id, stop_agent_run_input, authorization=authorization)

Remove Codegen From Pr

Remove Codegen from a PR.

This endpoint performs the same action as banning all checks but with more user-friendly naming.
It:
1. Flags the PR to prevent future CI/CD check suite events from being processed
2. Stops all current agents for that PR

### Example


```python
import codegen_api_client
from codegen_api_client.models.stop_agent_run_input import StopAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    stop_agent_run_input = codegen_api_client.StopAgentRunInput() # StopAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Remove Codegen From Pr
        api_response = api_instance.remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_0(org_id, stop_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **stop_agent_run_input** | [**StopAgentRunInput**](StopAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_1**
> object remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_1(org_id, stop_agent_run_input, authorization=authorization)

Remove Codegen From Pr

Remove Codegen from a PR.

This endpoint performs the same action as banning all checks but with more user-friendly naming.
It:
1. Flags the PR to prevent future CI/CD check suite events from being processed
2. Stops all current agents for that PR

### Example


```python
import codegen_api_client
from codegen_api_client.models.stop_agent_run_input import StopAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    stop_agent_run_input = codegen_api_client.StopAgentRunInput() # StopAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Remove Codegen From Pr
        api_response = api_instance.remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_1(org_id, stop_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->remove_codegen_from_pr_v1_organizations_org_id_agent_run_remove_from_pr_post_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **stop_agent_run_input** | [**StopAgentRunInput**](StopAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_agent_run_v1_organizations_org_id_agent_run_resume_post**
> AgentRunResponse resume_agent_run_v1_organizations_org_id_agent_run_resume_post(org_id, resume_agent_run_input, authorization=authorization)

Resume Agent Run

Resume a paused agent run.

Resumes a paused agent run, allowing it to continue processing.

### Example


```python
import codegen_api_client
from codegen_api_client.models.agent_run_response import AgentRunResponse
from codegen_api_client.models.resume_agent_run_input import ResumeAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    resume_agent_run_input = codegen_api_client.ResumeAgentRunInput() # ResumeAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Resume Agent Run
        api_response = api_instance.resume_agent_run_v1_organizations_org_id_agent_run_resume_post(org_id, resume_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->resume_agent_run_v1_organizations_org_id_agent_run_resume_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->resume_agent_run_v1_organizations_org_id_agent_run_resume_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **resume_agent_run_input** | [**ResumeAgentRunInput**](ResumeAgentRunInput.md)|  | 
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_agent_run_v1_organizations_org_id_agent_run_resume_post_0**
> AgentRunResponse resume_agent_run_v1_organizations_org_id_agent_run_resume_post_0(org_id, resume_agent_run_input, authorization=authorization)

Resume Agent Run

Resume a paused agent run.

Resumes a paused agent run, allowing it to continue processing.

### Example


```python
import codegen_api_client
from codegen_api_client.models.agent_run_response import AgentRunResponse
from codegen_api_client.models.resume_agent_run_input import ResumeAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    resume_agent_run_input = codegen_api_client.ResumeAgentRunInput() # ResumeAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Resume Agent Run
        api_response = api_instance.resume_agent_run_v1_organizations_org_id_agent_run_resume_post_0(org_id, resume_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->resume_agent_run_v1_organizations_org_id_agent_run_resume_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->resume_agent_run_v1_organizations_org_id_agent_run_resume_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **resume_agent_run_input** | [**ResumeAgentRunInput**](ResumeAgentRunInput.md)|  | 
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_agent_run_v1_organizations_org_id_agent_run_resume_post_1**
> AgentRunResponse resume_agent_run_v1_organizations_org_id_agent_run_resume_post_1(org_id, resume_agent_run_input, authorization=authorization)

Resume Agent Run

Resume a paused agent run.

Resumes a paused agent run, allowing it to continue processing.

### Example


```python
import codegen_api_client
from codegen_api_client.models.agent_run_response import AgentRunResponse
from codegen_api_client.models.resume_agent_run_input import ResumeAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    resume_agent_run_input = codegen_api_client.ResumeAgentRunInput() # ResumeAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Resume Agent Run
        api_response = api_instance.resume_agent_run_v1_organizations_org_id_agent_run_resume_post_1(org_id, resume_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->resume_agent_run_v1_organizations_org_id_agent_run_resume_post_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->resume_agent_run_v1_organizations_org_id_agent_run_resume_post_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **resume_agent_run_input** | [**ResumeAgentRunInput**](ResumeAgentRunInput.md)|  | 
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post**
> object unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post(org_id, stop_agent_run_input, authorization=authorization)

Unban All Checks For Agent Run

Unban all checks for a PR.

This endpoint:
1. Removes the ban flag from the PR to allow future CI/CD check suite events to be processed
2. Handles both URL-based bans and parent-agent-run-based bans

### Example


```python
import codegen_api_client
from codegen_api_client.models.stop_agent_run_input import StopAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    stop_agent_run_input = codegen_api_client.StopAgentRunInput() # StopAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Unban All Checks For Agent Run
        api_response = api_instance.unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post(org_id, stop_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **stop_agent_run_input** | [**StopAgentRunInput**](StopAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_0**
> object unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_0(org_id, stop_agent_run_input, authorization=authorization)

Unban All Checks For Agent Run

Unban all checks for a PR.

This endpoint:
1. Removes the ban flag from the PR to allow future CI/CD check suite events to be processed
2. Handles both URL-based bans and parent-agent-run-based bans

### Example


```python
import codegen_api_client
from codegen_api_client.models.stop_agent_run_input import StopAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    stop_agent_run_input = codegen_api_client.StopAgentRunInput() # StopAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Unban All Checks For Agent Run
        api_response = api_instance.unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_0(org_id, stop_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **stop_agent_run_input** | [**StopAgentRunInput**](StopAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_1**
> object unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_1(org_id, stop_agent_run_input, authorization=authorization)

Unban All Checks For Agent Run

Unban all checks for a PR.

This endpoint:
1. Removes the ban flag from the PR to allow future CI/CD check suite events to be processed
2. Handles both URL-based bans and parent-agent-run-based bans

### Example


```python
import codegen_api_client
from codegen_api_client.models.stop_agent_run_input import StopAgentRunInput
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
    api_instance = codegen_api_client.AgentsApi(api_client)
    org_id = 56 # int | 
    stop_agent_run_input = codegen_api_client.StopAgentRunInput() # StopAgentRunInput | 
    authorization = None # object |  (optional)

    try:
        # Unban All Checks For Agent Run
        api_response = api_instance.unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_1(org_id, stop_agent_run_input, authorization=authorization)
        print("The response of AgentsApi->unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->unban_all_checks_for_agent_run_v1_organizations_org_id_agent_run_unban_post_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **stop_agent_run_input** | [**StopAgentRunInput**](StopAgentRunInput.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

