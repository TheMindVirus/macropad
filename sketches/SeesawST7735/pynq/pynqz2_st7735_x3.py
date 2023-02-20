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
    pmoda_plug = PMODA_PLUG(base)
    pmodb_plug = PMODB_PLUG(base)
    raspberrypi_plug = RASPBERRYPI_PLUG(base)

    #base.select_arduino()
    base.select_pmoda()
    #base.select_pmodb()
    #base.select_rpi()

    arduino_thread = threading.Thread(target = arduino_runner, args = (arduino_plug,))
    pmoda_thread = threading.Thread(target = pmod_runner, args = (pmoda_plug,))
    pmodb_thread = threading.Thread(target = pmod_runner, args = (pmodb_plug,))
    raspberrypi_thread = threading.Thread(target = raspberrypi_runner, args = (raspberrypi_plug,))

    arduino_thread.start()
    pmoda_thread.start()
    pmodb_thread.start()
    raspberrypi_thread.start()

    launch_control = True

    #arduino_thread.join()
    #pmoda_thread.join()
    #pmodb_thread.join()
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

class PMODA_PLUG(ST7735_PLUG):
    def __init__(self, base):
        super().__init__()
        self.GND = pmod_io.Pmod_IO(base.iop_pmoda.mb_info, 0, "out")
        self.VCC = pmod_io.Pmod_IO(base.iop_pmoda.mb_info, 1, "out")
        self.SCL = pmod_io.Pmod_IO(base.iop_pmoda.mb_info, 2, "out")
        self.SDA = pmod_io.Pmod_IO(base.iop_pmoda.mb_info, 3, "out")
        self.RES = pmod_io.Pmod_IO(base.iop_pmoda.mb_info, 4, "out")
        self.DC = pmod_io.Pmod_IO(base.iop_pmoda.mb_info, 5, "out")
        self.CS = pmod_io.Pmod_IO(base.iop_pmoda.mb_info, 6, "out")
        self.BL = pmod_io.Pmod_IO(base.iop_pmoda.mb_info, 7, "out")

class PMODB_PLUG(ST7735_PLUG):
    def __init__(self, base):
        super().__init__()
        self.GND = pmod_io.Pmod_IO(base.iop_pmodb.mb_info, 0, "out")
        self.VCC = pmod_io.Pmod_IO(base.iop_pmodb.mb_info, 1, "out")
        self.SCL = pmod_io.Pmod_IO(base.iop_pmodb.mb_info, 2, "out")
        self.SDA = pmod_io.Pmod_IO(base.iop_pmodb.mb_info, 3, "out")
        self.RES = pmod_io.Pmod_IO(base.iop_pmodb.mb_info, 4, "out")
        self.DC = pmod_io.Pmod_IO(base.iop_pmodb.mb_info, 5, "out")
        self.CS = pmod_io.Pmod_IO(base.iop_pmodb.mb_info, 6, "out")
        self.BL = pmod_io.Pmod_IO(base.iop_pmodb.mb_info, 7, "out")

class RASPBERRYPI_PLUG(ST7735_PLUG):
    def __init__(self, base):
        super().__init__()

        self.address = rpi_io.MAILBOX_OFFSET + rpi_io.MAILBOX_PY2IOP_ADDR_OFFSET
        self.rpidata = rpi_io.MAILBOX_OFFSET + rpi_io.MAILBOX_PY2IOP_DATA_OFFSET
        self.command = rpi_io.MAILBOX_OFFSET + rpi_io.MAILBOX_PY2IOP_CMD_OFFSET

        self.gpio_base = rpi_io.RPI_DIO_BASEADDR + rpi_io.RPI_DIO_DATA_OFFSET
        self.tri_base = rpi_io.RPI_DIO_BASEADDR + rpi_io.RPI_DIO_TRI_OFFSET
        self.countdown = 10

        self.pi = rpi_io.Rpi(base.iop_rpi.mb_info,
            "/home/xilinx/microblaze/rpi_mailbox/rpi_mailbox.bin")
        self.pi.reset()
        self.pi.run()

        class custom_plug(PLUG):
           def __init__(self, instance, pin, direction, *args):
               self.instance = instance
               self.pin = pin
               self.direction = direction
               self.instance.gpio_mode(self.pin, self.direction)
           def read(self, *args):
               return self.instance.gpio_get(self.pin)
           def write(self, state, *args):
               self.instance.gpio_set(self.pin, state)

        self.VCC = custom_plug(self, 17, "out")
        self.SCL = custom_plug(self, 27, "out")
        self.SDA = custom_plug(self, 22, "out")

        self.DC = custom_plug(self, 10, "out")
        self.CS = custom_plug(self, 9, "out")
        self.BL = custom_plug(self, 11, "out")

    def idle_check(self):
        self.countdown = 10
        while ((self.pi.read(self.command) != 0x2) and (self.countdown > 0)):
            time.sleep(0.001)
            self.countdown -= 1
        return self.countdown

    def mbox_get(self, address):
        self.pi.write(self.address, address)
        self.pi.write(self.command, rpi_io.READ_CMD)
        if (self.idle_check() != 0):
            return self.pi.read(self.rpidata)
        else:
            return 0x00000000

    def mbox_set(self, address, rpidata):
        self.pi.write(self.address, address)
        self.pi.write(self.rpidata, rpidata)
        self.pi.write(self.command, rpi_io.WRITE_CMD)
        return self.idle_check()

    def gpio_mode(self, pin, direction = "out"):
        tmp = self.mbox_get(self.tri_base)
        if direction == "out":
            tmp &= 0xFFFFFFFF ^ (1 << pin)
        elif direction == "in":
            tmp |= 0x00000000 ^ (1 << pin)
        self.mbox_set(self.tri_base, tmp)

    def gpio_get(self, pin):
        tmp = self.mbox_get(self.gpio_base)
        return not ((tmp >> pin) & 1)

    def gpio_set(self, pin, value):
        tmp = self.mbox_get(self.gpio_base)
        if value:
            tmp |= (1 << pin)
        else:
            tmp &= 0xFFFFFFFF ^ (1 << pin)
        self.mbox_set(self.gpio_base, tmp)

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
