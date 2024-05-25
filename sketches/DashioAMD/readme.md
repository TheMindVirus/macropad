# dashio

Based on DASH by DMTF as implemented on select AMD PRO chipsets \
alongside IPMI system management firmware by Realtek, Qualcomm and Mediatek \
as found on ASPEED BMC, Intel AMT, NVidia SMBus, Dell iDRAC and ASUS iKVM.

```py
import dashio

def help():
    print()
    print("[_SYS]:", "dashio.system:", dashio.system, "\n")
    print("[THRM]:", "dashio.thermal:", dashio.thermal, "\n")
    print("[ASET]:", "dashio.asset:", dashio.asset, "\n")
    print("[_MEM]:", "dashio.memory:", dashio.memory, "\n")
    print("[CORE]:", "dashio.core:", dashio.core, "\n")
    print("[CHIP]:", "dashio.chips:", dashio.chips, "\n")
    print("[_PWR]:", "dashio.power:", dashio.power, "\n")
    print("[SNSR]:", "dashio.sensor:", dashio.sensor, "\n")
    print("[APPS]:", "dashio.apps:", dashio.apps, "\n")
    print("[BOOT]:", "dashio.boot:", dashio.boot, "\n")
    print("[USER]:", "dashio.user:", dashio.user, "\n")
    print("[MISC]:", "dashio.misc:", dashio.misc, "\n")
    print("[_AUX]:", "dashio.aux:", dashio.aux, "\n")
    print("[BATT]:", "dashio.battery:", dashio.battery, "\n")
    print("[BIOS]:", "dashio.bios:", dashio.bios, "\n")
    print("[DHCP]:", "dashio.dhcp:", dashio.dhcp, "\n")
    print("[_DNS]:", "dashio.dns:", dashio.dns, "\n")
    print("[_IP_]:", "dashio.ip:", dashio.ip, "\n")
    print("[_NET]:", "dashio.net:", dashio.net, "\n")
    print("[MGMT]:", "dashio.mgmt:", dashio.mgmt, "\n")
    print("[_OS_]:", "dashio.os:", dashio.os, "\n")
    print("[TERM]:", "dashio.console:", dashio.console, "\n")
    print("[_DEV]:", "dashio.device:", dashio.device, "\n")
    print("[MDIA]:", "dashio.media:", dashio.media, "\n")
    print("[_ETH]:", "dashio.ethernet:", dashio.ethernet, "\n")
    print("[PROF]:", "dashio.profile:", dashio.profile, "\n")
    print("[FLTR]:", "dashio.filter:", dashio.filter, "\n")
    print("[ALRT]:", "dashio.alert:", dashio.alert, "\n")
    print("[_LX_]:", "dashio.lights:", dashio.lights, "\n")
    print("dashio.")

help()
while True:
    try:
        io = input(">>> ")
        try:
            print(eval(io))
        except:
            exec(io)
    except Exception as error:
        print("dashio:", error)
```

More Details: https://github.com/juergh/dash-sdk
