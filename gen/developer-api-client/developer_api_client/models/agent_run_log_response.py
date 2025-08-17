from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_run_log_response_observation_type_0 import AgentRunLogResponseObservationType0
    from ..models.agent_run_log_response_tool_input_type_0 import AgentRunLogResponseToolInputType0
    from ..models.agent_run_log_response_tool_output_type_0 import AgentRunLogResponseToolOutputType0


T = TypeVar("T", bound="AgentRunLogResponse")


@_attrs_define
class AgentRunLogResponse:
    """Represents an agent run log in API responses

    Attributes:
        agent_run_id (int):
        created_at (Union[None, Unset, str]):
        tool_name (Union[None, Unset, str]):
        message_type (Union[None, Unset, str]):
        thought (Union[None, Unset, str]):
        observation (Union['AgentRunLogResponseObservationType0', None, Unset, str]):
        tool_input (Union['AgentRunLogResponseToolInputType0', None, Unset]):
        tool_output (Union['AgentRunLogResponseToolOutputType0', None, Unset]):
    """

    agent_run_id: int
    created_at: Union[None, Unset, str] = UNSET
    tool_name: Union[None, Unset, str] = UNSET
    message_type: Union[None, Unset, str] = UNSET
    thought: Union[None, Unset, str] = UNSET
    observation: Union["AgentRunLogResponseObservationType0", None, Unset, str] = UNSET
    tool_input: Union["AgentRunLogResponseToolInputType0", None, Unset] = UNSET
    tool_output: Union["AgentRunLogResponseToolOutputType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_run_log_response_observation_type_0 import AgentRunLogResponseObservationType0
        from ..models.agent_run_log_response_tool_input_type_0 import AgentRunLogResponseToolInputType0
        from ..models.agent_run_log_response_tool_output_type_0 import AgentRunLogResponseToolOutputType0

        agent_run_id = self.agent_run_id

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        tool_name: Union[None, Unset, str]
        if isinstance(self.tool_name, Unset):
            tool_name = UNSET
        else:
            tool_name = self.tool_name

        message_type: Union[None, Unset, str]
        if isinstance(self.message_type, Unset):
            message_type = UNSET
        else:
            message_type = self.message_type

        thought: Union[None, Unset, str]
        if isinstance(self.thought, Unset):
            thought = UNSET
        else:
            thought = self.thought

        observation: Union[None, Unset, dict[str, Any], str]
        if isinstance(self.observation, Unset):
            observation = UNSET
        elif isinstance(self.observation, AgentRunLogResponseObservationType0):
            observation = self.observation.to_dict()
        else:
            observation = self.observation

        tool_input: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tool_input, Unset):
            tool_input = UNSET
        elif isinstance(self.tool_input, AgentRunLogResponseToolInputType0):
            tool_input = self.tool_input.to_dict()
        else:
            tool_input = self.tool_input

        tool_output: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tool_output, Unset):
            tool_output = UNSET
        elif isinstance(self.tool_output, AgentRunLogResponseToolOutputType0):
            tool_output = self.tool_output.to_dict()
        else:
            tool_output = self.tool_output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_run_id": agent_run_id,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name
        if message_type is not UNSET:
            field_dict["message_type"] = message_type
        if thought is not UNSET:
            field_dict["thought"] = thought
        if observation is not UNSET:
            field_dict["observation"] = observation
        if tool_input is not UNSET:
            field_dict["tool_input"] = tool_input
        if tool_output is not UNSET:
            field_dict["tool_output"] = tool_output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_log_response_observation_type_0 import AgentRunLogResponseObservationType0
        from ..models.agent_run_log_response_tool_input_type_0 import AgentRunLogResponseToolInputType0
        from ..models.agent_run_log_response_tool_output_type_0 import AgentRunLogResponseToolOutputType0

        d = dict(src_dict)
        agent_run_id = d.pop("agent_run_id")

        def _parse_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_tool_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tool_name = _parse_tool_name(d.pop("tool_name", UNSET))

        def _parse_message_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message_type = _parse_message_type(d.pop("message_type", UNSET))

        def _parse_thought(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thought = _parse_thought(d.pop("thought", UNSET))

        def _parse_observation(data: object) -> Union["AgentRunLogResponseObservationType0", None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                observation_type_0 = AgentRunLogResponseObservationType0.from_dict(data)

                return observation_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AgentRunLogResponseObservationType0", None, Unset, str], data)

        observation = _parse_observation(d.pop("observation", UNSET))

        def _parse_tool_input(data: object) -> Union["AgentRunLogResponseToolInputType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_input_type_0 = AgentRunLogResponseToolInputType0.from_dict(data)

                return tool_input_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AgentRunLogResponseToolInputType0", None, Unset], data)

        tool_input = _parse_tool_input(d.pop("tool_input", UNSET))

        def _parse_tool_output(data: object) -> Union["AgentRunLogResponseToolOutputType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_output_type_0 = AgentRunLogResponseToolOutputType0.from_dict(data)

                return tool_output_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AgentRunLogResponseToolOutputType0", None, Unset], data)

        tool_output = _parse_tool_output(d.pop("tool_output", UNSET))

        agent_run_log_response = cls(
            agent_run_id=agent_run_id,
            created_at=created_at,
            tool_name=tool_name,
            message_type=message_type,
            thought=thought,
            observation=observation,
            tool_input=tool_input,
            tool_output=tool_output,
        )

        agent_run_log_response.additional_properties = d
        return agent_run_log_response

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
