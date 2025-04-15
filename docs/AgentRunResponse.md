# AgentRunResponse

Represents an agent run in API responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**organization_id** | **int** |  | 
**status** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 
**result** | **str** |  | [optional] 

## Example

```python
from codegen_api_client.models.agent_run_response import AgentRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRunResponse from a JSON string
agent_run_response_instance = AgentRunResponse.from_json(json)
# print the JSON string representation of the object
print(AgentRunResponse.to_json())

# convert the object into a dict
agent_run_response_dict = agent_run_response_instance.to_dict()
# create an instance of AgentRunResponse from a dict
agent_run_response_from_dict = AgentRunResponse.from_dict(agent_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


