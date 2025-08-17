# AgentRunNotFoundErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] [default to 'Agent run not found.']
**status_code** | **int** |  | [optional] [default to 404]

## Example

```python
from codegen_api_client.models.agent_run_not_found_error_response import AgentRunNotFoundErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRunNotFoundErrorResponse from a JSON string
agent_run_not_found_error_response_instance = AgentRunNotFoundErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AgentRunNotFoundErrorResponse.to_json())

# convert the object into a dict
agent_run_not_found_error_response_dict = agent_run_not_found_error_response_instance.to_dict()
# create an instance of AgentRunNotFoundErrorResponse from a dict
agent_run_not_found_error_response_from_dict = AgentRunNotFoundErrorResponse.from_dict(agent_run_not_found_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


