# Lego Macropad Keypad Entry - Alastair Cota & Adafruit Industries
# This sketch allows you to type the number of the MIDI control you want to edit,
# press enter or clear and then change its value with the endless rotary encoder.

from adafruit_macropad import MacroPad
import time

macropad = MacroPad()

last_pressed = 0
last_position = 0
clamped_position = 0
text_lines = macropad.display_text(title = "Macropad MIDI")
text_lines[0].text = str(clamped_position)
text_lines.show()

keys = \
{
    "0": "1",
    "1": "2",
    "2": "3",
    "3": "4",
    "4": "5",
    "5": "6",
    "6": "7",
    "7": "8",
    "8": "9",
    "9": "*",
    "10": "0",
    "11": "#",
}

data_entry = ""
selected = 0
last_position = 0
clamped_position = 0
characters = "1234567890"
text_lines = macropad.display_text(title = "////[ENTER_VALUE]\\\\\\\\")

def update_display():
    text_lines[0].text = "$> " + data_entry
    text_lines[1].text = str(selected)
    text_lines[2].text = str(clamped_position)
    text_lines.show()
update_display()

for key in keys:
    macropad.pixels[int(key)] = 0x330000;

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            cmd = keys[str(key_event.key_number)]
            if cmd == "#":
                try:
                    selected = int(data_entry)
                    selected = selected if (selected > 0) else 0
                    selected = selected if (selected <= 127) else 127
                except:
                    selected = 0
            elif (characters.find(cmd) > -1): #elif (str(cmd).isnumeric()):
                data_entry += cmd
            if (cmd == "*") or (cmd == "*"):
                data_entry = ""
            macropad.pixels[key_event.key_number] = 0xFF0000;
            macropad.start_tone(1000);
            time.sleep(0.05)
            macropad.pixels[key_event.key_number] = 0x330000;
            macropad.stop_tone();
        update_display()

    current_position = macropad.encoder

    if macropad.encoder > last_position:
        clamped_position += 1 if clamped_position < 127 else 0
        macropad.midi.send(macropad.ControlChange(selected, clamped_position))
        last_position = current_position
        update_display()

    elif macropad.encoder < last_position:
        clamped_position -= 1 if clamped_position > 0 else 0
        macropad.midi.send(macropad.ControlChange(selected, clamped_position))
        last_position = current_position
        update_display()