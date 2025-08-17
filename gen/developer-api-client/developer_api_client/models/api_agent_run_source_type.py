from enum import Enum


class ApiAgentRunSourceType(str, Enum):
    API = "API"
    CHAT = "CHAT"
    GITHUB = "GITHUB"
    GITHUB_CHECK_SUITE = "GITHUB_CHECK_SUITE"
    JIRA = "JIRA"
    LINEAR = "LINEAR"
    LOCAL = "LOCAL"
    SLACK = "SLACK"

    def __str__(self) -> str:
        return str(self.value)
