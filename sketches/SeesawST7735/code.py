import board, time
from adafruit_macropad import MacroPad
from adafruit_seesaw.seesaw import Seesaw

#https://learn.adafruit.com/adafruit-attiny817-seesaw/circuitpython

macropad = MacroPad()
seesaw = Seesaw(board.I2C())

ST7735_GND = 2
ST7735_VCC = 3
ST7735_SCL = 20
ST7735_SDA = 5
ST7735_RES = 6
ST7735_DC = 7
ST7735_CS = 8
ST7735_BL = 9

seesaw.pin_mode(ST7735_GND, seesaw.OUTPUT)
seesaw.pin_mode(ST7735_VCC, seesaw.OUTPUT)
seesaw.pin_mode(ST7735_SCL, seesaw.OUTPUT)
seesaw.pin_mode(ST7735_SDA, seesaw.OUTPUT)
seesaw.pin_mode(ST7735_RES, seesaw.OUTPUT)
seesaw.pin_mode(ST7735_DC, seesaw.OUTPUT)
seesaw.pin_mode(ST7735_CS, seesaw.OUTPUT)
seesaw.pin_mode(ST7735_BL, seesaw.OUTPUT)

seesaw.digital_write(ST7735_GND, False)
seesaw.digital_write(ST7735_VCC, False)
seesaw.digital_write(ST7735_SCL, False)
seesaw.digital_write(ST7735_SDA, False)
seesaw.digital_write(ST7735_RES, False)
seesaw.digital_write(ST7735_DC, False)
seesaw.digital_write(ST7735_CS, False)
seesaw.digital_write(ST7735_BL, False)

seesaw.digital_write(ST7735_VCC, True)
seesaw.digital_write(ST7735_BL, True)

print("<<<Seesaw>>>")

#while True:
#    seesaw.digital_write(ST7735_BL, True)
#    time.sleep(1)
#    seesaw.digital_write(ST7735_BL, False)
#    time.sleep(1)

#import displayio, busio
#from adafruit_st7735 import ST7735

#ST7735_SPI = busio.SPI()

#displayio.release_displays()
#display_bus = displayio.FourWire()
#microcontroller.Pin assumes that the GPIO pins are directly attached to the microcontroller

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

seesaw_display_width = 160
seesaw_display_height = 128
seesaw_display_pixels = seesaw_display_width * seesaw_display_height

seesaw_display_palette = \
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

rotation = \
[
    [0x40 | 0x80 | 0x00],
    [0x80 | 0x20 | 0x00],
    [0x00 | 0x00 | 0x00],
    [0x40 | 0x20 | 0x00],
]

def seesaw_spi_write(b, bits = 16):
    l = 1 << (bits - 1)
    for i in range(0, bits):
        seesaw.digital_write(ST7735_SDA, b & l)
        seesaw.digital_write(ST7735_SCL, True)
        seesaw.digital_write(ST7735_SCL, False)
        b <<= 1

def seesaw_send_command(cmd, addr = [], na = 0):
    seesaw.digital_write(ST7735_CS, False)
    seesaw.digital_write(ST7735_DC, False)
    seesaw_spi_write(cmd, 8)
    seesaw.digital_write(ST7735_DC, True)
    [seesaw_spi_write(addr[i], 8) for i in range(0, na)]
    seesaw.digital_write(ST7735_CS, True)

def seesaw_start_display(commands = []):
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
        seesaw_send_command(cmd, commands[idx:idx + na], na)
        idx += na
        if ms:
            ms = commands[idx]
            idx += 1
            if ms == 0xFF:
                ms = 500
            time.sleep(ms * 0.001)

def seesaw_rotate_display(r = 0):
    seesaw_send_command(0x36, rotation[r % 4], 1)

def seesaw_reset_display(r = 0):
    #seesaw.digital_write(ST7735_DC, True)
    seesaw.digital_write(ST7735_SDA, False)
    seesaw.digital_write(ST7735_SCL, False)
    seesaw.digital_write(ST7735_RES, True)
    time.sleep(0.1)
    seesaw.digital_write(ST7735_RES, False)
    time.sleep(0.1)
    seesaw.digital_write(ST7735_RES, True)
    time.sleep(0.2)
    seesaw.digital_write(ST7735_CS, True)
    seesaw_start_display(Rcmd1)
    seesaw_start_display(Rcmd2)
    seesaw_start_display(Rcmd3)
    seesaw_rotate_display(0)
    seesaw_rotate_display(r)
    seesaw_send_command(0x2C)
    seesaw.digital_write(ST7735_CS, False)

def seesaw_write_pixel(b = seesaw_display_palette["ST77XX_WHITE"]):
    for i in range(0, 16):
        seesaw.digital_write(ST7735_SDA, b & 0x8000)
        seesaw.digital_write(ST7735_SCL, True)
        seesaw.digital_write(ST7735_SCL, False)
        b <<= 1

def seesaw_fill_screen(b = seesaw_display_palette["ST77XX_WHITE"]):
    #seesaw.digital_write(ST7735_DC, True)
    #seesaw.digital_write(ST7735_CS, False)
    x = 0
    y = 0
    w = seesaw_display_width
    h = seesaw_display_height
    for i in range(0, seesaw_display_pixels):
        x += 1
        if x >= w:
            x = 0
            y += 1
        seesaw_write_pixel(x + y)
        #seesaw_write_pixel(int((x / w) * 0xFF))
    #seesaw.digital_write(ST7735_CS, True)

print("Starting Display")
seesaw_reset_display(3)

print("Drawing to Screen")
seesaw_fill_screen() # This might take a while through seesaw stock firmware...

print("Blitting Complete")
#print(dir(seesaw))

while True:
    time.sleep(1)