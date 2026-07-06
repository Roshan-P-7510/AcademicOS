from PySide6.QtWidgets import QMessageBox, QFileDialog
from services.recent_service import RecentService
from dialogs.create_workspace_dialog import CreateWorkspaceDialog
from services.workspace_service import WorkspaceService
from core.session import Session


class WorkspaceController:

    def __init__(self, parent):
        self.parent = parent

    # ---------------- CREATE WORKSPACE ----------------

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

    # ---------------- OPEN WORKSPACE ----------------

    def open_workspace(self):

        folder = QFileDialog.getExistingDirectory(
            self.parent,
            "Open Workspace"
        )

        if not folder:
            return

        try:
            path, data = WorkspaceService.open_workspace(folder)

            # update session
            Session.open_workspace(path, data)
            RecentService.add(path)

            # update UI
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

        except FileNotFoundError as e:
            QMessageBox.warning(self.parent, "Error", str(e))

        except ValueError as e:
            QMessageBox.warning(self.parent, "Error", str(e))

        except Exception as e:
            QMessageBox.critical(self.parent, "Error", str(e))