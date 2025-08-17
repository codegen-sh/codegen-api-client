# codegen_api_client.AgentsBetaApi

All URIs are relative to *https://api.codegen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_run_logs_v1_alpha_organizations_org_id_agent_run_agent_run_id_logs_get**](AgentsBetaApi.md#get_agent_run_logs_v1_alpha_organizations_org_id_agent_run_agent_run_id_logs_get) | **GET** /v1/alpha/organizations/{org_id}/agent/run/{agent_run_id}/logs | Get Agent Run Logs


# **get_agent_run_logs_v1_alpha_organizations_org_id_agent_run_agent_run_id_logs_get**
> AgentRunWithLogsResponse get_agent_run_logs_v1_alpha_organizations_org_id_agent_run_agent_run_id_logs_get(agent_run_id, org_id, skip=skip, limit=limit, authorization=authorization)

Get Agent Run Logs

Retrieve an agent run with its logs using pagination. This endpoint is currently in ALPHA and IS subject to change.

Returns the agent run details along with a paginated list of logs for the specified agent run.
The agent run must belong to the specified organization. Logs are returned in chronological order.
Uses standard pagination parameters (skip and limit) and includes pagination metadata in the response.

Rate limit: 60 requests per 60 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.agent_run_with_logs_response import AgentRunWithLogsResponse
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
    api_instance = codegen_api_client.AgentsBetaApi(api_client)
    agent_run_id = 56 # int | 
    org_id = 56 # int | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # Get Agent Run Logs
        api_response = api_instance.get_agent_run_logs_v1_alpha_organizations_org_id_agent_run_agent_run_id_logs_get(agent_run_id, org_id, skip=skip, limit=limit, authorization=authorization)
        print("The response of AgentsBetaApi->get_agent_run_logs_v1_alpha_organizations_org_id_agent_run_agent_run_id_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsBetaApi->get_agent_run_logs_v1_alpha_organizations_org_id_agent_run_agent_run_id_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_run_id** | **int**|  | 
 **org_id** | **int**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**AgentRunWithLogsResponse**](AgentRunWithLogsResponse.md)

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

