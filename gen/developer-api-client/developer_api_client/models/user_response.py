from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
    """Represents a user in API responses

    Attributes:
        id (int): Unique user ID
        github_user_id (str): GitHub user ID
        github_username (str): GitHub username
        email (Union[None, Unset, str]): User's email address
        avatar_url (Union[None, Unset, str]): URL to user's avatar image
        full_name (Union[None, Unset, str]): User's full name
        role (Union[None, Unset, str]): User's role in the organization (ADMIN, MANAGER, MEMBER)
        is_admin (Union[None, Unset, bool]): Whether the user is an admin (deprecated, use role instead)
    """

    id: int
    github_user_id: str
    github_username: str
    email: Union[None, Unset, str] = UNSET
    avatar_url: Union[None, Unset, str] = UNSET
    full_name: Union[None, Unset, str] = UNSET
    role: Union[None, Unset, str] = UNSET
    is_admin: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        github_user_id = self.github_user_id

        github_username = self.github_username

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        avatar_url: Union[None, Unset, str]
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        full_name: Union[None, Unset, str]
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        role: Union[None, Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        is_admin: Union[None, Unset, bool]
        if isinstance(self.is_admin, Unset):
            is_admin = UNSET
        else:
            is_admin = self.is_admin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "github_user_id": github_user_id,
                "github_username": github_username,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if role is not UNSET:
            field_dict["role"] = role
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        github_user_id = d.pop("github_user_id")

        github_username = d.pop("github_username")

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_avatar_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        def _parse_full_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))

        def _parse_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_is_admin(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_admin = _parse_is_admin(d.pop("is_admin", UNSET))

        user_response = cls(
            id=id,
            github_user_id=github_user_id,
            github_username=github_username,
            email=email,
            avatar_url=avatar_url,
            full_name=full_name,
            role=role,
            is_admin=is_admin,
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
