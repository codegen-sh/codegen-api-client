# OrganizationIntegrationsResponse

Response schema for organization integrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** | ID of the organization | 
**organization_name** | **str** | Name of the organization | 
**integrations** | [**List[IntegrationStatus]**](IntegrationStatus.md) | List of integration statuses | 
**total_active_integrations** | **int** | Total number of active integrations | 

## Example

```python
from codegen_api_client.models.organization_integrations_response import OrganizationIntegrationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationIntegrationsResponse from a JSON string
organization_integrations_response_instance = OrganizationIntegrationsResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationIntegrationsResponse.to_json())

# convert the object into a dict
organization_integrations_response_dict = organization_integrations_response_instance.to_dict()
# create an instance of OrganizationIntegrationsResponse from a dict
organization_integrations_response_from_dict = OrganizationIntegrationsResponse.from_dict(organization_integrations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


