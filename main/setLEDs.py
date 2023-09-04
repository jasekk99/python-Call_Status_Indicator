from __main__ import *
import time
from blinkstick import blinkstick

#Find the first BlinkStick
bstick = blinkstick.find_first()

if current_status == 'OnThePhone':
    #Use R, G and B channels to control single RGB LED
    bstick.set_mode(red=255, green=0, blue=0)