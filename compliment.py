import pyautogui as pg
import time
time.sleep(5)

txt=open('new.txt','r')  # open tareefe.txt file from you computer
for a in range(50):
    for i in txt:       
        pg.write("dee "+i) # it will print what you want to print
        pg.press('Enter')
