# CheckSuiteSettingsResponse

Response model for check suite settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retry_count** | **int** | Number of retry attempts for failed checks | 
**ignored_checks** | **List[str]** | List of check names to ignore | 

## Example

```python
from codegen_api_client.models.check_suite_settings_response import CheckSuiteSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSuiteSettingsResponse from a JSON string
check_suite_settings_response_instance = CheckSuiteSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(CheckSuiteSettingsResponse.to_json())

# convert the object into a dict
check_suite_settings_response_dict = check_suite_settings_response_instance.to_dict()
# create an instance of CheckSuiteSettingsResponse from a dict
check_suite_settings_response_from_dict = CheckSuiteSettingsResponse.from_dict(check_suite_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


