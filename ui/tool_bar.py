from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


class MainToolBar(QToolBar):
    """Main Application Toolbar."""

    def __init__(self, parent=None):
        super().__init__("Main Toolbar", parent)

        self.setMovable(False)

        self.setFloatable(False)

        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self._create_actions()

    def _create_actions(self):

        self.new_action = QAction("New", self)

        self.open_action = QAction("Open", self)

        self.save_action = QAction("Save", self)

        self.undo_action = QAction("Undo", self)

        self.redo_action = QAction("Redo", self)

        self.search_action = QAction("Search", self)

        self.addAction(self.new_action)

        self.addAction(self.open_action)

        self.addAction(self.save_action)

        self.addSeparator()

        self.addAction(self.undo_action)

        self.addAction(self.redo_action)

        self.addSeparator()

        self.addAction(self.search_action)