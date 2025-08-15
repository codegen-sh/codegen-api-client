from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResumeAgentRunInput")


@_attrs_define
class ResumeAgentRunInput:
    """
    Attributes:
        agent_run_id (int):
        prompt (str):
        images (Union[None, Unset, list[str]]): List of base64 encoded data URIs representing images to be processed by
            the agent
    """

    agent_run_id: int
    prompt: str
    images: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_run_id = self.agent_run_id

        prompt = self.prompt

        images: Union[None, Unset, list[str]]
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = self.images

        else:
            images = self.images

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_run_id": agent_run_id,
                "prompt": prompt,
            }
        )
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_run_id = d.pop("agent_run_id")

        prompt = d.pop("prompt")

        def _parse_images(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = cast(list[str], data)

                return images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        images = _parse_images(d.pop("images", UNSET))

        resume_agent_run_input = cls(
            agent_run_id=agent_run_id,
            prompt=prompt,
            images=images,
        )

        resume_agent_run_input.additional_properties = d
        return resume_agent_run_input

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
