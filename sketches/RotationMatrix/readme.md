![reassembled](https://github.com/themindvirus/macropad/blob/archive/sketches/RotationMatrix/reassembled.png)
![original](https://github.com/themindvirus/macropad/blob/archive/sketches/RotationMatrix/original.png)

```py
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
    [   1,    0,    0],
    [   0,  cos, -sin],
    [   0,  sin,  cos]
]

ry = \
[
    [ cos,    0,  sin],
    [   0,    1,    0],
    [-sin,    0,  cos]
]

rz = \
[
    [ cos, -sin,    0],
    [ sin,  cos,    0],
    [   0,    0,    1]
]
"""
# But this may be Y->X->Z instead of X->Y->Z...Simpler Solution?

class construct:
    def __init__(self, X = ""):
        self.X = str(X)
    def __add__(self, X):
        sign = "" if X[0] == "-" or self.X == "" else "+"
        return construct(str(self.X) + sign + str(X))
    def __sub__(self, X):
        sign = "+" if X[0] == "-" else "-"
        extend = 1 if X[0] == "-" else 0 # Untested
        return construct(str(self.X) + sign + str(X[extend:]))
    def __mul__(self, X):
        label = "-" + str(self.X) if "-" in X and "-" not in self.X else str(self.X)
        extend = 1 if "-" in label and "-" in X else 0
        return construct(str(label) + str(X[extend:]))
    def __repr__(self):
        return self.X
    def __getitem__(self, i):
        return self.X[i]
print(construct("-sinA") * construct("-cosB"))

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
```

![screenshot](https://github.com/themindvirus/macropad/blob/archive/sketches/RotationMatrix/screenshot.png)
![screenshot2](https://github.com/themindvirus/macropad/blob/archive/sketches/RotationMatrix/screenshot2.png)

The Construct Class is a heavily simplified version of a graphical calculator's compiler. \
It's simplified on purpose so it can more closely adapt to edge cases - it would have bugs in general cases. \
The alternative would be to over-optimise the matrix and all the operations which would cause reliability issues.

Here is an example of such over-optimisation being removed from the algebraic compiler:
![construct](https://github.com/themindvirus/macropad/blob/archive/sketches/RotationMatrix/construct.png)

# Corkscrew

Just in case all of that didn't make any sense, here's the equation of a corkscrew wave...
![screenshot3](https://github.com/themindvirus/macropad/blob/archive/sketches/RotationMatrix/screenshot3.png)
