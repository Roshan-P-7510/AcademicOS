from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTreeView,
    QFileSystemModel
)

from PySide6.QtCore import QModelIndex

from core.session import Session

class Sidebar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        # ---------------- FILE SYSTEM MODEL ----------------
        self.model = QFileSystemModel()
        self.model.setRootPath("C:/")

        # ---------------- TREE VIEW ----------------
        self.tree = QTreeView()
        self.tree.setModel(self.model)

        self.tree.setHeaderHidden(True)
        self.tree.setAnimated(True)
        self.tree.setIndentation(15)

        self.tree.doubleClicked.connect(self.on_double_click)

        self.layout.addWidget(self.tree)

    def update_workspace(self):
        """
        Call this when workspace changes.
        """

        if not Session.workspace_path:
            return

        root_path = Session.workspace_path

        self.tree.setRootIndex(
            self.model.setRootPath(root_path)
        )

    def on_double_click(self, index: QModelIndex):

        path = self.model.filePath(index)

        # For now: just print (later we open notes/files)
        print("Clicked:", path)