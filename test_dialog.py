import sys

from PySide6.QtWidgets import QApplication

from dialogs.create_workspace_dialog import CreateWorkspaceDialog

app = QApplication(sys.argv)

dialog = CreateWorkspaceDialog()

dialog.exec()

print(dialog.workspace_name())
print(dialog.workspace_location())