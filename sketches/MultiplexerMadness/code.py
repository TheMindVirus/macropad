# Multiplexer Madness - TheMindVirus
# This is a circuitpython port of my multiplexer simulator that uses abstract cpython language.
# First you define the traces on the board, then you run a kernel that enables all the channels.

import time

def board(MUX):
    MUX[1].D    = MUX[0].Q[0]
    MUX[1].S[0] = MUX[0].Q[1]
    MUX[1].S[1] = MUX[0].Q[2]
    MUX[1].S[2] = MUX[0].Q[3]
    for i in range(0, 4):
        MUX[4 + i].D = MUX[2].Q[0]
        MUX[8 + i].D = MUX[2].Q[4]
        MUX[12 + i].D = MUX[3].Q[0]
        MUX[16 + i].D = MUX[3].Q[4]
        for j in range(0, 3):
            MUX[4 + i].S[j] = MUX[2].Q[j + 1]
            MUX[8 + i].S[j] = MUX[2].Q[j + 5]
            MUX[12 + i].S[j] = MUX[3].Q[j + 1]
            MUX[16 + i].S[j] = MUX[3].Q[j + 5]
        if i >= 2:
            MUX[2].D = MUX[1].Q[0]
            MUX[3].D = MUX[1].Q[4]
            for j in range(0, 3):
                MUX[2].S[j] = MUX[1].Q[j + 1]
                MUX[3].S[j] = MUX[1].Q[j + 5]

def kernel(MUX, iteration):
    if iteration == 0:
        MUX[0].D = MUX[0].ON
        MUX.__run__(board)
    if iteration == 1:
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 2:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 3:
        MUX[0].D = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].D = MUX[0].ON
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 4:
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 20):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 5:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 6:
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].D = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 7:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 8:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        MUX[0].D = MUX[0].ON
        for i in range(0, 20):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 9:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 10:
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 11:
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        MUX[0].D = MUX[0].ON
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 12:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 13:
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 14:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 15:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 16:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        MUX[0].D = MUX[0].ON
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON    
    if iteration == 17:
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 18:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].ON
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 19:
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].D = MUX[0].ON
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 20:
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 21:
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].D = MUX[0].OFF
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 22:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 20):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 23:
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].D = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 24:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 25:
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 26:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 20):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 27:
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 28:
        MUX[0].S[1] = MUX[0].ON
        MUX[0].D = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 29:
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 30:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 31:
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 32:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        MUX[0].D = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 33:
        MUX[0].S[0] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 34:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 35:
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].D = MUX[0].ON
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 36:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 37:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 38:
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 39:
        MUX[0].D = MUX[0].ON
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 40:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 41:
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        MUX[0].D = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 42:
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 20):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 43:
        MUX[0].D = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 44:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        MUX[0].D = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 45:
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].D = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 46:
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 47:
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 48:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        MUX[0].D = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 49:
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 50:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 20):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 51:
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 52:
        MUX[0].S[1] = MUX[0].ON
        MUX[0].D = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 53:
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 54:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 55:
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].D = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 56:
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 57:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 58:
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 59:
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].D = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 60:
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 61:
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 62:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 63:
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].D = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 64:
        MUX[0].S[0] = MUX[0].ON
        for i in range(0, 20):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 65:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 66:
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 4):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 67:
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].ON
        MUX[0].D = MUX[0].ON
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[0] = MUX[0].OFF
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 68:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].ON
        for i in range(0, 20):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 69:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[0] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 70:
        MUX[0].S[0] = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON
    if iteration == 71:
        MUX[0].S[1] = MUX[0].ON
        MUX[0].nLE = MUX[0].OFF
        MUX.__run__(board)
        MUX[0].nLE = MUX[0].ON
        MUX[0].S[1] = MUX[0].OFF
        MUX[0].D = MUX[0].ON
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON  
    if iteration == 72:
        MUX[0].D = MUX[0].OFF
        MUX[0].S[1] = MUX[0].OFF
        for i in range(0, 2):
            MUX[i].nLE = MUX[i].OFF
            MUX.__run__(board)
            MUX[i].nLE = MUX[i].ON

def main():
    iteration = 0
    iterations = 72
    timestep = 0.1
    MUXTAB = multiplexer_table([8] * 20)
    while True:
        try:
            kernel(MUXTAB, iteration)
            print("__multiplexer_iteration_{}__".format(iteration))
            print(MUXTAB)
        except Exception as error:
            print(error)
        time.sleep(timestep)
        iteration += 1
        if iteration > iterations:
            return

class multiplexer:
    def __init__(self, n = 8):
        self._channel_selected = 0
        self._minimum_voltage = 3.3
        self._maximum_voltage = 7.3
        self._reverse_voltage = 3.3
        self._nominal_voltage = 5.0
        self._present_voltage = 0.0
        self._ground_connected = True
        self._disable_output = False
        self._disable_latch = False
        if n <= 0:
            self._disable_latch = True
            n = abs(n) # ValueError("n < 0")
            if n == 0:
                n = 1
        self._latch_input = [0] * n
        self.Q = [0.0] * n
        self.S = [0.0] * int(pow(n, 0.5) + 0.5)
        self.D = 0
        self.nRST = self._minimum_voltage
        self.nLE = self._minimum_voltage
        self.VCC = self._minimum_voltage
        self.VSS = self._present_voltage
        self.ON = self.VCC
        self.OFF = self.VSS

    def __run__(self):
        self.ON = self.VCC
        self.OFF = self.VSS
        self._present_voltage = self.VCC - self.VSS
        if not self._ground_connected:
            self._present_voltage = 0.0
        if self.D > self._maximum_voltage \
        and self._ground_connected:
            self.disable_output = True
        if self.nLE > self._maximum_voltage \
        and self._ground_connected:
            self.disable_output = True
        if self.nRST > self._maximum_voltage \
        and self._ground_connected:
            self.disable_output = True
        for i in range(0, len(self.Q)):
            if self.Q[i] > self._maximum_voltage \
            and self._ground_connected:
                self._disable_output = True
                break
        for i in range(0, len(self.S)):
            if self.S[i] > self._maximum_voltage \
            and self._ground_connected:
                self._disable_output = True
                break
        if self._present_voltage > self._maximum_voltage \
        or -self._present_voltage > self._reverse_voltage:
            self._disable_output = True
        if (self._present_voltage >= self._minimum_voltage \
        and self.nRST >= self._minimum_voltage) \
        and not self._disable_output:
            self._channel_selected = 0
            for i in range(0, len(self.S)):
                if self.S[i] >= self._minimum_voltage:
                    self._channel_selected += pow(2, i)
            self._channel_selected = abs(int(self._channel_selected))
            if self._channel_selected >= len(self._latch_input):
                self._channel_selected = len(self._latch_input) - 1
            self._latch_input[self._channel_selected] = self.D
            if self.nLE < self._minimum_voltage \
            or self._disable_latch:
                self.Q[self._channel_selected] = self._latch_input[self._channel_selected]
        else:
            for i in range(0, len(self.Q)):
                self.Q[i] = 0.0
    def __repr__(self):
        return "[{}]".format(", ".join(["{:.01f}".format(i) for i in self.Q]))

class multiplexer_table:
    def __init__(self, req = []):
        self.MUX = []
        for i in range(0, len(req)):
            self.MUX.append(multiplexer(req[i]))
    def __run__(self, board = None):
        if board:
            board(self)
        for i in range(0, len(self.MUX)):
            self.MUX[i].__run__()
    def __repr__(self):
        result = ""
        for i in range(0, len(self.MUX)):
            result += "{:d}:\t{}\n".format(i, self.MUX[i])
        return result
    def __getitem__(self, ie):
        return self.MUX[ie]

if __name__ == "__main__":
    main()
