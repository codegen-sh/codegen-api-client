# AgentRunWithLogsResponse

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
**metadata** | **Dict[str, object]** |  | [optional] 
**logs** | [**List[AgentRunLogResponse]**](AgentRunLogResponse.md) |  | 
**total_logs** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 

## Example

```python
from codegen_api_client.models.agent_run_with_logs_response import AgentRunWithLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentRunWithLogsResponse from a JSON string
agent_run_with_logs_response_instance = AgentRunWithLogsResponse.from_json(json)
# print the JSON string representation of the object
print(AgentRunWithLogsResponse.to_json())

# convert the object into a dict
agent_run_with_logs_response_dict = agent_run_with_logs_response_instance.to_dict()
# create an instance of AgentRunWithLogsResponse from a dict
agent_run_with_logs_response_from_dict = AgentRunWithLogsResponse.from_dict(agent_run_with_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


