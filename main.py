#<done>this program is going to run a sleet timer of 1 minute so use the time module
#<done>to find all the processe runncing
#<done>to exit the progrram after the process has even closed<

import psutil
import time
import sys
import pyautogui

check = True
time.sleep(60)
while (check == True):
    pro = [p.name() for p in psutil.process_iter()]
    if 'maya.exe' in pro:
        print("hello")
        pyautogui.keyDown('ctrl')
        pyautogui.typewrite("s")
        pyautogui.keyUp('ctrl')
    else:
        print("bye")
        sys.exit()
    time.sleep(120)
