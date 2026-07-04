from pathlib import Path

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QHBoxLayout,
    QDialogButtonBox,
    QMessageBox,
)


class CreateWorkspaceDialog(QDialog):
    """
    Dialog used to create a new AcademicOS workspace.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Create Workspace")
        self.setMinimumWidth(500)

        self._build_ui()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        # ---------------- Workspace Name ----------------

        layout.addWidget(QLabel("Workspace Name"))

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText(
            "Example: Class 12 Science"
        )

        layout.addWidget(self.name_edit)

        # ---------------- Location ----------------

        layout.addWidget(QLabel("Location"))

        location_layout = QHBoxLayout()

        self.location_edit = QLineEdit()
        self.location_edit.setPlaceholderText(
            "Choose where the workspace will be created..."
        )

        browse_button = QPushButton("Browse...")

        browse_button.clicked.connect(
            self.choose_location
        )

        location_layout.addWidget(self.location_edit)
        location_layout.addWidget(browse_button)

        layout.addLayout(location_layout)

        # ---------------- Buttons ----------------

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.Ok |
            QDialogButtonBox.Cancel
        )

        self.button_box.button(
            QDialogButtonBox.Ok
        ).setText("Create")

        self.button_box.accepted.connect(
            self.validate
        )

        self.button_box.rejected.connect(
            self.reject
        )

        layout.addWidget(self.button_box)

    # -------------------------------------------------

    def choose_location(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Workspace Location"
        )

        if folder:
            self.location_edit.setText(folder)

    # -------------------------------------------------

    def validate(self):

        name = self.workspace_name()

        location = self.workspace_location()

        if not name:

            QMessageBox.warning(
                self,
                "Invalid Name",
                "Please enter a workspace name."
            )

            return

        if not location:

            QMessageBox.warning(
                self,
                "Invalid Location",
                "Please choose a workspace location."
            )

            return

        workspace_path = Path(location) / name

        if workspace_path.exists():

            QMessageBox.warning(
                self,
                "Workspace Exists",
                "A workspace with this name already exists."
            )

            return

        self.accept()

    # -------------------------------------------------

    def workspace_name(self) -> str:

        return self.name_edit.text().strip()

    # -------------------------------------------------

    def workspace_location(self) -> str:

        return self.location_edit.text().strip()