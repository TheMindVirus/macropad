# BnL Loading Animation - Alastair Cota
# Plays the loading animation for the power terminals found in Disney Pixar's WALL-E
# the videogame on the macropad's built-in display

from adafruit_macropad import MacroPad
from adafruit_display_shapes.rect import Rect
import random, displayio, time

macropad = MacroPad()
group = displayio.Group()

def clear_screen(W = 127, H = 63):
    global group
    group = displayio.Group()
    group.append(Rect(0, 0, W, H, fill = 0x000000))
    macropad.display.show(group)

def draw_box(Y = 0):
    global group
    group.append(Rect(0, Y * 10, 127, 8, fill = 0xFFFFFF))
    macropad.display.show(group)

while True:
    clear_screen()
    time.sleep(0.5)
    for i in range(0, 5):
        draw_box(5 - i)
        time.sleep(0.5)
    for i in range(0, 12):
        macropad.pixels[i] = 0xFF7700
    for j in range(0, 10):
        clear_screen()
        for i in range(0, 5):
            draw_box(5 - i)
            time.sleep(0.1)
    for i in range(0, 12):
        macropad.pixels[i] = 0x000000