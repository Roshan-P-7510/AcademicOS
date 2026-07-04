from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QLineEdit,
)

from ui.components.action_card import ActionCard


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    def stat_card(self, number, title):

        card = QFrame()
        card.setObjectName("StatCard")

        layout = QVBoxLayout(card)

        layout.setContentsMargins(20, 20, 20, 20)

        value = QLabel(str(number))
        value.setObjectName("StatNumber")
        value.setAlignment(Qt.AlignCenter)

        label = QLabel(title)
        label.setObjectName("StatLabel")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(value)
        layout.addWidget(label)

        return card

    def build_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(50, 35, 50, 35)

        root.setSpacing(25)

        # =====================================================
        # Header
        # =====================================================

        title = QLabel("AcademicOS")
        title.setObjectName("DashboardTitle")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Your Digital Academic Workspace")
        subtitle.setObjectName("DashboardSubtitle")
        subtitle.setAlignment(Qt.AlignCenter)

        root.addWidget(title)
        root.addWidget(subtitle)

        # =====================================================
        # Search
        # =====================================================

        search = QLineEdit()

        search.setPlaceholderText(
            "Search notes, PDFs, subjects..."
        )

        search.setObjectName("SearchBar")

        root.addWidget(search)

        # =====================================================
        # Action Cards
        # =====================================================

        actions = QHBoxLayout()

        self.create = ActionCard(
            "Create Workspace",
            "Create a brand new workspace."
        )

        self.open_workspace = ActionCard(
            "Open Workspace",
            "Continue where you left off."
        )

        actions.addWidget(self.create)
        actions.addWidget(self.open_workspace)

        root.addLayout(actions)

        # =====================================================
        # Statistics
        # =====================================================

        stats_title = QLabel("Quick Overview")
        stats_title.setObjectName("SectionTitle")

        root.addWidget(stats_title)

        grid = QGridLayout()

        grid.addWidget(self.stat_card(0, "Subjects"), 0, 0)
        grid.addWidget(self.stat_card(0, "Notes"), 0, 1)
        grid.addWidget(self.stat_card(0, "PDFs"), 0, 2)
        grid.addWidget(self.stat_card(0, "Images"), 0, 3)

        root.addLayout(grid)

        # =====================================================
        # Bottom Panels
        # =====================================================

        bottom = QHBoxLayout()

        recent = QFrame()
        recent.setObjectName("Panel")

        recent_layout = QVBoxLayout(recent)

        recent_layout.addWidget(
            QLabel("Recent Workspaces")
        )

        recent_layout.addWidget(
            QLabel("No workspaces created yet.")
        )

        tip = QFrame()
        tip.setObjectName("Panel")

        tip_layout = QVBoxLayout(tip)

        tip_layout.addWidget(
            QLabel("Today's Tip")
        )

        tip_layout.addWidget(
            QLabel(
                "Small progress every day beats perfection."
            )
        )

        bottom.addWidget(recent, 2)
        bottom.addWidget(tip, 1)

        root.addLayout(bottom)

        root.addStretch()