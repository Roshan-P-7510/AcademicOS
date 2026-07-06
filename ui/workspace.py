"""
AcademicOS

Central Workspace
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

    # -------------------------------------------------
    # FILE API
    # -------------------------------------------------

    def open_text(self, filename: str, content: str):
        """
        Display a text file inside the editor.
        """

        self.show_editor()
        self.editor.open_text(filename, content)

    def clear(self):
        """
        Restore the welcome editor.
        """

        self.editor.clear()