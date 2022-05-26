```py
# Gray Code - Alastair Cota
# Gray Code monitors changes to bits in a bit stream of certain endianness
# Variants are used in protocols such as USB to minimise heat on the cable
# and Rotary Potentiometers (Knobs) use Gray Code to encode knob positions

# e.g. 1 => 0 changes to a 1 so write a 1
# e.g. 11 => 1 didn't change so write a 0
# e.g. 110 => 1 changed to 0 so write a 1

# e.g. 1 => 0 changed to a 1 so write a 1
# e.g. 0 => not changed to 0 so write a 1
# e.g. 1 => has changed to 0 so write a 0

def main():
    a = "0b0100"
    b = bin2gray(a)
    c = gray2bin(b)

    print(a)
    print(b)
    print(c)

    automated_test(0b1111)

def bin2list(a):
    a = list(a[2:])
    b = a
    for i in range(0, len(a)):
        b[i] = int(a[i], 2)
    print(b)
    return b

def list2bin(a):
    print(a)
    inter = "0b" + ("".join(str(i) for i in a))
    return ("0b{:0" + str(len(a)) + "b}").format(int(inter, 2))

def bin2gray(a):
    a = bin2list(a)
    b = a
    last = len(a) - 1
    for i in range(last -1, 0, -1):
        b[i] = (int(a[i]) + int(a[max(i - 1, 0)])) & 1
    b[last] = a[last]
    return list2bin(b)

def gray2bin(a):
    a = bin2list(a)
    b = a
    last = len(a) - 1
    for i in range(1, last):
        b[i] = (int(b[i - 1]) + int(a[i])) & 1
    return list2bin(b)

def automated_test(n):
    fails = 0
    for i in range(0, n + 1):
        a = bin(i)
        b = bin2gray(a)
        c = gray2bin(b)
        if a == c:
            print("[PASS]")
        else:
            print("[FAIL]")
            fails += 1
    if fails == 0:
        print("OUTCOME: [PASS]")
    else:
        print("OUTCOME: [FAIL]")

if __name__ == "__main__":
    main()
```