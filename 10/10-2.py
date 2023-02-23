import pyautogui
import time
import pyperclip

pyautogui.moveTo(1435, 303, 0.5)
pyautogui.click()
pyperclip.copy("서울날씨")
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.1)
pyautogui.write(["enter"])
