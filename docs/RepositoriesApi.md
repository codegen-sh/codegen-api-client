# codegen_api_client.RepositoriesApi

All URIs are relative to *https://api.codegen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get**](RepositoriesApi.md#get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get) | **GET** /v1/organizations/{org_id}/repos/{repo_id}/check-suite/stats | Get Check Suite Retry Stats
[**get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_0**](RepositoriesApi.md#get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_0) | **GET** /v1/organizations/{org_id}/repos/{repo_id}/check-suite/stats | Get Check Suite Retry Stats
[**get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_1**](RepositoriesApi.md#get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_1) | **GET** /v1/organizations/{org_id}/repos/{repo_id}/check-suite/stats | Get Check Suite Retry Stats
[**get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get**](RepositoriesApi.md#get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get) | **GET** /v1/organizations/{org_id}/repos/{repo_id}/check-suite/settings | Get Check Suite Settings
[**get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_0**](RepositoriesApi.md#get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_0) | **GET** /v1/organizations/{org_id}/repos/{repo_id}/check-suite/settings | Get Check Suite Settings
[**get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_1**](RepositoriesApi.md#get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_1) | **GET** /v1/organizations/{org_id}/repos/{repo_id}/check-suite/settings | Get Check Suite Settings
[**get_repositories_v1_organizations_org_id_repos_get**](RepositoriesApi.md#get_repositories_v1_organizations_org_id_repos_get) | **GET** /v1/organizations/{org_id}/repos | Get Repositories
[**get_repositories_v1_organizations_org_id_repos_get_0**](RepositoriesApi.md#get_repositories_v1_organizations_org_id_repos_get_0) | **GET** /v1/organizations/{org_id}/repos | Get Repositories
[**get_repositories_v1_organizations_org_id_repos_get_1**](RepositoriesApi.md#get_repositories_v1_organizations_org_id_repos_get_1) | **GET** /v1/organizations/{org_id}/repos | Get Repositories
[**update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put**](RepositoriesApi.md#update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put) | **PUT** /v1/organizations/{org_id}/repos/{repo_id}/check-suite/settings | Update Check Suite Settings
[**update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_0**](RepositoriesApi.md#update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_0) | **PUT** /v1/organizations/{org_id}/repos/{repo_id}/check-suite/settings | Update Check Suite Settings
[**update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_1**](RepositoriesApi.md#update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_1) | **PUT** /v1/organizations/{org_id}/repos/{repo_id}/check-suite/settings | Update Check Suite Settings


# **get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get**
> CheckSuiteRetryStatsResponse get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get(org_id, repo_id, authorization=authorization)

Get Check Suite Retry Stats

Get check suite retry statistics for a repository.

Returns comprehensive statistics about check suite orchestrations and retry attempts:
- Total, active, completed, and failed orchestrations
- Total retry attempts across all checks
- Number of checks that have reached their retry limit

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.check_suite_retry_stats_response import CheckSuiteRetryStatsResponse
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Check Suite Retry Stats
        api_response = api_instance.get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get(org_id, repo_id, authorization=authorization)
        print("The response of RepositoriesApi->get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**CheckSuiteRetryStatsResponse**](CheckSuiteRetryStatsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_0**
> CheckSuiteRetryStatsResponse get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_0(org_id, repo_id, authorization=authorization)

Get Check Suite Retry Stats

Get check suite retry statistics for a repository.

Returns comprehensive statistics about check suite orchestrations and retry attempts:
- Total, active, completed, and failed orchestrations
- Total retry attempts across all checks
- Number of checks that have reached their retry limit

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.check_suite_retry_stats_response import CheckSuiteRetryStatsResponse
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Check Suite Retry Stats
        api_response = api_instance.get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_0(org_id, repo_id, authorization=authorization)
        print("The response of RepositoriesApi->get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**CheckSuiteRetryStatsResponse**](CheckSuiteRetryStatsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_1**
> CheckSuiteRetryStatsResponse get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_1(org_id, repo_id, authorization=authorization)

Get Check Suite Retry Stats

Get check suite retry statistics for a repository.

Returns comprehensive statistics about check suite orchestrations and retry attempts:
- Total, active, completed, and failed orchestrations
- Total retry attempts across all checks
- Number of checks that have reached their retry limit

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.check_suite_retry_stats_response import CheckSuiteRetryStatsResponse
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Check Suite Retry Stats
        api_response = api_instance.get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_1(org_id, repo_id, authorization=authorization)
        print("The response of RepositoriesApi->get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_check_suite_retry_stats_v1_organizations_org_id_repos_repo_id_check_suite_stats_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**CheckSuiteRetryStatsResponse**](CheckSuiteRetryStatsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get**
> CheckSuiteSettingsResponse get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get(org_id, repo_id, authorization=authorization)

Get Check Suite Settings

Get check suite retry settings for a repository.

Returns the current configuration for check suite retry logic including:
- retry_count: Maximum number of retry attempts per failed check
- ignored_checks: List of check names that should be ignored

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.check_suite_settings_response import CheckSuiteSettingsResponse
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Check Suite Settings
        api_response = api_instance.get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get(org_id, repo_id, authorization=authorization)
        print("The response of RepositoriesApi->get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**CheckSuiteSettingsResponse**](CheckSuiteSettingsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_0**
> CheckSuiteSettingsResponse get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_0(org_id, repo_id, authorization=authorization)

Get Check Suite Settings

Get check suite retry settings for a repository.

Returns the current configuration for check suite retry logic including:
- retry_count: Maximum number of retry attempts per failed check
- ignored_checks: List of check names that should be ignored

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.check_suite_settings_response import CheckSuiteSettingsResponse
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Check Suite Settings
        api_response = api_instance.get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_0(org_id, repo_id, authorization=authorization)
        print("The response of RepositoriesApi->get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**CheckSuiteSettingsResponse**](CheckSuiteSettingsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_1**
> CheckSuiteSettingsResponse get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_1(org_id, repo_id, authorization=authorization)

Get Check Suite Settings

Get check suite retry settings for a repository.

Returns the current configuration for check suite retry logic including:
- retry_count: Maximum number of retry attempts per failed check
- ignored_checks: List of check names that should be ignored

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.check_suite_settings_response import CheckSuiteSettingsResponse
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | 
    authorization = None # object |  (optional)

    try:
        # Get Check Suite Settings
        api_response = api_instance.get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_1(org_id, repo_id, authorization=authorization)
        print("The response of RepositoriesApi->get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**CheckSuiteSettingsResponse**](CheckSuiteSettingsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_v1_organizations_org_id_repos_get**
> PageRepoResponse get_repositories_v1_organizations_org_id_repos_get(org_id, skip=skip, limit=limit, authorization=authorization)

Get Repositories

Get repositories for the specified organization.

Returns a paginated list of all repositories that belong to the specified organization.
Results include repository details such as name, ID, description, visibility, and setup status.
Use pagination parameters to control the number of results returned.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.page_repo_response import PageRepoResponse
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # Get Repositories
        api_response = api_instance.get_repositories_v1_organizations_org_id_repos_get(org_id, skip=skip, limit=limit, authorization=authorization)
        print("The response of RepositoriesApi->get_repositories_v1_organizations_org_id_repos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_repositories_v1_organizations_org_id_repos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageRepoResponse**](PageRepoResponse.md)

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

# **get_repositories_v1_organizations_org_id_repos_get_0**
> PageRepoResponse get_repositories_v1_organizations_org_id_repos_get_0(org_id, skip=skip, limit=limit, authorization=authorization)

Get Repositories

Get repositories for the specified organization.

Returns a paginated list of all repositories that belong to the specified organization.
Results include repository details such as name, ID, description, visibility, and setup status.
Use pagination parameters to control the number of results returned.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.page_repo_response import PageRepoResponse
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # Get Repositories
        api_response = api_instance.get_repositories_v1_organizations_org_id_repos_get_0(org_id, skip=skip, limit=limit, authorization=authorization)
        print("The response of RepositoriesApi->get_repositories_v1_organizations_org_id_repos_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_repositories_v1_organizations_org_id_repos_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageRepoResponse**](PageRepoResponse.md)

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

# **get_repositories_v1_organizations_org_id_repos_get_1**
> PageRepoResponse get_repositories_v1_organizations_org_id_repos_get_1(org_id, skip=skip, limit=limit, authorization=authorization)

Get Repositories

Get repositories for the specified organization.

Returns a paginated list of all repositories that belong to the specified organization.
Results include repository details such as name, ID, description, visibility, and setup status.
Use pagination parameters to control the number of results returned.

Rate limit: 60 requests per 30 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.page_repo_response import PageRepoResponse
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    authorization = None # object |  (optional)

    try:
        # Get Repositories
        api_response = api_instance.get_repositories_v1_organizations_org_id_repos_get_1(org_id, skip=skip, limit=limit, authorization=authorization)
        print("The response of RepositoriesApi->get_repositories_v1_organizations_org_id_repos_get_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_repositories_v1_organizations_org_id_repos_get_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**PageRepoResponse**](PageRepoResponse.md)

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

# **update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put**
> CheckSuiteSettingsResponse update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put(org_id, repo_id, update_check_suite_settings_request, authorization=authorization)

Update Check Suite Settings

Update check suite retry settings for a repository.

Updates the configuration for check suite retry logic. You can update:
- retry_count: Maximum number of retry attempts per failed check (0-10)
- ignored_checks: List of check names that should be ignored

Rate limit: 30 requests per 60 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.check_suite_settings_response import CheckSuiteSettingsResponse
from codegen_api_client.models.update_check_suite_settings_request import UpdateCheckSuiteSettingsRequest
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | 
    update_check_suite_settings_request = codegen_api_client.UpdateCheckSuiteSettingsRequest() # UpdateCheckSuiteSettingsRequest | 
    authorization = None # object |  (optional)

    try:
        # Update Check Suite Settings
        api_response = api_instance.update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put(org_id, repo_id, update_check_suite_settings_request, authorization=authorization)
        print("The response of RepositoriesApi->update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**|  | 
 **update_check_suite_settings_request** | [**UpdateCheckSuiteSettingsRequest**](UpdateCheckSuiteSettingsRequest.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**CheckSuiteSettingsResponse**](CheckSuiteSettingsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_0**
> CheckSuiteSettingsResponse update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_0(org_id, repo_id, update_check_suite_settings_request, authorization=authorization)

Update Check Suite Settings

Update check suite retry settings for a repository.

Updates the configuration for check suite retry logic. You can update:
- retry_count: Maximum number of retry attempts per failed check (0-10)
- ignored_checks: List of check names that should be ignored

Rate limit: 30 requests per 60 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.check_suite_settings_response import CheckSuiteSettingsResponse
from codegen_api_client.models.update_check_suite_settings_request import UpdateCheckSuiteSettingsRequest
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | 
    update_check_suite_settings_request = codegen_api_client.UpdateCheckSuiteSettingsRequest() # UpdateCheckSuiteSettingsRequest | 
    authorization = None # object |  (optional)

    try:
        # Update Check Suite Settings
        api_response = api_instance.update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_0(org_id, repo_id, update_check_suite_settings_request, authorization=authorization)
        print("The response of RepositoriesApi->update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**|  | 
 **update_check_suite_settings_request** | [**UpdateCheckSuiteSettingsRequest**](UpdateCheckSuiteSettingsRequest.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**CheckSuiteSettingsResponse**](CheckSuiteSettingsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_1**
> CheckSuiteSettingsResponse update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_1(org_id, repo_id, update_check_suite_settings_request, authorization=authorization)

Update Check Suite Settings

Update check suite retry settings for a repository.

Updates the configuration for check suite retry logic. You can update:
- retry_count: Maximum number of retry attempts per failed check (0-10)
- ignored_checks: List of check names that should be ignored

Rate limit: 30 requests per 60 seconds.

### Example


```python
import codegen_api_client
from codegen_api_client.models.check_suite_settings_response import CheckSuiteSettingsResponse
from codegen_api_client.models.update_check_suite_settings_request import UpdateCheckSuiteSettingsRequest
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
    api_instance = codegen_api_client.RepositoriesApi(api_client)
    org_id = 56 # int | 
    repo_id = 56 # int | 
    update_check_suite_settings_request = codegen_api_client.UpdateCheckSuiteSettingsRequest() # UpdateCheckSuiteSettingsRequest | 
    authorization = None # object |  (optional)

    try:
        # Update Check Suite Settings
        api_response = api_instance.update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_1(org_id, repo_id, update_check_suite_settings_request, authorization=authorization)
        print("The response of RepositoriesApi->update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->update_check_suite_settings_v1_organizations_org_id_repos_repo_id_check_suite_settings_put_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**|  | 
 **repo_id** | **int**|  | 
 **update_check_suite_settings_request** | [**UpdateCheckSuiteSettingsRequest**](UpdateCheckSuiteSettingsRequest.md)|  | 
 **authorization** | [**object**](.md)|  | [optional] 

### Return type

[**CheckSuiteSettingsResponse**](CheckSuiteSettingsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

