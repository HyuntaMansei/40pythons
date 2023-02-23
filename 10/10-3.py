import pyautogui
import pyperclip
import time

def timesleep():
    time.sleep(0.1)

site = 'www.naver.com'

pyautogui.moveTo(1534,303, 0.1)
timesleep()
pyautogui.click()

timesleep()
pyperclip.copy("서울날씨")
pyautogui.hotkey('ctrl', 'v')
pyautogui.write(['enter'])
timesleep()

capturexy = (1001, 315, 1837-1001, 824-315)
pyautogui.screenshot('seoul.png', region=capturexy)

