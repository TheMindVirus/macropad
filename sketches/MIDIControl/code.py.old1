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

while True:
    key_event = macropad.keys.events.get()
    #midi_event = macropad.midi.events.get()

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