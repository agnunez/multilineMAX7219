import time
import math
from random import randrange

import multilineMAX7219 as LEDMatrix
from multilineMAX7219_fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT
from multilineMAX7219 import DIR_L, DIR_R, DIR_U, DIR_D
from multilineMAX7219 import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from multilineMAX7219 import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT
import datetime,ephem

def utlst():
  gtc = ephem.Observer()
  gtc.lat, gtc.lon, gtc.elevation = '28.7565187', '-17.8919956', 2175.0
  t = "%s %s" % (gtc.date,gtc.sidereal_time())
  p = t.split(" ")
  lst=p[2].split(".")
  ut=p[1]
  return ut,lst[0]


# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()
LEDMatrix.brightness(2)
sun, moon = ephem.Sun(), ephem.Moon()

gtc = ephem.Observer()
gtc.lat, gtc.lon, gtc.elevation = '28.7565187', '-17.8919956', 2175.0
print gtc.date, gtc.sidereal_time()
print gtc.lon, gtc.lat

try:
  while 1:
        ut,lst=utlst()
        sut="%s" % ut
        slst="%s" % lst 
        if len(slst) < 8: slst = "0"+slst
	now = "UT        %sST        %s" % (sut.replace(":",""), slst.replace(":",""))
        LEDMatrix.static_message(now)
        time.sleep(0.1)

except KeyboardInterrupt:
    # reset array
    LEDMatrix.scroll_message_horiz(["","Goodbye!",""], 1, 8)
    LEDMatrix.clear_all()
