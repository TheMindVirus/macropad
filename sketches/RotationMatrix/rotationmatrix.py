# Rotation Matrix Calculator - Alastair Cota (source: Wikipedia)
# This sketch was originally written in or around 2011 in my spare time when I was in school.
# It does matrix multiplication on a rotation matrix to calculate where points should be after rotation.
# The original version was in Javascript, HTML and CSS and was ported to Python in 2022.
# This version may have a few bugs and edge cases for where I haven't tested it yet.

# These are known as Matrix Extensions. There are more dimensions to fill into the chip architecture:
# Voidix = 0, Linix = 1, Matrix = 2, Cubix = 3, Cylindrix = 4, Rimix = 5, Spherix = 6, Posix = 7
# Voidiy = 0, Liniy = 1, Matriy = 2, Cubiy = 3, Cylindriy = 4, Rimiy = 5, Spheriy = 6, Posiy = 8
# Voidiz = 0, Liniz = 1, Matriz = 2, Cubiz = 3, Cylindriz = 4, Rimiz = 5, Spheriz = 6, Posiz = 9
# Voidic = 0, Linic = 1, Matric = 2, Cubic = 3, Cylindric = 4, Rimic = 5, Spheric = 6, Posic = 10

# Voidic = 0, Linic = 1, Matric = 2, Cubic = 3, Cylindric = 4, Rimic = 5, Spheric = 6, Posic = 789X
# Timic = XI
# Spacic = XII
# Cullic = XIII
# Mirric = XIV
# Antic = XV

# Rendering Engines should distinguish between vertex, screen/clip, local, world and centroid positions.
# Normals and Texture Space are split into 3 Directional Categories: Vertex Facing, Edge Tangent and Face Map
# Each should have an input scaling range and an output scaling range, ideally -1.0->1.0 or standard -0.5->0.5

import math

try:
    tau = math.tau #not tan in this case :D
except:
    tau = 2.0 * math.pi

def sin(x):
    return math.sin(x * tau)

def cos(x):
    return math.cos(x * tau)

x = 0
y = 1
z = 2

p = [1.0, 0.0, 0.0]
a = [0.5, 0.5, 0.5]

r = \
[
    [
          cos(a[x]) * cos(a[z]),
        (-cos(a[y]) * sin(a[z])) + (sin(a[y]) * sin(a[x]) * cos(a[z])), 
         (sin(a[y]) * sin(a[z])) + (cos(a[y]) * sin(a[x]) * cos(a[z]))
    ],
    [
          cos(a[x]) * sin(a[z]),
         (cos(a[y]) * cos(a[z])) + (sin(a[y]) * sin(a[x]) * sin(a[z])),
        (-sin(a[y]) * cos(a[z])) + (cos(a[y]) * sin(a[x]) * sin(a[z]))
    ],
    [
         -sin(a[x]),
          sin(a[y]) * cos(a[x]),
          cos(a[y]) * cos(a[x])
    ]
]

t = [0.0, 0.0, 0.0]
t[x] = (p[x] * r[x][x]) + (p[y] * r[x][y]) + (p[z] * r[x][z])
t[y] = (p[x] * r[y][x]) + (p[y] * r[y][y]) + (p[z] * r[y][z])
t[z] = (p[x] * r[z][x]) + (p[y] * r[z][y]) + (p[z] * r[z][z])
print(", ".join([str(round(i, 2)) for i in t]))
# For FM Synthesis the built-in addition is incorrect, it should be multiplication
# Otherwise for Geometry it's largely a valid mangling of several multiplications

# Made from: https://en.wikipedia.org/wiki/Rotation_matrix
"""
rx = \
[
    [ cos, -sin,    0],
    [ sin,  cos,    0],
    [   0,    0,    1]
]

ry = \
[
    [ cos,    0,  sin],
    [   0,    1,    0],
    [-sin,    0,  cos]
]

rz = \
[
    [   1,    0,    0],
    [   0,  cos, -sin],
    [   0,  sin,  cos]
]
"""
# But this may be Y->X->Z instead of X->Y->Z...Simpler Solution?

class construct: # Requires Bracket Tokeniser
    def __init__(self, X = ""):
        self.X = str(X)
    def __add__(self, Y):
        Y = construct(Y)
        label = self.X
        sign = "+" #"" if "-" in X[0:2] or self.X == "" else "+"
        extend = Y
        if self.X == "" or self.X == construct("()"):
            return Y
        if Y == construct("") or Y == construct("()"):
            return self
        return construct("({}){}({})".format(str(label), str(sign), str(extend)))
    def __sub__(self, Y):
        Y = construct(Y)
        label = self.X
        sign = "-" #"+" if "-" in X[0:2] else "-"
        extend = Y
        if self.X == "" or self.X == construct("()"):
            return Y
        if Y == construct("") or Y == construct("()"):
            return self
        return construct("({}){}({})".format(str(label), str(sign), str(extend)))
    def __mul__(self, Y):
        Y = construct(Y)
        label = self.X # "-" + str(self.X) if "-" in Y[0:2] and "-" not in self.X[0:2] else str(self.X)
        sign = "x"
        extend = Y # if "-" not in Y[0:2] else Y.X.replace("-", "", 1)
        #if "0" in self.X or "0" in Y:
        #    return construct("")
        #if self.X == "":
        #    return Y
        return construct("({}){}({})".format(str(label), str(sign), str(extend)))
    def __repr__(self):
        return self.X
    def __getitem__(self, i):
        return self.X[i]
print(construct("-sinA") * construct("-cosB"))
print(construct("") - construct("(-cosBsinA)(-sinBcosA)"))
print(construct("(cosBcosA)(-sinBsinA)") - construct("(-cosBsinA)(-sinBcosA)"))
print(construct("(-cosBcosA)(-sinBsinA)") + construct("(-cosBsinA)(-sinBcosA)"))

def print2D(A):
    C = {}
    N = { 1: 0, 2: 0 }
    R = ""
    for n in A.keys():
        N[1] = n[0] if n[0] > N[1] else N[1]
        N[2] = n[1] if n[1] > N[2] else N[2]
    for i in range(1, N[1] + 1):
        for j in range(1, N[2] + 1):
            S = "({}, {}): {}\n".format(i, j, A[i, j])
            print(S, end = "")
            R += S
    return R

def mul2D(A, B):
    C = {}
    N = { 1: 0, 2: 0, 3: 0 }
    for n in A.keys():
        N[1] = n[0] if n[0] > N[1] else N[1]
        N[2] = n[1] if n[1] > N[2] else N[2]
    for n in B.keys():
        N[3] = n[1] if n[1] > N[3] else N[3]
    print(N)
    for i in range(1, N[1] + 1):
        for j in range(1, N[2] + 1):
            C[i, j] = A[1, 1].__class__()
            for k in range(1, N[3] + 1):
                C[i, j] += A[i, k] * B[k, j]
    return C

A = \
{
    (1, 1): construct("a11"), (1, 2): construct("a12"),
    (2, 1): construct("a21"), (2, 2): construct("a22"),
    (3, 1): construct("a31"), (3, 2): construct("a23")
}
B = \
{
    (1, 1): construct("b11"), (1, 2): construct("b12"),
    (2, 1): construct("b21"), (2, 2): construct("b22")
}
C = mul2D(A, B)
print2D(C)
#[print(str(i) + ": " + str(C[i])) for i in C]

A = \
{
    (1, 1):   1,  (1, 2):   0,  (1, 3):   1,
    (2, 1):   2,  (2, 2):   1,  (2, 3):   1,
    (3, 1):   0,  (3, 2):   0,  (3, 3):   1,
    (4, 1):   1,  (4, 2):   1,  (4, 3):   2,
}
B = \
{
    (1, 1):   1,  (1, 2):   2,  (1, 3):   1,
    (2, 1):   2,  (2, 2):   3,  (2, 3):   1,
    (3, 1):   4,  (3, 2):   2,  (3, 3):   2,
}
C = mul2D(A, B)
print2D(C)
#[print(str(i) + ": " + str(C[i])) for i in C]

A = \
{
    (1, 1): construct("cosB"), (1, 2): construct("-sinB"),
    (2, 1): construct("sinB"), (2, 2): construct("cosB")
}
B = \
{
    (1, 1): construct("cosA"), (1, 2): construct("-sinA"),
    (2, 1): construct("sinA"), (2, 2): construct("cosA")
}
C = mul2D(A, B)
print2D(C)
#[print(str(i) + ": " + str(C[i])) for i in C]
# Made from: https://en.wikipedia.org/wiki/Matrix_multiplication

RX = \
{
    (1, 1): construct("cosX"),  (1, 2): construct("-sinX"), (1, 3): construct("0"),
    (2, 1): construct("sinX"),  (2, 2): construct("cosX"),  (2, 3): construct("0"),
    (3, 1): construct("0"),     (3, 2): construct("0"),     (3, 3): construct("0"),
}
RY = \
{
    (1, 1): construct("cosY"),  (1, 2): construct("0"),     (1, 3): construct("sinY"),
    (2, 1): construct("0"),     (2, 2): construct("1"),     (2, 3): construct("0"),
    (3, 1): construct("-sinY"), (3, 2): construct("0"),     (3, 3): construct("cosY"),
}
RZ = \
{
    (1, 1): construct("1"),     (1, 2): construct("0"),     (1, 3): construct("0"),
    (2, 1): construct("0"),     (2, 2): construct("cosZ"),  (2, 3): construct("-sinZ"),
    (3, 1): construct("0"),     (3, 2): construct("sinZ"),  (3, 3): construct("cosZ"),
}

I = mul2D(RX, RY)
R = mul2D(I, RZ)
print2D(I)
print2D(R)
