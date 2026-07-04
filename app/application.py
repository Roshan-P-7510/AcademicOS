from PySide6.QtWidgets import QApplication

from app.constants import APP_NAME, ORGANIZATION


class AcademicApplication(QApplication):

    def __init__(self, argv):

        super().__init__(argv)

        self.setApplicationName(APP_NAME)

        self.setOrganizationName(ORGANIZATION)