from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RepoResponse")


@_attrs_define
class RepoResponse:
    """Represents a repository in API responses

    Attributes:
        id (int):
        name (str):
        full_name (str):
        description (Union[None, str]):
        github_id (str):
        organization_id (int):
        visibility (Union[None, str]):
        archived (Union[None, bool]):
        setup_status (str):
        language (Union[None, str]):
    """

    id: int
    name: str
    full_name: str
    description: Union[None, str]
    github_id: str
    organization_id: int
    visibility: Union[None, str]
    archived: Union[None, bool]
    setup_status: str
    language: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        full_name = self.full_name

        description: Union[None, str]
        description = self.description

        github_id = self.github_id

        organization_id = self.organization_id

        visibility: Union[None, str]
        visibility = self.visibility

        archived: Union[None, bool]
        archived = self.archived

        setup_status = self.setup_status

        language: Union[None, str]
        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "full_name": full_name,
                "description": description,
                "github_id": github_id,
                "organization_id": organization_id,
                "visibility": visibility,
                "archived": archived,
                "setup_status": setup_status,
                "language": language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        full_name = d.pop("full_name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        github_id = d.pop("github_id")

        organization_id = d.pop("organization_id")

        def _parse_visibility(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        visibility = _parse_visibility(d.pop("visibility"))

        def _parse_archived(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        archived = _parse_archived(d.pop("archived"))

        setup_status = d.pop("setup_status")

        def _parse_language(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        language = _parse_language(d.pop("language"))

        repo_response = cls(
            id=id,
            name=name,
            full_name=full_name,
            description=description,
            github_id=github_id,
            organization_id=organization_id,
            visibility=visibility,
            archived=archived,
            setup_status=setup_status,
            language=language,
        )

        repo_response.additional_properties = d
        return repo_response

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
