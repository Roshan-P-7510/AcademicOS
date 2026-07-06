"""
AcademicOS
Sprint B.1

Editor page for viewing text files.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import (
    QLabel,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)


class EditorPage(QWidget):
    """
    Central editor page.

    Displays a welcome screen until a file is opened.
    """

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # -------------------------------------------------
        # File Name
        # -------------------------------------------------

        self.title = QLabel("AcademicOS")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        # -------------------------------------------------
        # Text Viewer
        # -------------------------------------------------

        self.editor = QPlainTextEdit()

        self.editor.setReadOnly(True)

        self.editor.setPlainText(
            "No file is currently open.\n\n"
            "Open a file from the Explorer."
        )

        layout.addWidget(self.title)
        layout.addWidget(self.editor)

    # -------------------------------------------------

    def open_text(
        self,
        filename: str,
        content: str
    ):
        """
        Display a text file.
        """

        self.title.setText(filename)

        self.editor.setPlainText(content)

        self.editor.moveCursor(QTextCursor.Start)

    # -------------------------------------------------

    def clear(self):
        """
        Restore the welcome page.
        """

        self.title.setText("AcademicOS")

        self.editor.setPlainText(
            "No file is currently open.\n\n"
            "Open a file from the Explorer."
        )