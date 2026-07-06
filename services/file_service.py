"""
AcademicOS
Sprint B.1

Business logic for reading files.
"""

from pathlib import Path


class FileService:
    """
    Handles reading supported file types.
    """

    SUPPORTED_TEXT = {
        ".txt",
        ".md",
    }

    @staticmethod
    def read(path: str) -> tuple[str, str]:
        """
        Reads a supported file.

        Returns:
            (filename, content)

        Raises:
            FileNotFoundError
            ValueError
        """

        file = Path(path)

        if not file.exists():
            raise FileNotFoundError(
                "The selected file does not exist."
            )

        suffix = file.suffix.lower()

        if suffix not in FileService.SUPPORTED_TEXT:
            raise ValueError(
                f"Unsupported file type: {suffix}"
            )

        content = file.read_text(
            encoding="utf-8",
            errors="replace"
        )

        return file.name, content