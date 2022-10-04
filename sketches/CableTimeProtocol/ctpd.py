#Cable Time Protocol [CTP]
#Cable Time Synchronisation Protocol [CTSP]

# Host Keeps Time & Date (it relies on NTP Server Sync or Atomic Clock Card)
# Host Sends Time & Date (challenging on OS's with exclusive mode COM or USB)
# Device Receives Time & Date (varies by implementation much like web server)

# Host Loses Power (Device has the wrong time until it can sync again)
# Device Loses Power (Device can easily request time again at boot)
# Requires Events on Host Boot + Device Boot + Sync Interval of ek minute (1)

# Not all devices will need it (e.g. LoRaWAN probably doesn't need it)
# USB devices should use Ethernet (but some devices only have UART CDC Drivers)
# Most USB devices don't have WiFi (some have RTC but is volatile on power loss)

# WARNING: This application requires to be run with administrative privileges.
# WARNING: This may disrupt communication with devices which don't support CTP!

#pip install pyserial
import serial, sys, time

ports = \
{
    0: { "name": "COM6", "baud": 115200 },
}

while True:
    for port in ports:
        print("[INFO]: CTP Sync ({})".format(ports[port]["name"]))
        cable = None
        try:
            cable = serial.Serial(ports[port]["name"],
                                  ports[port]["baud"],
                                  timeout = 1, write_timeout = 1)
            if cable.is_open:
                cable.write(str(time.localtime()).encode())
                cable.close()
        except Exception as error:
            print("[WARN]: {} ({})".format(str(error), ports[port]["name"]),
                  file = sys.stderr)
            if cable and cable.is_open:
                cable.close()
    time.sleep(3)#60)

"""
#pip install pyusb
import usb, sys, time

IDs = \
{
    (0x239A, 0x8108)
}

while True:
    for device in usb.core.find(find_all = True):
        if ((device.idVendor, device.idProduct) in IDs):
            for config in device:
                for interface in config:
                    for endpoint in interface:
                        try:
                            addr = endpoint.bEndpointAddress
                            addrfmt = " (0x{:02X})".format(addr)
                            if usb.util.endpoint_direction(addr) == usb.util.ENDPOINT_OUT:
                                print("[INFO]: Output Endpoint Detected" + addrfmt)
                                endpoint.write(str(time.localtime()))
                            else:
                                raise Exception("Invalid Endpoint")
                        except Exception as error:
                            print("[WARN]: " + str(error) + addrfmt, file = sys.stderr)
    time.sleep(60)
"""
