from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class Inspector(QLabel):

    def __init__(self):
        super().__init__()

        self.setText("Nothing Selected")

        self.setAlignment(Qt.AlignTop)

        self.setMargin(15)