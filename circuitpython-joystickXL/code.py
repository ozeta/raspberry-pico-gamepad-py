"""
JoystickXL Test-01

This script must be run with circuitpython 9.0 or later
This script uses the joystick_xl library to read the inputs.
Windows will recognize this board as a HID device.
Device name can be configured into boot.py

to test the device:
- https://hardwaretester.com/gamepad
- win + R; run `joy.cpl`

TODO bugs to resolve:
with the current configuratio hardwaretester and Falcon will not detect LFUP button press, 
but 2 axis (so like a joystick), even if on joy.cpl the Hat seems to be recognized correctly.
some study is required to understand if it is possible to further configure the joystick_xl.inputs.Hat object
rather than use the 4 buttons as joystick_xl.inputs.Button, losing the hat structure

* Hat button press on pin GP14
* Hat switch:
    - Right = GP15
    - Left  = GP26
    - Down  = GP27
    - Up    = GP28
"""

import board  # type: ignore (this is a CircuitPython built-in)
from joystick_xl.inputs import Button, Hat
from joystick_xl.joystick import Joystick

joystick = Joystick()

# Add digital inputs
joystick.add_input(
    Button(board.GP14),
    Hat(
        up=board.GP28,
        down=board.GP27,
        left=board.GP26,
        right=board.GP15
    ),
)
while True:
    joystick.update()
