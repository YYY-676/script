# script  --   python 脚本工具
Useful Python scripts for enhancing software &amp;website usability. 

---

# 鼠标连点器 AutoClicker

## 简介
鼠标连点器是一个简单的GUI应用程序，允许用户通过热键（F6 开始连点，F7 停止连点）来控制鼠标自动点击。用户可以通过点击按钮来开启或关闭热键监听。

## 安装依赖
确保你已经安装了以下Python库：
- `tkinter` (通常默认安装)
- `pyautogui`
- `keyboard`

## 使用方法
1. **启动脚本**：
   - 双击 `run_autoclick.bat` 文件来启动应用程序(autoclick.py)。

2. **开启键盘热键监听**：
   - 点击“start”按钮，应用程序将开始监听热键 F6 和 F7。

3. **控制连点**：
   - 按下 F6 键开始连点。
   - 按下 F7 键停止连点。

4. **关闭监听**：
   - 点击“pause”按钮，应用程序将停止监听热键。


# AutoClicker

## Introduction
AutoClicker is a simple GUI application that allows users to control mouse auto-clicking using hotkeys (F6 to start clicking, F7 to stop clicking). Users can start or stop listening to hotkeys by clicking buttons.

## Installation Dependencies
Ensure you have the following Python libraries installed:
- `tkinter` (usually installed by default)
- `pyautogui`
- `keyboard`
## Usage
1. **Start the Script**:
   - Double-click the `run_autoclick.bat` file to start the application(autoclick.py).

2. **Start Listening**:
   - Click the "start" button, the application will start listening to hotkeys F6 and F7.

3. **Control Clicking**:
   - Press F6 key to start clicking.
   - Press F7 key to stop clicking.

4. **Stop Listening**:
   - Click the "pause" button, the application will stop listening to hotkeys.

## Notes
- Use this script responsibly and ensure you understand its functionality.
- Do not use this script for any illegal activities.


---

## bilibili3倍加速
加速
此脚本旨在为 bilibili.com 提供自动右键3倍速加速播放功能。通过 PyQt6 和 pyautogui 库，用户可以通过图形界面轻松控制视频的加速和停止。脚本使用 `Alt+Tab` 组合键切换回原窗口，确保在正确窗口中进行按键模拟。

### 文件结构
- `run_acc.bat`: 批处理文件，用于启动 Python 脚本。
- `acc.py`: 主 Python 脚本，实现视频加速功能。

### 使用方法

#### Windows 环境
1. **安装依赖库**
   - 确保已安装 Anaconda 或 Python 环境。
   - 使用以下命令安装所需的 Python 库：
     ```bash
     pip install pyautogui PyQt6
     ```


2. **运行脚本**
   - 双击 `run_acc.bat` 文件启动脚本。


#### GUI 操作
- **开始加速**：点击“开始加速”按钮，程序将使用 `Alt+Tab` 切换回 bilibili 页面，并模拟按下右箭头键以加速视频播放。
- **停止加速**：点击“停止加速”按钮，程序将停止发送按键指令。

---

## README (English)

### Introduction
This script is designed to provide an automatic right-key 3x speed playback feature for bilibili.com. Using the PyQt6 and pyautogui libraries, users can easily control video acceleration and stopping through a graphical interface. The script uses the `Alt+Tab` key combination to switch back to the original window, ensuring that key presses are simulated in the correct window.

### File Structure
- `run_acc.bat`: Batch file used to start the Python script.
- `acc.py`: Main Python script that implements the video acceleration functionality.

### Usage

#### Windows Environment
1. **Install Dependencies**
   - Ensure you have Anaconda or Python environment installed.
   - Install the required Python libraries using the following command:
     ```bash
     pip install pyautogui PyQt6
     ```


2. **Run the Script**
   - Double-click the `run_acc.bat` file to start the script.


#### GUI Operations
- **Start Acceleration**: Click the "Start Acceleration" button, and the program will use `Alt+Tab` to switch back to the bilibili page and simulate pressing the right arrow key to accelerate video playback.
- **Stop Acceleration**: Click the "Stop Acceleration" button to stop sending key press commands.

---

### 注意事项
- 请确保在使用该脚本时，bilibili 页面处于前台并已加载完毕。
- 由于该脚本使用了 `pyautogui` 库进行按键模拟，请勿在其他需要输入的窗口操作时使用该脚本，以免造成误操作。

### Notes
- Make sure the bilibili page is in the foreground and fully loaded when using this script.
- Since this script uses the `pyautogui` library for key simulation, avoid using it while performing input operations in other windows to prevent accidental actions.

---
