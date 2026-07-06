from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMenuBar


class MainMenuBar(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._create_menus()

    def _create_menus(self):

        file_menu = self.addMenu("&File")

        self.new_workspace_action = QAction("New Workspace", self)
        self.new_workspace_action.setShortcut(QKeySequence.New)

        self.open_workspace_action = QAction("Open Workspace", self)
        self.open_workspace_action.setShortcut(QKeySequence.Open)

        self.recent_menu = file_menu.addMenu("Open Recent")

        self.save_action = QAction("Save", self)
        self.save_action.setShortcut(QKeySequence.Save)

        self.exit_action = QAction("Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")

        file_menu.addAction(self.new_workspace_action)
        file_menu.addAction(self.open_workspace_action)
        file_menu.addMenu(self.recent_menu)
        file_menu.addSeparator()
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        edit_menu = self.addMenu("&Edit")

        self.undo_action = QAction("Undo", self)
        self.undo_action.setShortcut(QKeySequence.Undo)

        self.redo_action = QAction("Redo", self)
        self.redo_action.setShortcut(QKeySequence.Redo)

        edit_menu.addAction(self.undo_action)
        edit_menu.addAction(self.redo_action)

        self.view_menu = self.addMenu("&View")
        self.workspace_menu = self.addMenu("&Workspace")
        self.tools_menu = self.addMenu("&Tools")

        help_menu = self.addMenu("&Help")

        self.about_action = QAction("About AcademicOS", self)
        help_menu.addAction(self.about_action)

    # 🔥 NEW: helper for Feature Pack 4
    def set_recent_items(self, items, callback):
        """
        items: list of workspace paths
        callback: function(path) -> open workspace
        """

        self.recent_menu.clear()

        if not items:
            empty = QAction("No recent workspaces", self)
            empty.setEnabled(False)
            self.recent_menu.addAction(empty)
            return

        for path in items:
            action = QAction(path, self)

            action.triggered.connect(
                lambda checked, p=path: callback(p)
            )

            self.recent_menu.addAction(action)