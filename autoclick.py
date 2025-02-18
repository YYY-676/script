import tkinter as tk
import pyautogui
import threading
import time
import keyboard  # 用于监听热键 / keyboard listening

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("鼠标连点器")  # Set window title
        self.root.geometry("300x150")  # Set window size

        self.running = False  # 控制连点 / Control clicking
        self.listening = False  # 控制键盘监听 / Control keyboard listening

        # 创建 UI 组件 / Create UI components
        self.btn_start_listen = tk.Button(root, text="start", command=self.start_listening)
        self.btn_start_listen.pack(pady=20)

        self.btn_stop_listen = tk.Button(root, text="pause", command=self.stop_listening, state="disabled")
        self.btn_stop_listen.pack(pady=5)

        self.check_input_thread = threading.Thread(target=self.check_input)
        self.check_input_thread.daemon = True
        self.check_input_thread.start()

    def auto_click(self):
        """ 连点线程 / Clicking thread """
        while self.running:
            pyautogui.click()
            time.sleep(0.05)

    def check_input(self):
        """ 监听热键控制连点 / Listen for hotkeys to control clicking """
        while True:
            if self.listening:
                if keyboard.is_pressed('f6') and not self.running:  # F6 开启连点 / F6 to start clicking
                    self.running = True
                    threading.Thread(target=self.auto_click, daemon=True).start()
                    print("连点已开启 / Clicking started")
                elif keyboard.is_pressed('f7') and self.running:  # F7 停止连点 / F7 to stop clicking
                    self.running = False
                    print("连点已停止 / Clicking stopped")
            time.sleep(0.1)

    def start_listening(self):
        """ 开启监听，监听热键 F6 和 F7 / Start listening for hotkeys F6 and F7 """
        self.listening = True
        self.btn_start_listen.config(state="disabled")
        self.btn_stop_listen.config(state="normal")
        print("开始监听热键，按 F6 开始连点，按 F7 停止连点 / Start listening for hotkeys, press F6 to start clicking, press F7 to stop clicking")

    def stop_listening(self):
        """ 关闭监听，防止误触 / Stop listening to prevent accidental triggers """
        self.listening = False
        self.btn_start_listen.config(state="normal")
        self.btn_stop_listen.config(state="disabled")
        self.running = False
        print("已关闭监听热键 / Listening for hotkeys stopped")

# 启动 GUI / Start GUI
root = tk.Tk()
app = AutoClickerApp(root)
root.mainloop()