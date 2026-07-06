from pathlib import Path

from storage.filesystem import FileSystem


class WorkspaceService:
    """
    Business logic for workspace operations.
    """

    @staticmethod
    def create_workspace(name: str, directory: str) -> str:
        """
        Creates a new AcademicOS workspace.

        Args:
            name:
                Workspace name.

            directory:
                Parent directory.

        Returns:
            Full workspace path.
        """

        workspace_path = Path(directory) / name

        if workspace_path.exists():
            raise FileExistsError(
                f"Workspace already exists.\n\n{workspace_path}"
            )

        FileSystem.create_directory(str(workspace_path))
        FileSystem.create_workspace_structure(str(workspace_path))

        return str(workspace_path)

    @staticmethod
    def open_workspace(path: str) -> tuple[str, dict]:
        """
        Opens an existing workspace.

        Args:
            path:
                Workspace directory.

        Returns:
            (workspace_path, workspace_data)

        Raises:
            FileNotFoundError
            ValueError
        """

        if not FileSystem.workspace_exists(path):
            raise FileNotFoundError(
                "The selected folder does not exist."
            )

        if not FileSystem.is_workspace(path):
            raise ValueError(
                "This is not an AcademicOS workspace."
            )

        data = FileSystem.load_workspace(path)

        return path, data

    @staticmethod
    def workspace_name(path: str) -> str:
        """
        Returns the workspace name.
        """

        return FileSystem.load_workspace(path).get(
            "name",
            "Unknown Workspace"
        )

    @staticmethod
    def workspace_version(path: str) -> str:
        """
        Returns workspace version.
        """

        return FileSystem.load_workspace(path).get(
            "version",
            "Unknown"
        )