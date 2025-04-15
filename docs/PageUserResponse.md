# PageUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UserResponse]**](UserResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | 

## Example

```python
from openapi_client.models.page_user_response import PageUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageUserResponse from a JSON string
page_user_response_instance = PageUserResponse.from_json(json)
# print the JSON string representation of the object
print(PageUserResponse.to_json())

# convert the object into a dict
page_user_response_dict = page_user_response_instance.to_dict()
# create an instance of PageUserResponse from a dict
page_user_response_from_dict = PageUserResponse.from_dict(page_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


