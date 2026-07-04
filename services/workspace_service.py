from pathlib import Path

from storage.filesystem import FileSystem


class WorkspaceService:

    @staticmethod
    def create_workspace(
        name: str,
        location: str,
    ) -> Path:

        if not name:
            raise ValueError(
                "Workspace name cannot be empty."
            )

        if not location:
            raise ValueError(
                "Please choose a location."
            )

        return FileSystem.create_workspace(
            parent_folder=location,
            workspace_name=name,
        )