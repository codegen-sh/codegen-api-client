# GithubPullRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**url** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from codegen_api_client.models.github_pull_request_response import GithubPullRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GithubPullRequestResponse from a JSON string
github_pull_request_response_instance = GithubPullRequestResponse.from_json(json)
# print the JSON string representation of the object
print(GithubPullRequestResponse.to_json())

# convert the object into a dict
github_pull_request_response_dict = github_pull_request_response_instance.to_dict()
# create an instance of GithubPullRequestResponse from a dict
github_pull_request_response_from_dict = GithubPullRequestResponse.from_dict(github_pull_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


