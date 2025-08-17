# UserNotFoundErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] [default to 'User not found.']
**status_code** | **int** |  | [optional] [default to 404]

## Example

```python
from codegen_api_client.models.user_not_found_error_response import UserNotFoundErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserNotFoundErrorResponse from a JSON string
user_not_found_error_response_instance = UserNotFoundErrorResponse.from_json(json)
# print the JSON string representation of the object
print(UserNotFoundErrorResponse.to_json())

# convert the object into a dict
user_not_found_error_response_dict = user_not_found_error_response_instance.to_dict()
# create an instance of UserNotFoundErrorResponse from a dict
user_not_found_error_response_from_dict = UserNotFoundErrorResponse.from_dict(user_not_found_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


