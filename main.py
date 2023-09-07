import pyautogui
import keyboard
import webbrowser
import time

webbrowser.open("https://elgoog.im/dinosaur-game/")
time.sleep(1)
keyboard.press('space')
time.sleep(3)

while not keyboard.is_pressed('q'):
    low_obstacle_area = pyautogui.screenshot(region=(250, 460, 100, 100))
    bg_color = low_obstacle_area.getpixel((50, 50))
    if bg_color != (255, 255, 255):
        keyboard.press('space')

    high_obstacle_area = pyautogui.screenshot(region=(300, 400, 100, 100))
    bg_color2 = high_obstacle_area.getpixel((50, 50))
    if bg_color2 != (255, 255, 255):
        keyboard.press('down')

