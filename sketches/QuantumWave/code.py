# QuantumWave - TheMindVirus
# This sketch runs somewhat limited on the macropad due to a lack of AnalogOut pins
# Originally tested on Adafruit Feather ESP32S2 with [LED, A0, D10]

import board, time, math
import digitalio
import analogio
import pwmio
import sys

dotcode = \
"""
macropad = None
try:
    from adafruit_macropad import MacroPad

    _board = board
    class board:
        pass
    board = board()
    board.LED = _board.LED
    board.A0 = _board.KEY3
    board.D10 = _board.BUTTON

    class _macropad:
        instance = MacroPad()
        instance._led.deinit()
        instance._encoder_switch.deinit()
    macropad = _macropad

    class _AnalogOut:
        p = len(macropad.instance.pixels)
        _value = 0
        .property
        def value(self):
            return self._value
        .value.getter
        def value(self):
            return self._value
        .value.setter
        def value(self, item):
            v = slurp(item, 255, 65535)
            for i in range(0, self.p):
                macropad.instance.pixels[i] = v
            self._value = item

    macropad.AnalogOut = _AnalogOut

except Exception as error:
    print(error)
"""
dotcode = dotcode.replace(".property", "@property")
dotcode = dotcode.replace(".value.getter", "@value.getter")
dotcode = dotcode.replace(".value.setter", "@value.setter")
exec(dotcode)

class dio:
    Direction = digitalio.Direction
    DigitalPin = digitalio.DigitalInOut

dotcode = \
"""
class _AnalogPin:
    def __init__(self, *args):
        try:
            self.instance = analogio.AnalogOut(*args)
        except:
            self.instance = macropad.AnalogOut(*args)
        self._value = 0
    .property
    def value(self):
        return self._value
    .value.getter
    def value(self):
        return self._value
    .value.setter
    def value(self, item):
        self._value = self.instance.value = item
"""
dotcode = dotcode.replace(".property", "@property")
dotcode = dotcode.replace(".value.getter", "@value.getter")
dotcode = dotcode.replace(".value.setter", "@value.setter")
exec(dotcode)

class aio:
    Direction = digitalio.Direction
    def AnalogPin(*args):
        return _AnalogPin(*args)

dotcode = \
"""
class _Qubit:
    def __init__(self, copy = None, duty_cycle = None, frequency = None):
        if copy != None:
            self.duty_cycle = copy.duty_cycle
            self.frequency = copy.frequency
        else:
            self.duty_cycle = 0.5
            self.frequency = 1.0
        if duty_cycle != None:
            self.duty_cycle = float(duty_cycle)
        if frequency != None:
            self.frequency = float(frequency)

    def __repr__(self):
        return str({ "duty_cycle": self.duty_cycle, "frequency": self.frequency })

class _QuantumPin:
    def __init__(self, *args):
        self.instance = pwmio.PWMOut(*args, variable_frequency = True)
        self._value = _Qubit()
    .property
    def value(self):
        return self._value
    .value.getter
    def value(self):
        return self._value
    .value.setter
    def value(self, item):
        self._value = item
        self.instance.duty_cycle = int(self._value.duty_cycle * 100)
        self.instance.frequency = int(max(1, self._value.frequency))
        return self._value
    .property
    def duty_cycle(self):
        return self._value.duty_cycle
    .duty_cycle.getter
    def duty_cycle(self):
        return self._value.duty_cycle
    .duty_cycle.setter
    def duty_cycle(self, item):
        self._value.duty_cycle = item
        self.instance.duty_cycle = int(self._value.duty_cycle * 100)
        return self._value.duty_cycle
    .property
    def frequency(self):
        return self._value.frequency
    .frequency.getter
    def frequency(self):
        return self._value.frequency
    .frequency.setter
    def frequency(self, item):
        self._value.frequency = item
        self.instance.frequency = int(max(1, self._value.frequency))
        return self._value.frequency
"""
dotcode = dotcode.replace(".property", "@property")
dotcode = dotcode.replace(".value.getter", "@value.getter")
dotcode = dotcode.replace(".value.setter", "@value.setter")
dotcode = dotcode.replace(".duty_cycle.getter", "@duty_cycle.getter")
dotcode = dotcode.replace(".duty_cycle.setter", "@duty_cycle.setter")
dotcode = dotcode.replace(".frequency.getter", "@frequency.getter")
dotcode = dotcode.replace(".frequency.setter", "@frequency.setter")
exec(dotcode)

class quantumio:
    Direction = digitalio.Direction
    Qubit = _Qubit
    def QuantumPin(*args):
        return _QuantumPin(*args)
sys.modules["quantumio"] = quantumio
import quantumio
qio = quantumio
qbit = qio.Qubit

tau = 2.0 * math.pi

def main():
    a = dio.DigitalPin(board.LED)
    b = aio.AnalogPin(board.A0)
    c = qio.QuantumPin(board.D10)

    a.direction = dio.Direction.OUTPUT
    b.direction = aio.Direction.OUTPUT
    c.direction = qio.Direction.OUTPUT

    a.value = False
    b.value = 0
    c.value = qbit()

    c.frequency = 0.5
    d = 1.0 / c.frequency
    print(notes) ; time.sleep(1)

    while True:
        t = time.monotonic()
        x = blink(t, d)
        y = wave(t, d)
        z = shift(t, d)
        print(x, y, z)
        a.value = bool(lerp(x, D = 65535))
        b.value = int(slurp(y, X = 65535))
        c.value = qbit(tarp(z, H = 65535))
        #time.sleep(0.01)

def blink(t = 0, d = 1):
    return (t % (d * 2)) < d

def wave(t = 0, d = 1, l = 0, a = 1):
    r = ((t % d) / d)
    w = math.cos(tau * r)
    return (((w + 1) * 0.5) * a) + l

def shift(t = 0, d = 1):
    return qbit(duty_cycle = wave(t, d), frequency = blink(t, d))

def lerp(y = 0, A = 0, B = 1, C = 0, D = 1):
    return ((C * (B - y)) - (D * (A - y))) / (B - A)

def slurp(y = 0, X = 1, Y = 1):
    return (y * X) / Y

def tarp(y = 0, H = 1):
    if type(y) == type(qbit()):
        return qbit(y, frequency = H)
    return qbit(duty_cycle = y, frequency = H)

notes = \
"""
# full form linear interpolation / lerp

a - y - b
    |
c - x - d

(b - y) / (y - a) = (d - x) / (x - c)
(b - y)(x - c) = (d - x)(y - a)
bx - bc - xy + cy = dy - ad - xy + ax
bx - bc + cy = dy - ad + ax
bx - ax = bc + dy - ad - cy
x(b - a) = bc + dy - ad - cy
x = (bc + dy - ad - cy) / (b - a)
x - (c(b - y) - d(a - y)) / (b - a)

# quick form linear interpolation / slurp

0 - y - Y
    |
0 - x - X

(Y - y) / (y - 0) = (X - x) / (x - 0)
(Y - y) / y = (X - x) / x
x(Y - y) = y(X - x)
xY - xy = yX - xy
xY - xy + xy = yX
x(Y - y + y) = yX
x = yX / Y

# ideal example numeric equation / tarp

0 - 2 - 4
    |
0 - 1 - 2

(4 - 2) / (2 - 0) = (2 - 1) / (1 - 0)
2 / 2 = 1 / 1
(4 - 2) x (1 - 0) = (2 - 1) x (2 - 0)
2 x 1 = 1 x 2
"""

if __name__ == "__main__":
    main()