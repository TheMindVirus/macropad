# WARNING! THIS MAY BRICK YOUR CIRCUITPYTHON DEVICE!

# For RP2040, use the Pico CircuitPython build as a recovery image.
# No peripherals will light up but you may still get your data back.

# For other chips, use a Minimal CircuitPython build as a recovery image.
# Again, no peripherals will light up but the data may still be accessible over serial.

# Once you have finished recovering your data (if you needed to), remove the code.py
# and then you will be able to use BOOTSEL to switch back to your usual .uf2 image.

# With any luck this shouldn't have to happen and this zero day may be fixed soon.

import usb_cdc, rtc, sys, time

usb_cdc.console.timeout = 1

def try_get(data, label):
    try:
        offset = data.find(label)
        if not offset:
            raise
        offset += len(label)
        start = data.find("=", offset)
        if not start:
            start = data.find(":", offset)
            if not start:
                raise
        start += 1
        end = data.find(",", start)
        if not end:
            end = data.find(")", start)
            if not end:
                raise
        result = int(data[start:end].replace(" ", ""))
        return result
    except:
        return 0

class rtcdata:
    def __init__(self, ctp):
        self.ctp = ctp
    @property
    def datetime(self):
        return self.ctp

while True:
    try:
    	msg = usb_cdc.console.read(4096)
        #msg = "struct_time(tm_year=2020, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=11, tm_sec=44, tm_wday=2, tm_yday=1, tm_isdst=-1)"
        if msg:
            print(msg)
            """
            ctp = (try_get(msg, "tm_year"),
                   try_get(msg, "tm_mon"),
                   try_get(msg, "tm_mday"),
                   try_get(msg, "tm_hour"),
                   try_get(msg, "tm_min"),
                   try_get(msg, "tm_sec"),
                   try_get(msg, "tm_wday"),
                   try_get(msg, "tm_yday"),
                   try_get(msg, "tm_isdst"))
    	    print(ctp)
            rtc.set_time_source(rtcdata(ctp)) # WARNING! Potential Zero Day Security Risk!
            print(time.localtime())
            """
        else:
            print("No Response...")
        time.sleep(1)
    except Exception as error:
        print(error)
        time.sleep(1)
