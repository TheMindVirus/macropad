```py
# PushTheButton - TheMindVirus
# This sketch turns the adafruit macropad rp2040 into a gamepad for a quick game of push the button.
# The macropad will wait between 3-6 seconds before giving you a randomly coloured button to press.

from adafruit_macropad import MacroPad

import random, time

macropad = MacroPad()

first_key = 0
num_keys = 11

count = 0
watch = 0
error = 0

for el in range(first_key, num_keys):
    macropad.pixels[int(el)] = 0x000000

def random_randrgb(min = 16, max = 255):
    r = random.randint(min, max)
    g = random.randint(min, max)
    b = random.randint(min, max)
    return (r << 16) + (g << 8) + b

print("[!#]", "[0xrrggbb]", "[num]", "[sec]", "[err]", sep = " \t")

while True: # possibly write goto semantics
    time.sleep(random.random() * 3 + 3)
    aw = random.randint(first_key, num_keys)
    berry = random_randrgb()
    macropad.pixels[aw] = berry
    watch = 0
    error = 0
    print("!" + str(aw), hex(berry), count, watch, error, sep = " \t")
    watch = int(time.monotonic())
    found = False
    while not found:
        event = macropad.keys.events.get()
        if event and event.pressed and event.key_number == aw:
            watch = int((time.monotonic()) - watch)
            found = True
            break
        elif event and event.pressed and event.key_number != aw:
            error += 1
    count += 1
    print("#" + str(aw), hex(berry), count, watch, error, sep = " \t")
    macropad.pixels[aw] = 0x000000
```