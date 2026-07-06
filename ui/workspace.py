"""
AcademicOS
Sprint A.2.1

Central workspace widget.
"""

from PySide6.QtWidgets import QStackedWidget

from ui.dashboard import Dashboard
from ui.editor_page import EditorPage


class Workspace(QStackedWidget):

    def __init__(self):
        super().__init__()

        self.dashboard = Dashboard()
        self.editor = EditorPage()

        self.addWidget(self.dashboard)
        self.addWidget(self.editor)

        self.show_dashboard()

    # -------------------------------------------------

    def show_dashboard(self):
        self.setCurrentWidget(self.dashboard)

    def show_editor(self):
        self.setCurrentWidget(self.editor)