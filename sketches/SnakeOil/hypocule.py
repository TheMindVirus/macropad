# Iterate a Batch Loop Kernel # Spin a textured Wheel #
# Resonate a Patch Grid Matrix # Look for a Pattern #
# Culminate a Latch Spot Oculus # Stick with what Works #

# Iterate a Batch Loop Kernel #

print("\n_Batch_Loop_Kernel_\n")

def rol(data):
    sz = len(data)
    tmp = data[0]
    for i in range(0, sz):
        data[i] = data[(i - 1) % sz]
    data[-1] = tmp
    return data

def mov(data):
    for i in range(0, len(data)):
        data[i] = 1 - (data[i])
    return data

def add(data):
    data[-1] = 1
    return data

def ret(data):
    data[-1] = 0
    return data

asm = \
[
    ["rol", rol], # rotate (roller skates shift)
    ["mov", mov], # translate (moving light pan)
    ["add", add], # dilate (additional info sum)
    ["ret", ret], # reflect (yield return print)
]

rolls = len(asm)
comb = pow(rolls, rolls)

counters = [0] * rolls
indices = []
kernels = []

for i in range(0, comb):
    unique = True
    for j in range(0, rolls):
        if counters.count(j) > 1:
            unique = False
    if unique:
        indices.append(counters[:])
    for j in range(0, rolls):
        counters[j] += 1
        if counters[j] >= rolls:
            counters[j] = 0
        else:
            break

records = len(indices)
#kernels = [[asm[j] for j in indices[i]] for i in range(records -1, -1, -1)]
#methods = [[asm[j].__name__ for j in indices[i]] for i in range(records -1, -1, -1)]
kernels = [[asm[j][1] for j in indices[i]] for i in range(records -1, -1, -1)]
methods = [[asm[j][0] for j in indices[i]] for i in range(records -1, -1, -1)]

bits = 8
rounds = 10
results = [[0] * bits] * records

for i in range(0, rounds):
    for j in range(0, records):
        for k in range(0, rolls):
            results[j] = kernels[j][k](results[j][:])

index = [str(indices[i]) + str(methods[i]) + str(results[i]) for i in range(0, records)]
print("\n".join(index))

# Resonate a Patch Grid Matrix #

print("\n_Patch_Grid_Matrix_\n")

a = 1 #15
b = 8 #32
c = 6 #6

print("[INFO]:", "A wants to call C in an " + str(b) + "-bit network")
print("[INFO]:", "A has the number " + str(a) + " and needs to dial " + str(c))

i = 0
j = 0
called = False
for i in range(0, b):
    if i == c:
        for j in range(0, b):
            if j == a:
                called = True
                break
        if called:
            break
print("[CALL]:", called, str(i) + "+" + str(j), "(" + str(i + j) + " iterations)")
        
# Culminate a Latch Spot Oculus #

print("\n_Latch_Spot_Oculus_\n")

a_x_b = a * b
b_x_b = b * b

print(a, b, c)

A = bin(a)
B = bin(b)
C = bin(c)

print(A, B, C)

D = (pow(2, b_x_b) - 1)
E = D - (1 << ((a_x_b) + c))
F = ("{:0" + str(b_x_b) + "b}").format(E)

print(D, E, F)

G = F.replace("0", "2").replace("1", "0").replace("2", "1")
H = int(G, 2)
I = str(H)

print(G, H, I)

print("Thread the result on " + str(b_x_b) + "-bit multicore router processing pipeline")
