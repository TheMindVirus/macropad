```py
# ShiftRegMod - TheMindVirus
# This sketch...does not use a seesaw...to use an actual shift register ic...
# It instead simulates each individual logical element built up into a mod...

import random, time

class NOT: # NC Transistor Redstone Torch
    def __init__(self):
        self.x = 0
        self.y = 1
    def __call__(self):
        self.y = 1 - self.x
        return self
    def __repr__(self):
        return "[[" + str(self.x) + "], [" + str(self.y) + "]]"

class _OR: # Bare Wire Redstone Dust
    def __init__(self):
        self.x = 0
        self.X = 0
        self.y = 0
    def __call__(self):
        self.y = self.x if self.x else self.X if self.X else 0
        return self
    def __repr__(self):
        return "[[" + str(self.x) + ", " + str(self.X) + "], [" + str(self.y) + "]]"

class AND: # 3x NOT 1x _OR
    def __init__(self):
        self.x = 0
        self.X = 0
        self.y = 0
        self.NOTx = NOT()
        self.NOTX = NOT()
        self._ORy = _OR()
        self.NOTy = NOT()
    def __call__(self):
        self.NOTx.x = self.x
        self.NOTx()
        self.NOTX.x = self.X
        self.NOTX()
        self._ORy.x = self.NOTx.y
        self._ORy.X = self.NOTX.y
        self._ORy()
        self.NOTy.x = self._ORy.y
        self.NOTy()
        self.y = self.NOTy.y
        return self
    def __repr__(self):
        return "[[" + str(self.x) + ", " + str(self.X) + "], [" + str(self.y) + "]]"

class INIT:
    def __init__(self):
        self.clk = NOT()
        self.a = AND()
        self.b = _OR()
        self.rst = _OR()
        self.MANUAL_OVERRIDE = False
    def __call__(self):
        if 1 - self.MANUAL_OVERRIDE:
            self.clk.x = 1 - self.clk.x
        self.clk()
        if 1 - self.MANUAL_OVERRIDE:
            self.a.x = random.randint(0, 1)
        self.a.X = self.clk.y
        self.a()
        if 1 - self.MANUAL_OVERRIDE:
            self.b.x = random.randint(0, 1)
        self.b()
        if 1 - self.MANUAL_OVERRIDE:
            self.rst.x = 1 if (random.randint(0, 100) < 6) else 0
        self.rst()
        return self
    def __repr__(self):
        this = self.clk.__repr__()
        this += " " + self.a.__repr__()
        this += " " + self.b.__repr__()
        this += " " + self.rst.__repr__()
        return this

class LATCH:
    def __init__(self):
        self.clk = NOT()
        self.o = _OR()
        self.n = NOT()
        self.N = NOT()
        self.O = _OR()
        self.rst = _OR()
    def __call__(self):
        self.clk()
        self.o.X = self.N.y
        self.o()
        self.n.x = self.o.y
        self.n()
        self.N.x = self.O.y
        self.N()
        self.O.x = self.n.y
        self.O()
        self.rst()
        return self
    def __repr__(self):
        this = self.clk.__repr__()
        this += " " + self.o.__repr__()
        this += " " + self.n.__repr__()
        this += " " + self.N.__repr__()
        this += " " + self.O.__repr__()
        this += " " + self.rst.__repr__()
        this += " <" + str(self.o.y) + ">"
        return this

class SHIFT:
    def __init__(self):
        self.clk = _OR()
        self.a = AND()
        self.o = _OR()
        self.n = NOT()
        self.O = _OR()
        self.rst = _OR()
    def __call__(self):
        self.clk()
        self.a.X = self.clk.y
        self.a()
        self.o.x = self.clk.y
        self.o()
        self.n.x = self.o.y
        self.n()
        self.O.x = self.n.y
        self.O.X = self.rst.y
        self.O()
        self.rst()
        return self
    def __repr__(self):
        this = self.clk.__repr__()
        this += " " + self.a.__repr__()
        this += " " + self.o.__repr__()
        this += " " + self.n.__repr__()
        this += " " + self.O.__repr__()
        this += " " + self.rst.__repr__()
        return this

class REG:
    def __init__(self, count = 8):
        self.count = count
        self.init = INIT()
        self.latch = []
        self.shift = []
        for i in range(0, self.count):
            self.latch.append(LATCH())
            self.shift.append(SHIFT())
        self.init.a.x = 0
        self.init.b.x = 1
        self.init.rst.x = 1
        self.init.MANUAL_OVERRIDE = True
        self.__call__()
        self.init.MANUAL_OVERRIDE = False
    def __call__(self):
        self.init()
        self.latch[0].clk.x = self.init.clk.y
        self.latch[0].o.x = self.init.a.y
        self.latch[0].O.X = self.init.b.y
        self.latch[0].rst.x = self.init.rst.y
        self.latch[0]() ; self.latch[0]()
        self.shift[0].clk.x = self.latch[0].clk.y
        self.shift[0].a.x = self.latch[0].o.y
        self.shift[0].o.X = self.latch[0].o.y
        self.shift[0].rst.x = self.latch[0].rst.y
        self.shift[0]() ; self.shift[0]()
        for i in range(0, self.count - 1):
            d = (i + 1) % self.count
            self.latch[d].clk.x = self.shift[i].clk.y
            self.latch[d].o.x = self.shift[i].a.y
            self.latch[d].O.X = self.shift[i].O.y
            self.latch[d].rst.x = self.shift[i].rst.y
            self.latch[d]() ; self.latch[d]()
            self.shift[d].clk.x = self.latch[d].clk.y
            self.shift[d].a.x = self.latch[d].o.y
            self.shift[d].o.X = self.latch[d].o.y
            self.shift[d].rst.x = self.latch[d].rst.y
            self.shift[d]() ; self.shift[d]()
        return self
    def __repr__(self):
        this = self.init.__repr__()
        for i in range(0, self.count):
            this += "\n" + self.latch[i].__repr__() + "\n" + self.shift[i].__repr__()
        this += "\n"
        return this

if __name__ == "__main__":
    A = REG()
    while True:
        print(A())
        time.sleep(1)
```