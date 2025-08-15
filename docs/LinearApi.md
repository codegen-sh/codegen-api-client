# codegen_api_client.LinearApi

All URIs are relative to *https://api.codegen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_linear_projects_v1_linear_projects_get**](LinearApi.md#get_linear_projects_v1_linear_projects_get) | **GET** /v1/linear/projects | Get Linear Projects
[**get_linear_projects_v1_linear_projects_get_0**](LinearApi.md#get_linear_projects_v1_linear_projects_get_0) | **GET** /v1/linear/projects | Get Linear Projects
[**get_linear_projects_v1_linear_projects_get_1**](LinearApi.md#get_linear_projects_v1_linear_projects_get_1) | **GET** /v1/linear/projects | Get Linear Projects
[**get_linear_teams_v1_linear_teams_get**](LinearApi.md#get_linear_teams_v1_linear_teams_get) | **GET** /v1/linear/teams | Get Linear Teams
[**get_linear_teams_v1_linear_teams_get_0**](LinearApi.md#get_linear_teams_v1_linear_teams_get_0) | **GET** /v1/linear/teams | Get Linear Teams
[**get_linear_teams_v1_linear_teams_get_1**](LinearApi.md#get_linear_teams_v1_linear_teams_get_1) | **GET** /v1/linear/teams | Get Linear Teams


# **get_linear_projects_v1_linear_projects_get**
> object get_linear_projects_v1_linear_projects_get(authorization=authorization, x_organization_id=x_organization_id)

Get Linear Projects

Get Linear projects for the authenticated user's organization.

Returns a list of all Linear projects that the authenticated user has access to
within the specified organization. This endpoint is used to populate project
selection dropdowns in repository settings.

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
    api_instance = codegen_api_client.LinearApi(api_client)
    authorization = None # object |  (optional)
    x_organization_id = None # object |  (optional)

    try:
        # Get Linear Projects
        api_response = api_instance.get_linear_projects_v1_linear_projects_get(authorization=authorization, x_organization_id=x_organization_id)
        print("The response of LinearApi->get_linear_projects_v1_linear_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinearApi->get_linear_projects_v1_linear_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | [**object**](.md)|  | [optional] 
 **x_organization_id** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linear_projects_v1_linear_projects_get_0**
> object get_linear_projects_v1_linear_projects_get_0(authorization=authorization, x_organization_id=x_organization_id)

Get Linear Projects

Get Linear projects for the authenticated user's organization.

Returns a list of all Linear projects that the authenticated user has access to
within the specified organization. This endpoint is used to populate project
selection dropdowns in repository settings.

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
    api_instance = codegen_api_client.LinearApi(api_client)
    authorization = None # object |  (optional)
    x_organization_id = None # object |  (optional)

    try:
        # Get Linear Projects
        api_response = api_instance.get_linear_projects_v1_linear_projects_get_0(authorization=authorization, x_organization_id=x_organization_id)
        print("The response of LinearApi->get_linear_projects_v1_linear_projects_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinearApi->get_linear_projects_v1_linear_projects_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | [**object**](.md)|  | [optional] 
 **x_organization_id** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linear_projects_v1_linear_projects_get_1**
> object get_linear_projects_v1_linear_projects_get_1(authorization=authorization, x_organization_id=x_organization_id)

Get Linear Projects

Get Linear projects for the authenticated user's organization.

Returns a list of all Linear projects that the authenticated user has access to
within the specified organization. This endpoint is used to populate project
selection dropdowns in repository settings.

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
    api_instance = codegen_api_client.LinearApi(api_client)
    authorization = None # object |  (optional)
    x_organization_id = None # object |  (optional)

    try:
        # Get Linear Projects
        api_response = api_instance.get_linear_projects_v1_linear_projects_get_1(authorization=authorization, x_organization_id=x_organization_id)
        print("The response of LinearApi->get_linear_projects_v1_linear_projects_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinearApi->get_linear_projects_v1_linear_projects_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | [**object**](.md)|  | [optional] 
 **x_organization_id** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linear_teams_v1_linear_teams_get**
> object get_linear_teams_v1_linear_teams_get(authorization=authorization, x_organization_id=x_organization_id)

Get Linear Teams

Get Linear teams for the authenticated user's organization.

Returns a list of all Linear teams that the authenticated user has access to
within the specified organization. This endpoint is used to populate team
selection dropdowns in repository settings.

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
    api_instance = codegen_api_client.LinearApi(api_client)
    authorization = None # object |  (optional)
    x_organization_id = None # object |  (optional)

    try:
        # Get Linear Teams
        api_response = api_instance.get_linear_teams_v1_linear_teams_get(authorization=authorization, x_organization_id=x_organization_id)
        print("The response of LinearApi->get_linear_teams_v1_linear_teams_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinearApi->get_linear_teams_v1_linear_teams_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | [**object**](.md)|  | [optional] 
 **x_organization_id** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linear_teams_v1_linear_teams_get_0**
> object get_linear_teams_v1_linear_teams_get_0(authorization=authorization, x_organization_id=x_organization_id)

Get Linear Teams

Get Linear teams for the authenticated user's organization.

Returns a list of all Linear teams that the authenticated user has access to
within the specified organization. This endpoint is used to populate team
selection dropdowns in repository settings.

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
    api_instance = codegen_api_client.LinearApi(api_client)
    authorization = None # object |  (optional)
    x_organization_id = None # object |  (optional)

    try:
        # Get Linear Teams
        api_response = api_instance.get_linear_teams_v1_linear_teams_get_0(authorization=authorization, x_organization_id=x_organization_id)
        print("The response of LinearApi->get_linear_teams_v1_linear_teams_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinearApi->get_linear_teams_v1_linear_teams_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | [**object**](.md)|  | [optional] 
 **x_organization_id** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linear_teams_v1_linear_teams_get_1**
> object get_linear_teams_v1_linear_teams_get_1(authorization=authorization, x_organization_id=x_organization_id)

Get Linear Teams

Get Linear teams for the authenticated user's organization.

Returns a list of all Linear teams that the authenticated user has access to
within the specified organization. This endpoint is used to populate team
selection dropdowns in repository settings.

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
    api_instance = codegen_api_client.LinearApi(api_client)
    authorization = None # object |  (optional)
    x_organization_id = None # object |  (optional)

    try:
        # Get Linear Teams
        api_response = api_instance.get_linear_teams_v1_linear_teams_get_1(authorization=authorization, x_organization_id=x_organization_id)
        print("The response of LinearApi->get_linear_teams_v1_linear_teams_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinearApi->get_linear_teams_v1_linear_teams_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | [**object**](.md)|  | [optional] 
 **x_organization_id** | [**object**](.md)|  | [optional] 

### Return type

**object**

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

