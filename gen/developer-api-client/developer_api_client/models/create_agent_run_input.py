from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_agent_run_input_metadata_type_0 import CreateAgentRunInputMetadataType0


T = TypeVar("T", bound="CreateAgentRunInput")


@_attrs_define
class CreateAgentRunInput:
    """
    Attributes:
        prompt (str):
        images (Union[None, Unset, list[str]]): List of base64 encoded data URIs representing images to be processed by
            the agent
        metadata (Union['CreateAgentRunInputMetadataType0', None, Unset]): Arbitrary JSON metadata to be stored with the
            agent run
        repo_id (Union[None, Unset, int]): ID of the repository to use for the agent run
        model (Union[None, Unset, str]): Model to use for this agent run (optional, uses org default if not specified)
    """

    prompt: str
    images: Union[None, Unset, list[str]] = UNSET
    metadata: Union["CreateAgentRunInputMetadataType0", None, Unset] = UNSET
    repo_id: Union[None, Unset, int] = UNSET
    model: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_agent_run_input_metadata_type_0 import CreateAgentRunInputMetadataType0

        prompt = self.prompt

        images: Union[None, Unset, list[str]]
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = self.images

        else:
            images = self.images

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CreateAgentRunInputMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        repo_id: Union[None, Unset, int]
        if isinstance(self.repo_id, Unset):
            repo_id = UNSET
        else:
            repo_id = self.repo_id

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
            }
        )
        if images is not UNSET:
            field_dict["images"] = images
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if repo_id is not UNSET:
            field_dict["repo_id"] = repo_id
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_agent_run_input_metadata_type_0 import CreateAgentRunInputMetadataType0

        d = dict(src_dict)
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

        def _parse_metadata(data: object) -> Union["CreateAgentRunInputMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CreateAgentRunInputMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CreateAgentRunInputMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_repo_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        repo_id = _parse_repo_id(d.pop("repo_id", UNSET))

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        create_agent_run_input = cls(
            prompt=prompt,
            images=images,
            metadata=metadata,
            repo_id=repo_id,
            model=model,
        )

        create_agent_run_input.additional_properties = d
        return create_agent_run_input

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
