import pyautogui
import pyperclip
import time

def sleep():
    time.sleep(0.1)
def clicktypeenter(text):
    pyautogui.click()
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.write(['enter'])

site_addr = 'www.naver.com'
city_names = ["서울날씨", "부산날씨", "대구날씨", "시카코날씨"]

addrbar_xy = (1234, 73)
search_xy = (1435, 303)
capture_xy = (1001, 315, 1837-1001, 824-315)


for city in city_names:
    pyautogui.moveTo(addrbar_xy[0], addrbar_xy[1], 0.1)
    clicktypeenter(site_addr)
    time.sleep(1)

    pyautogui.moveTo(search_xy[0], search_xy[1], 0.1)
    clicktypeenter(city)
    time.sleep(1)

    pyautogui.screenshot(city+'.png', capture_xy)