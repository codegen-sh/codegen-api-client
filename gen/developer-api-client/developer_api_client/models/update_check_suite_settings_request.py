from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCheckSuiteSettingsRequest")


@_attrs_define
class UpdateCheckSuiteSettingsRequest:
    """Request model for updating check suite settings.

    Example:
        {'ignored_checks': ['dependency-review', 'security-scan'], 'retry_count': 3}

    Attributes:
        retry_count (Union[None, Unset, int]): Number of retry attempts for failed checks
        ignored_checks (Union[None, Unset, list[str]]): List of check names to ignore
    """

    retry_count: Union[None, Unset, int] = UNSET
    ignored_checks: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retry_count: Union[None, Unset, int]
        if isinstance(self.retry_count, Unset):
            retry_count = UNSET
        else:
            retry_count = self.retry_count

        ignored_checks: Union[None, Unset, list[str]]
        if isinstance(self.ignored_checks, Unset):
            ignored_checks = UNSET
        elif isinstance(self.ignored_checks, list):
            ignored_checks = self.ignored_checks

        else:
            ignored_checks = self.ignored_checks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if ignored_checks is not UNSET:
            field_dict["ignored_checks"] = ignored_checks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_retry_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        retry_count = _parse_retry_count(d.pop("retry_count", UNSET))

        def _parse_ignored_checks(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ignored_checks_type_0 = cast(list[str], data)

                return ignored_checks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        ignored_checks = _parse_ignored_checks(d.pop("ignored_checks", UNSET))

        update_check_suite_settings_request = cls(
            retry_count=retry_count,
            ignored_checks=ignored_checks,
        )

        update_check_suite_settings_request.additional_properties = d
        return update_check_suite_settings_request

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
