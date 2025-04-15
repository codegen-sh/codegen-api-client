# OrganizationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_pr_creation** | **bool** |  | [optional] [default to True]
**enable_rules_detection** | **bool** |  | [optional] [default to True]

## Example

```python
from codegen_api_client.models.organization_settings import OrganizationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSettings from a JSON string
organization_settings_instance = OrganizationSettings.from_json(json)
# print the JSON string representation of the object
print(OrganizationSettings.to_json())

# convert the object into a dict
organization_settings_dict = organization_settings_instance.to_dict()
# create an instance of OrganizationSettings from a dict
organization_settings_from_dict = OrganizationSettings.from_dict(organization_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


