"""
AcademicOS

Workspace Explorer
"""

from PySide6.QtCore import QModelIndex, Signal
from PySide6.QtWidgets import (
    QFileSystemModel,
    QTreeView,
    QVBoxLayout,
    QWidget,
)

from core.session import Session


class Sidebar(QWidget):
    """
    Displays the currently opened workspace.
    """

    # Emitted when the user wants to open a file.
    file_open_requested = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # ---------------- FILE SYSTEM MODEL ----------------

        self.model = QFileSystemModel()
        self.model.setRootPath("")

        # ---------------- TREE VIEW ----------------

        self.tree = QTreeView()
        self.tree.setModel(self.model)

        self.tree.setHeaderHidden(True)
        self.tree.setAnimated(True)
        self.tree.setIndentation(18)

        self.tree.doubleClicked.connect(
            self.on_double_click
        )

        layout.addWidget(self.tree)

    # -------------------------------------------------

    def update_workspace(self):
        """
        Refresh explorer.
        """

        if not Session.is_workspace_open():
            return

        root = Session.workspace_path

        index = self.model.setRootPath(root)
        self.tree.setRootIndex(index)

    # -------------------------------------------------

    def on_double_click(self, index: QModelIndex):
        """
        Emit a signal only for files.
        """

        path = self.model.filePath(index)

        # Ignore folders
        if self.model.isDir(index):
            return

        self.file_open_requested.emit(path)