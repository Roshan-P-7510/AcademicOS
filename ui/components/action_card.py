from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QFrame,
)


class ActionCard(QFrame):

    clicked = Signal()

    def __init__(
        self,
        title: str,
        description: str,
        icon: str = "",
        parent=None,
    ):
        super().__init__(parent)

        self.setObjectName("ActionCard")
        self.setCursor(Qt.PointingHandCursor)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        self.icon = QLabel(icon)
        self.icon.setObjectName("ActionCardIcon")
        self.icon.setAlignment(Qt.AlignCenter)

        self.title = QLabel(title)
        self.title.setObjectName("ActionCardTitle")
        self.title.setAlignment(Qt.AlignCenter)

        self.description = QLabel(description)
        self.description.setWordWrap(True)
        self.description.setAlignment(Qt.AlignCenter)
        self.description.setObjectName("ActionCardDescription")

        layout.addStretch()

        layout.addWidget(self.icon)
        layout.addWidget(self.title)
        layout.addWidget(self.description)

        layout.addStretch()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)