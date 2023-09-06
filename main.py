import webbrowser
import pyautogui
import time

webbrowser.open('https://elgoog.im/t-rex/')

time.sleep(2)

pyautogui.press('space')

im = pyautogui.screenshot()
