#!/usr/bin/python3
#pip3 install pyserial
import serial, time

pad = serial.Serial("/dev/ttyACM0", 115200)
if not pad.is_open:
    pad.open()
#pad.write(b"\xFF\xEC\r\n")
pad.write(b"\x03\r\n")
time.sleep(1)
pad.write(b"\x04\r\n")
