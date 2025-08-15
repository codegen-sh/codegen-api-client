from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_agent_run_source_type import ApiAgentRunSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_run_response_metadata_type_0 import AgentRunResponseMetadataType0
    from ..models.github_pull_request_response import GithubPullRequestResponse


T = TypeVar("T", bound="AgentRunResponse")


@_attrs_define
class AgentRunResponse:
    """Represents an agent run in API responses

    Attributes:
        id (int):
        organization_id (int):
        status (Union[None, Unset, str]):
        created_at (Union[None, Unset, str]):
        web_url (Union[None, Unset, str]):
        result (Union[None, Unset, str]):
        source_type (Union[ApiAgentRunSourceType, None, Unset]):
        github_pull_requests (Union[None, Unset, list['GithubPullRequestResponse']]):
        metadata (Union['AgentRunResponseMetadataType0', None, Unset]):
    """

    id: int
    organization_id: int
    status: Union[None, Unset, str] = UNSET
    created_at: Union[None, Unset, str] = UNSET
    web_url: Union[None, Unset, str] = UNSET
    result: Union[None, Unset, str] = UNSET
    source_type: Union[ApiAgentRunSourceType, None, Unset] = UNSET
    github_pull_requests: Union[None, Unset, list["GithubPullRequestResponse"]] = UNSET
    metadata: Union["AgentRunResponseMetadataType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_run_response_metadata_type_0 import AgentRunResponseMetadataType0

        id = self.id

        organization_id = self.organization_id

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        web_url: Union[None, Unset, str]
        if isinstance(self.web_url, Unset):
            web_url = UNSET
        else:
            web_url = self.web_url

        result: Union[None, Unset, str]
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        source_type: Union[None, Unset, str]
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        elif isinstance(self.source_type, ApiAgentRunSourceType):
            source_type = self.source_type.value
        else:
            source_type = self.source_type

        github_pull_requests: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.github_pull_requests, Unset):
            github_pull_requests = UNSET
        elif isinstance(self.github_pull_requests, list):
            github_pull_requests = []
            for github_pull_requests_type_0_item_data in self.github_pull_requests:
                github_pull_requests_type_0_item = github_pull_requests_type_0_item_data.to_dict()
                github_pull_requests.append(github_pull_requests_type_0_item)

        else:
            github_pull_requests = self.github_pull_requests

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, AgentRunResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organization_id": organization_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if web_url is not UNSET:
            field_dict["web_url"] = web_url
        if result is not UNSET:
            field_dict["result"] = result
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if github_pull_requests is not UNSET:
            field_dict["github_pull_requests"] = github_pull_requests
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_response_metadata_type_0 import AgentRunResponseMetadataType0
        from ..models.github_pull_request_response import GithubPullRequestResponse

        d = dict(src_dict)
        id = d.pop("id")

        organization_id = d.pop("organization_id")

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_web_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        web_url = _parse_web_url(d.pop("web_url", UNSET))

        def _parse_result(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        result = _parse_result(d.pop("result", UNSET))

        def _parse_source_type(data: object) -> Union[ApiAgentRunSourceType, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_type_0 = ApiAgentRunSourceType(data)

                return source_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ApiAgentRunSourceType, None, Unset], data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_github_pull_requests(data: object) -> Union[None, Unset, list["GithubPullRequestResponse"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                github_pull_requests_type_0 = []
                _github_pull_requests_type_0 = data
                for github_pull_requests_type_0_item_data in _github_pull_requests_type_0:
                    github_pull_requests_type_0_item = GithubPullRequestResponse.from_dict(
                        github_pull_requests_type_0_item_data
                    )

                    github_pull_requests_type_0.append(github_pull_requests_type_0_item)

                return github_pull_requests_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["GithubPullRequestResponse"]], data)

        github_pull_requests = _parse_github_pull_requests(d.pop("github_pull_requests", UNSET))

        def _parse_metadata(data: object) -> Union["AgentRunResponseMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AgentRunResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AgentRunResponseMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        agent_run_response = cls(
            id=id,
            organization_id=organization_id,
            status=status,
            created_at=created_at,
            web_url=web_url,
            result=result,
            source_type=source_type,
            github_pull_requests=github_pull_requests,
            metadata=metadata,
        )

        agent_run_response.additional_properties = d
        return agent_run_response

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
