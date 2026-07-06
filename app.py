import sys
from PySide6.QtWidgets import QApplication
from app.core.app_controller import AppController

def main():
    app = QApplication(sys.argv)
    controller = AppController()
    controller.start()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
