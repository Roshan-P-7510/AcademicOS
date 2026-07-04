from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMenuBar


class MainMenuBar(QMenuBar):
    """Application Menu Bar."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self._create_menus()

    def _create_menus(self):

        # ---------------- FILE ----------------

        file_menu = self.addMenu("&File")

        self.new_workspace_action = QAction("New Workspace", self)
        self.new_workspace_action.setShortcut(QKeySequence.New)

        self.open_workspace_action = QAction("Open Workspace", self)
        self.open_workspace_action.setShortcut(QKeySequence.Open)

        self.save_action = QAction("Save", self)
        self.save_action.setShortcut(QKeySequence.Save)

        self.exit_action = QAction("Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")

        file_menu.addAction(self.new_workspace_action)
        file_menu.addAction(self.open_workspace_action)
        file_menu.addSeparator()
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        # ---------------- EDIT ----------------

        edit_menu = self.addMenu("&Edit")

        self.undo_action = QAction("Undo", self)
        self.undo_action.setShortcut(QKeySequence.Undo)

        self.redo_action = QAction("Redo", self)
        self.redo_action.setShortcut(QKeySequence.Redo)

        edit_menu.addAction(self.undo_action)
        edit_menu.addAction(self.redo_action)

        # ---------------- VIEW ----------------

        self.view_menu = self.addMenu("&View")

        # ---------------- WORKSPACE ----------------

        self.workspace_menu = self.addMenu("&Workspace")

        # ---------------- TOOLS ----------------

        self.tools_menu = self.addMenu("&Tools")

        # ---------------- HELP ----------------

        help_menu = self.addMenu("&Help")

        self.about_action = QAction("About AcademicOS", self)

        help_menu.addAction(self.about_action)