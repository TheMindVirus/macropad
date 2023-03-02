```py
# PowerRelay - TheMindVirus
# This sketch is designed for a relay to be attached via StemmaQT to GPIO pin cable.
# The relay/transistor/MOSFET can then be used to switch on/off ATX Motherboards.

from adafruit_macropad import MacroPad
import board, digitalio, time

macropad = MacroPad()

tmp = 0
state = 0
previous = 0
threshold = 3
result = 0

outputA = digitalio.DigitalInOut(board.SCL)
outputB = digitalio.DigitalInOut(board.SDA)
outputA.direction = digitalio.Direction.OUTPUT
outputB.direction = digitalio.Direction.OUTPUT
outputA.value = False
outputB.value = not outputA.value

keys = \
{
    "0"  : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "1"  : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "2"  : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "3"  : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "4"  : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "5"  : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "6"  : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "7"  : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "8"  : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "9"  : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "10" : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
    "11" : { "on": 0x00FFFF, "off": 0x003333, "state": 0 },
}

def reset():
    global keys
    for key in keys:
        macropad.pixels[int(key)] = keys[key]["off"]
        keys[key]["state"] = 0
    outputA.value = False
    outputB.value = not outputA.value

def refresh():
    global keys, tmp, state, previous, threshold, result, outputA, outputB
    tmp = 0
    for i in range(0, len(keys)):
        tmp += keys[str(i)]["state"]
    state = tmp
    result = (state >= threshold)
    if state != previous:
        print("on" if result else "off")
        outputA.value = result
        outputB.value = not outputA.value
    previous = state

reset()
while True:
    key_event = macropad.keys.events.get()
    if key_event:
        data = keys[str(key_event.key_number)]
        key_state = "on" if key_event.pressed else "off"
        macropad.pixels[key_event.key_number] = data[key_state]
        data["state"] = key_event.pressed
        refresh()
```