from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_execution_request_arguments import ToolExecutionRequestArguments


T = TypeVar("T", bound="ToolExecutionRequest")


@_attrs_define
class ToolExecutionRequest:
    """Request schema for tool execution.

    Attributes:
        tool_name (str): Name of the tool to execute
        arguments (ToolExecutionRequestArguments): JSON arguments to pass to the tool
        repo_id (Union[None, Unset, int]): Optional repository ID for repository-specific tool context
    """

    tool_name: str
    arguments: "ToolExecutionRequestArguments"
    repo_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tool_name = self.tool_name

        arguments = self.arguments.to_dict()

        repo_id: Union[None, Unset, int]
        if isinstance(self.repo_id, Unset):
            repo_id = UNSET
        else:
            repo_id = self.repo_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tool_name": tool_name,
                "arguments": arguments,
            }
        )
        if repo_id is not UNSET:
            field_dict["repo_id"] = repo_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_execution_request_arguments import ToolExecutionRequestArguments

        d = dict(src_dict)
        tool_name = d.pop("tool_name")

        arguments = ToolExecutionRequestArguments.from_dict(d.pop("arguments"))

        def _parse_repo_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        repo_id = _parse_repo_id(d.pop("repo_id", UNSET))

        tool_execution_request = cls(
            tool_name=tool_name,
            arguments=arguments,
            repo_id=repo_id,
        )

        tool_execution_request.additional_properties = d
        return tool_execution_request

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
