# Unrivalled Squishy Function

![screenshot](https://github.com/themindvirus/macropad/blob/archive/sketches/SquishyMod/gridcube.png)

```py
import math

def power_root(a, b):
    _1b = 1 / b
    return -(pow(abs(a), _1b)) if a < 0 else pow(a, _1b)

def fn1(x, m = 0.7, c = 0.2 - 0.007, d = 0.1):
    x += d if x > 0 else -d
    _m = abs(m * x)
    __m = abs(_m * x)
    m = __m
    y = m + c
    y = min(1, y)
    return y

def fn2(x, m = 0.4, c = 0.4):
    x = math.cos(x * math.pi)
    x = power_root(x, 2)
    y = (m * x) + c
    y = min(1, y)
    y = 1 - y
    return y

def fn3(x, m = 0.4, c = 0.4):
    y = 0
    if x < -0.5 or x > 0.5:
        x = math.cos((x * math.pi) + math.pi)
        x = -power_root(x, 2)
        y = ((1 - m) * x) + c + 0.2
    else:
        x = math.cos(x * math.pi)
        x = power_root(x, 2)
        y = (m * x) + c
    y = min(1, y)
    y = 1 - y
    return y

def f12(x, p = 3):
    a = ("{:0.0" + str(p) + "}").format(float(x))
    if a.find(".") == -1: # absurdly required on cp7
        a += ".0"
    n = p - (len(a) - a.find(".") - 1)
    b = a + ("0" * n)
    return b

#print(f12(1))

#"""
n = 10 # subdivisions
nd2 = int(n + 1)
print(" [IDX] \t [FN1] \t [FN2] \t [FN3] ")
for i in range(-nd2, nd2 + 1):
    print(str(i) + "/" + str(nd2),
          "\t", f12(fn1(i/nd2)),
          "\t", f12(fn2(i/nd2)),
          "\t", f12(fn3(i/nd2)))
#"""
```

![screenshot](https://github.com/themindvirus/macropad/blob/archive/sketches/SquishyMod/blender.png)

```py
Adafruit CircuitPython 7.0.0-rc.1 on 2021-09-02; Adafruit Macropad RP2040 with rp2040
>>>
soft reboot

Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
code.py output:
 [IDX]   [FN1]   [FN2]   [FN3]
-11/11   1.000   1.000   1.000
-10/11   0.906   0.992   0.988
-9/11    0.783   0.967   0.950
-8/11    0.672   0.924   0.886
-7/11    0.573   0.858   0.787
-6/11    0.485   0.751   0.626
-5/11    0.408   0.449   0.449
-4/11    0.343   0.342   0.342
-3/11    0.290   0.276   0.276
-2/11    0.249   0.233   0.233
-1/11    0.219   0.208   0.208
0/11     0.200   0.200   0.200
1/11     0.219   0.208   0.208
2/11     0.249   0.233   0.233
3/11     0.290   0.276   0.276
4/11     0.343   0.342   0.342
5/11     0.408   0.449   0.449
6/11     0.485   0.751   0.626
7/11     0.573   0.858   0.787
8/11     0.672   0.924   0.886
9/11     0.783   0.967   0.950
10/11    0.906   0.992   0.988
11/11    1.000   1.000   1.000

Code done running.

Press any key to enter the REPL. Use CTRL-D to reload.
```