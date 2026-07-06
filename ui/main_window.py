from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDockWidget,
    QMainWindow,
)

from core.session import Session
from controllers.file_controller import FileController
from controllers.workspace_controller import WorkspaceController
from services.recent_service import RecentService
from ui.inspector import Inspector
from ui.menu_bar import MainMenuBar
from ui.sidebar import Sidebar
from ui.tool_bar import MainToolBar
from ui.workspace import Workspace


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AcademicOS")
        self.resize(1600, 900)

        self.workspace_controller = WorkspaceController(self)
        self.file_controller = FileController(self)

        self.build_ui()

    def build_ui(self):

        # ---------------- Menu ----------------

        self.menu = MainMenuBar(self)
        self.setMenuBar(self.menu)

        # ---------------- Toolbar ----------------

        self.toolbar = MainToolBar(self)
        self.addToolBar(self.toolbar)

        # ---------------- Workspace ----------------

        self.workspace = Workspace()
        self.setCentralWidget(self.workspace)

        # ---------------- Sidebar ----------------

        self.sidebar = Sidebar()

        left_dock = QDockWidget("Explorer")
        left_dock.setWidget(self.sidebar)
        left_dock.setAllowedAreas(Qt.LeftDockWidgetArea)

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            left_dock
        )

        # ---------------- Inspector ----------------

        self.inspector = Inspector()

        right_dock = QDockWidget("Inspector")
        right_dock.setWidget(self.inspector)
        right_dock.setAllowedAreas(Qt.RightDockWidgetArea)

        self.addDockWidget(
            Qt.RightDockWidgetArea,
            right_dock
        )

        # ---------------- Status ----------------

        self.statusBar().showMessage("Ready")

        # ---------------- Menu Signals ----------------

        self.menu.exit_action.triggered.connect(
            self.close
        )

        self.menu.open_workspace_action.triggered.connect(
            self.workspace_controller.open_workspace
        )

        # ---------------- Dashboard ----------------

        self.workspace.dashboard.create.clicked.connect(
            self.workspace_controller.create_workspace
        )

        # ---------------- Explorer ----------------

        self.sidebar.file_open_requested.connect(
            self.file_controller.open_file
        )

        # ---------------- Recent ----------------

        self.load_recent_menu()

    # ==================================================
    # RECENT WORKSPACES
    # ==================================================

    def load_recent_menu(self):

        items = RecentService.load()

        self.menu.set_recent_items(
            items,
            self._open_recent_workspace
        )

    def _open_recent_workspace(self, path: str):

        self.workspace_controller.open_workspace_from_path(path)

    # ==================================================
    # UI REFRESH
    # ==================================================

    def refresh_workspace(self):

        if not Session.is_workspace_open():
            return

        self.setWindowTitle(
            f"AcademicOS — {Session.workspace_name}"
        )

        self.sidebar.update_workspace()

        self.workspace.show_editor()

        self.statusBar().showMessage(
            f"Workspace: {Session.workspace_name}"
        )

        self.load_recent_menu()