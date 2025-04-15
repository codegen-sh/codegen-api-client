# openapi_client.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organizations_v1_organizations_get**](OrganizationsApi.md#get_organizations_v1_organizations_get) | **GET** /v1/organizations | Get Organizations
[**get_organizations_v1_organizations_get_0**](OrganizationsApi.md#get_organizations_v1_organizations_get_0) | **GET** /v1/organizations | Get Organizations
[**get_organizations_v1_organizations_get_1**](OrganizationsApi.md#get_organizations_v1_organizations_get_1) | **GET** /v1/organizations | Get Organizations


# **get_organizations_v1_organizations_get**
> PageOrganizationResponse get_organizations_v1_organizations_get(skip=skip, limit=limit, authorization=authorization)

Get Organizations

Get organizations for the authenticated user.

Returns a paginated list of all organizations that the authenticated user is a member of.
Results include basic organization details such as name, ID, and membership information.
Use pagination parameters to control the number of results returned.

### Example


```python
import openapi_client
from openapi_client.models.page_organization_response import PageOrganizationResponse
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
    api_instance = openapi_client.OrganizationsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # Get Organizations
        api_response = api_instance.get_organizations_v1_organizations_get(skip=skip, limit=limit, authorization=authorization)
        print("The response of OrganizationsApi->get_organizations_v1_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organizations_v1_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageOrganizationResponse**](PageOrganizationResponse.md)

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

# **get_organizations_v1_organizations_get_0**
> PageOrganizationResponse get_organizations_v1_organizations_get_0(skip=skip, limit=limit, authorization=authorization)

Get Organizations

Get organizations for the authenticated user.

Returns a paginated list of all organizations that the authenticated user is a member of.
Results include basic organization details such as name, ID, and membership information.
Use pagination parameters to control the number of results returned.

### Example


```python
import openapi_client
from openapi_client.models.page_organization_response import PageOrganizationResponse
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
    api_instance = openapi_client.OrganizationsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # Get Organizations
        api_response = api_instance.get_organizations_v1_organizations_get_0(skip=skip, limit=limit, authorization=authorization)
        print("The response of OrganizationsApi->get_organizations_v1_organizations_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organizations_v1_organizations_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageOrganizationResponse**](PageOrganizationResponse.md)

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

# **get_organizations_v1_organizations_get_1**
> PageOrganizationResponse get_organizations_v1_organizations_get_1(skip=skip, limit=limit, authorization=authorization)

Get Organizations

Get organizations for the authenticated user.

Returns a paginated list of all organizations that the authenticated user is a member of.
Results include basic organization details such as name, ID, and membership information.
Use pagination parameters to control the number of results returned.

### Example


```python
import openapi_client
from openapi_client.models.page_organization_response import PageOrganizationResponse
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
    api_instance = openapi_client.OrganizationsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # Get Organizations
        api_response = api_instance.get_organizations_v1_organizations_get_1(skip=skip, limit=limit, authorization=authorization)
        print("The response of OrganizationsApi->get_organizations_v1_organizations_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organizations_v1_organizations_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageOrganizationResponse**](PageOrganizationResponse.md)

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

