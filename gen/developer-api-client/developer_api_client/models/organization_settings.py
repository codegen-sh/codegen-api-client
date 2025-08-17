from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationSettings")


@_attrs_define
class OrganizationSettings:
    """
    Attributes:
        enable_pr_creation (Union[Unset, bool]):  Default: True.
        enable_rules_detection (Union[Unset, bool]):  Default: True.
    """

    enable_pr_creation: Union[Unset, bool] = True
    enable_rules_detection: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_pr_creation = self.enable_pr_creation

        enable_rules_detection = self.enable_rules_detection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_pr_creation is not UNSET:
            field_dict["enable_pr_creation"] = enable_pr_creation
        if enable_rules_detection is not UNSET:
            field_dict["enable_rules_detection"] = enable_rules_detection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_pr_creation = d.pop("enable_pr_creation", UNSET)

        enable_rules_detection = d.pop("enable_rules_detection", UNSET)

        organization_settings = cls(
            enable_pr_creation=enable_pr_creation,
            enable_rules_detection=enable_rules_detection,
        )

        organization_settings.additional_properties = d
        return organization_settings

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
