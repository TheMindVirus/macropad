# Lego Macropad MIDI Control - Alastair Cota & Adafruit Industries
# A simple patch demonstrating basic MIDI Controller capabilities of the Macropad RP2040
# The encoder is clamped from 0 to 127 as is the standard range for Control Change values in the MIDI 1.0 Specification

from adafruit_macropad import MacroPad

macropad = MacroPad()

last_pressed = 0
last_position = 0
clamped_position = 0
text_lines = macropad.display_text(title = "Macropad MIDI")
text_lines[0].text = str(clamped_position)
text_lines.show()

rgb = \
{
    "0"  : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "1"  : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "2"  : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "3"  : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "4"  : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "5"  : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "6"  : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "7"  : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "8"  : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "9"  : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "10" : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
    "11" : { "R" : { "A" : 0, "B" : 0 }, "G" : { "A" : 0, "B" : 0 }, "B" : { "A" : 0, "B" : 0 } },
}

while True:
    key_event = macropad.keys.events.get()
    midi_event = macropad.midi.receive()

    if key_event:
        macropad.midi.send(macropad.ControlChange(key_event.key_number, 127 if key_event.pressed else 0))
    if macropad.encoder_switch != last_pressed:
        macropad.midi.send(macropad.ControlChange(13, 127 if not last_pressed else 0))
    last_pressed = macropad.encoder_switch
    
    current_position = macropad.encoder

    if macropad.encoder > last_position:
        clamped_position += 1 if clamped_position < 127 else 0
        macropad.midi.send(macropad.ControlChange(12, clamped_position))
        text_lines[0].text = str(clamped_position)
        text_lines.show()
        last_position = current_position

    elif macropad.encoder < last_position:
        clamped_position -= 1 if clamped_position > 0 else 0
        macropad.midi.send(macropad.ControlChange(12, clamped_position))
        text_lines[0].text = str(clamped_position)
        text_lines.show()
        last_position = current_position

    if midi_event:
        if type(midi_event).__name__ == "ControlChange":
            idx = str(int(midi_event.control / 6))
            mod = int((midi_event.control % 6) / 2)
            col = "R" if mod == 0 else "G" if mod == 1 else "B" if mod == 2 else "R"
            cof = "A" if midi_event.control % 2 == 0 else "B"
            if (int(idx) < 12):
                rgb[idx][col][cof] = midi_event.value
                macropad.pixels[int(idx)] = ((rgb[idx]["R"]["A"] + rgb[idx]["R"]["B"]) << 16) \
                                          + ((rgb[idx]["G"]["A"] + rgb[idx]["G"]["B"]) << 8) \
                                          + ((rgb[idx]["B"]["A"] + rgb[idx]["B"]["B"]))
            text_lines[1].text = str(midi_event.control) + " " + str(midi_event.value)
            text_lines.show()
