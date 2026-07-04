from PySide6.QtWidgets import QListWidget


class Sidebar(QListWidget):

    def __init__(self):
        super().__init__()

        self.addItems([
            "🏠 Dashboard",
            "📚 Subjects",
            "📝 Notes",
            "📄 PDF Library",
            "🖼 Images",
            "📅 Timeline",
            "⭐ Favorites",
            "⚙ Settings"
        ])

        self.setMinimumWidth(230)