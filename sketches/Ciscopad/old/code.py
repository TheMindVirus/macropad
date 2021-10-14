# Ciscopad - Unknown
# Adafruit Macropad running Cisco IOS Router Firmware Emulation and basic Macropad Sketch
# Press Ctrl+C when connected to the Serial Terminal at COM# 115200 Baud (8n1)

from adafruit_macropad import MacroPad

macropad = MacroPad()

text_lines = macropad.display_text(title = "\\\\\\\\[CiscoPad]////")
text_lines[0] = "Router#"
text_lines.show()

keys = \
{
    "0"  : (macropad.Keycode.ESCAPE,       0x00FFFF, 0x003333),
    "1"  : (macropad.Keycode.ENTER,        0x00FFFF, 0x003333),
    "2"  : (macropad.Keycode.PRINT_SCREEN, 0x00FFFF, 0x003333),
    "3"  : (macropad.Keycode.SHIFT,        0x00FFFF, 0x003333),
    "4"  : (macropad.Keycode.GUI,          0x00FFFF, 0x003333),
    "5"  : (macropad.Keycode.DELETE,       0x00FFFF, 0x003333),
    "6"  : (macropad.Keycode.CONTROL,      0x00FFFF, 0x003333),
    "7"  : (macropad.Keycode.UP_ARROW,     0x00FFFF, 0x003333),
    "8"  : (macropad.Keycode.ALT,          0x00FFFF, 0x003333),
    "9"  : (macropad.Keycode.LEFT_ARROW,   0x00FFFF, 0x003333),
    "10" : (macropad.Keycode.DOWN_ARROW,   0x00FFFF, 0x003333),
    "11" : (macropad.Keycode.RIGHT_ARROW,  0x00FFFF, 0x003333),
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