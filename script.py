import pydirectinput
import time

def wheelie():
    time.sleep(3)
    pydirectinput.keyDown('shift')
    pydirectinput.keyDown('ctrl')
    pydirectinput.keyDown('w')
    pydirectinput.keyDown('a')

wheelie()
