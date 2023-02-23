import pyautogui
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pic_position = pyautogui.locateOnScreen('1.png')
print(pic_position)

if pic_position is None:
    pic_position = pyautogui.locateOnScreen('2.png')
    print(pic_position)

if pic_position is None:
    pic_position = pyautogui.locateOnScreen('3.png')
    print(pic_position)

pic_position
pyautogui.moveTo(pic_position)


