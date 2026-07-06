from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDockWidget,
    QMainWindow,
)

from services.recent_service import RecentService
from controllers.workspace_controller import WorkspaceController
from ui.menu_bar import MainMenuBar
from ui.tool_bar import MainToolBar
from ui.workspace import Workspace
from ui.sidebar import Sidebar
from ui.inspector import Inspector


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AcademicOS")
        self.resize(1600, 900)

        self.workspace_controller = WorkspaceController(self)

        self.build_ui()

    def build_ui(self):

        # ---------- Menu ----------
        self.menu = MainMenuBar(self)
        self.setMenuBar(self.menu)

        # ---------- Toolbar ----------
        self.toolbar = MainToolBar(self)
        self.addToolBar(self.toolbar)

        # ---------- Workspace ----------
        self.workspace = Workspace()
        self.setCentralWidget(self.workspace)

        # ---------- Sidebar ----------
        self.sidebar = Sidebar()

        left_dock = QDockWidget("Navigation")
        left_dock.setWidget(self.sidebar)
        left_dock.setAllowedAreas(Qt.LeftDockWidgetArea)

        self.addDockWidget(Qt.LeftDockWidgetArea, left_dock)

        # ---------- Inspector ----------
        self.inspector = Inspector()

        right_dock = QDockWidget("Inspector")
        right_dock.setWidget(self.inspector)
        right_dock.setAllowedAreas(Qt.RightDockWidgetArea)

        self.addDockWidget(Qt.RightDockWidgetArea, right_dock)

        # ---------- Status ----------
        self.statusBar().showMessage("Ready")

        # ---------- Signals ----------
        self.menu.exit_action.triggered.connect(self.close)

        self.menu.open_workspace_action.triggered.connect(
            self.workspace_controller.open_workspace
        )

        dashboard = self.workspace.dashboard

        dashboard.create.clicked.connect(
            self.workspace_controller.create_workspace
        )

        # ---------- Recent Workspaces ----------
        self.load_recent_menu()

    # =========================================================
    # RECENT WORKSPACE METHODS
    # =========================================================

    def load_recent_menu(self):

        items = RecentService.load()

        self.menu.set_recent_items(
            items,
            self._open_recent_workspace
        )

    def _open_recent_workspace(self, path: str):

        self.workspace_controller.open_workspace_from_path(path)
        self.sidebar.update_workspace()