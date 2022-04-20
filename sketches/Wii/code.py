# Mii Channel Theme - Alastair Cota, Nintendo Wii Dev Team

from adafruit_macropad import MacroPad
import time

macropad = MacroPad()

def note(n, t = 1.0, p = 0.0):
    macropad.start_tone(n)
    time.sleep(t)
    macropad.stop_tone()
    time.sleep(p)

def drop(t = 0.5):
    macropad.stop_tone()
    time.sleep(t)

C_4 = 530
CS4 = 570
D_4 = 590
DS4 = 630
E_4 = 660
F_4 = 690
FS4 = 750
G_4 = 785
GS4 = 845
A_4 = 885
AS4 = 945
B_4 = 995
C_5 = 1050
CS5 = 1111
D_5 = 1200
DS5 = 1250
E_5 = 1350
F_5 = 1400
FS5 = 1485
G_5 = 1550
GS5 = 1660

T0 = 0.000
T1 = 0.125
T2 = 0.250
T3 = 0.500
T4 = 1.000

T5 = T3 + T1
T6 = T3 + T2

note(FS4, T2, T2)
note(A_4, T2, T0)
note(CS5, T2, T2)
note(A_4, T2, T2)
note(FS4, T2, T0)
note(D_4, T1, T1)
note(D_4, T1, T1)
note(D_4, T1, T1)
drop(T4)
note(CS4, T2, T0)
note(D_4, T1, T1)
note(FS4, T2, T0)
note(A_4, T1, T1)
note(CS5, T2, T2)
note(A_4, T2, T2)
note(FS4, T1, T1)
note(E_5, T5, T0)
note(DS5, T2, T0)
note(D_5, T2, T0)
drop(T5)
note(GS4, T2, T2)
note(CS5, T2, T0)
note(FS4, T2, T2)
note(CS5, T2, T2)
note(GS4, T2, T2)
note(CS5, T2, T2)
note(G_4, T2, T0)
note(FS4, T2, T2)
note(E_4, T2, T2)
note(C_4, T1, T1)
note(C_4, T1, T1)
note(C_4, T1, T1)
drop(T5)
note(C_4, T1, T1)
note(C_4, T1, T1)
note(C_4, T1, T1)
drop(T5)
note(DS4, T3, T0)
note(D_4, T3, T0)
note(FS4, T2, T2)
note(A_4, T2, T0)
note(CS5, T2, T2)
note(A_4, T2, T2)
note(FS4, T2, T0)
note(E_4, T1, T1)
note(E_4, T1, T1)
note(E_4, T1, T1)
drop(T2)
note(E_5, T1, T1)
note(E_5, T1, T1)
note(E_5, T1, T1)
drop(T3)
note(FS4, T2, T0)
note(A_4, T1, T1)
note(CS5, T2, T2)
note(A_4, T2, T2)
note(FS4, T1, T1)
note(CS5, T4, T0)
note(B_4, T2, T5)
note(B_4, T2, T0)
note(FS4, T2, T0)
note(E_4, T2, T0)
note(DS4, T2, T2)
note(B_4, T2, T0)
note(GS4, T2, T0)
note(E_4, T2, T0)
note(A_4, T2, T0)
note(E_4, T2, T0)
note(D_4, T2, T0)
note(CS4, T2, T2)
note(A_4, T2, T0)
note(E_4, T2, T0)
note(CS4, T2, T0)
note(DS4, T1, T1)
note(DS4, T1, T1)
note(DS4, T1, T1)
drop(T4)
note(F_4, T2, T0)
note(FS4, T1, T1)
note(GS4, T2, T0)
note(A_4, T1, T1)
note(CS5, T2, T0)
note(E_5, T2, T6)
drop(T4)
note(A_4, T3, T0)
note(AS4, T3, T0)
note(B_4, T6, T0)
note(AS4, T2, T0)
note(B_4, T4, T3)
note(A_4, T2, T0)
note(AS4, T2, T0)
note(B_4, T2, T0)
note(FS5, T3, T0)
note(CS5, T2, T0)
note(B_4, T6, T0)
note(AS4, T2, T0)
note(B_4, T4, T4)
note(B_4, T3, T0)
note(C_5, T3, T0)
note(CS5, T6, T0)
note(C_5, T2, T0)
note(CS5, T4, T3)
note(CS5, T2, T0)
note(C_5, T2, T0)
note(CS5, T2, T0)
note(GS5, T3, T0)
note(DS5, T2, T0)
note(CS5, T6, T0)
note(DS5, T2, T0)
note(B_4, T3, T2)
note(CS4, T2, T0)
note(D_4, T2, T0)
note(A_4, T3, T0)
note(D_4, T2, T0)
note(GS4, T1, T1)
note(GS4, T1, T1)
note(GS4, T1, T1)
drop(T2)