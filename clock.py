import time
import math
from random import randrange

import multilineMAX7219 as LEDMatrix
from multilineMAX7219_fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT
from multilineMAX7219 import DIR_L, DIR_R, DIR_U, DIR_D
from multilineMAX7219 import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from multilineMAX7219 import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT
import datetime,ephem
from myfont import f

def utlst():
  gtc = ephem.Observer()
  gtc.lat, gtc.lon, gtc.elevation = '28.7565187', '-17.8919956', 2175.0
  t = "%s %s" % (gtc.date,gtc.sidereal_time())
  p = t.split(" ")
  lst=p[2].split(".")
  ut=p[1]
  return ut,lst[0]

def at(x,y,string,state=GFX_ON):
  for c in string:
    LEDMatrix.gfx_sprite_array(f[ord(c)-48],x,y,state)
    x+=len(f[ord(c)-48][0])
    if c == ":" : x-=7
    if c >= "A" : x-=1



# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()
LEDMatrix.brightness(5)
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
        at(0,16,"UT%s" % sut)
        at(0, 0,"ST%s" % slst)
        LEDMatrix.gfx_render()
        time.sleep(0.1)

except KeyboardInterrupt:
    # reset array
    LEDMatrix.clear_all()
