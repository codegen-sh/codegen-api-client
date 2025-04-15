# openapi_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_v1_organizations_org_id_users_user_id_get**](UsersApi.md#get_user_v1_organizations_org_id_users_user_id_get) | **GET** /v1/organizations/{org_id}/users/{user_id} | Get User
[**get_user_v1_organizations_org_id_users_user_id_get_0**](UsersApi.md#get_user_v1_organizations_org_id_users_user_id_get_0) | **GET** /v1/organizations/{org_id}/users/{user_id} | Get User
[**get_user_v1_organizations_org_id_users_user_id_get_1**](UsersApi.md#get_user_v1_organizations_org_id_users_user_id_get_1) | **GET** /v1/organizations/{org_id}/users/{user_id} | Get User
[**get_users_v1_organizations_org_id_users_get**](UsersApi.md#get_users_v1_organizations_org_id_users_get) | **GET** /v1/organizations/{org_id}/users | Get Users
[**get_users_v1_organizations_org_id_users_get_0**](UsersApi.md#get_users_v1_organizations_org_id_users_get_0) | **GET** /v1/organizations/{org_id}/users | Get Users
[**get_users_v1_organizations_org_id_users_get_1**](UsersApi.md#get_users_v1_organizations_org_id_users_get_1) | **GET** /v1/organizations/{org_id}/users | Get Users


# **get_user_v1_organizations_org_id_users_user_id_get**
> UserResponse get_user_v1_organizations_org_id_users_user_id_get(org_id, user_id, authorization=authorization)

Get User

Get details for a specific user in an organization.

Returns detailed information about a user within the specified organization.
The requesting user must be a member of the organization to access this endpoint.

### Example


```python
import openapi_client
from openapi_client.models.user_response import UserResponse
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
    api_instance = openapi_client.UsersApi(api_client)
    org_id = 'org_id_example' # str | 
    user_id = 'user_id_example' # str | 
    authorization = None # object |  (optional)

    try:
        # Get User
        api_response = api_instance.get_user_v1_organizations_org_id_users_user_id_get(org_id, user_id, authorization=authorization)
        print("The response of UsersApi->get_user_v1_organizations_org_id_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_v1_organizations_org_id_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user_v1_organizations_org_id_users_user_id_get_0**
> UserResponse get_user_v1_organizations_org_id_users_user_id_get_0(org_id, user_id, authorization=authorization)

Get User

Get details for a specific user in an organization.

Returns detailed information about a user within the specified organization.
The requesting user must be a member of the organization to access this endpoint.

### Example


```python
import openapi_client
from openapi_client.models.user_response import UserResponse
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
    api_instance = openapi_client.UsersApi(api_client)
    org_id = 'org_id_example' # str | 
    user_id = 'user_id_example' # str | 
    authorization = None # object |  (optional)

    try:
        # Get User
        api_response = api_instance.get_user_v1_organizations_org_id_users_user_id_get_0(org_id, user_id, authorization=authorization)
        print("The response of UsersApi->get_user_v1_organizations_org_id_users_user_id_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_v1_organizations_org_id_users_user_id_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user_v1_organizations_org_id_users_user_id_get_1**
> UserResponse get_user_v1_organizations_org_id_users_user_id_get_1(org_id, user_id, authorization=authorization)

Get User

Get details for a specific user in an organization.

Returns detailed information about a user within the specified organization.
The requesting user must be a member of the organization to access this endpoint.

### Example


```python
import openapi_client
from openapi_client.models.user_response import UserResponse
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
    api_instance = openapi_client.UsersApi(api_client)
    org_id = 'org_id_example' # str | 
    user_id = 'user_id_example' # str | 
    authorization = None # object |  (optional)

    try:
        # Get User
        api_response = api_instance.get_user_v1_organizations_org_id_users_user_id_get_1(org_id, user_id, authorization=authorization)
        print("The response of UsersApi->get_user_v1_organizations_org_id_users_user_id_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_v1_organizations_org_id_users_user_id_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **user_id** | **str**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_users_v1_organizations_org_id_users_get**
> PageUserResponse get_users_v1_organizations_org_id_users_get(org_id, skip=skip, limit=limit, authorization=authorization)

Get Users

Get paginated list of users for a specific organization.

Returns a paginated list of all users associated with the specified organization.
The requesting user must be a member of the organization to access this endpoint.

### Example


```python
import openapi_client
from openapi_client.models.page_user_response import PageUserResponse
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
    api_instance = openapi_client.UsersApi(api_client)
    org_id = 'org_id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # Get Users
        api_response = api_instance.get_users_v1_organizations_org_id_users_get(org_id, skip=skip, limit=limit, authorization=authorization)
        print("The response of UsersApi->get_users_v1_organizations_org_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_v1_organizations_org_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageUserResponse**](PageUserResponse.md)

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

# **get_users_v1_organizations_org_id_users_get_0**
> PageUserResponse get_users_v1_organizations_org_id_users_get_0(org_id, skip=skip, limit=limit, authorization=authorization)

Get Users

Get paginated list of users for a specific organization.

Returns a paginated list of all users associated with the specified organization.
The requesting user must be a member of the organization to access this endpoint.

### Example


```python
import openapi_client
from openapi_client.models.page_user_response import PageUserResponse
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
    api_instance = openapi_client.UsersApi(api_client)
    org_id = 'org_id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # Get Users
        api_response = api_instance.get_users_v1_organizations_org_id_users_get_0(org_id, skip=skip, limit=limit, authorization=authorization)
        print("The response of UsersApi->get_users_v1_organizations_org_id_users_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_v1_organizations_org_id_users_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageUserResponse**](PageUserResponse.md)

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

# **get_users_v1_organizations_org_id_users_get_1**
> PageUserResponse get_users_v1_organizations_org_id_users_get_1(org_id, skip=skip, limit=limit, authorization=authorization)

Get Users

Get paginated list of users for a specific organization.

Returns a paginated list of all users associated with the specified organization.
The requesting user must be a member of the organization to access this endpoint.

### Example


```python
import openapi_client
from openapi_client.models.page_user_response import PageUserResponse
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
    api_instance = openapi_client.UsersApi(api_client)
    org_id = 'org_id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # Get Users
        api_response = api_instance.get_users_v1_organizations_org_id_users_get_1(org_id, skip=skip, limit=limit, authorization=authorization)
        print("The response of UsersApi->get_users_v1_organizations_org_id_users_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_v1_organizations_org_id_users_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageUserResponse**](PageUserResponse.md)

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

