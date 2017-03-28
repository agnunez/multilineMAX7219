multilineMAX7219
================

Drive n x m MAX7219 LED Matrices via SPI in Python from the Raspberry Pi

You can find an introduction of this library here: http://www.tutorials-raspberrypi.de/allgemein/library-installation-for-multiline-m-x-n-max7219-led-matrices/

NOTE: https://github.com/agnunez/multilineMAX7219
Upgraded to allow any type of matrix disposition. 
 - First run python location.py to realize your specific dispostion order
 - Second, edit multilineMAX7219.py :
     update MATRIX_HEIGHT and MATRIX_WIDTH with your configuration
     update pos array with resulting matrix ids in decimal (not hex)
      following your order 1st row left-rigth, 2nd row left-right... etc.
     test again location.py, to see that your matrix order is now correct
      in left-right, top-botton 
 - enjoy. (Warging. Fix message works, but scrolling message not. in todo's)

Aslo added an astronomical Universal Time, Sidereal Time clock example, using
pyephem library. Update longitud, latitud of your site to get correct readings.
This example, use sprites to adjust better a customized font that you can edit
in myfont.py. Only numbers and specific letters are implemented. You can add more and use at(x,y,text) function to display any text at any x,y location

Have fun!
Agustin
agnunez @ github

