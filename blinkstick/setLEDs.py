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
bstick = blinkstick.find_first()
"""
try:
    bstick = blinkstick.find_first()
    print('blinkstick.find_first(): '+bstick)
    print('bstick found: '+print(bstick))
except:
    #BlinkStick not found or cannot be reached; error=True
    error = True
    print('No BlinkStick found (Check if the device is Plugged in via USB)')
    #invoke loop (Wait for recognition)
    wait_for_Blinkstick(error)
"""


print('Error: '+str(error))



def allLEDs(color):
    for i in range(7):
        bstick.set_color(index=i, name=color)
        #time.sleep(0.1)

def allLEDsMorph(color):
    for i in range(7):
        bstick.morph(index=i, name=color)
        time.sleep(0.1)

def multiColor(color1, color2):
    for a in range(5):
        for i in range(7):
            bstick.set_color(index=i, name=color1)
            time.sleep(0.05)
        time.sleep(0.5)
        for i in range(7):
            bstick.set_color(index=i, name=color2)
            time.sleep(0.05)
        time.sleep(0.25)


if error == False:
    #Use R, G and B channels to control single RGB LED
    match current_status:
        case 'incomingCall':
            multiColor('red','black')
        case 'OnThePhone': 
            allLEDs('red')
            #bstick.set_color(red=255, green=0, blue=0, name=None, hex=None)       #Set LEDs Red
        case 'DoNotDisturb':
            allLEDs('red')
            #bstick.set_color(red=255, green=0, blue=0, name=None, hex=None)
        case 'Busy':
            allLEDs('black')
            #bstick.set_color(red=255, green=255, blue=0, name=None, hex=None)    #Turn LEDs off/No Action
        case 'Available':
            allLEDs('black')
            #bstick.turn_off()      #Turn LEDs off/No Action
        case _:
            allLEDs('black')
            #bstick.turn_off()