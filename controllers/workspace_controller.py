from PySide6.QtWidgets import QMessageBox

from dialogs.create_workspace_dialog import CreateWorkspaceDialog
from services.workspace_service import WorkspaceService


class WorkspaceController:

    def __init__(self, parent):
        self.parent = parent

    def create_workspace(self):

        dialog = CreateWorkspaceDialog(self.parent)

        if dialog.exec():

            try:

                workspace = WorkspaceService.create_workspace(
                    dialog.workspace_name(),
                    dialog.workspace_location()
                )

                QMessageBox.information(
                    self.parent,
                    "Success",
                    f"Workspace created!\n\n{workspace}"
                )

            except Exception as e:

                QMessageBox.critical(
                    self.parent,
                    "Error",
                    str(e)
                )