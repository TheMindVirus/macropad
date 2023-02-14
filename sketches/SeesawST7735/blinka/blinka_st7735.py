import board, digitalio, time
from PIL import Image

# Board uses BCM Standard instead of WiringPi Standard Pin Labelling
#PIN_ST7735_GND = board.pin9
PIN_ST7735_VCC = board.D17
PIN_ST7735_SCL = board.D27
PIN_ST7735_SDA = board.D22
#PIN_ST7735_RES = board.pin17
PIN_ST7735_DC = board.D10
PIN_ST7735_CS = board.D9
PIN_ST7735_BL = board.D11

# Board uses WiringPi Standard instead of BCM Standard Pin Labelling
"""
PIN_ST7735_VCC = board.D0
PIN_ST7735_SCL = board.D2
PIN_ST7735_SDA = board.D3

PIN_ST7735_DC = board.D12
PIN_ST7735_CS = board.D13
PIN_ST7735_BL = board.D14
"""

ST7735_VCC = digitalio.DigitalInOut(PIN_ST7735_VCC)
ST7735_SCL = digitalio.DigitalInOut(PIN_ST7735_SCL)
ST7735_SDA = digitalio.DigitalInOut(PIN_ST7735_SDA)

ST7735_DC = digitalio.DigitalInOut(PIN_ST7735_DC)
ST7735_CS = digitalio.DigitalInOut(PIN_ST7735_CS)
ST7735_BL = digitalio.DigitalInOut(PIN_ST7735_BL)

ST7735_VCC.direction = digitalio.Direction.OUTPUT
ST7735_SCL.direction = digitalio.Direction.OUTPUT
ST7735_SDA.direction = digitalio.Direction.OUTPUT

ST7735_DC.direction = digitalio.Direction.OUTPUT
ST7735_CS.direction = digitalio.Direction.OUTPUT
ST7735_BL.direction = digitalio.Direction.OUTPUT

ST7735_VCC.value = False
ST7735_SCL.value = False
ST7735_SDA.value = False

ST7735_DC.value = False
ST7735_CS.value = False
ST7735_BL.value = False

ST7735_VCC.value = True
ST7735_BL.value = True

print("<<<Blinka>>>")

#while True:
#    ST7735_BL.value = True
#    time.sleep(1)
#    ST7735_BL.value = False
#    time.sleep(1)

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
        ST7735_SDA.value = b & l
        ST7735_SCL.value = True
        ST7735_SCL.value = False
        b <<= 1

def send_command(cmd, addr = [], na = 0):
    ST7735_CS.value = False
    ST7735_DC.value = False
    spi_write(cmd, 8)
    ST7735_DC.value = True
    [spi_write(addr[i], 8) for i in range(0, na)]
    ST7735_CS.value = True

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
    ST7735_VCC.value = False
    time.sleep(0.1)
    ST7735_VCC.value = True
    time.sleep(0.2)
    ST7735_CS.value = True
    start_display(Rcmd1)
    start_display(Rcmd2)
    start_display(Rcmd3)
    rotate_display(0)
    rotate_display(r)
    send_command(0x2C)
    ST7735_CS.value = False

def write_pixel(b = display_palette["ST77XX_BLACK"]):
    for i in range(0, 16):
        ST7735_SDA.value = b & 0x8000
        ST7735_SCL.value = True
        ST7735_SCL.value = False
        b <<= 1

def fill_screen(b = display_palette["ST77XX_BLACK"]):
    for i in range(0, display_pixels):
        write_pixel(b)

def draw_image(filename = "splash.png"):
    x = 0
    y = 0
    w = display_width
    h = display_height
    img = Image.open(filename).resize((w, h)).getdata()
    for i in range(0, display_pixels):
        rgb = img[i] #16-bit RGB 5-6-5 Encoding
        raw = (int((rgb[0] * 32) / 256) << 11) \
            + (int((rgb[1] * 64) / 256) << 5) \
            + (int((rgb[2] * 32) / 256))
        write_pixel(raw)
        x += 1
        if x >= w:
            x = 0
            y += 1

print("Initialising Display")
reset_display(1)

print("Clearing Screen")
fill_screen() # This might take a while through blinka compatibility layer...

print("Blitting Image")
draw_image() # This might also take a while to decode splash.png...

print("Done!")
#print(dir(digitalio))
