from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDockWidget,
    QMainWindow,
)

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

        left_dock.setAllowedAreas(
            Qt.LeftDockWidgetArea
        )

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            left_dock
        )

        # ---------- Inspector ----------

        self.inspector = Inspector()

        right_dock = QDockWidget("Inspector")

        right_dock.setWidget(self.inspector)

        right_dock.setAllowedAreas(
            Qt.RightDockWidgetArea
        )

        self.addDockWidget(
            Qt.RightDockWidgetArea,
            right_dock
        )

        # ---------- Status ----------

        self.statusBar().showMessage("Ready")

        # ---------- Signals ----------

        self.menu.exit_action.triggered.connect(
            self.close
        )