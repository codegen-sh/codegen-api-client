from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_run_log_response import AgentRunLogResponse
    from ..models.agent_run_with_logs_response_metadata_type_0 import AgentRunWithLogsResponseMetadataType0


T = TypeVar("T", bound="AgentRunWithLogsResponse")


@_attrs_define
class AgentRunWithLogsResponse:
    """Represents an agent run in API responses

    Attributes:
        id (int):
        organization_id (int):
        logs (list['AgentRunLogResponse']):
        status (Union[None, Unset, str]):
        created_at (Union[None, Unset, str]):
        web_url (Union[None, Unset, str]):
        result (Union[None, Unset, str]):
        metadata (Union['AgentRunWithLogsResponseMetadataType0', None, Unset]):
        total_logs (Union[None, Unset, int]):
        page (Union[None, Unset, int]):
        size (Union[None, Unset, int]):
        pages (Union[None, Unset, int]):
    """

    id: int
    organization_id: int
    logs: list["AgentRunLogResponse"]
    status: Union[None, Unset, str] = UNSET
    created_at: Union[None, Unset, str] = UNSET
    web_url: Union[None, Unset, str] = UNSET
    result: Union[None, Unset, str] = UNSET
    metadata: Union["AgentRunWithLogsResponseMetadataType0", None, Unset] = UNSET
    total_logs: Union[None, Unset, int] = UNSET
    page: Union[None, Unset, int] = UNSET
    size: Union[None, Unset, int] = UNSET
    pages: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_run_with_logs_response_metadata_type_0 import AgentRunWithLogsResponseMetadataType0

        id = self.id

        organization_id = self.organization_id

        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()
            logs.append(logs_item)

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

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, AgentRunWithLogsResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        total_logs: Union[None, Unset, int]
        if isinstance(self.total_logs, Unset):
            total_logs = UNSET
        else:
            total_logs = self.total_logs

        page: Union[None, Unset, int]
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        pages: Union[None, Unset, int]
        if isinstance(self.pages, Unset):
            pages = UNSET
        else:
            pages = self.pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organization_id": organization_id,
                "logs": logs,
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
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if total_logs is not UNSET:
            field_dict["total_logs"] = total_logs
        if page is not UNSET:
            field_dict["page"] = page
        if size is not UNSET:
            field_dict["size"] = size
        if pages is not UNSET:
            field_dict["pages"] = pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run_log_response import AgentRunLogResponse
        from ..models.agent_run_with_logs_response_metadata_type_0 import AgentRunWithLogsResponseMetadataType0

        d = dict(src_dict)
        id = d.pop("id")

        organization_id = d.pop("organization_id")

        logs = []
        _logs = d.pop("logs")
        for logs_item_data in _logs:
            logs_item = AgentRunLogResponse.from_dict(logs_item_data)

            logs.append(logs_item)

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

        def _parse_metadata(data: object) -> Union["AgentRunWithLogsResponseMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AgentRunWithLogsResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AgentRunWithLogsResponseMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_total_logs(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_logs = _parse_total_logs(d.pop("total_logs", UNSET))

        def _parse_page(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        page = _parse_page(d.pop("page", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_pages(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pages = _parse_pages(d.pop("pages", UNSET))

        agent_run_with_logs_response = cls(
            id=id,
            organization_id=organization_id,
            logs=logs,
            status=status,
            created_at=created_at,
            web_url=web_url,
            result=result,
            metadata=metadata,
            total_logs=total_logs,
            page=page,
            size=size,
            pages=pages,
        )

        agent_run_with_logs_response.additional_properties = d
        return agent_run_with_logs_response

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
