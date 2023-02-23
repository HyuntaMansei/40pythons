import pyautogui
import pyperclip
import os

os.chdir(os.path.dirname((os.path.abspath(__file__))))

def get_pic_position(pic_file_names):
    for name in pic_file_names:
        position = pyautogui.locateOnScreen(name)
        if position is not None:
            return position

hee_file_names = ['1.png', '2,png', '3.png']
msg = "자기 자면 안 되요! 힘내요!"

hee_position = get_pic_position((hee_file_names))

if hee_position is None:
    print("Error")
    exit()

pyautogui.doubleClick(pyautogui.center(hee_position))
pyautogui.sleep(0.5)

for i in range(10):
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.sleep(0.2)

pyautogui.press('escape')