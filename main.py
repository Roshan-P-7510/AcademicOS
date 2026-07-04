import sys
from ui.theme import ThemeManager

from app.application import AcademicApplication
from core.logger import setup_logger
from ui.main_window import MainWindow


def main():

    logger = setup_logger()

    logger.info("Starting AcademicOS")

    app = AcademicApplication(sys.argv)

    

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()