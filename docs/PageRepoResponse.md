# PageRepoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RepoResponse]**](RepoResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | 

## Example

```python
from codegen_api_client.models.page_repo_response import PageRepoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageRepoResponse from a JSON string
page_repo_response_instance = PageRepoResponse.from_json(json)
# print the JSON string representation of the object
print(PageRepoResponse.to_json())

# convert the object into a dict
page_repo_response_dict = page_repo_response_instance.to_dict()
# create an instance of PageRepoResponse from a dict
page_repo_response_from_dict = PageRepoResponse.from_dict(page_repo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


