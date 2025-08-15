# codegen_api_client.UsersApi

All URIs are relative to *https://api.codegen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user_info_v1_users_me_get**](UsersApi.md#get_current_user_info_v1_users_me_get) | **GET** /v1/users/me | Get Current User Info
[**get_current_user_info_v1_users_me_get_0**](UsersApi.md#get_current_user_info_v1_users_me_get_0) | **GET** /v1/users/me | Get Current User Info
[**get_current_user_info_v1_users_me_get_1**](UsersApi.md#get_current_user_info_v1_users_me_get_1) | **GET** /v1/users/me | Get Current User Info
[**get_user_v1_organizations_org_id_users_user_id_get**](UsersApi.md#get_user_v1_organizations_org_id_users_user_id_get) | **GET** /v1/organizations/{org_id}/users/{user_id} | Get User
[**get_user_v1_organizations_org_id_users_user_id_get_0**](UsersApi.md#get_user_v1_organizations_org_id_users_user_id_get_0) | **GET** /v1/organizations/{org_id}/users/{user_id} | Get User
[**get_user_v1_organizations_org_id_users_user_id_get_1**](UsersApi.md#get_user_v1_organizations_org_id_users_user_id_get_1) | **GET** /v1/organizations/{org_id}/users/{user_id} | Get User
[**get_users_v1_organizations_org_id_users_get**](UsersApi.md#get_users_v1_organizations_org_id_users_get) | **GET** /v1/organizations/{org_id}/users | Get Users
[**get_users_v1_organizations_org_id_users_get_0**](UsersApi.md#get_users_v1_organizations_org_id_users_get_0) | **GET** /v1/organizations/{org_id}/users | Get Users
[**get_users_v1_organizations_org_id_users_get_1**](UsersApi.md#get_users_v1_organizations_org_id_users_get_1) | **GET** /v1/organizations/{org_id}/users | Get Users


# **get_current_user_info_v1_users_me_get**
> UserResponse get_current_user_info_v1_users_me_get(authorization=authorization)

Get Current User Info

Get current user information from API token.

Returns detailed information about the user associated with the provided API token.
This is useful for applications that need to identify the current user from their API token.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.user_response import UserResponse
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
    api_instance = codegen_api_client.UsersApi(api_client)
    authorization = None # object |  (optional)

    try:
        # Get Current User Info
        api_response = api_instance.get_current_user_info_v1_users_me_get(authorization=authorization)
        print("The response of UsersApi->get_current_user_info_v1_users_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_info_v1_users_me_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_info_v1_users_me_get_0**
> UserResponse get_current_user_info_v1_users_me_get_0(authorization=authorization)

Get Current User Info

Get current user information from API token.

Returns detailed information about the user associated with the provided API token.
This is useful for applications that need to identify the current user from their API token.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.user_response import UserResponse
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
    api_instance = codegen_api_client.UsersApi(api_client)
    authorization = None # object |  (optional)

    try:
        # Get Current User Info
        api_response = api_instance.get_current_user_info_v1_users_me_get_0(authorization=authorization)
        print("The response of UsersApi->get_current_user_info_v1_users_me_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_info_v1_users_me_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_info_v1_users_me_get_1**
> UserResponse get_current_user_info_v1_users_me_get_1(authorization=authorization)

Get Current User Info

Get current user information from API token.

Returns detailed information about the user associated with the provided API token.
This is useful for applications that need to identify the current user from their API token.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.user_response import UserResponse
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
    api_instance = codegen_api_client.UsersApi(api_client)
    authorization = None # object |  (optional)

    try:
        # Get Current User Info
        api_response = api_instance.get_current_user_info_v1_users_me_get_1(authorization=authorization)
        print("The response of UsersApi->get_current_user_info_v1_users_me_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user_info_v1_users_me_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_v1_organizations_org_id_users_user_id_get**
> UserResponse get_user_v1_organizations_org_id_users_user_id_get(org_id, user_id, authorization=authorization)

Get User

Get details for a specific user in an organization.

Returns detailed information about a user within the specified organization.
The requesting user must be a member of the organization to access this endpoint.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.user_response import UserResponse
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
    api_instance = codegen_api_client.UsersApi(api_client)
    org_id = 56 # int | 
    user_id = 56 # int | 
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
 **org_id** | **int**|  | 
 **user_id** | **int**|  | 
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_v1_organizations_org_id_users_user_id_get_0**
> UserResponse get_user_v1_organizations_org_id_users_user_id_get_0(org_id, user_id, authorization=authorization)

Get User

Get details for a specific user in an organization.

Returns detailed information about a user within the specified organization.
The requesting user must be a member of the organization to access this endpoint.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.user_response import UserResponse
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
    api_instance = codegen_api_client.UsersApi(api_client)
    org_id = 56 # int | 
    user_id = 56 # int | 
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
 **org_id** | **int**|  | 
 **user_id** | **int**|  | 
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_v1_organizations_org_id_users_user_id_get_1**
> UserResponse get_user_v1_organizations_org_id_users_user_id_get_1(org_id, user_id, authorization=authorization)

Get User

Get details for a specific user in an organization.

Returns detailed information about a user within the specified organization.
The requesting user must be a member of the organization to access this endpoint.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.user_response import UserResponse
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
    api_instance = codegen_api_client.UsersApi(api_client)
    org_id = 56 # int | 
    user_id = 56 # int | 
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
 **org_id** | **int**|  | 
 **user_id** | **int**|  | 
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_v1_organizations_org_id_users_get**
> PageUserResponse get_users_v1_organizations_org_id_users_get(org_id, skip=skip, limit=limit, authorization=authorization)

Get Users

Get users for the specified organization.

Returns a paginated list of all users that belong to the specified organization.
Results include user details such as name, email, GitHub username, and avatar.
Use pagination parameters to control the number of results returned.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.page_user_response import PageUserResponse
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
    api_instance = codegen_api_client.UsersApi(api_client)
    org_id = 56 # int | 
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
 **org_id** | **int**|  | 
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_v1_organizations_org_id_users_get_0**
> PageUserResponse get_users_v1_organizations_org_id_users_get_0(org_id, skip=skip, limit=limit, authorization=authorization)

Get Users

Get users for the specified organization.

Returns a paginated list of all users that belong to the specified organization.
Results include user details such as name, email, GitHub username, and avatar.
Use pagination parameters to control the number of results returned.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.page_user_response import PageUserResponse
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
    api_instance = codegen_api_client.UsersApi(api_client)
    org_id = 56 # int | 
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
 **org_id** | **int**|  | 
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_v1_organizations_org_id_users_get_1**
> PageUserResponse get_users_v1_organizations_org_id_users_get_1(org_id, skip=skip, limit=limit, authorization=authorization)

Get Users

Get users for the specified organization.

Returns a paginated list of all users that belong to the specified organization.
Results include user details such as name, email, GitHub username, and avatar.
Use pagination parameters to control the number of results returned.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.page_user_response import PageUserResponse
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
    api_instance = codegen_api_client.UsersApi(api_client)
    org_id = 56 # int | 
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
 **org_id** | **int**|  | 
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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

