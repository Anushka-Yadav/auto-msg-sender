import pyautogui as pg
import time

time.sleep(5)

txt=open('new.txt','r')
for i in txt:
    pg.write("<name> is",i)
    pg.press('Enter')
