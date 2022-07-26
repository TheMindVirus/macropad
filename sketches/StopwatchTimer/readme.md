```py
# Stopwatch Timer - Alastair Cota
# This sketch emulates the Stopwatch Function of the Clock App found on iPhones
# with Reset and Start buttons that change to Lap and Stop buttons and a Scrolling Display History

from adafruit_macropad import MacroPad
import time, supervisor

macropad = MacroPad()
macropad_display_lines = 4
text_lines = macropad.display_text()

KEY_START_STOP = 11
KEY_RESET_LAP = 9

chroma = \
{
    "RESET": { "ON": 0x000077, "OFF": 0x0000FF, },
    "LAP":   { "ON": 0x777700, "OFF": 0xFFFF00, },
    "START": { "ON": 0x007700, "OFF": 0x00FF00, },
    "STOP":  { "ON": 0x770000, "OFF": 0xFF0000, },
}

key_state_reset_lap = 0
key_state_start_stop = 0

encoder_this_position = 0
encoder_last_position = 0

line_history = []
line_offset = 0

timer_state = 0
timer_time = 0
timer_offset = 0
timer_reset = 0
timer_error = 0

def reset():
    global timer_reset, timer_offset, timer_time, line_offset, line_history
    timer_reset = 0
    timer_offset = 0
    timer_time = 0
    line_offset = 0
    line_history = []
    supervisor.enable_autoreload()

def lap():
    global line_history, line_offset, timer_time, timer_error
    this_lap = str(len(line_history) + 1)
    this_time = str(timer_time - timer_error)
    line_history.append(str("Lap " + this_lap + ": " + this_time))
    line_offset = max(0, len(line_history) - macropad_display_lines + 1)

def start():
    global timer_reset, timer_offset, timer_state
    if timer_reset == 0:
        timer_offset = time.monotonic()
    timer_reset = 1
    timer_state = 1
    supervisor.disable_autoreload()

def stop():
    global timer_state, timer_time, timer_error
    timer_state = 0
    timer_time -= timer_error
    supervisor.enable_autoreload()

while True:
    if timer_state == 1:
        timer_time = time.monotonic() - timer_offset

    key_event = macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            if key_event.key_number == KEY_RESET_LAP:
                reset() if timer_state == 0 else lap()
                key_state_reset_lap = 1
            elif key_event.key_number == KEY_START_STOP:
                start() if timer_state == 0 else stop()
                key_state_start_stop = 1
            pass
        else:
            if key_event.key_number == KEY_RESET_LAP:
                key_state_reset_lap = 0
            elif key_event.key_number == KEY_START_STOP:
                key_state_start_stop = 0

    macropad.pixels[KEY_RESET_LAP] = chroma["RESET" if timer_state == 0 else "LAP"]["OFF" if key_state_reset_lap == 0 else "ON"]
    macropad.pixels[KEY_START_STOP] = chroma["START" if timer_state == 0 else "STOP"]["OFF" if key_state_start_stop == 0 else "ON"]

    encoder_current_position = macropad.encoder
    if macropad.encoder < encoder_last_position:
        if line_offset - 1 >= 0:
            line_offset -= 1
    elif macropad.encoder > encoder_last_position:
        if line_offset + 1 < len(line_history):
            line_offset += 1
    encoder_last_position = encoder_current_position
    
    text_lines[0].text = "Time: " + str(timer_time)
    for i in range(0, macropad_display_lines):
        if i + line_offset >= len(line_history):
            text_lines[i + 1].text = ""
        else:
            text_lines[i + 1].text = str(line_history[i + line_offset])
    text_lines.show()
```