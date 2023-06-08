import time
import pyautogui as auto
time.sleep(3)
for i in range(0,100):
    with open('theText.txt', 'r') as theFile:
        auto.FAILSAFE = False
        for line in theFile:
            auto.typewrite(line)
            auto.press('enter')