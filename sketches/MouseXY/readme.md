```py
# MouseXY Gyroless Mouse - TheMindVirus
# This sketch converts the macropad's buttons into mouse actions
# with the scroll wheel mapped to the rotary push encoder.

from adafruit_macropad import MacroPad

macropad = MacroPad()

keys = \
{
    "0"  : ("macropad_key0", 0x000000, 0x000000),
    "1"  : ("macropad_key1", 0x000000, 0x000000),
    "2"  : ("macropad_key2", 0x000000, 0x000000),
    "3"  : ("macropad_key3", 0x000000, 0x000000),
    "4"  : ("macropad_key4", 0x000000, 0x000000),
    "5"  : ("macropad_key5", 0x000000, 0x000000),
    "6"  : ("macropad_key6", 0x0000FF, 0x000033),
    "7"  : ("macropad_key7", 0x00FFFF, 0x003333),
    "8"  : ("macropad_key8", 0x0000FF, 0x000033),
    "9"  : ("macropad_key9", 0x00FFFF, 0x003333),
    "10" : ("macropad_keyA", 0x00FFFF, 0x003333),
    "11" : ("macropad_keyB", 0x00FFFF, 0x003333),
}

last_position = 0
last_switch = False
direction = [0, 0, 0, 0]

def main():
    global macropad, keys, last_position, last_switch, direction

    for key in keys:
        macropad.pixels[int(key)] = keys[key][2]

    while True:
        if direction[0]:
            macropad.mouse.move(y = -5)
        if direction[1]:
            macropad.mouse.move(x = -5)
        if direction[2]:
            macropad.mouse.move(y = +5)
        if direction[3]:
            macropad.mouse.move(x = +5)

        key_event = macropad.keys.events.get()
        if key_event:
            data = keys[str(key_event.key_number)]
            if key_event.pressed:
                eval(data[0])(True)
                macropad.pixels[key_event.key_number] = data[1]
            else:
                eval(data[0])(False)
                macropad.pixels[key_event.key_number] = data[2]

        current_switch = macropad.encoder_switch
        if current_switch > last_switch:
            macropad.mouse.press(macropad.Mouse.MIDDLE_BUTTON)
        elif current_switch < last_switch:
            macropad.mouse.release(macropad.Mouse.MIDDLE_BUTTON)
        last_switch = current_switch
    
        current_position = macropad.encoder
        if current_position > last_position:
            macropad.mouse.move(wheel = -1)
            last_position = current_position
        if current_position < last_position:
            macropad.mouse.move(wheel = +1)
            last_position = current_position

def macropad_key0(state):
    pass

def macropad_key1(state):
    pass

def macropad_key2(state):
    pass

def macropad_key3(state):
    pass

def macropad_key4(state):
    pass

def macropad_key5(state):
    pass

def macropad_key6(state):
    if state:
        macropad.mouse.press(macropad.Mouse.LEFT_BUTTON)
    else:
        macropad.mouse.release(macropad.Mouse.LEFT_BUTTON)

def macropad_key7(state):
    global direction
    direction[0] = state

def macropad_key8(state):
    if state:
        macropad.mouse.press(macropad.Mouse.RIGHT_BUTTON)
    else:
        macropad.mouse.release(macropad.Mouse.RIGHT_BUTTON)

def macropad_key9(state):
    global direction
    direction[1] = state

def macropad_keyA(state):
    global direction
    direction[2] = state

def macropad_keyB(state):
    global direction
    direction[3] = state

if __name__ == "__main__":
    main()
```