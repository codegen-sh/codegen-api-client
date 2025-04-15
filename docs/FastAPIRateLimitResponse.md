# FastAPIRateLimitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | [optional] [default to 'Rate limit exceeded']
**status_code** | **int** |  | [optional] [default to 429]

## Example

```python
from codegen_api_client.models.fast_api_rate_limit_response import FastAPIRateLimitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FastAPIRateLimitResponse from a JSON string
fast_api_rate_limit_response_instance = FastAPIRateLimitResponse.from_json(json)
# print the JSON string representation of the object
print(FastAPIRateLimitResponse.to_json())

# convert the object into a dict
fast_api_rate_limit_response_dict = fast_api_rate_limit_response_instance.to_dict()
# create an instance of FastAPIRateLimitResponse from a dict
fast_api_rate_limit_response_from_dict = FastAPIRateLimitResponse.from_dict(fast_api_rate_limit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


