from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FastAPIRateLimitResponse")


@_attrs_define
class FastAPIRateLimitResponse:
    """
    Attributes:
        detail (Union[Unset, str]):  Default: 'Rate limit exceeded'.
        status_code (Union[Unset, int]):  Default: 429.
    """

    detail: Union[Unset, str] = "Rate limit exceeded"
    status_code: Union[Unset, int] = 429
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detail is not UNSET:
            field_dict["detail"] = detail
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detail = d.pop("detail", UNSET)

        status_code = d.pop("status_code", UNSET)

        fast_api_rate_limit_response = cls(
            detail=detail,
            status_code=status_code,
        )

        fast_api_rate_limit_response.additional_properties = d
        return fast_api_rate_limit_response

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
