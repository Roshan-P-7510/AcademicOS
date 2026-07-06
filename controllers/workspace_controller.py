from PySide6.QtWidgets import QFileDialog, QMessageBox

from core.session import Session
from dialogs.create_workspace_dialog import CreateWorkspaceDialog
from services.recent_service import RecentService
from services.workspace_service import WorkspaceService


class WorkspaceController:

    def __init__(self, parent):
        self.parent = parent

    # --------------------------------------------------
    # CREATE WORKSPACE
    # --------------------------------------------------

    def create_workspace(self):

        dialog = CreateWorkspaceDialog(self.parent)

        if not dialog.exec():
            return

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

    # --------------------------------------------------
    # OPEN WORKSPACE
    # --------------------------------------------------

    def open_workspace(self):

        folder = QFileDialog.getExistingDirectory(
            self.parent,
            "Open Workspace"
        )

        if not folder:
            return

        self._open(folder)

    # --------------------------------------------------
    # INTERNAL
    # --------------------------------------------------

    def _open(self, folder: str):

        try:

            path, data = WorkspaceService.open_workspace(folder)

            Session.open_workspace(path, data)

            RecentService.add(path)

            self.parent.setWindowTitle(
                f"AcademicOS — {Session.workspace_name}"
            )

            self.parent.statusBar().showMessage(
                "Workspace opened successfully."
            )

            QMessageBox.information(
                self.parent,
                "Success",
                "Workspace opened successfully."
            )

        except (FileNotFoundError, ValueError) as e:

            QMessageBox.warning(
                self.parent,
                "Workspace",
                str(e)
            )

        except Exception as e:

            QMessageBox.critical(
                self.parent,
                "Error",
                str(e)
            )