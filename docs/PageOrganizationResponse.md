# PageOrganizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OrganizationResponse]**](OrganizationResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | 

## Example

```python
from openapi_client.models.page_organization_response import PageOrganizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageOrganizationResponse from a JSON string
page_organization_response_instance = PageOrganizationResponse.from_json(json)
# print the JSON string representation of the object
print(PageOrganizationResponse.to_json())

# convert the object into a dict
page_organization_response_dict = page_organization_response_instance.to_dict()
# create an instance of PageOrganizationResponse from a dict
page_organization_response_from_dict = PageOrganizationResponse.from_dict(page_organization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


