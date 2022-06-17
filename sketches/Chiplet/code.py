# Chiplet - Alastair Cota - 22:10 17/06/2022
# This code.py simulates a custom chiplet that I designed in Minecraft Mods
# using the IC Workbench from Project Red Fabrication to place logic blocks

import time

class Chiplet:
    def __init__(self):
        self.inputs = [0, 0, 0, 0, 0, 0, 0, 0,  0]
        self.outputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.frequency = 2#Hz
        self.internal = True
        self.tied = True
    def __main__(self):
        if self.internal:
            self.inputs[0] = 1

        if self.inputs[0]:
            for i in range(7, 4, -1):
                self.outputs[i] = self.outputs[i - 1]
            if self.tied:
                self.outputs[4] = self.outputs[3]
            for i in range(3, 0, -1):
                self.outputs[i] = self.outputs[i - 1]
            self.outputs[0] = self.inputs[1]

            if self.inputs[2]:
                self.outputs[8:12] = self.outputs[0:4]
                self.inputs[2] = 0
            if self.inputs[3]:
                self.outputs[0:4] = self.outputs[8:12]
                self.inputs[3] = 0

            if self.inputs[4]:
                self.outputs[12:16] = self.outputs[4:8]
                self.inputs[4] = 0
            if self.inputs[5]:
                self.outputs[4:8] = self.outputs[12:16]
                self.inputs[5] = 0

            if self.inputs[6]:
                self.outputs[8:12] = [0, 0, 0, 0]
                self.inputs[6] = 0
            if self.inputs[7]:
                self.outputs[12:16] = [0, 0, 0, 0]
                self.inputs[7] = 0

            self.inputs[0] = 0
            print(chiplet.outputs)
            time.sleep(1.0 / self.frequency)

chiplet = Chiplet()
while True:
    chiplet.inputs[1] = 1
    chiplet.__main__()
    chiplet.inputs[1] = 0
    for i in range(0, 7):
        if i == 2:
            chiplet.inputs[2] = 1
        if i == 6:
            chiplet.inputs[4] = 1
        chiplet.__main__()
    chiplet.inputs[6] = 1
    chiplet.inputs[7] = 1