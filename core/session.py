from typing import Dict, Optional


class Session:
    """
    Stores the currently opened workspace.

    This class acts as the single source of truth for
    the active workspace during the application's lifetime.
    """

    workspace_path: Optional[str] = None
    workspace_name: Optional[str] = None
    workspace_data: Optional[Dict] = None

    @classmethod
    def is_workspace_open(cls) -> bool:
        return cls.workspace_path is not None

    @classmethod
    def open_workspace(cls, path: str, data: Dict) -> None:
        cls.workspace_path = path
        cls.workspace_name = data.get("name")
        cls.workspace_data = data.copy()

    @classmethod
    def close_workspace(cls) -> None:
        cls.workspace_path = None
        cls.workspace_name = None
        cls.workspace_data = None

    @classmethod
    def current_workspace(cls) -> Optional[Dict]:
        return cls.workspace_data