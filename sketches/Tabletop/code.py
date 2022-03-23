# Tabletop Simulator Scripting Buttons - Alastair Cota
# Tabletop Simulator running on Unity Engine 2019 does not allow C# Scripting for Custom Assetbundles
# but it does turn numberpad keys into 1->10 as "scripting buttons" for triggering lua events and controlling Unity Components.

# Notes:
# * The lua scripting takes the following code layout: `function onScriptingButtonDown(index, color) print(index) end`
# * Similarly there is also `function onScriptingButtonUp(index, color) print(index) end`
# * 0 for whatever reason becomes 10 instead of 0
# * The arrow keys which would be WASD will now be 1234
# * The rest of the keys will be in order in portrait orientation starting from 5
# * 2 keys remain unused and will be open for user-customisable macro keys

# More Information:
# * https://api.tabletopsimulator.com/events/#onscriptingbuttondown
# * https://api.tabletopsimulator.com/components/examples/
# * https://api.tabletopsimulator.com/types/#vector
# * https://docs.circuitpython.org/projects/hid/en/latest/api.html

from adafruit_macropad import MacroPad

macropad = MacroPad()
k = macropad.Keycode

keys = \
{
    "0"  : ([k.KEYPAD_FIVE],  0x00FFFF, 0x003333),
    "1"  : ([k.KEYPAD_SIX],   0x00FFFF, 0x003333),
    "2"  : ([k.KEYPAD_SEVEN], 0x00FFFF, 0x003333),
    "3"  : ([k.KEYPAD_EIGHT], 0x00FFFF, 0x003333),
    "4"  : ([k.KEYPAD_NINE],  0x00FFFF, 0x003333),
    "5"  : ([k.KEYPAD_ZERO],  0x00FFFF, 0x003333),
    "6"  : ([],               0x00FF00, 0x000000),
    "7"  : ([k.KEYPAD_ONE],   0xFF0000, 0xFF0000),
    "8"  : ([],               0x00FF00, 0x000000),
    "9"  : ([k.KEYPAD_TWO],   0xFF0000, 0xFF0000),
    "10" : ([k.KEYPAD_THREE], 0xFF0000, 0xFF0000),
    "11" : ([k.KEYPAD_FOUR],  0xFF0000, 0xFF0000),
}

for key in keys:
    macropad.pixels[int(key)] = keys[key][2]

numlock = macropad.keyboard.led_on(macropad.keyboard.LED_NUM_LOCK)
def toggle_numlock():
    macropad.keyboard.press(k.KEYPAD_NUMLOCK)
    macropad.keyboard.release(k.KEYPAD_NUMLOCK)
toggle_numlock()
toggle_numlock()

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        data = keys[str(key_event.key_number)]
        if key_event.pressed:
            numlock = macropad.keyboard.led_on(macropad.keyboard.LED_NUM_LOCK)
            print(numlock)
            if not numlock:
                toggle_numlock()
            [macropad.keyboard.press(key) for key in data[0]]
            if not numlock:
                toggle_numlock()
            macropad.pixels[key_event.key_number] = data[1]
        else:
            numlock = macropad.keyboard.led_on(macropad.keyboard.LED_NUM_LOCK)
            if not numlock:
                toggle_numlock()
            [macropad.keyboard.release(key) for key in data[0]]
            if not numlock:
                toggle_numlock()
            macropad.pixels[key_event.key_number] = data[2]
    