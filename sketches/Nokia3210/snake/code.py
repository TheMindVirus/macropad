# Lego Macropad Nokia 3210 Snake - Alastair Cota & Adafruit Industries
# This is an emulation of a classic 2D game that shipped with Nokia 3210 series mobile phones.
# Arrow keys are the bottom row of keys in portrait orientation and key 7 for up.

from adafruit_macropad import MacroPad
from adafruit_display_shapes.rect import Rect
import random, displayio, time

macropad = MacroPad()
group = displayio.Group()

w = 127
h = 63
dx = 0
dy = -1
snake = [[int(w / 2), int(h / 2)]]
snake.insert(0, [snake[0][0], snake[0][1] - 1])
snake.insert(0, [snake[0][0], snake[0][1] - 1])

cookie = [0, 0]
keys = [7, 9, 10, 11]
directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]

debug_view = macropad.display_text(title = "<<<Debug>>>")

def debug(*messages):
    global debug_view
    i = 0
    for line in messages:
        debug_view[i].text = str(line)
        i += 1
    debug_view.show()

def clear_screen(W = w, H = h):
    global group
    group = displayio.Group()
    group.append(Rect(0, 0, W, H, fill = 0x000000))
    #macropad.display.show(group)

def draw_pixel(X = 0, Y = 0):
    global group
    group.append(Rect(X, Y, 1, 1, fill = 0xFFFFFF))
    macropad.display.show(group)

def update_cookie():
    global cookie
    random.seed(time.monotonic_ns())
    cookie = [random.randint(0, w), random.randint(0, h)]
update_cookie()

locked = False
interval = 10.0
t = 0.0

for key in keys:
    macropad.pixels[key] = 0x003300

while True:
    key_event = macropad.keys.events.get()
    
    if key_event:
        if key_event.pressed:
            if key_event.key_number in keys:
                macropad.pixels[key_event.key_number] = 0x00FF33
                idx = directions[keys.index(key_event.key_number)]
                opp = [-dx, -dy]
                if idx != opp:
                    dx, dy = idx
        else:
            if key_event.key_number in keys:
                macropad.pixels[key_event.key_number] = 0x003300
    
    t = (time.monotonic_ns() / 1000.0) % (interval * 2)
    if (t < interval):
        if not locked:
            for i in range(len(snake) - 1, 0, -1):
                snake[i][0] = snake[i - 1][0]
                snake[i][1] = snake[i - 1][1]
            
            if snake[0] == cookie:
                update_cookie()
                snake.insert(0, [snake[0][0], snake[0][1]])
                for i in range(len(snake) - 1, 0, -1):
                    snake[i][0] = snake[i - 1][0]
                    snake[i][1] = snake[i - 1][1]

            snake[0][0] += dx
            snake[0][1] += dy
            
            if (snake[0][0] > w):
                snake[0][0] = 0
            
            if (snake[0][0] < 0):
                snake[0][0] = w

            if (snake[0][1] > h):
                snake[0][1] = 0

            if (snake[0][1] < 0):
                snake[0][1] = h
            
            clear_screen()
            for i in range(0, len(snake)):
                draw_pixel(snake[i][0], snake[i][1])
            draw_pixel(cookie[0], cookie[1])
            #debug(snake)
            locked = True
    else:
        locked = False
    
    #debug(t, t < interval, locked)
    #draw_pixel()
