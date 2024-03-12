# Pascal Network - TheMindVirus
# After some introspection into electronic units of measurement and counting links in a network,
# I stumbled across the third diagonal of Pascal's Triangle...Pascal's Pyramid???

"""
tensors
unit-plus, unit-minus, anti-plus, anti-minus
unit, negative unit, one over unit, negative one over unit
i-unit-plus, i-unit-minus, i-anti-plus, i-anti-minus
imaginary unit, imaginary negative unit, imaginary one over unit, imaginary negative one over unit

cells...wires
voltage/flux...current/charge
volts/webers...amps/coulombs
resistor-ohms...capacitor-farads
anti-resistor...anti-capacitor
transistor-teslas...inductor-henries / henriettas

attack...decay...sustain...release...envelope...resonance
transience/slew...pressure/tolerance...agitation/stasis...moisture/potential...iterations/window...repetitions/spreads
distance/rate...acceleration/force...momenta/inertia...humidity/saturation...bandwidth/wavelength...feedback/ring
meters/hertz...pascals/newtons...joules/watts...hectors/bars...bauds/lambdas...overlaps/loops
anti-velocity...anti-mass...anti-energy...anti-fluid...anti-light...anti-phase
ramp...gravity...fatigue...viscosity...darkness...flange
deltas-deltrons...gals-gallons...stets-stetsons...poises-poissons...bortles-bartons...nipples-nippons

...
"""

"""

[0]: (0)
[1]: (0)
[2]: 1-2 (1)
[3]: 1-2 1-3 2-3 (3)
[4]: 1-2 1-3 1-4 2-3 2-4 3-4 (6)
[5]: 1-2 1-3 1-4 1-5 2-3 2-4 2-5 3-4 3-5 4-5 (10)
[6]: 1-2 1-3 1-4 1-5 1-6 2-3 2-4 2-5 2-6 3-4 3-5 3-6 4-5 4-6 5-6 (15)
[7]: 1-2 1-3 1-4 1-5 1-6 1-7 2-3 2-4 2-5 2-6 2-7 3-4 3-5 3-6 3-7 4-5 4-6 4-7 5-6 5-7 6-7 (21)
[8]: 1-2 1-3 1-4 1-5 1-6 1-7 1-8 2-3 2-4 2-5 2-6 2-7 2-8 3-4 3-5 3-6 3-7 3-8 4-5 4-6 4-7 4-8 5-6 5-7 5-8 6-7 6-8 7-8 (28)
[9]: 1-2 1-3 1-4 1-5 1-6 1-7 1-8 1-9 2-3 2-4 2-5 2-6 2-7 2-8 2-9 3-4 3-5 3-6 3-7 3-8 3-9 4-5 4-6 4-7 4-8 4-9 5-6 5-7 5-8 5-9 6-7 6-8 6-9 7-8 7-9 8-9 (36)

Zeros - Null diagonal of Pascal's Triangle (NC0)
Ones - First diagonal of Pascal's Triangle (NC1)
Units - Second diagonal of Pascal's Triangle (NC2)
Links - Third diagonal of Pascal's Triangle (NC3) <-- This One
Verses - 3+ diagonal of Pascal's Triangle (NCR)

Converse Universal Omniverse, Converse Universal Reverse, Converse Subversive Omniverse, Converse Subversive Reverse
Upper-Top-Right, Upper-Top-Left, Upper-Bottom-Right, Upper-Bottom-Left

Inverse Universal Omniverse, Inverse Universal Reverse, Inverse Subversive Omniverse, Inverse Subversive Reverse
Lower-Top-Right, Lower-Top-Left, Lower-Bottom-Right, Lower-Bottom-Left

O-O
|X|
O-O
"""

def factorial(n):
    sig = -1 if n[0] == "-" else 1
    n = abs(int(n))
    acc = max(1, n)
    for i in range(n - 1, 0, -1):
        acc *= i
    return ("-" if sig == -1 else "") + str(acc)

print(factorial("-6"), factorial("-0"))

def pascal(n, r):
    sig = -1 if n[0] == "-" else 1
    n = str(abs(int(n)))
    r = str(abs(int(r)))
    diff = str(int(n) - int(r))
    acc = int(int(factorial(n)) / (int(factorial(r)) * int(factorial(diff))))
    return ("-" if sig == -1 else "") + str(acc)

print(pascal("-3", "-2"), pascal("-0", "-0"), end = "\n\n")

def triangle(n):
    n = abs(int(n) + 1)
    acc = ""
    for i in range(n -1, -1, -1):
        for j in range(0, abs(i) + 1):
            acc += str(pascal("-" + str(i), str(j))) + " "
        acc += "\n"  
    for i in range(0, n):
        for j in range(0, abs(i) + 1):
            acc += str(pascal(str(i), str(j))) + " "
        acc += "\n"
    return acc

print(triangle("10"))

def diagonal(n, a):
    sig = -1 if n[0] == "-" else 1
    a = abs(int(a))
    n = abs(int(n)) - 1
    acc = []
    for i in range(0, a + n - 1):
        acc.append(("-" if sig == -1 else "") + pascal(str(i), n))
    return acc

print(diagonal("3", "9"), diagonal("-3", "-9"), sep = "\n", end = "\n\n")

def links(n, l = "3"):
    sig = -1 if n[0] == "-" else 1
    s = "-" if sig == -1 else ""
    n = abs(int(n))
    acc = ""
    for i in range(0, n + 1):
        v = ""
        for j in range(1, i):
            for k in range(j, i):
                v += str(j) + "-" + str(k + 1) + " "
        acc += "[{}]: {}({})\n".format(s + str(i), v, s + diagonal(str(l), str(n))[i])
    return acc

print(links("-9"), links("9"), sep = "\n")

def pyramidal(*_, **__):
    pass
    return "???"

print(pyramidal())