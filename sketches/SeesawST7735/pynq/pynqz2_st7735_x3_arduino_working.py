#!/usr/bin/python3
from pynq.overlays.base import BaseOverlay
from pynq.lib.arduino import arduino_io
from pynq.lib.pmod import pmod_io
import pynq.lib.rpi as rpi_io
import threading, time, sys

launch_control = False

def arduino_runner(plug):
    global launch_control
    while not launch_control:
        pass
    reset_display(plug)
    fill_screen(plug)

def pmod_runner(plug):
    global launch_control
    while not launch_control:
        pass
    reset_display(plug)
    fill_screen(plug)

def raspberrypi_runner(plug):
    global launch_control
    while not launch_control:
        pass
    reset_display(plug)
    fill_screen(plug)

def main():
    global launch_control
    print("[INFO]: Loading Base Overlay...")
    base = BaseOverlay("base.bit")
    print("[INFO]: Initialising Display...")

    arduino_plug = ARDUINO_PLUG(base)
    pmod_plug = PMOD_PLUG(base)
    raspberrypi_plug = RASPBERRYPI_PLUG(base)

    arduino_thread = threading.Thread(target = arduino_runner, args = (arduino_plug,))
    pmod_thread = threading.Thread(target = pmod_runner, args = (pmod_plug,))
    raspberrypi_thread = threading.Thread(target = raspberrypi_runner, args = (raspberrypi_plug,))

    arduino_thread.start()
    pmod_thread.start()
    raspberrypi_thread.start()

    launch_control = True

    #arduino_thread.join()
    #pmod_thread.join()
    #raspberrypi_thread.join()

    print("[INFO]: Done!")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        sys.exit(0)

class PLUG:
    def read(self, *args, **kwargs):
        pass
    def write(self, *args, **kwargs):
        pass

class ST7735_PLUG:
    def __init__(self):
        self.GND = PLUG()
        self.VCC = PLUG()
        self.SCL = PLUG()
        self.SDA = PLUG()
        self.RES = PLUG()
        self.DC = PLUG()
        self.CS = PLUG()
        self.BL = PLUG()

class ARDUINO_PLUG(ST7735_PLUG):
    def __init__(self, base):
        super().__init__()
        self.GND = arduino_io.Arduino_IO(base.iop_arduino.mb_info, 7, "out")
        self.VCC = arduino_io.Arduino_IO(base.iop_arduino.mb_info, 6, "out")
        self.SCL = arduino_io.Arduino_IO(base.iop_arduino.mb_info, 5, "out")
        self.SDA = arduino_io.Arduino_IO(base.iop_arduino.mb_info, 4, "out")
        self.RES = arduino_io.Arduino_IO(base.iop_arduino.mb_info, 3, "out")
        self.DC = arduino_io.Arduino_IO(base.iop_arduino.mb_info, 2, "out")
        self.CS = arduino_io.Arduino_IO(base.iop_arduino.mb_info, 1, "out")
        self.BL = arduino_io.Arduino_IO(base.iop_arduino.mb_info, 0, "out")

class PMOD_PLUG(ST7735_PLUG):
    def __init__(self, base):
        super().__init__()
        #self.GND = None
        #self.VCC = None
        #self.SCL = None
        #self.SDA = None
        #self.RES = None
        #self.DC = None
        #self.CS = None
        #self.BL = None

class RASPBERRYPI_PLUG(ST7735_PLUG):
    def __init__(self, base):
        super().__init__()
        #self.GND = None
        #self.VCC = None
        #self.SCL = None
        #self.SDA = None
        #self.RES = None
        #self.DC = None
        #self.CS = None
        #self.BL = None

display_width = 160
display_height = 128
display_pixels = display_width * display_height

display_boot = \
[
    0x18,
    0x11, 0x80, 0x96,
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
    0x3A, 0x01, 0x05,
    0x2A, 0x04, 0x00, 0x01, 0x00, 0xA0,
    0x2B, 0x04, 0x00, 0x02, 0x00, 0x81,
    0xE0, 0x10, 0x02, 0x1C, 0x07, 0x12, 0x37, 0x32, 0x29, 0x2D, 0x29, 0x25, 0x2B, 0x39, 0x00, 0x01, 0x03, 0x10,
    0xE1, 0x10, 0x03, 0x1D, 0x07, 0x06, 0x2E, 0x2C, 0x29, 0x2D, 0x2E, 0x2E, 0x37, 0x3F, 0x00, 0x00, 0x02, 0x10,
    0x13, 0x80, 0x0A,
    0x29, 0x80, 0x64,
    0x36, 0x01, 0xC0,
    0x36, 0x01, 0xA0,
    0x2C, 0x00
]

def SPI_write(plug, B, bits = 16):
    L = 1 << (bits - 1)
    for i in range(0, bits):
        plug.SDA.write(1 if B & L else 0)
        plug.SCL.write(1)
        plug.SCL.write(0)
        B <<= 1

def send_command(plug, cmd, addr = [], na = 0):
    plug.CS.write(0)
    plug.DC.write(0)
    SPI_write(plug, cmd, 8)
    plug.DC.write(1)
    [SPI_write(plug, addr[i], 8) for i in range(0, na)]
    plug.CS.write(1)

def start_display(plug, commands = []):
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
        send_command(plug, cmd, commands[idx:idx + na], na)
        idx += na
        if ms:
            ms = commands[idx]
            idx += 1
            if ms == 0xFF:
                ms = 500
            time.sleep(ms * 0.001)

def reset_display(plug):
    plug.GND.write(0)
    plug.VCC.write(0)
    plug.SCL.write(0)
    plug.SDA.write(0)
    plug.RES.write(0)
    plug.DC.write(0)
    plug.CS.write(0)
    plug.BL.write(0)

    plug.VCC.write(1)
    plug.BL.write(1)

    plug.RES.write(1)
    time.sleep(0.1)
    plug.RES.write(0)
    time.sleep(0.1)
    plug.RES.write(1)
    time.sleep(0.2)

    plug.CS.write(1)
    start_display(plug, display_boot)
    plug.CS.write(0)

def fill_screen(plug, chroma = 0xF800):
    for i in range(0, display_pixels):
        SPI_write(plug, chroma, 16)

if __name__ == "__main__":
    main()
