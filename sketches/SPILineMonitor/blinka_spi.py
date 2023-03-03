#!/usr/bin/python3
import board, busio, digitalio, time, atexit
from PIL import Image

SPI = None

def main():
    global SPI
    print("[INFO]: <<<Blinka>>>")

    CE0 = digitalio.DigitalInOut(board.CE0)
    CE1 = digitalio.DigitalInOut(board.CE1)
    CE0.direction = digitalio.Direction.OUTPUT
    CE1.direction = digitalio.Direction.INPUT
    CE0.value = False

    SPI = busio.SPI(board.SCK, MOSI = board.MOSI, MISO = board.MISO)
    print("[INFO]:", SPI)

    print("[INFO]:", "Acquiring SPI Lock...")
    SPI.try_lock()
    print("[INFO]:", "SPI Lock Acquired")

    SPI.configure(baudrate = 100000)
    print("[INFO]:", "Frequency:", SPI.frequency, "baud")
    time.sleep(3)

    while True:
        n = 1
        read_buffer = bytearray(n)
        write_buffer = bytearray(n)
        write_buffer[0] = 0x7F
        SPI.write_readinto(write_buffer, read_buffer)
        print("[INFO]:", read_buffer)
        time.sleep(1)

def release():
    global SPI
    print("[INFO]:", "Releasing SPI Lock...")
    if SPI:
        SPI.unlock()
    print("[INFO]: Done!")

if __name__ == "__main__":
    atexit.register(release)
    try:
        main()
    except BaseException as error:
        print("\n[WARN]:", repr(error))
