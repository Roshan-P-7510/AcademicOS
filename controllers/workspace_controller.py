from PySide6.QtWidgets import QMessageBox

from dialogs.create_workspace_dialog import CreateWorkspaceDialog
from services.workspace_service import WorkspaceService


class WorkspaceController:

    def __init__(self, parent):
        self.parent = parent

    def create_workspace(self):

        dialog = CreateWorkspaceDialog()

        if dialog.exec():

            name = dialog.workspace_name()
            location = dialog.workspace_location()

            if not name or not location:
                QMessageBox.warning(
                    self.parent,
                    "Missing Information",
                    "Please enter both a workspace name and location."
                )
                return

            path = WorkspaceService.create_workspace(
                name,
                location
            )

            QMessageBox.information(
                self.parent,
                "Success",
                f"Workspace created:\n\n{path}"
            )