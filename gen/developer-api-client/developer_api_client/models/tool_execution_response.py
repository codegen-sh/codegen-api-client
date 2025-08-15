from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolExecutionResponse")


@_attrs_define
class ToolExecutionResponse:
    """Response schema for tool execution.

    Attributes:
        success (bool): Whether the tool execution was successful
        tool_name (str): Name of the executed tool
        result (Union[Unset, Any]): The result returned by the tool
        error (Union[None, Unset, str]): Error message if execution failed
        execution_time_ms (Union[None, Unset, float]): Tool execution time in milliseconds
    """

    success: bool
    tool_name: str
    result: Union[Unset, Any] = UNSET
    error: Union[None, Unset, str] = UNSET
    execution_time_ms: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        tool_name = self.tool_name

        result = self.result

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        execution_time_ms: Union[None, Unset, float]
        if isinstance(self.execution_time_ms, Unset):
            execution_time_ms = UNSET
        else:
            execution_time_ms = self.execution_time_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "tool_name": tool_name,
            }
        )
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error
        if execution_time_ms is not UNSET:
            field_dict["execution_time_ms"] = execution_time_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        tool_name = d.pop("tool_name")

        result = d.pop("result", UNSET)

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_execution_time_ms(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        execution_time_ms = _parse_execution_time_ms(d.pop("execution_time_ms", UNSET))

        tool_execution_response = cls(
            success=success,
            tool_name=tool_name,
            result=result,
            error=error,
            execution_time_ms=execution_time_ms,
        )

        tool_execution_response.additional_properties = d
        return tool_execution_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
