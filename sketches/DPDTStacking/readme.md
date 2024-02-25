```py
# DPDT Stacking - TheMindVirus
# This sketch simulates a stack of Double-Pole-Double-Throw (DPDT) crossover light-switches/relays.
# The expected output state is predicted by the parity number of ones (mod 2 of on-state switches).

# (e.g.): Chain 4x DPDT Crossover Switch together into a ladder and power one side (with a separate ground).
#         On the output side you should see the same signal if there was an odd number of on-state switches.
#         If there was an even number of on-state switches then the signal would be swapped around.

# CS:    [=|=]     [=|=]     [=|=]     [=|=]           
#          |         |         |         |             
# AI -1-[=\|/=]---[=\|/=]---[=\|/=]---[=\|/=]-0- AO    
#       [  X  ]   [  X  ]   [  X  ]   [  X  ]          
# BI -0-[=/ \=]---[=/ \=]---[=/ \=]---[=/ \=]-1- BO --\
#                                                     |
# GND ----------------------------------------- LED --/

class DPDT:
    def __init__(self):
        self.AI = 0
        self.BI = 0
        self.AO = 0
        self.BO = 0
        self.CS = 0
        self._strtype = type(str())

    def toggle(self):
        self.CS = 1 - self.CS

    def run(self):
        if self.CS:
            self.AO = self.BI
            self.BO = self.AI
        else:
            self.AO = self.AI
            self.BO = self.BI

    def __repr__(self):
        return "[" + str(self.AI) + \
               "," + str(self.BI) + \
               "," + str(self.AO) + \
               "," + str(self.BO) + \
               "]" + str(self.CS)

    def __setitem__(self, index, value):
        if (type(index) != self._strtype):
            print(type(index))
            index %= 4
        if index == 0 or (type(index) == self._strtype and index.upper() == "AI"):
            self.AI = value
        if index == 1 or (type(index) == self._strtype and index.upper() == "BI"):
            self.BI = value
        if index == 2 or (type(index) == self._strtype and index.upper() == "AO"):
            self.AO = value
        if index == 3 or (type(index) == self._strtype and index.upper() == "BO"):
            self.BO = value
        if               (type(index) == self._strtype and index.upper() == "CS"):
            self.CS = value

    def spacer(self, fles):
        return " |" + ("=" if self.CS else " ") + "| |" \
                    + ("=" if fles.CS else " ") + "| "

def ones(stack):
    count = 0
    for dpdt in stack:
        count += dpdt.CS
    return count

N = 4

STACK = [None] * N
for i in range(0, N):
    STACK[i] = DPDT()

STACK[0]["AI"] = 1

for a in range(0, pow(2, N)):
    for i in range(0, N):
        #print((a >> i) & 1)
        STACK[i].CS = (a >> i) & 1
    for i in range(0, N):
        STACK[i].run()
        print(STACK[i])
        if i < N - 1:
            print(STACK[i].spacer(STACK[i + 1]))
            STACK[i + 1].AI = STACK[i].AO
            STACK[i + 1].BI = STACK[i].BO
    print("[EXP:0,1]: ON\n" if ones(STACK) % 2 else "[EXP:1,0]: OFF\n")
```

```
Adafruit CircuitPython 7.0.0-rc.1 on 2021-09-02; Adafruit Macropad RP2040 with rp2040
>>>
soft reboot

Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
code.py output:
[1,0,1,0]0
 | | | |
[1,0,1,0]0
 | | | |
[1,0,1,0]0
 | | | |
[1,0,1,0]0
[EXP:1,0]: OFF

[1,0,0,1]1
 |=| | |
[0,1,0,1]0
 | | | |
[0,1,0,1]0
 | | | |
[0,1,0,1]0
[EXP:0,1]: ON

[1,0,1,0]0
 | | |=|
[1,0,0,1]1
 |=| | |
[0,1,0,1]0
 | | | |
[0,1,0,1]0
[EXP:0,1]: ON

[1,0,0,1]1
 |=| |=|
[0,1,1,0]1
 |=| | |
[1,0,1,0]0
 | | | |
[1,0,1,0]0
[EXP:1,0]: OFF

[1,0,1,0]0
 | | | |
[1,0,1,0]0
 | | |=|
[1,0,0,1]1
 |=| | |
[0,1,0,1]0
[EXP:0,1]: ON

[1,0,0,1]1
 |=| | |
[0,1,0,1]0
 | | |=|
[0,1,1,0]1
 |=| | |
[1,0,1,0]0
[EXP:1,0]: OFF

[1,0,1,0]0
 | | |=|
[1,0,0,1]1
 |=| |=|
[0,1,1,0]1
 |=| | |
[1,0,1,0]0
[EXP:1,0]: OFF

[1,0,0,1]1
 |=| |=|
[0,1,1,0]1
 |=| |=|
[1,0,0,1]1
 |=| | |
[0,1,0,1]0
[EXP:0,1]: ON

[1,0,1,0]0
 | | | |
[1,0,1,0]0
 | | | |
[1,0,1,0]0
 | | |=|
[1,0,0,1]1
[EXP:0,1]: ON

[1,0,0,1]1
 |=| | |
[0,1,0,1]0
 | | | |
[0,1,0,1]0
 | | |=|
[0,1,1,0]1
[EXP:1,0]: OFF

[1,0,1,0]0
 | | |=|
[1,0,0,1]1
 |=| | |
[0,1,0,1]0
 | | |=|
[0,1,1,0]1
[EXP:1,0]: OFF

[1,0,0,1]1
 |=| |=|
[0,1,1,0]1
 |=| | |
[1,0,1,0]0
 | | |=|
[1,0,0,1]1
[EXP:0,1]: ON

[1,0,1,0]0
 | | | |
[1,0,1,0]0
 | | |=|
[1,0,0,1]1
 |=| |=|
[0,1,1,0]1
[EXP:1,0]: OFF

[1,0,0,1]1
 |=| | |
[0,1,0,1]0
 | | |=|
[0,1,1,0]1
 |=| |=|
[1,0,0,1]1
[EXP:0,1]: ON

[1,0,1,0]0
 | | |=|
[1,0,0,1]1
 |=| |=|
[0,1,1,0]1
 |=| |=|
[1,0,0,1]1
[EXP:0,1]: ON

[1,0,0,1]1
 |=| |=|
[0,1,1,0]1
 |=| |=|
[1,0,0,1]1
 |=| |=|
[0,1,1,0]1
[EXP:1,0]: OFF


Code done running.

Press any key to enter the REPL. Use CTRL-D to reload.

```