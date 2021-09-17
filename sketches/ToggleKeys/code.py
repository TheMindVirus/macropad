# Lego Macropad Toggle Keys - Alastair Cota & Adafruit Industries
# This sketch builds upon Menu Select and adds Momentary vs. OneShot vs. Toggle which can get complex.
# The Python Dictionary can handle this multidimentional data structure without if/else for every case.

from adafruit_macropad import MacroPad
import time

macropad = MacroPad()

MOMENTARY = 0
ONESHOT = 1
TOGGLE = 2

keys = \
{
    "0"  : { "action" : macropad.Keycode.ESCAPE,       "colour" : { "off" : 0x333333, "on" : 0xFFFFFF }, "state" : { "previous" : 0, "latch" : 0, "mode" : MOMENTARY }, "tone" : { "enabled" : False, "frequency" : 1000 } },
    "1"  : { "action" : macropad.Keycode.ENTER,        "colour" : { "off" : 0x333333, "on" : 0xFFFFFF }, "state" : { "previous" : 0, "latch" : 0, "mode" : MOMENTARY }, "tone" : { "enabled" : False, "frequency" : 1000 } },
    "2"  : { "action" : macropad.Keycode.PRINT_SCREEN, "colour" : { "off" : 0x333333, "on" : 0xFFFFFF }, "state" : { "previous" : 0, "latch" : 0, "mode" : MOMENTARY }, "tone" : { "enabled" : False, "frequency" : 1000 } },
    "3"  : { "action" : macropad.Keycode.SHIFT,        "colour" : { "off" : 0x333333, "on" : 0xFFFFFF }, "state" : { "previous" : 0, "latch" : 0, "mode" : MOMENTARY }, "tone" : { "enabled" : False, "frequency" : 1000 } },
    "4"  : { "action" : macropad.Keycode.GUI,          "colour" : { "off" : 0x333333, "on" : 0xFFFFFF }, "state" : { "previous" : 0, "latch" : 0, "mode" :   ONESHOT }, "tone" : { "enabled" :  True, "frequency" : 1000 } },
    "5"  : { "action" : macropad.Keycode.DELETE,       "colour" : { "off" : 0x333333, "on" : 0xFFFFFF }, "state" : { "previous" : 0, "latch" : 0, "mode" :   ONESHOT }, "tone" : { "enabled" :  True, "frequency" : 1000 } },
    "6"  : { "action" : macropad.Keycode.CONTROL,      "colour" : { "off" : 0x333333, "on" : 0xFFFFFF }, "state" : { "previous" : 0, "latch" : 0, "mode" : MOMENTARY }, "tone" : { "enabled" : False, "frequency" : 1000 } },
    "8"  : { "action" : macropad.Keycode.ALT,          "colour" : { "off" : 0x333333, "on" : 0xFFFFFF }, "state" : { "previous" : 0, "latch" : 0, "mode" : MOMENTARY }, "tone" : { "enabled" : False, "frequency" : 1000 } },
    "7"  : { "action" : macropad.Keycode.UP_ARROW,     "colour" : { "off" : 0x330000, "on" : 0xFF0000 }, "state" : { "previous" : 0, "latch" : 0, "mode" :    TOGGLE }, "tone" : { "enabled" : False, "frequency" : 1000 } },
    "9"  : { "action" : macropad.Keycode.LEFT_ARROW,   "colour" : { "off" : 0x330000, "on" : 0xFF0000 }, "state" : { "previous" : 0, "latch" : 0, "mode" :    TOGGLE }, "tone" : { "enabled" : False, "frequency" : 1000 } },
    "10" : { "action" : macropad.Keycode.DOWN_ARROW,   "colour" : { "off" : 0x330000, "on" : 0xFF0000 }, "state" : { "previous" : 0, "latch" : 0, "mode" :    TOGGLE }, "tone" : { "enabled" : False, "frequency" : 1000 } },
    "11" : { "action" : macropad.Keycode.RIGHT_ARROW,  "colour" : { "off" : 0x330000, "on" : 0xFF0000 }, "state" : { "previous" : 0, "latch" : 0, "mode" :    TOGGLE }, "tone" : { "enabled" : False, "frequency" : 1000 } },
}

for key in keys:
    macropad.pixels[int(key)] = keys[key]["colour"]["off"]

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        data = keys[str(key_event.key_number)]
        
        if (data["state"]["mode"] == MOMENTARY):
            if key_event.pressed:
                macropad.keyboard.press(data["action"])
                macropad.pixels[key_event.key_number] = data["colour"]["on"]
                if data["tone"]["enabled"]:
                    macropad.start_tone(data["tone"]["frequency"])
            else:
                macropad.keyboard.release(data["action"])
                macropad.pixels[key_event.key_number] = data["colour"]["off"]
                if data["tone"]["enabled"]:
                    macropad.stop_tone()
        
        elif (data["state"]["mode"] == ONESHOT):
            if key_event.pressed:
                macropad.keyboard.press(data["action"])
                macropad.pixels[key_event.key_number] = data["colour"]["on"]
                if data["tone"]["enabled"]:
                    macropad.start_tone(data["tone"]["frequency"])
                time.sleep(0.1)
                macropad.keyboard.release(data["action"])
                macropad.pixels[key_event.key_number] = data["colour"]["off"]
                if data["tone"]["enabled"]:
                    macropad.stop_tone()
        
        elif (data["state"]["mode"] == TOGGLE):
            if key_event.pressed:
                data["state"]["latch"] = 1 if data["state"]["latch"] == 0 else 0
                if (data["state"]["latch"] == 1):
                    macropad.keyboard.press(data["action"])
                    macropad.pixels[key_event.key_number] = data["colour"]["on"]
                else:
                    macropad.keyboard.release(data["action"])
                    macropad.pixels[key_event.key_number] = data["colour"]["off"]
                if data["tone"]["enabled"]:
                    macropad.start_tone(data["tone"]["frequency"])
                    time.sleep(0.1)
                    macropad.stop_tone()
        
        data["state"]["previous"] = key_event.pressed
        keys[str(key_event.key_number)] = data