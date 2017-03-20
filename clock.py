import time
import math
from random import randrange

# Import library
import multilineMAX7219 as LEDMatrix
# Import fonts
from multilineMAX7219_fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT

# The following imported variables make it easier to feed parameters to the library functions
from multilineMAX7219 import DIR_L, DIR_R, DIR_U, DIR_D
from multilineMAX7219 import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from multilineMAX7219 import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT
import datetime 

# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()
LEDMatrix.brightness(5)

try:
  while 1:
	now = datetime.datetime.utcnow().strftime("UT %m/%d%H:%M:%SST      17:55:32")
	print now
        LEDMatrix.static_message(now)
        time.sleep(1)

except KeyboardInterrupt:
    # reset array
    LEDMatrix.scroll_message_horiz(["","Goodbye!",""], 1, 8)
    LEDMatrix.clear_all()
