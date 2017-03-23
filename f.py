import multilineMAX7219 as LEDMatrix
from multilineMAX7219_fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT
from multilineMAX7219 import DIR_L, DIR_R, DIR_U, DIR_D
from multilineMAX7219 import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from multilineMAX7219 import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT
import time
import numpy as np
from myfont import f

# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()
LEDMatrix.brightness(2)

try:
  while 1:
                          #def gfx_sprite_array(sprite, start_x=0, start_y=0, state=GFX_INVERT)
    for i in range (8):
       LEDMatrix.gfx_sprite_array(f[i], 8*i,16,state=GFX_ON)
    for i in range (8,10):
       LEDMatrix.gfx_sprite_array(f[i], 8*(i-8),0,state=GFX_ON)
    #render() 
    LEDMatrix.gfx_render()
    while 1:
      time.sleep(1)
except KeyboardInterrupt:
    # reset array
    LEDMatrix.scroll_message_horiz(["","Goodbye!",""], 1, 8)
    LEDMatrix.clear_all()
