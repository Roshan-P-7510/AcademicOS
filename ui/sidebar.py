"""
AcademicOS

Sidebar (Explorer)
"""

from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import (
    QFileSystemModel,
    QTreeView,
    QVBoxLayout,
    QWidget,
)

from core.session import Session


class Sidebar(QWidget):
    """
    Workspace Explorer.
    Displays the currently opened AcademicOS workspace.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # -------------------------------------------------
        # File System Model
        # -------------------------------------------------

        self.model = QFileSystemModel()
        self.model.setRootPath("")

        # -------------------------------------------------
        # Tree View
        # -------------------------------------------------

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
        Refresh the explorer to display
        the currently opened workspace.
        """

        if not Session.is_workspace_open():
            return

        root = Session.workspace_path

        index = self.model.setRootPath(root)
        self.tree.setRootIndex(index)

    # -------------------------------------------------

    def on_double_click(self, index: QModelIndex):
        """
        Placeholder.

        Sprint B:
            Open notes
            Open PDFs
            Open images
        """

        path = self.model.filePath(index)

        print(f"Open file: {path}")