from pathlib import Path
import json


class WorkspaceService:

    @staticmethod
    def create_workspace(name, location):

        root = Path(location) / name

        root.mkdir(parents=True, exist_ok=True)

        folders = [
            "Subjects",
            "Notes",
            "PDFs",
            "Images",
            "Exports",
            "Backups",
            "Cache",
            "Trash",
        ]

        for folder in folders:
            (root / folder).mkdir(exist_ok=True)

        (root / "workspace.db").touch()

        (root / "search.db").touch()

        config = {
            "name": name,
            "version": "1.0",
            "created_by": "AcademicOS",
        }

        with open(root / "workspace.json", "w") as f:
            json.dump(config, f, indent=4)

        return root