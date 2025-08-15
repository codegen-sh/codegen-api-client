# AgentRunLimitReachedErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] [default to 'Alloted agent runs for the current billing plan have been reached. Please upgrade your plan to continue.']
**status_code** | **int** |  | [optional] [default to 402]

## Example

```python
from codegen_api_client.models.agent_run_limit_reached_error_response import AgentRunLimitReachedErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRunLimitReachedErrorResponse from a JSON string
agent_run_limit_reached_error_response_instance = AgentRunLimitReachedErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AgentRunLimitReachedErrorResponse.to_json())

# convert the object into a dict
agent_run_limit_reached_error_response_dict = agent_run_limit_reached_error_response_instance.to_dict()
# create an instance of AgentRunLimitReachedErrorResponse from a dict
agent_run_limit_reached_error_response_from_dict = AgentRunLimitReachedErrorResponse.from_dict(agent_run_limit_reached_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


