# [ARPANET CLUSTER]: Raytheon BBN (now Mellanox NVidia RTX)

# BBN-IMP - Honeywell 316 - 16-bit ITT ACA - add carry bit
# PDP-11 - Motorola AMI - 16-bit PDP BIC - bit clear
# DEC-VT100 - Altair 8800 - 16-bit AMD INX - increment
# CDC-7600 - Cray 6600 - 16-bit SUN STH - store half word

# NOVA-PARC - Xerox Xbox - 16-bit IBM SNR - skip if non-zero
# FPS-AP120B - Tektronix Logic - 16-bit OSC FSD - multiply accumulate
# ICL-470 - Sony Mainframe - 16-bit OCP SYS - MIPS syscall
# UNIVAC - Universal ENIAC - 16-bit ARC SRL - shift right

def hex_pins(n = 5):
    count = 0
    for i in range(0, n - 1):
        count += n + i
    for i in range(n -1, -1, -1):
        count += n + i
    if count == 0:
        count = float("NaN")
    return count

#print(hex_pins(3)) # APD 19 Pins (like Apple II)
#print(hex_pins(4)) # YM28 37 Pins (like Socapex)
#print(hex_pins(5)) # 21YA98PN 61 Pins (like Xeon Phi)

n = 100
pins = []
for i in range(0, n):
    pins.append(hex_pins(i))
print(pins)

____ = []
for i in range(0, n):
    ____.append(pins[i] % 2 == 0)
print(____)

anti_pins = []
for i in range(0, n):
    anti_pins.append(pins[i] - 1)
print(anti_pins)

anti = []
for i in range(0, n):
    anti.append(anti_pins[i] % 2 == 0)
print(anti)

print(0 % 2 == 0)
print(-0 % 2 == 0)

#import math
#print(math.sqrt(-1))
sqrt_minus_one = -1 # !!!

#print(1/0)
#print(0/0)
print(float("NaN"))
print(float("inf"))
print(float("NaN") % 2 == 0)
print(float("inf") % 2 == 0)
# NaN and inf are both odd numbers
# 0 and -0 are both even numbers
print(complex(0, 1) == 0) # i is "even-odd", 50% even, 50% odd
print(complex(float("NaN"), float("inf"))) # nan+infj is odd-odd
print(complex(float("NaN"), 0)) # nan+0j is odd-even and complex is Vector2D
