# NoReposFoundInOrgErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] [default to 'No repos found in the organization. Please add some repos and try again.']
**status_code** | **int** |  | [optional] [default to 404]

## Example

```python
from codegen_api_client.models.no_repos_found_in_org_error_response import NoReposFoundInOrgErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NoReposFoundInOrgErrorResponse from a JSON string
no_repos_found_in_org_error_response_instance = NoReposFoundInOrgErrorResponse.from_json(json)
# print the JSON string representation of the object
print(NoReposFoundInOrgErrorResponse.to_json())

# convert the object into a dict
no_repos_found_in_org_error_response_dict = no_repos_found_in_org_error_response_instance.to_dict()
# create an instance of NoReposFoundInOrgErrorResponse from a dict
no_repos_found_in_org_error_response_from_dict = NoReposFoundInOrgErrorResponse.from_dict(no_repos_found_in_org_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


