#from Maix import freq
#print(dir(freq))
#freq.set(400, 400) # No Other Frequency Is Supported
#print("[INFO]: CPU: {:0.2}MHz".format(freq.get_cpu()))
#print("[INFO]: KPU: {:0.2}MHz".format(freq.get_kpu()))

import time
from fpioa_manager import fm
from Maix import GPIO
#from machine import SPI

# IO14/GPIO6 jumped to pin 1 so it powers pin 17
# on Seeed Studio Grove AI HAT only

ST7735_VCC = 30 #17
ST7735_SCL = 19 #27
ST7735_SDA = 18 #22

ST7735_RES = 14 #6

ST7735_DC = 28 #10
ST7735_CS = 26 #9
ST7735_BL = 27 #11

fm.register(ST7735_VCC, fm.fpioa.GPIOHS1, force = True)
fm.register(ST7735_SCL, fm.fpioa.GPIOHS2, force = True)
fm.register(ST7735_SDA, fm.fpioa.GPIOHS3, force = True)

fm.register(ST7735_RES, fm.fpioa.GPIOHS4, force = True)

fm.register(ST7735_DC, fm.fpioa.GPIOHS5, force = True)
fm.register(ST7735_CS, fm.fpioa.GPIOHS6, force = True)
fm.register(ST7735_BL, fm.fpioa.GPIOHS7, force = True)

vcc = GPIO(GPIO.GPIOHS1, GPIO.OUT)
scl = GPIO(GPIO.GPIOHS2, GPIO.OUT)
sda = GPIO(GPIO.GPIOHS3, GPIO.OUT)

res = GPIO(GPIO.GPIOHS4, GPIO.OUT)

dc = GPIO(GPIO.GPIOHS5, GPIO.OUT)
cs = GPIO(GPIO.GPIOHS6, GPIO.OUT)
bl = GPIO(GPIO.GPIOHS7, GPIO.OUT)

vcc.value(0)
scl.value(0)
sda.value(0)

res.value(0)

dc.value(0)
cs.value(0)
bl.value(0)

vcc.value(1)
res.value(1)
bl.value(1)

print("<<<MaixPy>>>")

#while True:
#    bl.value(1)
#    time.sleep(1)
#    bl.value(0)
#    time.sleep(1)

#spi = SPI(SPI.SPI1, mode = SPI.MODE_MASTER,
#          baudrate = 10000000, polarity = 0,
#          phase = 0, bits = 8, firstbit = SPI.MSB)

#cs.value(0)
#spi.write(0xFF)
#cs.value(1)

Rcmd1 = \
[
    0x0F,
    0x01, 0x80, 0x96,
    0x11, 0x80, 0xFF,
    0xB1, 0x03, 0x01, 0x2C, 0x2D,
    0xB2, 0x03, 0x01, 0x2C, 0x2D,
    0xB3, 0x06, 0x01, 0x2C, 0x2D, 0x01, 0x2C, 0x2D,
    0xB4, 0x01, 0x07,
    0xC0, 0x03, 0xA2, 0x02, 0x84,
    0xC1, 0x01, 0xC5,
    0xC2, 0x02, 0x0A, 0x00,
    0xC3, 0x02, 0x8A, 0x2A,
    0xC4, 0x02, 0x8A, 0xEE,
    0xC5, 0x01, 0x0E,
    0x20, 0x00,
    0x36, 0x01, 0xC8,
    0x3A, 0x01, 0x05
]

Rcmd2 = \
[
    0x02,
#    0x2A, 0x04, 0x00, 0x02, 0x00, (0x7F + 0x02),
#    0x2B, 0x04, 0x00, 0x01, 0x00, (0x9F + 0x01)
    0x2A, 0x04, 0x00, 0x01, 0x00, (0x9F + 0x01),
    0x2B, 0x04, 0x00, 0x02, 0x00, (0x7F + 0x02)
]

Rcmd3 = \
[
    0x04,
    0xE0, 0x10, 0x02, 0x1C, 0x07, 0x12, 0x37, 0x32, 0x29, 0x2D, 0x29, 0x25, 0x2B, 0x39, 0x00, 0x01, 0x03, 0x10,
    0xE1, 0x10, 0x03, 0x1D, 0x07, 0x06, 0x2E, 0x2C, 0x29, 0x2D, 0x2E, 0x2E, 0x37, 0x3F, 0x00, 0x00, 0x02, 0x10,
    0x13, 0x80, 0x0A,
    0x29, 0x80, 0x64
]

display_width = 160
display_height = 128
display_pixels = display_width * display_height

display_palette = \
{
    "ST77XX_BLACK":   0x0000,
    "ST77XX_WHITE":   0xFFFF,
    "ST77XX_RED":     0xF800,
    "ST77XX_GREEN":   0x07E0,
    "ST77XX_BLUE":    0x001F,
    "ST77XX_CYAN":    0x07FF,
    "ST77XX_MAGENTA": 0xF81F,
    "ST77XX_YELLOW":  0xFFE0,
    "ST77XX_ORANGE":  0xFC00,
}

display_rotation = \
[
    [0x40 | 0x80 | 0x00],
    [0x80 | 0x20 | 0x00],
    [0x00 | 0x00 | 0x00],
    [0x40 | 0x20 | 0x00],
]

def spi_write(b, bits = 16):
    l = 1 << (bits - 1)
    for i in range(0, bits):
        sda.value((b & l))
        scl.value(1)
        scl.value(0)
        b <<= 1

def send_command(cmd, addr = [], na = 0):
    cs.value(0)
    dc.value(0)
    spi_write(cmd, 8)
    dc.value(1)
    [spi_write(addr[i], 8) for i in range(0, na)]
    cs.value(1)

def start_display(commands = []):
    idx = 0
    nc = commands[idx]
    idx += 1
    for i in range(0, nc):
        cmd = commands[idx]
        idx += 1
        na = commands[idx]
        idx += 1
        ms = na & 0x80
        na &= 0x7F
        send_command(cmd, commands[idx:idx + na], na)
        idx += na
        if ms:
            ms = commands[idx]
            idx += 1
            if ms == 0xFF:
                ms = 500
            time.sleep(ms * 0.001)

def rotate_display(r = 0):
    send_command(0x36, display_rotation[r % 4], 1)

def reset_display(r = 0):
    res.value(0)
    time.sleep(0.1)
    res.value(1)
    time.sleep(0.2)
    cs.value(1)
    start_display(Rcmd1)
    start_display(Rcmd2)
    start_display(Rcmd3)
    rotate_display(0)
    rotate_display(r)
    send_command(0x2C)
    cs.value(0)

def write_pixel(b = display_palette["ST77XX_RED"]):
    for i in range(0, 16):
        sda.value((b & 0x8000))
        scl.value(1)
        scl.value(0)
        b <<= 1

def fill_screen(b = display_palette["ST77XX_RED"]):
    for i in range(0, display_pixels):
        write_pixel(b)

print("Initialising the Display")
reset_display(1)

print("Filling the Screen")
fill_screen() # This might take a while through fpioa gpio matrix...

print("Done!")
#print(dir(Maix))
