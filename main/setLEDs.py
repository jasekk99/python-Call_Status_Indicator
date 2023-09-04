from __main__ import *
import time
from blinkstick import blinkstick

#Find the first BlinkStick
bstick = blinkstick.find_first()


#Use R, G and B channels to control single RGB LED
match current_status:
    case 'OnThePhone': 
        bstick.set_mode(red=255, green=0, blue=0)       #Set LEDs Red
    case 'Busy':
        bstick.set_mode(red=235, green=168, blue=52)    #Set LEDs Orange
    case 'Available':
        bstick.set_mode(red=0, green=255, blue=0)       #Set LEDs Green
    case _:
        bstick.turn_off()