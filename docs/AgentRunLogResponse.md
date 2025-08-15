# AgentRunLogResponse

Represents an agent run log in API responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_run_id** | **int** |  | 
**created_at** | **str** |  | [optional] 
**tool_name** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**thought** | **str** |  | [optional] 
**observation** | [**Observation**](Observation.md) |  | [optional] 
**tool_input** | **Dict[str, object]** |  | [optional] 
**tool_output** | **Dict[str, object]** |  | [optional] 

## Example

```python
from codegen_api_client.models.agent_run_log_response import AgentRunLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRunLogResponse from a JSON string
agent_run_log_response_instance = AgentRunLogResponse.from_json(json)
# print the JSON string representation of the object
print(AgentRunLogResponse.to_json())

# convert the object into a dict
agent_run_log_response_dict = agent_run_log_response_instance.to_dict()
# create an instance of AgentRunLogResponse from a dict
agent_run_log_response_from_dict = AgentRunLogResponse.from_dict(agent_run_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


