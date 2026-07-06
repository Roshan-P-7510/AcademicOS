from pathlib import Path
import json
from typing import Dict, Any


class FileSystem:
    """
    Handles all filesystem operations for AcademicOS.
    """

    APP_FOLDER = ".academicos"
    CONFIG_FILE = "workspace.json"

    @staticmethod
    def workspace_exists(path: str) -> bool:
        return Path(path).exists()

    @staticmethod
    def create_directory(path: str):
        Path(path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def create_workspace_structure(path: str):
        root = Path(path)

        folders = [
            "Notes",
            "Assignments",
            "Resources",
            "Exams",
            "Projects",
            ".academicos"
        ]

        for folder in folders:
            (root / folder).mkdir(parents=True, exist_ok=True)

        config = {
            "name": root.name,
            "version": "1.0",
            "type": "AcademicOS Workspace"
        }

        config_path = root / FileSystem.APP_FOLDER / FileSystem.CONFIG_FILE

        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)

    @staticmethod
    def is_workspace(path: str) -> bool:
        config = (
            Path(path)
            / FileSystem.APP_FOLDER
            / FileSystem.CONFIG_FILE
        )

        return config.exists()

    @staticmethod
    def load_workspace(path: str) -> Dict[str, Any]:
        config = (
            Path(path)
            / FileSystem.APP_FOLDER
            / FileSystem.CONFIG_FILE
        )

        with open(config, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def save_workspace(path: str, data: Dict[str, Any]):
        config = (
            Path(path)
            / FileSystem.APP_FOLDER
            / FileSystem.CONFIG_FILE
        )

        with open(config, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)