# ResumeAgentRunInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_run_id** | **int** |  | 
**prompt** | **str** |  | 
**images** | **List[str]** |  | [optional] 

## Example

```python
from codegen_api_client.models.resume_agent_run_input import ResumeAgentRunInput

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeAgentRunInput from a JSON string
resume_agent_run_input_instance = ResumeAgentRunInput.from_json(json)
# print the JSON string representation of the object
print(ResumeAgentRunInput.to_json())

# convert the object into a dict
resume_agent_run_input_dict = resume_agent_run_input_instance.to_dict()
# create an instance of ResumeAgentRunInput from a dict
resume_agent_run_input_from_dict = ResumeAgentRunInput.from_dict(resume_agent_run_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


