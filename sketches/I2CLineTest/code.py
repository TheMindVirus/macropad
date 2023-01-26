# I2C Line Tester - Alastair Cota
# This sketch tests the quality of the GPIO connection on the pins used
# by your I2C devices by pulsing them on and off to check for a response.

# This code is intended for the MacroPad RP2040

import board, digitalio, time

clk = digitalio.DigitalInOut(board.SCL)
dat = digitalio.DigitalInOut(board.SDA)
clk.direction = digitalio.Direction.OUTPUT
dat.direction = digitalio.Direction.OUTPUT # Optionally change to Input
def test():
    clk.value = True
    dat.value = True
    time.sleep(1)
    clk.value = False
    dat.value = False

### Ctrl-D to Pause and Any Key to Enter REPL
# from code import *
# test()
### OR
# import code
# code.test()
### Ctrl-D to restart and return to code.py