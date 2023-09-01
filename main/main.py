import time
import os

substring_StatusIndicator_Added = "StatusIndicatorStateService: Added"
separatorLeft = ": Added "
separatorRight = " ("

def follow(thefile):
    '''generator function that yields new lines in a file
    '''
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)
    
    # start infinite loop
    while True:
        # read last line of file
        line = thefile.readline()        # sleep if file hasn't been updated
        if not line:
            time.sleep(0.1)
            continue

        yield line
if __name__ == '__main__':
    logfile = open(r"C:\Users\jgreen\AppData\Roaming\Microsoft\Teams\logs.txt", "r")
    loglines = follow(logfile)    # iterate over the generator
    for line in loglines:
        if substring_StatusIndicator_Added in line:
            stripped = line.split(separatorLeft,1)
            final_stripped = stripped[1].split(separatorRight,1)
            line = final_stripped[0]
            print(line)
