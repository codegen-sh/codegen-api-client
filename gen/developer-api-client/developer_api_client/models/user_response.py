from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
    """Represents a user in API responses

    Attributes:
        id (int):
        email (Union[None, str]):
        github_user_id (str):
        github_username (str):
        avatar_url (Union[None, str]):
        full_name (Union[None, str]):
    """

    id: int
    email: Union[None, str]
    github_user_id: str
    github_username: str
    avatar_url: Union[None, str]
    full_name: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email: Union[None, str]
        email = self.email

        github_user_id = self.github_user_id

        github_username = self.github_username

        avatar_url: Union[None, str]
        avatar_url = self.avatar_url

        full_name: Union[None, str]
        full_name = self.full_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "github_user_id": github_user_id,
                "github_username": github_username,
                "avatar_url": avatar_url,
                "full_name": full_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        email = _parse_email(d.pop("email"))

        github_user_id = d.pop("github_user_id")

        github_username = d.pop("github_username")

        def _parse_avatar_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url"))

        def _parse_full_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        full_name = _parse_full_name(d.pop("full_name"))

        user_response = cls(
            id=id,
            email=email,
            github_user_id=github_user_id,
            github_username=github_username,
            avatar_url=avatar_url,
            full_name=full_name,
        )

        user_response.additional_properties = d
        return user_response

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
