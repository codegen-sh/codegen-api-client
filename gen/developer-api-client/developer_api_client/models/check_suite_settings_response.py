from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CheckSuiteSettingsResponse")


@_attrs_define
class CheckSuiteSettingsResponse:
    """Response model for check suite settings.

    Example:
        {'ignored_checks': ['dependency-review', 'security-scan'], 'retry_count': 3}

    Attributes:
        retry_count (int): Number of retry attempts for failed checks
        ignored_checks (list[str]): List of check names to ignore
    """

    retry_count: int
    ignored_checks: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retry_count = self.retry_count

        ignored_checks = self.ignored_checks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retry_count": retry_count,
                "ignored_checks": ignored_checks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retry_count = d.pop("retry_count")

        ignored_checks = cast(list[str], d.pop("ignored_checks"))

        check_suite_settings_response = cls(
            retry_count=retry_count,
            ignored_checks=ignored_checks,
        )

        check_suite_settings_response.additional_properties = d
        return check_suite_settings_response

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
