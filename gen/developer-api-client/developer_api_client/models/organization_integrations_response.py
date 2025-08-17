from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.integration_status import IntegrationStatus


T = TypeVar("T", bound="OrganizationIntegrationsResponse")


@_attrs_define
class OrganizationIntegrationsResponse:
    """Response schema for organization integrations.

    Attributes:
        organization_id (int): ID of the organization
        organization_name (str): Name of the organization
        integrations (list['IntegrationStatus']): List of integration statuses
        total_active_integrations (int): Total number of active integrations
    """

    organization_id: int
    organization_name: str
    integrations: list["IntegrationStatus"]
    total_active_integrations: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        organization_name = self.organization_name

        integrations = []
        for integrations_item_data in self.integrations:
            integrations_item = integrations_item_data.to_dict()
            integrations.append(integrations_item)

        total_active_integrations = self.total_active_integrations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
                "organization_name": organization_name,
                "integrations": integrations,
                "total_active_integrations": total_active_integrations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_status import IntegrationStatus

        d = dict(src_dict)
        organization_id = d.pop("organization_id")

        organization_name = d.pop("organization_name")

        integrations = []
        _integrations = d.pop("integrations")
        for integrations_item_data in _integrations:
            integrations_item = IntegrationStatus.from_dict(integrations_item_data)

            integrations.append(integrations_item)

        total_active_integrations = d.pop("total_active_integrations")

        organization_integrations_response = cls(
            organization_id=organization_id,
            organization_name=organization_name,
            integrations=integrations,
            total_active_integrations=total_active_integrations,
        )

        organization_integrations_response.additional_properties = d
        return organization_integrations_response

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
