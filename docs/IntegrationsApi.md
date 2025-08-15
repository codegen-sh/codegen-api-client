# codegen_api_client.IntegrationsApi

All URIs are relative to *https://api.codegen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get**](IntegrationsApi.md#get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get) | **GET** /v1/organizations/{org_id}/integrations | Get Organization Integrations Endpoint
[**get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_0**](IntegrationsApi.md#get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_0) | **GET** /v1/organizations/{org_id}/integrations | Get Organization Integrations Endpoint
[**get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_1**](IntegrationsApi.md#get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_1) | **GET** /v1/organizations/{org_id}/integrations | Get Organization Integrations Endpoint


# **get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get**
> OrganizationIntegrationsResponse get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get(org_id, authorization=authorization)

Get Organization Integrations Endpoint

Get all integration statuses for the given organization.

Returns a comprehensive overview of all integrations configured for the organization,
including:
- OAuth-based integrations (Slack, Linear, Notion, Figma, ClickUp, Jira, Sentry, Monday.com)
- GitHub app installations
- API key-based integrations (CircleCI)
- Database connections (PostgreSQL)

Each integration includes its current status (active/inactive), associated token/installation IDs,
and relevant metadata such as app names, organization names, etc.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.organization_integrations_response import OrganizationIntegrationsResponse
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
    api_instance = codegen_api_client.IntegrationsApi(api_client)
    org_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Organization Integrations Endpoint
        api_response = api_instance.get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get(org_id, authorization=authorization)
        print("The response of IntegrationsApi->get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**OrganizationIntegrationsResponse**](OrganizationIntegrationsResponse.md)

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

# **get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_0**
> OrganizationIntegrationsResponse get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_0(org_id, authorization=authorization)

Get Organization Integrations Endpoint

Get all integration statuses for the given organization.

Returns a comprehensive overview of all integrations configured for the organization,
including:
- OAuth-based integrations (Slack, Linear, Notion, Figma, ClickUp, Jira, Sentry, Monday.com)
- GitHub app installations
- API key-based integrations (CircleCI)
- Database connections (PostgreSQL)

Each integration includes its current status (active/inactive), associated token/installation IDs,
and relevant metadata such as app names, organization names, etc.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.organization_integrations_response import OrganizationIntegrationsResponse
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
    api_instance = codegen_api_client.IntegrationsApi(api_client)
    org_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Organization Integrations Endpoint
        api_response = api_instance.get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_0(org_id, authorization=authorization)
        print("The response of IntegrationsApi->get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**OrganizationIntegrationsResponse**](OrganizationIntegrationsResponse.md)

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

# **get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_1**
> OrganizationIntegrationsResponse get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_1(org_id, authorization=authorization)

Get Organization Integrations Endpoint

Get all integration statuses for the given organization.

Returns a comprehensive overview of all integrations configured for the organization,
including:
- OAuth-based integrations (Slack, Linear, Notion, Figma, ClickUp, Jira, Sentry, Monday.com)
- GitHub app installations
- API key-based integrations (CircleCI)
- Database connections (PostgreSQL)

Each integration includes its current status (active/inactive), associated token/installation IDs,
and relevant metadata such as app names, organization names, etc.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.organization_integrations_response import OrganizationIntegrationsResponse
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
    api_instance = codegen_api_client.IntegrationsApi(api_client)
    org_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Organization Integrations Endpoint
        api_response = api_instance.get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_1(org_id, authorization=authorization)
        print("The response of IntegrationsApi->get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_organization_integrations_endpoint_v1_organizations_org_id_integrations_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**OrganizationIntegrationsResponse**](OrganizationIntegrationsResponse.md)

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

