# PageAgentRunResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AgentRunResponse]**](AgentRunResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | 

## Example

```python
from codegen_api_client.models.page_agent_run_response import PageAgentRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageAgentRunResponse from a JSON string
page_agent_run_response_instance = PageAgentRunResponse.from_json(json)
# print the JSON string representation of the object
print(PageAgentRunResponse.to_json())

# convert the object into a dict
page_agent_run_response_dict = page_agent_run_response_instance.to_dict()
# create an instance of PageAgentRunResponse from a dict
page_agent_run_response_from_dict = PageAgentRunResponse.from_dict(page_agent_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


