# Threading Without Threading #

print("\n_Threading_Without_Threading_\n")

#import threading

a = 0b10011001
b = 8
c = [0] * b

ns = 5
nss = ns * 2
matrix = []

for x in range(0, b):
    c[x] = (a >> x) & 1

msg_data = ["HELLO", "WORLD!"]

tmp_data = \
"""
HW
EO
LR
LL
OD
 !
""" #.removeprefix("\n").removesuffix("\n")
tmp_data = tmp_data[1:len(tmp_data)-1]

def threaded_print(msgs, indent = nss):
    max_len = 0
    for i in msgs:
        sz = len(i)
        if sz > max_len:
            max_len = sz
    for i in range(0, max_len):
        print(" " * indent, end = " ")
        for j in range(0, len(msg_data)):
            if i < len(msg_data[j]):
                print(msg_data[j][i], end = "")
            else:
                print(" ", end = "")
        print()

def threaded_buffer(msgs, indent = nss):
    max_len = 0
    for i in msgs:
        sz = len(i)
        if sz > max_len:
            max_len = sz
    buffer = ""
    for i in range(0, max_len):
        buffer += " " * (indent + 1)
        for j in range(0, len(msg_data)):
            if i < len(msg_data[j]):
                buffer += msg_data[j][i]
            else:
                buffer += " "
        buffer += "\n"
    return buffer

def threaded_spec():
    for i in tmp_data.split("\n"):
        print(" " * (nss), i)
    threaded_print(msg_data)
    print(threaded_buffer(msg_data), end = "")
threaded_spec()

# Multiple Parallel Rotors #

print("\n_Multiple_Parallel_Rotors_\n")

for i in range(0, ns):
    print(c)
    if i != ns - 1:
        print(" " * (ns + i), "#" * ((nss + 2) - (2 * i)))
        #print(" " * ns, "\b" * len(str(c)))
    tmp = c[0]
    for j in range(0, b - 1):
        c[j] = c[j + 1]
    c[-1] = tmp

# Exchange Aggregator Cabasa #

print("\n_Exchange_Aggregator_Cabasa_\n")

for i in range(0, b):
    template = [[0] * b]
    matrix += template[:]

for i in range(1, b):
    matrix[0][i] = i
    matrix[i][0] = i

for i in range(1, b):
    for j in range(1, b):
        matrix[i][j] = i ^ j

print("\n".join([str(i) for i in matrix]))

# Multicast Address Pipeline #

print("\n_Multicast_Address_Pipeline_\n")

msg = 4165385116089503914822723506981544234729075658905412581529231370
mtu = 1500
pdu = 0

x = msg
y = ""
z = 0

for i in range(0, mtu):
    c = x & 0xFF
    if c == 0:
        break
    x >>= 8
    y += chr(c)
    z += 1
pdu = z

pos = 25
y = y[:pos] + "(" + str(z) + ")" + y[pos:]
print(y)

print("\n| Aperture Science Carilien Hypercule |\n", end = "")