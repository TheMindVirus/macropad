# Lego Macropad Nokia 3210 - Alastair Cota & Adafruit Industries
# Nokia 3210 is considered to be a classic mobile phone with its keypad that allows you to type
# any letter of the alphabet, numbers and special characters for text messages. This sketch replicates that keypad.

from adafruit_macropad import MacroPad
import time

macropad = MacroPad()

keys = \
{
    "0"  : ("1", "o_o"),
    "1"  : ("2", "a", "b", "c"),
    "2"  : ("3", "d", "e", "f"),
    "3"  : ("4", "g", "h", "i"),
    "4"  : ("5", "j", "k", "l"),
    "5"  : ("6", "m", "n", "o"),
    "6"  : ("7", "p", "q", "r", "s"),
    "7"  : ("8", "t", "u", "v"),
    "8"  : ("9", "w", "x", "y", "z"),
    "9"  : ("*"),
    "10" : ("0", "_"),
    "11" : ("#"),
}

presses = \
{
    "0"  : 0,
    "1"  : 0,
    "2"  : 0,
    "3"  : 0,
    "4"  : 0,
    "5"  : 0,
    "6"  : 0,
    "7"  : 0,
    "8"  : 0,
    "9"  : 0,
    "10" : 0,
    "11" : 0,
}

def reset_presses():
    for key in presses:
        presses[key] = 0

shift = False
data_entry = ""
last_entry = ""
last_entered = ""
last_pressed = "0"
text_lines = macropad.display_text(title = "////[NOKIA_3210m]\\\\\\\\")

def update_display():
    text_lines[0].text = "$> " + str(data_entry)
    text_lines[1].text = str(last_entry)
    text_lines.show()
update_display()

for key in keys:
    macropad.pixels[int(key)] = 0x330000

while True:
    c = ""
    idx = last_pressed
    run = False

    macropad.encoder_switch_debounced.update()
    if macropad.encoder_switch_debounced.pressed:
        c = "^"
        run = True

    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed:
        idx = str(key_event.key_number)
        run = True

    if run:
        if c == "^":
            shift = False if shift else True
            c = last_entered 
        else:
            c = keys[idx][presses[idx]]
        c = c.upper() if shift else c.lower()

        if c == "#":
            macropad.keyboard_layout.write(data_entry)
            last_entry = data_entry
            data_entry = ""
            reset_presses()
        
        elif c == "*":
            data_entry = ""
            reset_presses()
        
        elif idx == last_pressed:
            data_entry = data_entry[ : len(data_entry) - len(last_entered) ]
            data_entry += c
        
        else:
            reset_presses()
            data_entry += c
        
        if key_event:
            presses[idx] += 1
            presses[idx] %= len(keys[idx])
        
        last_entered = c
        last_pressed = idx

        if key_event:
            macropad.pixels[key_event.key_number] = 0xFF0000
        macropad.start_tone(5000)
        time.sleep(0.05)
        
        if key_event:
            macropad.pixels[key_event.key_number] = 0x330000
        macropad.stop_tone()
        update_display()
       