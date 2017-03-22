import multilineMAX7219 as LEDMatrix
from multilineMAX7219_fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT
from multilineMAX7219 import DIR_L, DIR_R, DIR_U, DIR_D
from multilineMAX7219 import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from multilineMAX7219 import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT
import time

# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()
LEDMatrix.brightness(2)

#gfx_set_col(g_col, state=GFX_INVERT):
vx,vy=1,1
x,y=0,0
LEDMatrix.gfx_set_px(x,y)
try:
  while 1:
    LEDMatrix.gfx_set_px(x,y)
    if x>63 or x < 0: vx=-vx
    x=x+vx
    if y>32 or y < 0: vy=-vy
    y=y+vy
    LEDMatrix.gfx_set_px(x,y)
    LEDMatrix.gfx_render()
    #time.sleep(0.1)
except KeyboardInterrupt:
    # reset array
    LEDMatrix.scroll_message_horiz(["","Goodbye!",""], 1, 8)
    LEDMatrix.clear_all()
