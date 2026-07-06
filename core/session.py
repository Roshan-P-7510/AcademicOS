from typing import Optional


class Session:
    """
    Global application session (single workspace state).
    """

    workspace_path: Optional[str] = None
    workspace_name: Optional[str] = None
    workspace_data: dict = {}

    @classmethod
    def is_workspace_open(cls) -> bool:
        return cls.workspace_path is not None

    @classmethod
    def open_workspace(cls, path: str, data: dict) -> None:
        cls.workspace_path = path
        cls.workspace_name = data.get("name")
        cls.workspace_data = data

    @classmethod
    def close_workspace(cls) -> None:
        cls.workspace_path = None
        cls.workspace_name = None
        cls.workspace_data = {}

    @classmethod
    def current_workspace(cls) -> dict:
        return cls.workspace_data