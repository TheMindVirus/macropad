# Lego Macropad Menu Select Navigation - Alastair Cota & Adafruit Industries
# This layout feels quite natural for menu selection and simple games with the arrow keys.
# It also demonstrates how to store different on/off colour values for each individual key.

from adafruit_macropad import MacroPad

macropad = MacroPad()

keys = \
{
    "0"  : (macropad.Keycode.ESCAPE,       0xFF0000, 0x330000),
    "1"  : (macropad.Keycode.ENTER,        0xFFFF00, 0x333300),
    "2"  : (macropad.Keycode.PRINT_SCREEN, 0x00FF00, 0x003300),
    "3"  : (macropad.Keycode.SHIFT,        0x00FFFF, 0x003333),
    "4"  : (macropad.Keycode.GUI,          0x0000FF, 0x000033),
    "5"  : (macropad.Keycode.DELETE,       0xFF00FF, 0x330033),
    "6"  : (macropad.Keycode.CONTROL,      0xFFFFFF, 0x333333),
    "7"  : (macropad.Keycode.UP_ARROW,     0x0000FF, 0x000033),
    "8"  : (macropad.Keycode.ALT,          0xFFFFFF, 0x333333),
    "9"  : (macropad.Keycode.LEFT_ARROW,   0x0000FF, 0x000033),
    "10" : (macropad.Keycode.DOWN_ARROW,   0x0000FF, 0x000033),
    "11" : (macropad.Keycode.RIGHT_ARROW,  0x0000FF, 0x000033),
}

for key in keys:
    macropad.pixels[int(key)] = keys[key][2];

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        data = keys[str(key_event.key_number)]
        if key_event.pressed:
            macropad.keyboard.press(data[0])
            macropad.pixels[key_event.key_number] = data[1];
            #macropad.start_tone(1000);
        else:
            macropad.keyboard.release(data[0])
            macropad.pixels[key_event.key_number] = data[2];
            #macropad.stop_tone();