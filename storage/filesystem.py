from pathlib import Path
import json
import sqlite3


class FileSystem:

    DEFAULT_FOLDERS = [
        "Subjects",
        "Notes",
        "PDFs",
        "Images",
        "Exports",
        "Backups",
        "Trash",
    ]

    DATABASES = [
        "workspace.db",
        "search.db",
    ]

    @classmethod
    def create_workspace(
        cls,
        parent_folder: str,
        workspace_name: str,
    ) -> Path:

        workspace_path = Path(parent_folder) / workspace_name

        if workspace_path.exists():
            raise FileExistsError(
                f'"{workspace_name}" already exists.'
            )

        # Create root folder
        workspace_path.mkdir(parents=True)

        # Create subfolders
        for folder in cls.DEFAULT_FOLDERS:
            (workspace_path / folder).mkdir()

        # Create databases
        for db in cls.DATABASES:
            sqlite3.connect(
                workspace_path / db
            ).close()

        # Create workspace.json
        metadata = {
            "name": workspace_name,
            "version": "0.1",
            "subjects": 0,
            "notes": 0,
            "pdfs": 0,
            "images": 0,
        }

        with open(
            workspace_path / "workspace.json",
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
            )

        return workspace_path