from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CheckSuiteRetryStatsResponse")


@_attrs_define
class CheckSuiteRetryStatsResponse:
    """Response model for check suite retry statistics.

    Example:
        {'active_orchestrations': 2, 'checks_at_retry_limit': 8, 'completed_orchestrations': 40,
            'failed_orchestrations': 3, 'repo_id': 123, 'total_orchestrations': 45, 'total_retry_attempts': 67}

    Attributes:
        repo_id (int): Repository ID
        total_orchestrations (int): Total number of orchestrations
        active_orchestrations (int): Number of active orchestrations
        completed_orchestrations (int): Number of completed orchestrations
        failed_orchestrations (int): Number of failed orchestrations
        total_retry_attempts (int): Total number of retry attempts across all checks
        checks_at_retry_limit (int): Number of checks that have reached their retry limit
    """

    repo_id: int
    total_orchestrations: int
    active_orchestrations: int
    completed_orchestrations: int
    failed_orchestrations: int
    total_retry_attempts: int
    checks_at_retry_limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_id = self.repo_id

        total_orchestrations = self.total_orchestrations

        active_orchestrations = self.active_orchestrations

        completed_orchestrations = self.completed_orchestrations

        failed_orchestrations = self.failed_orchestrations

        total_retry_attempts = self.total_retry_attempts

        checks_at_retry_limit = self.checks_at_retry_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repo_id": repo_id,
                "total_orchestrations": total_orchestrations,
                "active_orchestrations": active_orchestrations,
                "completed_orchestrations": completed_orchestrations,
                "failed_orchestrations": failed_orchestrations,
                "total_retry_attempts": total_retry_attempts,
                "checks_at_retry_limit": checks_at_retry_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_id = d.pop("repo_id")

        total_orchestrations = d.pop("total_orchestrations")

        active_orchestrations = d.pop("active_orchestrations")

        completed_orchestrations = d.pop("completed_orchestrations")

        failed_orchestrations = d.pop("failed_orchestrations")

        total_retry_attempts = d.pop("total_retry_attempts")

        checks_at_retry_limit = d.pop("checks_at_retry_limit")

        check_suite_retry_stats_response = cls(
            repo_id=repo_id,
            total_orchestrations=total_orchestrations,
            active_orchestrations=active_orchestrations,
            completed_orchestrations=completed_orchestrations,
            failed_orchestrations=failed_orchestrations,
            total_retry_attempts=total_retry_attempts,
            checks_at_retry_limit=checks_at_retry_limit,
        )

        check_suite_retry_stats_response.additional_properties = d
        return check_suite_retry_stats_response

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
