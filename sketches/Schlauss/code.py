# Schlauss - TheMindVirus
# Named after the river in eastern Germany and the predecessor of Fraunhofer from Erlangen,
# The Schlauss Cosine Frequency Transform is the low frequency alternative to FFT and Bode

import math

max_len = pow(2, 8)
max_iter = 1000

def __(n, b = 8): # ration
    return pow(2, n * b)

def ___(n, l = max_iter, endian = "big"): # range
    count = 0
    for i in range(0, l):
        if n < pow(2, i * 8):
            return i, endian
    return -1, endian

def ____(a = max_len, l = max_iter): # radix
    b = b""
    for i in range(0, l):
        c = i
        b += i.to_bytes(*___(i))
        if len(b) > a:
            return i, b
    return -1, b

def _____(a, b = math.pi / 2): # schlauss cosine transform
    return a * math.cos(b) # otherwise piecewise integration

def ______(a, b = math.pi / 2): # inverse schlauss cosine transform
    return a / math.cos(b) # math.acos(a) would cause wrap around

def ß(*args, **kwargs):
    if len(args) > 0:
        n = args[0]
        if type(n) == type(int()):
            return ___(n)
        if type(n) == type(float()):
            return ___(n)
        if type(n) == type(complex()):
            return ___(n.real)
    return len(*args, **kwargs)

a = "hallo"
b = ß(a)
c = ß(b)
print(a, b, c)

d = float(c[0])
e = complex(d)
f = ____(e.real)
print(d, ß(d), e, ß(e), f, ß(f))

g = 7
h = _____(g)
i = ______(h)
print(g, h, i)

"""
max_len = pow(2, 20) #16384 #8192 #4096 #1500 #255 #100 #20
max_iter = 1000000000 #Long Duration in the range of seconds

def ___(n, l = max_iter, endian = "big"):
    count = 0
    for i in range(0, l):
        if n < pow(2, i * 8):
            return i, endian
    return -1, endian

def ____(a = max_len, l = max_iter):
    b = b""
    for i in range(0, l):
        c = i
        b += i.to_bytes(*___(i))
        if len(b) > a:
            return i, b
    return -1, b
"""

# ... Well ... Everyone ... Welcome to Katowice ... #