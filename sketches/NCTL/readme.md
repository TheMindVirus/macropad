```py
# NCTL - TheMindVirus
# This sketch demonstrates the inner workings of a particular variant of logic unit
# which returns the truth tables of each of a set of 2-input 1-output logic blocks.

# NCTL - Normally Closed Transistor Logic (not-gate)
# NOTL - Normally Open Transistor Logic (half-and-gate-buffer)

# The design and pinout is akin to 74HC259N 8-bit Addressable Latched Multiplexers
# but with additional logic output which just happens to match the selected opcode

# The requested manufacturing process is translucent red perspex in DIP4/DIP8 x2
# essentially the same as Pimoroni Microdot (Lite-On LTP) each containing 1x RP2040

# Traits may be shared between this, Microchip ATtiny45 and Analog Devices MAX7219CNG
# where one is a microcontroller using minimal transistors and one is a 7-segment display driver

pinout_full = \
"""
  S0 - [01 16] - VCC
  S1 - [02 15] - C
  S2 - [03 14] - B
INVS - [04 13] - A
INVA - [05 12] - NOTA
INVB - [06 11] - NOTB
INVC - [07 10] - NOTC
 GND - [08 09] - NEN
"""

pinout_half = \
"""
  S0 - [01 08] - VCC
  S1 - [02 07] - C
  S2 - [03 06] - B
INVS - [04 05] - A
"""

layout_ext = \
"""
INVA - [01 08] - NOTA
INVB - [02 07] - NOTB
INVC - [03 06] - NOTC
 GND - [04 05] - NEN
"""

opcode_list = \
{
    0b0000: "NIL",  #0x0
    0b0001: "AND",  #0x1
    0b0010: "XB",   #0x2
    0b0011: "B",    #0x3
    0b0100: "XA",   #0x4
    0b0101: "A",    #0x5
    0b0110: "XOR",  #0x6
    0b0111: "OR",   #0x7
    0b1000: "NOR",  #0x8
    0b1001: "XNOR", #0x9
    0b1010: "NA",   #0xA
    0b1011: "XNA",  #0xB
    0b1100: "NB",   #0xC
    0b1101: "XNB",  #0xD
    0b1110: "NAND", #0xE
    0b1111: "ONE",  #0xF
}
    
def _nmap(a, b):
    return 0b1000 if not a and not b \
      else 0b0100 if a and not b \
      else 0b0010 if not a and b \
      else 0b0001 if a and b \
      else 0b0000

def __nint(i):
    return 0b1000 if i == 0 \
      else 0b0100 if i == 1 \
      else 0b0010 if i == 2 \
      else 0b0001 if i == 3 \
      else 0b0000#if i == -1

def _nint(i):
    i = __nint(i)
    return [0, 0] if i == 0b1000 \
      else [1, 0] if i == 0b0100 \
      else [0, 1] if i == 0b0010 \
      else [1, 1] if i == 0b0001 \
      else [0,-1]#if i == 0b0000

def NCTL(A, B, S, INVS = 0, VCC = 1):
    I = _nmap(A, B) ; M = 0b1000 if INVS else 0b0000
    C = 1 if (M | S & I) != 0 else 0
    return 0 if VCC < 1 else C if not INVS else not C

def NRAW(A, B, S):
    BUFA = A ; BUFB = B ; S = S if S < 8 else 23 - S
    OPPA = 0 if A else 1 ; OPPB = 0 if B else 1
    S0 = S & 1 ; S1 = (S >> 1) & 1 ; S2 = (S >> 2) & 1 ; INVS = (S >> 3) & 1
    OPPS0 = not S0 ; OPPS1 = not S1 ; OPPS2 = not S2 ; OPPINVS = not INVS
    OR1 = OPPS0 | S1 | S2 ; OR2 = S0 | OPPS1 | S2 ; OR3 = OPPS0 | OPPS1 | S2
    OR4 = S0 | S1 | OPPS2 ; OR5 = OPPS0 | S1 | OPPS2 ; OR6 = S0 | OPPS1 | OPPS2 ; OR7 = OPPS0 | OPPS1 | OPPS2
    OPPOR1 = not OR1 ; OPPOR2 = not OR2 ; OPPOR3 = not OR3
    OPPOR4 = not OR4 ; OPPOR5 = not OR5 ; OPPOR6 = not OR6 ; OPPOR7 = not OR7
    ABOR0 = BUFA | BUFB
    ABOR1 = OPPA | BUFB; NABOR1 = not ABOR1
    ABOR2 = BUFA | OPPB; NABOR2 = not ABOR2
    ABOR3 = OPPA | OPPB; NABOR3 = not ABOR3
    ABOR4 = NABOR2 | NABOR3 ; ABOR5 = NABOR1 | NABOR3 ; ABOR6 = NABOR1 | NABOR2
    TRIBUF1 = NABOR3 if OPPOR1 else 0
    TRIBUF2 = NABOR2 if OPPOR2 else 0
    TRIBUF3 =  ABOR4 if OPPOR3 else 0
    TRIBUF4 = NABOR1 if OPPOR4 else 0
    TRIBUF5 =  ABOR5 if OPPOR5 else 0
    TRIBUF6 =  ABOR6 if OPPOR6 else 0
    TRIBUF7 =  ABOR0 if OPPOR7 else 0
    ACC = TRIBUF1 | TRIBUF2 | TRIBUF3 | TRIBUF4 | TRIBUF5 | TRIBUF6 | TRIBUF7
    NACC = not ACC
    return int(ACC if not INVS else NACC)

def NITE(X = False, Y = False):
    for S in range(0, len(list(opcode_list.items()))):
        for I in range(0, 4):
            A, B = _nint(I)
            C = NRAW(A, B, S) if Y else NCTL(A, B, S) if not X else NCTL_EXT(A, B, S)
            print(opcode_list[S], A, B, "=>", C)

code = \
"""
int* NCTL_EXT
(
    int A, int B, int S, int INVS = 0, int VCC = 1,
    int INVA = 0, int INVB = 0, int INVC = 0, int GND = 0, int NEN = 0
)
{
    int R[] = { -1, -1, -1, -1 };
    if ((GND != 0) || (VCC != 1) || (NEN != 0)) { return R; }
    A = INVA ? !A : A; B = INVB ? !B : B;
    int C = NCTL(A, B, S, INVS, VCC);
    C = INVC ? !C : C;
    int R2[] = { C, !C, !B, !A }
    return R2;
}
"""
code = code.replace("int*", "def")
code = code.replace("int ", "")
code = code.replace("new ", "")
code = code.replace("||", "or")
code = code.replace("[]", "")
code = code.replace("{ -1, -1, -1, -1 }", "[ -1, -1, -1, -1 ]")
code = code.replace("{ C, !C, !B, !A }", "[ C, int(not C), int(not B), int(not A)]")
code = code.replace(" { ", ":\n        ")
code = code.replace("; }", "")
code = code.replace(";", "")
code = code.replace("INVA ? !A : A B = INVB ? !B : B", "A if not INVA else ~A ; B if not INVA else ~B")
code = code.replace("INVC ? !C : C", "C if not INVC else ~C")
code = code.replace(",\n    ", ", ")
code = code.replace("\n(\n    ", "(")
code = code.replace("\n)\n{", "):")
code = code.replace("}", "")
code = code.replace("!=", "__!=__")
code = code.replace("!", "~")
code = code.replace("__~=__", "!=")

test = True

if __name__ == "__main__":
    if test:
        NITE(Y = True)
    else:
        NITE()
        print(code)
        exec(code)
        NITE(X = True)
```