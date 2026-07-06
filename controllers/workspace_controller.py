from PySide6.QtWidgets import QFileDialog, QMessageBox

from core.session import Session
from dialogs.create_workspace_dialog import CreateWorkspaceDialog
from services.recent_service import RecentService
from services.workspace_service import WorkspaceService


class WorkspaceController:
    """
    Handles workspace-related UI actions.
    """

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
                "Workspace Created",
                f"Workspace created successfully.\n\n{workspace}"
            )

        except Exception as e:

            QMessageBox.critical(
                self.parent,
                "Error",
                str(e)
            )

    # --------------------------------------------------
    # OPEN FROM DIALOG
    # --------------------------------------------------

    def open_workspace(self):

        folder = QFileDialog.getExistingDirectory(
            self.parent,
            "Open Workspace"
        )

        if not folder:
            return

        self.open_workspace_from_path(folder)

    # --------------------------------------------------
    # OPEN FROM PATH
    # --------------------------------------------------

    def open_workspace_from_path(self, folder: str):

        try:

            path, data = WorkspaceService.open_workspace(folder)

            # Update session
            Session.open_workspace(path, data)

            # Save to recent workspaces
            RecentService.add(path)

            # Refresh entire UI
            self.parent.refresh_workspace()

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