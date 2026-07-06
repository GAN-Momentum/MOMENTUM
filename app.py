import sys
from PySide6.QtWidgets import QApplication
from app.core.app_controller import AppController

app = QApplication(sys.argv)
controller = AppController()
controller.start()
sys.exit(app.exec())
