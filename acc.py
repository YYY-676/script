
 #!/usr/bin/env python3
import sys
import pyautogui
import time
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QThread, pyqtSignal

class KeyPressThread(QThread):
    stop_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        self.running = True

        # 使用 Alt+Tab 切回原窗口
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

        pyautogui.keyDown('right')
        while self.running:
            time.sleep(0.1)
        pyautogui.keyUp('right')

    def stop(self):
        self.running = False
        self.stop_signal.emit()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.thread = KeyPressThread()

    def initUI(self):
        self.setWindowTitle("视频加速器")
        self.setGeometry(100, 100, 200, 100)

        self.start_button = QPushButton("开始加速", self)
        self.start_button.clicked.connect(self.start_acceleration)

        self.stop_button = QPushButton("停止加速", self)
        self.stop_button.clicked.connect(self.stop_acceleration)

        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

    def start_acceleration(self):
        if not self.thread.isRunning():
            self.thread = KeyPressThread()
            self.thread.start()

    def stop_acceleration(self):
        self.thread.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
