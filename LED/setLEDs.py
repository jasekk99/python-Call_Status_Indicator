from __main__ import *
import time
from blinkstick import blinkstick


error = False

#Loops while error=True (until Blinkstick is recognized) then continues and sets error=False
def wait_for_Blinkstick(error):
    while error == True:
        try:
            blinkstick.find_first()
        except:
            error = True
            time.sleep(1)
    error = False

#Find the first BlinkStick
try:
    bstick = blinkstick.find_first()
    print('blinkstick.find_first(): '+bstick)
except:
    #BlinkStick not found or cannot be reached; error=True
    error = True
    print('No BlinkStick found (Check if the device is Plugged in via USB)')
    #invoke loop (Wait for recognition)
    wait_for_Blinkstick(error)
    


print('Error: '+str(error))

if error == False:
    #Use R, G and B channels to control single RGB LED
    match current_status:
        case 'OnThePhone': 
            bstick.set_color(red=255, green=0, blue=0, name=None, hex=None)       #Set LEDs Red
        case 'Busy':
            bstick.set_color(red=235, green=168, blue=52, name=None, hex=None)    #Set LEDs Orange
        case 'Available':
            bstick.set_color (red=0, green=255, blue=0, name=None, hex=None)       #Set LEDs Green
        case _:
            bstick.turn_off()