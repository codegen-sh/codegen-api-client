# ToolExecutionResponse

Response schema for tool execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the tool execution was successful | 
**result** | **object** |  | [optional] 
**error** | **str** |  | [optional] 
**tool_name** | **str** | Name of the executed tool | 
**execution_time_ms** | **float** |  | [optional] 

## Example

```python
from codegen_api_client.models.tool_execution_response import ToolExecutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ToolExecutionResponse from a JSON string
tool_execution_response_instance = ToolExecutionResponse.from_json(json)
# print the JSON string representation of the object
print(ToolExecutionResponse.to_json())

# convert the object into a dict
tool_execution_response_dict = tool_execution_response_instance.to_dict()
# create an instance of ToolExecutionResponse from a dict
tool_execution_response_from_dict = ToolExecutionResponse.from_dict(tool_execution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


