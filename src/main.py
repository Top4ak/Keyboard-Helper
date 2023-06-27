from pynput.keyboard import Controller
from pynput import keyboard
import threading
import time
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from gui.ui_main import Ui_MainWindow
import webbrowser
from settings.binds import Settings

class AntiPasta(QMainWindow):
    def __init__(self):
        super(AntiPasta, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Manual Setup
        self.ui.frame_settings.setVisible(False)

        #Restore user settings
        self.user_settings = Settings()

        self.ui.start_value.setKeySequence(self.user_settings.get_start_hk())
        self.ui.stop_value.setKeySequence(self.user_settings.get_stop_hk())
        self.ui.delay_value.setValue(self.user_settings.get_starting_delay())
        self.ui.interval_value.setValue(self.user_settings.get_inteval())
        self.ui.randomFactor_value.setValue(self.user_settings.get_random_factor())


        #Button connection
        self.ui.btn_info.clicked.connect(self.btn_info_clicked)
        self.ui.btn_settings.clicked.connect(self.btn_settings_clicked)

        self.ui.btn_save.clicked.connect(self.btn_save_clicked)

        self.ui.btn_github.clicked.connect(self.btn_github_clicked)
        self.ui.btn_telegram.clicked.connect(self.btn_telegram_clicked)

    def btn_save_clicked(self):
        data = {
            "start_hot_key": self.ui.start_value.keySequence().toString(),
            "stop_hot_key": self.ui.stop_value.keySequence().toString(),
            "starting_delay": self.ui.delay_value.value(),
            "interval": self.ui.interval_value.value(),
            "random_factor": self.ui.randomFactor_value.value()
        }

        self.user_settings.update(data)

    def btn_settings_clicked(self):
        self.ui.frame_settings.setVisible(True)
        self.ui.frame_info.setVisible(False)

    def btn_info_clicked(self):
        self.ui.frame_info.setVisible(True)
        self.ui.frame_settings.setVisible(False)

    def btn_github_clicked(self):
        webbrowser.open("https://github.com/Top4ak")

    def btn_telegram_clicked(self):
        webbrowser.open("https://t.me/miketapok")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AntiPasta()
    window.show()

    sys.exit(app.exec())