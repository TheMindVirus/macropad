# Cable Time Protocol [CTP]
# Cable Time Synchronisation Protocol [CTSP]

![screenshot](https://github.com/TheMindVirus/macropad/blob/archive/sketches/CableTimeProtocol/screenshot.png)

```
# Host Keeps Time & Date (it relies on NTP Server Sync or Atomic Clock Card)
# Host Sends Time & Date (challenging on OS's with exclusive mode COM or USB)
# Device Receives Time & Date (varies by implementation much like web server)

# Host Loses Power (Device has the wrong time until it can sync again)
# Device Loses Power (Device can easily request time again at boot)
# Requires Events on Host Boot + Device Boot + Sync Interval of ek minute (1)

# Not all devices will need it (e.g. LoRaWAN probably doesn't need it)
# USB devices should use Ethernet (but some devices only have UART CDC Drivers)
# Most USB devices don't have WiFi (some have RTC but is volatile on power loss)
```
## WARNING: This application requires to be run with Administrative Privileges.
## WARNING: This may disrupt communication with devices which don't support CTP!
## WARNING! THIS MAY BRICK YOUR CIRCUITPYTHON DEVICE!
```
# For RP2040, use the Pico CircuitPython build as a recovery image.
# No peripherals will light up but you may still get your data back.

# For other chips, use a Minimal CircuitPython build as a recovery image.
# Again, no peripherals will light up but the data may still be accessible over serial.

# Once you have finished recovering your data (if you needed to), remove the code.py
# and then you will be able to use BOOTSEL to switch back to your usual .uf2 image.
```
With any luck this shouldn't have to happen and this zero day may be fixed soon.
