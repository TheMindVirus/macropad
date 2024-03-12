# Virtual Transistor - TheMindVirus
# A house of cards made of transistors forms all sorts of integrated circuit (IC) internals
# Rings of feedback caused by reverse analog signals makes an oscillation pattern through this stack.

class transistor:
    def __init__(self):
        self.C = 0
        self.B = 0
        self.E = 0

    def __call__(self):
        self.E = self.C if self.B else 0

    def __repr__(self):
        return str([self.C, self.B, self.E])

"""
 B
A+C
"""

class darlington_ring():
    def __init__(self):
        self.A = transistor()
        self.B = transistor()
        self.C = transistor()

    def __call__(self):
        self.A.C = self.B.E
        self.B.C = self.C.E
        self.C.C = self.A.E
        self.A()
        self.B()
        self.C()
        return self

    def __repr__(self):
        return str({"A": self.A, "B": self.B, "C": self.C})

stack = darlington_ring()
stack.A.B = 1
stack.B.B = 1
stack.C.B = 1
stack.C.E = 1
print(stack, stack.C.E)
for i in range(0, 10):
    print(stack(), stack.C.E)