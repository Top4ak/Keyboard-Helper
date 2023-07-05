from pynput.keyboard import Controller
import pynput 
import threading
import time
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from gui.ui_main import Ui_MainWindow
import webbrowser
from settings.binds import Settings
import keyboard

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
        self.ui.btn_start.clicked.connect(self.start_simulation)
        self.ui.btn_stop.clicked.connect(self.stop_simulation)

        self.ui.btn_save.clicked.connect(self.btn_save_clicked)

        self.ui.btn_github.clicked.connect(self.btn_github_clicked)
        self.ui.btn_telegram.clicked.connect(self.btn_telegram_clicked)

        #Type bindings
        self.is_typing = False

        self.start_hk_is_binded = False
        self.stop_hk_is_binded = False

        if self.user_settings.get_start_hk() != '':
            self.start_hk = keyboard.add_hotkey(self.user_settings.get_start_hk(), self.start_simulation)
            self.start_hk_is_binded = True

        if self.user_settings.get_stop_hk() != '':
            self.stop_hk = keyboard.add_hotkey(self.user_settings.get_stop_hk(), self.stop_simulation)
            self.stop_hk_is_binded = True
    
    def start_simulation(self):
        self.is_typing = True
        time.sleep(self.user_settings.get_starting_delay())

        keyboard_controller = pynput.keyboard.Controller()
        text = self.ui.textedit_userText.toPlainText()
        
        interval = self.user_settings.get_inteval()
        random_factor = self.user_settings.get_random_factor()

        if random_factor == 0:
            for a in text:
                if not self.is_typing:
                    break
                time.sleep(interval)
                keyboard_controller.type(a)

    def stop_simulation(self):
        self.is_typing = False

    def btn_save_clicked(self):
        if self.start_hk_is_binded:
            keyboard.remove_hotkey(self.start_hk)
            self.start_hk_is_binded = False

        if self.stop_hk_is_binded:
            keyboard.remove_hotkey(self.stop_hk)
            self.stop_hk_is_binded = False

        if self.ui.start_value.keySequence().toString() == self.ui.stop_value.keySequence().toString():
            self.ui.stop_value.setKeySequence("")

        data = {
            "start_hot_key": self.ui.start_value.keySequence().toString(),
            "stop_hot_key": self.ui.stop_value.keySequence().toString(),
            "starting_delay": self.ui.delay_value.value(),
            "interval": self.ui.interval_value.value(),
            "random_factor": self.ui.randomFactor_value.value()
        }

        if self.user_settings.get_start_hk() != '':
            self.start_hk = keyboard.add_hotkey(self.user_settings.get_start_hk(), self.start_simulation)
            self.start_hk_is_binded = True

        if self.user_settings.get_stop_hk() != '':
            self.stop_hk = keyboard.add_hotkey(self.user_settings.get_stop_hk(), self.stop_simulation)
            self.stop_hk_is_binded = True

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