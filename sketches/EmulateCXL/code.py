# CXL Stack Recovery Emulation - Alastair Cota
# This sketch emulates a minimal emulation of a basic stack found in CPU's
# and demonstrates how Compute eXpress Link (CXL) can assist with C++ pointer issues

length = (16 * 2)
memory = [0x00] * length
#SP = None # Stackless
SP = length
RA = None # Returns
CXL = dict()

def print_memory(m):
    print(" " + " ".join(["{:02X}{}".format(m[i], "" if (i + 1) % 16 else "\n") for i in range(0, len(m))]), end = "")

def push():
    global SP
    tmp = SP
    SP -= 16
    return tmp

def pop(i):
    global SP
    SP = i
    return SP # ---

def c_str(ptr):
    buffer = ""
    for i in range(ptr-1,-1,-1):
        if memory[i] == 0x00:
            break
        buffer += chr(memory[i])
    return buffer

def strlen(ptr):
    count = 0
    for i in range(ptr-1,-1,-1):
        if memory[i] == 0x00:
            break
        count += 1
    return count

def alloc(string):
    global SP, memory
    for i in range(0, len(string)):
        memory[SP - i - 1] = ord(string[i])
    return SP

def Cfunction():
    global SP, memory
    i = push()
    print("[SPDC]:", SP)
    pointer = alloc("Hello")
    CXL["remember"] = pointer
    SP -= strlen(pointer) + 1
    print("[SPDR]:", SP)
    alloc("Something")
    #RA = pointer # return
    #RA = SP # ???
    RA = pop(i)
    return RA # The sun god?

def main():
    err = alloc("WALLE")
    print_memory(memory)
    print("[SPBC]:", SP)
    result = Cfunction()
    print("[SPAC]:", SP)
    print_memory(memory)
    print(c_str(result))

    if (result == err):
       print("[WARN]:", "SIGSEGV:", "Segmentation Fault")

    result = CXL["remember"]
    print("[_CXL]:", c_str(result))
    print("[INFO]:", "Done!")

main()
while True:
    pass

