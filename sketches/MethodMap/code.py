# Lego Macropad Method Map - Alastair Cota & Adafruit Industries
# Python Dictionaries can handle multidimentional data structure without if/else for every case.
# They are much like their equivalent of std::map in the C++ Standard Template Library (STL). Dictionaries can also contain Methods.

from adafruit_macropad import MacroPad

macropad = MacroPad()

def key0_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F13)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F13)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key1_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F14)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F14)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key2_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F15)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F15)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key3_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F16)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F16)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key4_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F17)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F17)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key5_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F18)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F18)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key6_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F19)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F19)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key7_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F20)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F20)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key8_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F21)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F21)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key9_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F22)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F22)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key10_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F23)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F23)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

def key11_action(key_event, data, parameters):
    if key_event.pressed:
        macropad.keyboard.press(macropad.Keycode.F24)
        macropad.pixels[key_event.key_number] = 0xFFFFFF
    else:
        macropad.keyboard.release(macropad.Keycode.F24)
        macropad.pixels[key_event.key_number] = 0x000000
    return data

keys = \
{
    "0"  : { "callback" : key0_action,  "parameters" : { } },
    "1"  : { "callback" : key1_action,  "parameters" : { } },
    "2"  : { "callback" : key2_action,  "parameters" : { } },
    "3"  : { "callback" : key3_action,  "parameters" : { } },
    "4"  : { "callback" : key4_action,  "parameters" : { } },
    "5"  : { "callback" : key5_action,  "parameters" : { } },
    "6"  : { "callback" : key6_action,  "parameters" : { } },
    "7"  : { "callback" : key7_action,  "parameters" : { } },
    "8"  : { "callback" : key8_action,  "parameters" : { } },
    "9"  : { "callback" : key9_action,  "parameters" : { } },
    "10" : { "callback" : key10_action, "parameters" : { } },
    "11" : { "callback" : key11_action, "parameters" : { } },
}

last_position = 0
text_lines = macropad.display_text(title = "Macropad")

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        data = keys[str(key_event.key_number)]
        if data["callback"]:
            data = data["callback"](key_event, data, data["parameters"])
        keys[str(key_event.key_number)] = data

    text_lines[0].text = "{}".format(macropad.encoder)
    text_lines[1].text = "{}".format(macropad.encoder_switch)
    text_lines.show()

    current_position = macropad.encoder

    if macropad.encoder > last_position:
        if macropad.encoder_switch:
            macropad.mouse.move(y = +10)
        else:
            macropad.mouse.move(x = +10)
        last_position = current_position

    elif macropad.encoder < last_position:
        if macropad.encoder_switch:
            macropad.mouse.move(y = -10)
        else:
            macropad.mouse.move(x = -10)
        last_position = current_position