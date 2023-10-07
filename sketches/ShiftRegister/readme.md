```py
# Seesaw DigitalIO Shift Register - Take a wild guess
# This sketch tests DigitalIO through Seesaw I2C
# and Texas Instruments Shift Register IC SN74HC595N 

# https://docs.circuitpython.org/projects/seesaw/en/stable/api.html#adafruit_seesaw.seesaw.Seesaw

# VCC -> 3V -> SRCLR
# GND -> G
# 12 -> RCLK -> SRCLK
# 13 -> SER

test_mode = False
#test_mode = True

code = \
"""
import board, busio, time
from adafruit_seesaw import seesaw as seesaw_i2c

i2c = busio.I2C(board.SCL, board.SDA)
#i2c.try_lock()

seesaw = seesaw_i2c.Seesaw(i2c, addr = 0x49)
seesaw.sw_reset()
print("[INFO]: Seesaw Version:", seesaw.get_version())

seesaw.pin_mode(12, seesaw.OUTPUT)
seesaw.pin_mode(13, seesaw.OUTPUT)

seesaw.digital_write(12, False)
seesaw.digital_write(13, False)

def o():
    while True:
        try:
            seesaw.digital_write(13, True)
            time.sleep(0.1)
            seesaw.digital_write(12, True)
            time.sleep(0.1)
            seesaw.digital_write(12, False)
            print("on")
            time.sleep(0.5)
            seesaw.digital_write(13, False)
            time.sleep(0.1)
            seesaw.digital_write(12, True)
            time.sleep(0.1)
            seesaw.digital_write(12, False)
            print("off")
            time.sleep(0.5)
        except Exception as error:
            print(error)
            #yield
            pass
o()

#i2c.unlock()
#i2c.deinit()

"""

test = \
"""
import board, busio, time

seesaw = busio.I2C(board.SCL, board.SDA)
seesaw.try_lock()

devices = seesaw.scan()
address = [hex(a) for a in devices]
print(address)

data = []
for i in devices:
    try:
        buffer = bytearray()
        seesaw.readfrom_into(i, buffer)
        data.append(buffer)
    except:
        buffer = bytearray()
        data.append(buffer)
print(data)

seesaw.unlock()
seesaw.deinit()
"""

if test_mode:
    exec(test)
else:
    exec(code)
```