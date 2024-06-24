# ShiftRegister - TheMindVirus
# This sketch...does not use a seesaw...to use an actual shift register ic...
# It instead emulates each individual logical element built up into a blob...

import random, time

class BUF:
    def __init__(self):
        self.x = 0
        self.y = 0
    def __call__(self):
        self.y = self.x
        return self
    def __repr__(self):
        return "[[" + str(self.x) + "], [" + str(self.y) + "]]"

class NOT:
    def __init__(self):
        self.x = 0
        self.y = 1
    def __call__(self):
        self.y = 1 - self.x
        return self
    def __repr__(self):
        return "[[" + str(self.x) + "], [" + str(self.y) + "]]"

class OR:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.y = 0
    def __call__(self):
        self.y = self.x1 | self.x2
        return self
    def __repr__(self):
        return "[[" + str(self.x1) + ", " + str(self.x2) + "], [" + str(self.y) + "]]"

class AND:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.y = 0
    def __call__(self):
        self.y = self.x1 & self.x2
        return self
    def __repr__(self):
        return "[[" + str(self.x1) + ", " + str(self.x2) + "], [" + str(self.y) + "]]"

class INIT:
    def __init__(self):
        self.clk = NOT()
        self.a1 = AND()
        self.b1 = BUF()
        self.rst = BUF()
        self.MANUAL_OVERRIDE = False
    def __call__(self):
        if 1 - self.MANUAL_OVERRIDE:
            self.clk.x = 1 - self.clk.x
        self.clk()
        if 1 - self.MANUAL_OVERRIDE:
            self.a1.x1 = random.randint(0, 1)
        self.a1.x2 = self.clk.y
        self.a1()
        if 1 - self.MANUAL_OVERRIDE:
            self.b1.x = random.randint(0, 1)
        self.b1()
        if 1 - self.MANUAL_OVERRIDE:
            self.rst.x = 1 if (random.randint(0, 100) < 6) else 0
        self.rst()
        return self
    def __repr__(self):
        this = self.clk.__repr__()
        this += " " + self.a1.__repr__()
        this += " " + self.b1.__repr__()
        this += " " + self.rst.__repr__()
        return this

class LATCH:
    def __init__(self):
        self.clk = NOT()
        self.d1 = OR()
        self.i1 = NOT()
        self.i2 = NOT()
        self.d2 = OR()
        self.rst = BUF()
    def __call__(self):
        self.clk()
        self.d1.x2 = self.i2.y
        self.d1()
        self.i1.x = self.d1.y
        self.i1()
        self.i2.x = self.d2.y
        self.i2()
        self.d2.x1 = self.i1.y
        self.d2()
        self.rst()
        return self
    def __repr__(self):
        this = self.clk.__repr__()
        this += " " + self.d1.__repr__()
        this += " " + self.i1.__repr__()
        this += " " + self.i2.__repr__()
        this += " " + self.d2.__repr__()
        this += " " + self.rst.__repr__()
        this += " <" + str(self.d1.y) + ">"
        return this

class SHIFT:
    def __init__(self):
        self.clk = BUF()
        self.a1 = AND()
        self.d1 = OR()
        self.i1 = NOT()
        self.d2 = OR()
        self.rst = BUF()
    def __call__(self):
        self.clk()
        self.a1.x2 = self.clk.y
        self.a1()
        self.d1.x1 = self.clk.y
        self.d1()
        self.i1.x = self.d1.y
        self.i1()
        self.d2.x1 = self.i1.y
        self.d2.x2 = self.rst.y
        self.d2()
        self.rst()
        return self
    def __repr__(self):
        this = self.clk.__repr__()
        this += " " + self.a1.__repr__()
        this += " " + self.d1.__repr__()
        this += " " + self.i1.__repr__()
        this += " " + self.d2.__repr__()
        this += " " + self.rst.__repr__()
        return this

class REG:
    def __init__(self, n = 8):
        self.n = n
        self.init = INIT()
        self.latch = []
        self.shift = []
        for i in range(0, self.n):
            self.latch.append(LATCH())
            self.shift.append(SHIFT())
        self.init.a1.x = 0
        self.init.b1.x = 1
        self.init.rst.x = 1
        self.init.MANUAL_OVERRIDE = True
        self.__call__()
        self.init.MANUAL_OVERRIDE = False
    def __call__(self):
        self.init()
        self.latch[0].clk.x = self.init.clk.y
        self.latch[0].d1.x1 = self.init.a1.y
        self.latch[0].d2.x2 = self.init.b1.y
        self.latch[0].rst.x = self.init.rst.y
        self.latch[0]() ; self.latch[0]()
        self.shift[0].clk.x = self.latch[0].clk.y
        self.shift[0].a1.x1 = self.latch[0].d1.y
        self.shift[0].d1.x2 = self.latch[0].d1.y
        self.shift[0].rst.x = self.latch[0].rst.y
        self.shift[0]() ; self.shift[0]()
        for i in range(0, self.n - 1):
            d = (i + 1) % self.n
            self.latch[d].clk.x = self.shift[i].clk.y
            self.latch[d].d1.x1 = self.shift[i].a1.y
            self.latch[d].d2.x2 = self.shift[i].d2.y
            self.latch[d].rst.x = self.shift[i].rst.y
            self.latch[d]() ; self.latch[d]()
            self.shift[d].clk.x = self.latch[d].clk.y
            self.shift[d].a1.x1 = self.latch[d].d1.y
            self.shift[d].d1.x2 = self.latch[d].d1.y
            self.shift[d].rst.x = self.latch[d].rst.y
            self.shift[d]() ; self.shift[d]()
        return self
    def __repr__(self):
        this = self.init.__repr__()
        for i in range(0, self.n):
            this += "\n" + self.latch[i].__repr__() + "\n" + self.shift[i].__repr__()
        this += "\n"
        return this

if __name__ == "__main__":
    A = REG()
    while True:
        print(A())
        time.sleep(1)