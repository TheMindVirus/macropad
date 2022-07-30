# Traktor Pro 2 Live Preset - TheMindVirus/SobaBoii
# MIDI Controller for Live Performance in Native Instruments Traktor Pro 2
# For use with "Adafruit_MacroPad_RP2040.tsi" and "CircuitPython Audio" in the Controller Manager

help_text = \
"""
[macropad traktor settings file]
hold nothing to control looping with encoder
hold button 0 to control looping with encoder
hold button 1 to control iceverb with encoder
hold button 2 to control deck select with encoder
hold button 3 to control bass with encoder
hold button 4 to control mid with encoder
hold button 5 to control high with encoder
hold button 6 to control filter with encoder
hold button 7 to control gain with encoder
hold button 8 to control pitch with encoder
hold button 9 to control mute/cut with encoder
hold button 10 to control crossfader with encoder
press button 11 to cue the selected deck
release button 11 to play the selected deck
hold encoder with nothing selected to browse in exclusive mode
"""

from adafruit_macropad import MacroPad

macropad = MacroPad()

chroma_on = 0xFF000F
chroma_off = 0x00F
chroma_override = 0x11FF11

num_keys = 12

encoder_key = 126
encoder_cc = 127
browser_cc = 125

cc = 0
encoder_last = 0
encoder_current = 0
encoder_position = 0
current_mode = 0
key_stack = []
key_override_on = False
key_override_off = False
exclusive_list = [7, 8, 10, 11]
exclusive_mode = False
midi_warn = False

text_lines = macropad.display_text(title = "[Traktor Pro 2]")

for key in range(0, num_keys):
    macropad.pixels[key] = chroma_off

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            key_stack.insert(0, key_event.key_number)
            cc = key_event.key_number
            if exclusive_mode and cc in exclusive_list:
                 cc = 64 + key_event.key_number
            macropad.midi.send(macropad.ControlChange(cc, 127))
        elif key_event.released:
            key_stack.remove(key_event.key_number)
            cc = key_event.key_number
            if exclusive_mode and cc in exclusive_list:
                 cc = 64 + key_event.key_number
            macropad.midi.send(macropad.ControlChange(cc, 0))

    macropad.encoder_switch_debounced.update()
    if macropad.encoder_switch:
        exclusive_mode = True
    if macropad.encoder_switch_debounced.pressed:
        key_stack.insert(0, encoder_cc)
        macropad.midi.send(macropad.ControlChange(encoder_cc, 127))
        exclusive_mode = True
    elif macropad.encoder_switch_debounced.released:
        key_stack.remove(encoder_cc)
        macropad.midi.send(macropad.ControlChange(encoder_cc, 0))
        exclusive_mode = False
    key_override_off = exclusive_mode

    current_mode = encoder_key if len(key_stack) == 0 else key_stack[0]
    text_lines[0].text = str(key_stack)

    encoder_current = macropad.encoder
    if encoder_current != encoder_last:
        encoder_position = encoder_current % 128
        cc = browser_cc if exclusive_mode else encoder_key if current_mode == 0 else 32 + current_mode if current_mode < 100 else current_mode
        macropad.midi.send(macropad.ControlChange(cc, encoder_position))
        encoder_last = encoder_current
    text_lines[1].text = str(encoder_position)

    midi_event = macropad.midi.receive()
    if midi_event:
        if midi_event.control == 0:
            key_override_on = (midi_event.value == 2)
        elif midi_event.control == 1:
            midi_warn = midi_event.value
    text_lines[2].text = "///!!!WARNING!!!\\\\\\" if midi_warn else ""
    key_override_on = True if midi_warn else key_override_on
    
    for key in range(0, num_keys):
        macropad.pixels[key] = chroma_override if key_override_off and key in exclusive_list \
            else chroma_on if key_override_on or key in key_stack else chroma_off if not key_override_off else 0
    text_lines.show()