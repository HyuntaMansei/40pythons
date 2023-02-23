import threading

import pyautogui
import os
import pyperclip

hee_file_names = ["1.png", "2.png", "3.png"]
msg = "우와 우리 자기 안 자네! 짱이다! 사랑해욧!"

os.chdir(os.path.dirname((os.path.abspath(__file__))))

def get_pic_position(pic_file_names):
    for name in pic_file_names:
        position = pyautogui.locateOnScreen(name)
        if position is not None:
            return position

def send_msg(pic_file_names, msg):
    position = get_pic_position(pic_file_names)
    pyautogui.doubleClick(position)
    pyperclip.copy(msg)
    pyautogui.sleep((0.5))
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press(['enter', 'escape'])

def thread_send_msg():
    threading.Timer(5, thread_send_msg).start()

    send_msg(hee_file_names, msg)

thread_send_msg()
