# AntiMaths - TheMindVirus
# This sketch explores the idea of -0 x -0 being -0 instead of 0.
# The curve is a lot simpler, otherwise it has to alternate using a coefficient of -cos(2n)

def a(n, x = 8):
    return n * pow(x, abs(n))

def b(n, x = 8):
    return max(1, abs(n) - 1) * (x * n)

def y(n, x = 8):
    return a(n, x) - b(n, x)

def edge(n, x = 8):
    return a(n, x) - y(n, x)

def ratio(n, x = 8):
    c = a(n, x)
    return abs(y(n, x) / (c if c else 1))

def reduction(n, x = 8):
    return 100 * (1 - ratio(n, x))

xx = 2 #8 #16 #32 #64
lo = -6
hi = 6

print("__Interconnects__")
for i in range(lo, hi + 1):
    print("{}: {}".format(i, y(i, xx)))
print()

print("__Optimisation__")
for i in range(lo, hi + 1):
    print("{}: {}".format(i, b(i, xx)))
print()

print("__Total__")
for i in range(lo, hi + 1):
    print("{}: {}".format(i, a(i, xx)))
print()

print("__Edge__")
for i in range(lo, hi + 1):
    print("{}: {}".format(i, edge(i, xx)))
print()

print("__Ratio__")
for i in range(lo, hi + 1):
    print("{}: {}".format(i, ratio(i, xx)))
print()

print("__Reduction__")
for i in range(lo, hi + 1):
    print("{}: {:.02f}%".format(i, reduction(i, xx)))
print()

#x=8;n=1;(n*pow(x,abs(n)))-max(1,abs(n)-1)*(x*n)
#(n*pow(x,abs(n)))-max(1,abs(n)-1)*(x*n)
