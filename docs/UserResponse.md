# UserResponse

Represents a user in API responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique user ID | 
**email** | **str** |  | [optional] 
**github_user_id** | **str** | GitHub user ID | 
**github_username** | **str** | GitHub username | 
**avatar_url** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**is_admin** | **bool** |  | [optional] 

## Example

```python
from codegen_api_client.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print(UserResponse.to_json())

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_from_dict = UserResponse.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


