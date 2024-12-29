# Double It - TheMindVirus
# Think of a number, Double It, Add 6, Halve It, Subtract the original number
# The answer is 3 (with some caveats involving division by zero and radicals)

def double_it(x):
    a = x * 2
    b = a + 6
    c = b / 2
    return c - x

for i in range(-10, 10):
    n = double_it(i)
    print(n, n == 3)

print()

def double_it_ext(x):
    a = x * 2
    b = a + 6
    c = b / 2
    return c - x, a, b, c

for i in range(-10, 10):
    n, a, b, c = double_it_ext(i)
    print(n, n == 3, i, a, b, c)

print()

def double_it_mod(x, y = 6, z = 1):
    a = x << z
    b = a + y
    c = b >> z
    return c - x, y >> z

for i in range(-10, 10):
    n, p = double_it_mod(i)
    print(n, n == p)

print()

def double_it_mod_ext(x, y = 6, z = 1):
    a = x << z
    b = a + y
    c = b >> z
    return c - x, y >> z, a, b, c

for i in range(-10, 10):
    n, p, a, b, c = double_it_mod_ext(i)
    print(n, n == p, a, b, c)

print()

def triple_it(i = 3):
    xyzw = [3.0, 6.0, 9.0, 1.0]
    #xyzw *= i
    xyzw = [j * i for j in xyzw]
    i = 0
    xyzw = [j / xyzw[-1] for j in xyzw]
    #xyzw /= xyzw[-1]
    return xyzw

print(triple_it(), end = "\n\n")

def layer_it(n = 26, p = 10652200): #!!!CAUTION!!! prone to model overfitting #
    a = [0] * n
    b = [0] * n
    c = [0] * n
    # the inference will need to select the lease wrong answer #
    a = [1 if (x % 3) < 2 else 0 for x in range(0, len(a))]
    b = [1 if (y % 6) < 4 else 0 for y in range(0, len(b))]
    c = [1 - b[z] if (p >> (n - z - 1)) & 1 else b[z] for z in range(0, len(c))]
    return a, b, [a[q] ^ b[q] for q in range(0, len(a))], c # xor not pow #

print(layer_it(), end = "\n\n")
