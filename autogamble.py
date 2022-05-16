import pyautogui as pag
import time as t
import random as r
import keyboard as kb

t.sleep(5)
for i in range(500):
    if(kb.is_pressed("k")):
        break
    rng = r.randint(50,100000)
    pag.write("bg "+ str(rng))
    pag.hotkey("enter",interval = 0.5)
    
    
