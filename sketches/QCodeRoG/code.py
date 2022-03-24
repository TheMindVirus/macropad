# ASUS RoG Q-Code Replicator - Alastair Cota
# Most ASUS and Republic of Gamers Motherboards have a small dual 7-segment display or 2 to display BIOS Boot Codes.
# These are used to diagnose any problems a self-built PC may have if it fails to start up correctly.

# [WARNING]: USING A MACROPAD WITH Q-CODE LOGGER IN ITS CURRENT STATE MAY CAUSE DATA LOSS TO YOUR MACROPAD'S CIRCUITPY DRIVE!

# Alternatives include a special USB Port (such as Q-Code Logger) for presenting this information to an unbricked device
# or a Pi Zero Gadget with HyperPixel4 Display over USB showing this information across its single USB cable with multiple protocols
# or even a traditional ISA/PCIe/LPC POST Card connected to a Pi to broadcast live remote Q-Code displays to a Mobile App
# including a custom feature to display your own Q-Codes after boot has completed

from adafruit_macropad import MacroPad
import time

L = 0
T = 0.25
T1 = 0
def process_qcode(code):
    global L, T, T1
    try:
        line = code[L]
        T2 = time.monotonic()
        if T2 > T1 + T:
            if ":" in line:
                print(line[:2], line[2:4], line[4], line[5:].replace("\n", ""))
            else:
                print(line.replace("\n", ""))
            L += 1
            T1 = T2
    except:
        pass

macropad = MacroPad()

k = macropad.Keycode
keys = \
{
    "0"  : ([k.ESCAPE],       0x0000FF, 0xFF0000),
    "1"  : ([k.ENTER],        0x0000FF, 0xFF0000),
    "2"  : ([k.PRINT_SCREEN], 0x0000FF, 0xFF0000),
    "3"  : ([k.SHIFT],        0x0000FF, 0xFF0000),
    "4"  : ([k.GUI],          0x0000FF, 0xFF0000),
    "5"  : ([k.DELETE],       0x0000FF, 0xFF0000),
    "6"  : ([k.CONTROL],      0x0000FF, 0xFF0000),
    "7"  : ([k.UP_ARROW],     0x0000FF, 0xFF0000),
    "8"  : ([k.ALT],          0x0000FF, 0xFF0000),
    "9"  : ([k.LEFT_ARROW],   0x0000FF, 0xFF0000),
    "10" : ([k.DOWN_ARROW],   0x0000FF, 0xFF0000),
    "11" : ([k.RIGHT_ARROW],  0x0000FF, 0xFF0000),
}

for key in keys:
    macropad.pixels[int(key)] = keys[key][2]

with open("Q_CODE.LOG", "r") as file:
    Q = file.readlines()

while True:
    process_qcode(Q)
    key_event = macropad.keys.events.get()
    if key_event:
        data = keys[str(key_event.key_number)]
        if key_event.pressed:
            macropad.keyboard.press(data[0])
            macropad.pixels[key_event.key_number] = data[1]
            macropad.start_tone(1000)
        else:
            macropad.keyboard.release(data[0])
            macropad.pixels[key_event.key_number] = data[2]
            macropad.stop_tone()