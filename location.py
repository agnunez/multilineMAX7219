#!/usr/bin/env python
# ---------------------------------------------------------
# Filename: multilineMAX7219_demo.py
# ---------------------------------------------------------
# Demonstration of the features in the multilineMAX7219 library
#
# v1.0
# F.Stern 2014
# ---------------------------------------------------------
# improved and extended version of JonA1961's MAX7219array
# ( https://github.com/JonA1961/MAX7219array )
# ---------------------------------------------------------
# See multilineMAX7219.py library file for more details
# ---------------------------------------------------------
# This demo script is intended to run on an array of 9 (3x3)
#   MAX7219 boards, connected as described in the library
#   script. 
# The variables MATRIX_WIDTH and MATRIX_HEIGHT, defined in the 
#	multilineMAX7219.py library script, should always be set to be 
#	consistent with the actual hardware setup in use.  If it is 
#	not set correctly, then the functions will not work as
#   intended
# ---------------------------------------------------------

import time
import math
from random import randrange

# Import library
import multilineMAX7219 as LEDMatrix
from multilineMAX7219 import *
# Import fonts
from multilineMAX7219_fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT

# The following imported variables make it easier to feed parameters to the library functions
from multilineMAX7219 import DIR_L, DIR_R, DIR_U, DIR_D
from multilineMAX7219 import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from multilineMAX7219 import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT

# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()

print "Do not forget to update MATRIX_WIDTH and MATRIX_HEIGHT in multilineMAX7219.py prior this test"

try:
	LEDMatrix.clear_all()

	LEDMatrix.brightness(0)
	# Display all characters from the font individually
	for char in range(NUM_MATRICES):
		LEDMatrix.send_matrix_letter(char, ord("%0.1X" % (char%16)))
		time.sleep(0.22)
	time.sleep(0.5)
except:
	print "display error. Check M x N configuration library"
