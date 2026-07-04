from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QHBoxLayout,
    QVBoxLayout,
)


class CreateWorkspaceDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Create Workspace")
        self.setMinimumWidth(500)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Workspace Name"))

        self.name_edit = QLineEdit()
        layout.addWidget(self.name_edit)

        layout.addWidget(QLabel("Location"))

        row = QHBoxLayout()

        self.location_edit = QLineEdit()
        self.location_edit.setReadOnly(True)

        browse_btn = QPushButton("Browse")

        row.addWidget(self.location_edit)
        row.addWidget(browse_btn)

        layout.addLayout(row)

        buttons = QHBoxLayout()

        self.create_btn = QPushButton("Create")
        self.cancel_btn = QPushButton("Cancel")

        buttons.addStretch()
        buttons.addWidget(self.cancel_btn)
        buttons.addWidget(self.create_btn)

        layout.addLayout(buttons)

        browse_btn.clicked.connect(self.choose_folder)
        self.cancel_btn.clicked.connect(self.reject)
        self.create_btn.clicked.connect(self.accept)

    def choose_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Choose Workspace Location"
        )

        if folder:
            self.location_edit.setText(folder)

    def workspace_name(self):
        return self.name_edit.text().strip()

    def workspace_location(self):
        return self.location_edit.text().strip()