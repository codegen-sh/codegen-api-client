# UpdateCheckSuiteSettingsRequest

Request model for updating check suite settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retry_count** | **int** |  | [optional] 
**ignored_checks** | **List[str]** |  | [optional] 

## Example

```python
from codegen_api_client.models.update_check_suite_settings_request import UpdateCheckSuiteSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCheckSuiteSettingsRequest from a JSON string
update_check_suite_settings_request_instance = UpdateCheckSuiteSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCheckSuiteSettingsRequest.to_json())

# convert the object into a dict
update_check_suite_settings_request_dict = update_check_suite_settings_request_instance.to_dict()
# create an instance of UpdateCheckSuiteSettingsRequest from a dict
update_check_suite_settings_request_from_dict = UpdateCheckSuiteSettingsRequest.from_dict(update_check_suite_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


