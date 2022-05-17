import sys
import time
import pyautogui
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow

from output import Ui_mainWindow

stop = 1
scroll_distance = 10
scroll_timing = 1


class AutoScrollThread(QThread):
    signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.signal.connect(self.autoscroll_toggle)

    def run(self):
        global stop
        while True:
            if stop == 0:
                pyautogui.scroll(-scroll_distance)
            time.sleep(scroll_timing)

    def autoscroll_toggle(self):
        global stop
        if stop == 1:
            stop = 0
        elif stop == 0:
            stop = 1


class MainWindow(QMainWindow, Ui_mainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        print("init调用")
        self.scroll_distance.setValue(scroll_distance)
        self.scroll_timing.setValue(scroll_timing)

    @staticmethod
    def start():
        global stop
        stop = 0

    @staticmethod
    def stop():
        global stop
        stop = 1

    def scroll_distance_edited(self, value_):
        global scroll_distance
        scroll_distance = value_

    def scroll_timing_edited(self, value_):
        global scroll_timing
        scroll_timing = value_


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()

    t = AutoScrollThread()
    t.start()

    main_window.show()
    sys.exit(app.exec())
