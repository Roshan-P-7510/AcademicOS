from PySide6.QtWidgets import QStackedWidget

from ui.dashboard import Dashboard


class Workspace(QStackedWidget):

    def __init__(self):
        super().__init__()

        self.dashboard = Dashboard()

        self.addWidget(self.dashboard)

        self.setCurrentWidget(self.dashboard)