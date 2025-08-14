from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.organization_settings import OrganizationSettings


T = TypeVar("T", bound="OrganizationResponse")


@_attrs_define
class OrganizationResponse:
    """Represents an organization in API responses

    Attributes:
        id (int):
        name (str):
        settings (OrganizationSettings):
    """

    id: int
    name: str
    settings: "OrganizationSettings"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_settings import OrganizationSettings

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        settings = OrganizationSettings.from_dict(d.pop("settings"))

        organization_response = cls(
            id=id,
            name=name,
            settings=settings,
        )

        organization_response.additional_properties = d
        return organization_response

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
