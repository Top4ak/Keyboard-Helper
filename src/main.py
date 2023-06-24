from pynput.keyboard import Controller
from pynput import keyboard
import threading
import time
from gui import menu
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from gui.ui_main import Ui_MainWindow

class AntiPasta(QMainWindow):
    def __init__(self):
        super(AntiPasta, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AntiPasta()
    window.show()

    sys.exit(app.exec())