# CheckSuiteRetryStatsResponse

Response model for check suite retry statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_id** | **int** | Repository ID | 
**total_orchestrations** | **int** | Total number of orchestrations | 
**active_orchestrations** | **int** | Number of active orchestrations | 
**completed_orchestrations** | **int** | Number of completed orchestrations | 
**failed_orchestrations** | **int** | Number of failed orchestrations | 
**total_retry_attempts** | **int** | Total number of retry attempts across all checks | 
**checks_at_retry_limit** | **int** | Number of checks that have reached their retry limit | 

## Example

```python
from codegen_api_client.models.check_suite_retry_stats_response import CheckSuiteRetryStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSuiteRetryStatsResponse from a JSON string
check_suite_retry_stats_response_instance = CheckSuiteRetryStatsResponse.from_json(json)
# print the JSON string representation of the object
print(CheckSuiteRetryStatsResponse.to_json())

# convert the object into a dict
check_suite_retry_stats_response_dict = check_suite_retry_stats_response_instance.to_dict()
# create an instance of CheckSuiteRetryStatsResponse from a dict
check_suite_retry_stats_response_from_dict = CheckSuiteRetryStatsResponse.from_dict(check_suite_retry_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


