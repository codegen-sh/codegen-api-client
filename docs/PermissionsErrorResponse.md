# PermissionsErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] [default to 'You do not have access to this organization.']
**status_code** | **int** |  | [optional] [default to 403]

## Example

```python
from codegen_api_client.models.permissions_error_response import PermissionsErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsErrorResponse from a JSON string
permissions_error_response_instance = PermissionsErrorResponse.from_json(json)
# print the JSON string representation of the object
print(PermissionsErrorResponse.to_json())

# convert the object into a dict
permissions_error_response_dict = permissions_error_response_instance.to_dict()
# create an instance of PermissionsErrorResponse from a dict
permissions_error_response_from_dict = PermissionsErrorResponse.from_dict(permissions_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


