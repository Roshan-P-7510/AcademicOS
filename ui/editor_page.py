"""
AcademicOS
Sprint A.2.1

Editor page shown after a workspace is opened.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class EditorPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)

        title = QLabel("AcademicOS")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
        """)

        subtitle = QLabel(
            "No file is currently open.\n\n"
            "Open a file from the Explorer\n"
            "or create a new note."
        )
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("""
            font-size: 14px;
            color: gray;
        """)

        self.new_note = QPushButton("New Note")
        self.new_note.setFixedWidth(180)
        self.new_note.setEnabled(False)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.new_note, alignment=Qt.AlignCenter)