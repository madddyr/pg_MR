import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.3)

pg.hotkey('winleft','up')
pg.typewrite('espn.com\n',.3)
time.sleep(2)

pg.moveTo(424, 171, 1)
pg.moveTo(807, 402, 1)
pg.click()
time.sleep(60)

pg.hotkey('ctrl','t')
pg.typewrite('')
