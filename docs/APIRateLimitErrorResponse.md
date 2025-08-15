# APIRateLimitErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] [default to 'Rate limit exceeded. Please try again later.']
**status_code** | **int** |  | [optional] [default to 429]

## Example

```python
from codegen_api_client.models.api_rate_limit_error_response import APIRateLimitErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIRateLimitErrorResponse from a JSON string
api_rate_limit_error_response_instance = APIRateLimitErrorResponse.from_json(json)
# print the JSON string representation of the object
print(APIRateLimitErrorResponse.to_json())

# convert the object into a dict
api_rate_limit_error_response_dict = api_rate_limit_error_response_instance.to_dict()
# create an instance of APIRateLimitErrorResponse from a dict
api_rate_limit_error_response_from_dict = APIRateLimitErrorResponse.from_dict(api_rate_limit_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


