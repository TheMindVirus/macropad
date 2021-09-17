# Lego Macropad F13-F24 With Tone - Alastair Cota & Adafruit Industries
# The inspiration for this project came from the door unlock mechanism in The Crystal Maze
# and also the typewriter sound from Among Us. For use with 12x Trans-Red Lego Keycaps. Enjoy!

from adafruit_macropad import MacroPad

macropad = MacroPad()

keys = \
{
    "0": macropad.Keycode.F13,
    "1": macropad.Keycode.F14,
    "2": macropad.Keycode.F15,
    "3": macropad.Keycode.F16,
    "4": macropad.Keycode.F17,
    "5": macropad.Keycode.F18,
    "6": macropad.Keycode.F19,
    "7": macropad.Keycode.F20,
    "8": macropad.Keycode.F21,
    "9": macropad.Keycode.F22,
    "10": macropad.Keycode.F23,
    "11": macropad.Keycode.F24,
}

for key in keys:
    macropad.pixels[int(key)] = 0x330000;

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            macropad.keyboard.press(keys[str(key_event.key_number)])
            macropad.pixels[key_event.key_number] = 0xFF0000;
            macropad.start_tone(1000);
        else:
            macropad.keyboard.release(keys[str(key_event.key_number)])
            macropad.pixels[key_event.key_number] = 0x330000;
            macropad.stop_tone();