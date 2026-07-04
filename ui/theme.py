from pathlib import Path


class ThemeManager:

    @staticmethod
    def load_dark_theme(app):

        qss = Path("themes/dark.qss")

        if qss.exists():
            app.setStyleSheet(qss.read_text(encoding="utf-8"))