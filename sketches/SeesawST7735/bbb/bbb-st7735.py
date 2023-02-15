#!/usr/bin/python3
#sudo pip3 install Adafruit_BBIO
import Adafruit_BBIO.GPIO as BBIO
import time

#P8 Header has too many MMC Memory Conflicts due to nearby interfering pins
#P9 Header has too many UART Serial Conflicts and UART2_RXD does not function

PIN_ST7735_GND = "P8_19"
PIN_ST7735_VCC = "P8_17"
PIN_ST7735_SCL = "P8_15"
PIN_ST7735_SDA = "P8_13"
PIN_ST7735_RES = "P8_11"
PIN_ST7735_DC = "P8_9"
PIN_ST7735_CS = "P8_7"
PIN_ST7735_BL = "P8_5"

PIN_ST7735_EXT = "P8_3"

BBIO.setup(PIN_ST7735_GND, BBIO.OUT)
BBIO.setup(PIN_ST7735_VCC, BBIO.OUT)
BBIO.setup(PIN_ST7735_SCL, BBIO.OUT)
BBIO.setup(PIN_ST7735_SDA, BBIO.OUT)
BBIO.setup(PIN_ST7735_RES, BBIO.OUT)
BBIO.setup(PIN_ST7735_DC, BBIO.OUT)
BBIO.setup(PIN_ST7735_CS, BBIO.OUT)

#BBIO.setup(PIN_ST7735_BL, BBIO.OUT)
#BBIO.setup(PIN_ST7735_EXT, BBIO.OUT)

BBIO.output(PIN_ST7735_GND, BBIO.LOW)
BBIO.output(PIN_ST7735_VCC, BBIO.LOW)
BBIO.output(PIN_ST7735_SCL, BBIO.LOW)
BBIO.output(PIN_ST7735_SDA, BBIO.LOW)
BBIO.output(PIN_ST7735_RES, BBIO.LOW)
BBIO.output(PIN_ST7735_DC, BBIO.LOW)
BBIO.output(PIN_ST7735_CS, BBIO.LOW)

#BBIO.output(PIN_ST7735_BL, BBIO.LOW)
#BBIO.output(PIN_ST7735_EXT, BBIO.LOW)

BBIO.output(PIN_ST7735_VCC, BBIO.HIGH)
BBIO.output(PIN_ST7735_RES, BBIO.HIGH)
#BBIO.output(PIN_ST7735_BL, BBIO.HIGH)

print("<<<BBIO>>>")

def test(pin = PIN_ST7735_VCC, ext = PIN_ST7735_VCC, sleep = 1):
    while True:
        BBIO.output(pin, BBIO.HIGH)
        BBIO.output(ext, BBIO.HIGH)
        print("On")
        time.sleep(sleep)
        BBIO.output(pin, BBIO.LOW)
        BBIO.output(ext, BBIO.LOW)
        print("Off")
        time.sleep(sleep)
#test(PIN_ST7735_VCC, PIN_ST7735_VCC)

#test(PIN_ST7735_BL, PIN_ST7735_EXT) # Do Not Use
#test(PIN_ST7735_GND, PIN_st7735_VCC) # Do Not Use

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
        BBIO.output(PIN_ST7735_SDA, BBIO.HIGH if (b & l) else BBIO.LOW)
        BBIO.output(PIN_ST7735_SCL, BBIO.HIGH)
        BBIO.output(PIN_ST7735_SCL, BBIO.LOW)
        b <<= 1

def send_command(cmd, addr = [], na = 0):
    BBIO.output(PIN_ST7735_CS, BBIO.LOW)
    BBIO.output(PIN_ST7735_DC, BBIO.LOW)
    spi_write(cmd, 8)
    BBIO.output(PIN_ST7735_DC, BBIO.HIGH)
    [spi_write(addr[i], 8) for i in range(0, na)]
    BBIO.output(PIN_ST7735_CS, BBIO.HIGH)

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
    BBIO.output(PIN_ST7735_RES, BBIO.LOW)
    time.sleep(0.1)
    BBIO.output(PIN_ST7735_RES, BBIO.HIGH)
    time.sleep(0.2)
    BBIO.output(PIN_ST7735_CS, BBIO.HIGH)
    start_display(Rcmd1)
    start_display(Rcmd2)
    start_display(Rcmd3)
    rotate_display(0)
    rotate_display(r)
    send_command(0x2C)
    BBIO.output(PIN_ST7735_CS, BBIO.LOW)

def write_pixel(b = display_palette["ST77XX_RED"]):
    for i in range(0, 16):
        BBIO.output(PIN_ST7735_SDA, BBIO.HIGH if (b & 0x8000) else BBIO.LOW)
        BBIO.output(PIN_ST7735_SCL, BBIO.HIGH)
        BBIO.output(PIN_ST7735_SCL, BBIO.LOW)
        b <<= 1

def fill_screen(b = display_palette["ST77XX_RED"]):
    for i in range(0, display_pixels):
        write_pixel(b)

print("[BOOT]: Enumerating Display...")
reset_display(1)

print("[WARN]: Commence Screen Blanking!")
fill_screen() # This might take a while through BBB GPIO/BBIO Abstraction...

print("[INFO]: 1 Frame(s) Rendered")
#print(dir(BBIO))

BBIO.cleanup()
