# python-Call_Status_Indicator ![Static Badge](https://img.shields.io/badge/version-pre%20release-orange)
Changes colour of a BlinkStick LED stick to match your current Microsoft Teams status


![BlinkStick Logo](https://www.blinkstick.com/images/home/logo-home.png)

## Pre-requisites
- Python 3.11 and up [Download the latest version [here](https://www.python.org/downloads/)]
- Any BlinkStick product that is supported by Python and allows the set_mode function [[BlinkStick API implementations overview](https://www.blinkstick.com/help/api-implementations)]
- Microsoft Teams

## Usage
From a Terminal, navigate to the project folder and execute command `./run.cmd`

## How it works
Python constantly reads from the `logs.txt` file under the default path: `<UserPATH>\AppData\Roaming\Microsoft\Teams\logs.txt`.
If a log entry containing "StatusIndicatorStateService: Added" is found the **setLEDs.py** script is called and decides which color the LEDs will be set, according to the current Status.

### Teams status':
- Available
- Away
- BeRightBack
- Offline
- Busy
- DoNotDisturb
- OnThePhone
- InAMeeting (unsure, will have to test)

## Future features
Features i would like to implement into the App in the near future

### Animated transition on status change ![](https://geps.dev/progress/50)
> [!NOTE]
> Not happy with the current "Animation" i've implemented, which is only a delay in cycling through the LED index. Hopefully Blinkstick fixes the Bugs in the ´´´Pulse()´´´ function soon

Implement some sort of non-obtrusive Animation when the Status changes

### LEDs alert of incoming call ![](https://geps.dev/progress/90)
LEDs flash or pulse on incoming call

### Display color when workstation Locked ![](https://geps.dev/progress/70)
Implemented, but LEDs don't turn on Smoothly.