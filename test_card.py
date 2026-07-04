import sys

from PySide6.QtWidgets import QApplication

from ui.components.action_card import ActionCard

app = QApplication(sys.argv)

card = ActionCard(
    "Create Workspace",
    "Create a brand new AcademicOS workspace."
)

card.resize(320, 180)

card.show()

app.exec()