import time
import os
import sys
from blinkstick import blinkstick

substring_StatusIndicator_Added = "StatusIndicatorStateService: Added"
separatorStatusLeft = ": Added "
separatorStatusRight = " ("

substring_reportIncomingCall = "DeviceCallControlManager Desktop: reportIncomingCall processed"

current_status = 'Unknown'

def follow(thefile):
    #generator function that yields new lines in a file
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)
    
    # start infinite loop
    while True:
        try:
            # read last line of file
            line = thefile.readline()        # sleep if file hasn't been updated
            if not line:
                time.sleep(0.1)
                continue

            yield line
        except KeyboardInterrupt:
            bstick = blinkstick.find_first()
            def allLEDs(colour):
                for i in range(7):
                    bstick.set_color(index=i, name=colour)
                    time.sleep(0.1)
            allLEDs('black')
            print("Excited through keyboard interrupt")
            sys.exit()



if __name__ == '__main__':
    path_to_file = os.path.expanduser('~')+r"\AppData\Roaming\Microsoft\Teams\logs.txt"
    logfile = open(path_to_file, "r")
    print(path_to_file)
    loglines = follow(logfile)    # iterate over the generator

    for line in loglines:
        if substring_StatusIndicator_Added in line:
            split_left = line.split(separatorStatusLeft,1)
            split_endResult = split_left[1].split(separatorStatusRight,1)
            current_status = split_endResult[0]
            print(current_status)
            with open(r"blinkstick\setLEDs.py") as f:
                exec(f.read())
        if substring_reportIncomingCall in line:
            current_status = 'incomingCall'
            print("Incoming Call detected!")
            with open(r"blinkstick\setLEDs.py") as f:
                exec(f.read())
