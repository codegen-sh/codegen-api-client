# RepoResponse

Represents a repository in API responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**full_name** | **str** |  | 
**description** | **str** |  | 
**github_id** | **str** |  | 
**organization_id** | **int** |  | 
**visibility** | **str** |  | 
**archived** | **bool** |  | 
**setup_status** | **str** |  | 
**language** | **str** |  | 

## Example

```python
from codegen_api_client.models.repo_response import RepoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RepoResponse from a JSON string
repo_response_instance = RepoResponse.from_json(json)
# print the JSON string representation of the object
print(RepoResponse.to_json())

# convert the object into a dict
repo_response_dict = repo_response_instance.to_dict()
# create an instance of RepoResponse from a dict
repo_response_from_dict = RepoResponse.from_dict(repo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


