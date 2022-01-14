# VT-100 Teletext for Ceefax - Alastair Cota
# Included in this package is a very minimal definition of some common VT-100 Escape Sequences known by PuTTY
# and most Standard High-Level Serial Graphical Terminal Apps. Make your own Teletext Pages such as BBC CeeFax.

import sys, vt100

print(vt100.bell + vt100.reset)

print(vt100.bg_black + vt100.red +"RED" + vt100.reset)
print(vt100.bg_black + vt100.green + "GREEN" + vt100.reset)
print(vt100.bg_black + vt100.blue + "BLUE" + vt100.reset)

print(vt100.bg_white + vt100.red +"RED" + vt100.reset)
print(vt100.bg_white + vt100.green + "GREEN" + vt100.reset)
print(vt100.bg_white + vt100.blue + "BLUE" + vt100.reset)

print(vt100.bg_red + vt100.white + "RED" + vt100.reset)
print(vt100.bg_green + vt100.white + "GREEN" + vt100.reset)
print(vt100.bg_blue + vt100.white + "BLUE" + vt100.reset)

print(vt100.bg_red + vt100.black + "RED" + vt100.reset)
print(vt100.bg_green + vt100.black + "GREEN" + vt100.reset)
print(vt100.bg_blue + vt100.black + "BLUE" + vt100.reset)

print(vt100.bg_black + vt100.red +"RED" + vt100.reset)
print(vt100.bg_black + vt100.green + "GREEN" + vt100.reset)
print(vt100.bg_black + vt100.blue + "BLUE" + vt100.reset)

for x in range(0, 100):
    for y in range(0, 100):
        sys.stdout.write(vt100.cursor(x, y) + vt100.bg_blue + " " + vt100.reset)
print()

import shader
shader.main()
