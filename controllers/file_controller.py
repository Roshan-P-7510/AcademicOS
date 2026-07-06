"""
AcademicOS
Sprint B.1

Coordinates file opening.
"""

from PySide6.QtWidgets import QMessageBox

from services.file_service import FileService


class FileController:

    def __init__(self, parent):
        self.parent = parent

    def open_file(self, path: str):

        try:

            filename, content = FileService.read(path)

            self.parent.workspace.open_text(
                filename,
                content
            )

            self.parent.statusBar().showMessage(filename)

        except Exception as e:

            QMessageBox.warning(
                self.parent,
                "Open File",
                str(e)
            )