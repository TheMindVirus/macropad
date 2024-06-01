# GCD - TheMindVirus
# This sketch aims to make a microarchitectural instruction set
# out of o-level mathematical principles and prime numbers.

# !!! - WARNING: USE WITH CAUTION - Tweaks might be required - !!! #

def PCH(n, s = 2): # Prime Check Heuristic
    if not len(n):
        return 1
    m = max(n)
    c = []
    d = []
    for a in range(s, m + 1):
        is_prime = True
        for b in range(2, a):
            if a % b == 0:
                is_prime = False
                break
        c.append([a, is_prime])
    for i in c:
        if i[1]:
            d.append(i[0])
    return d

def GCD(n, s = -1): # Greatest Common Denominator
    if not len(n):
        return 1
    m = max(n)
    s = m if s < 0 else s
    for a in range(s, 0, -1):
        c = 0
        for i in n:
            if i % a == 0:
                c += 1
            if c == len(n):
                return a
    return a

def LCD(n, s = 3): # Least Common Denominator
    if not len(n):
        return 1
    m = max(n)
    for a in range(s, m + 1):
        c = 0
        for i in n:
            if i % a == 0:
                c += 1
            if c == len(n):
                return a
    return 1

def PFL(n, s = 2): # Prime Factor List
    if not len(n):
        return [{}]
    m = max(n)
    c = []
    d = PCH(n, s)
    for i in range(0, len(n)):
        r = n[i]
        p = 1
        c.append(dict())
        #print(r)
        while (r > 1):
            for j in d:
                p = j
                if r % j == 0:
                    r = r / p
                    break
            #print(r, p)
            try:
                c[i][p] += 1
            except:
                c[i][p] = 1
    return c

def PFA(n, s = 2): # Prime Factor Accumulate
    if not len(n):
        return [{}]
    c = PFL(n, s)
    d = dict()
    for i in c:
        p = list(i.keys())
        for j in range(0, len(p)):
            try:
                d[p[j]] += i[p[j]]
            except:
                d[p[j]] = i[p[j]]
    return [d]

def HCM(n, s = 2): # Highest Common Multiple
    c = PFA(n, s)[0]
    p = list(c.keys())
    q = list(c.values())
    d = 1
    for i in range(0, len(p)):
        d *= pow(p[i], q[i])
        #print(d)
    return d

def LCM(n, s = 2, _s = -1): # Lowest Common Multiple
    return int(HCM(n, s) / GCD(n, _s))

#data = [ ]
#data = [ 1 ]
data = [ 48, 180 ]
#data = [8, 9, 21]
#data = [ 16, 32, 64 ]
print(data)
print("GCD:", GCD(data))
print("LCD:", LCD(data))
print("PFL:", PFL(data))
print("PFA:", PFA(data))
print("HCM:", HCM(data))
print("LCM:", LCM(data))

"""
[48, 180]
GCD: 12
LCD: 3
PFL: [{2: 4, 3: 1}, {2: 2, 3: 2, 5: 1}]
PFA: [{2: 6, 3: 3, 5: 1}]
HCM: 8640
LCM: 720
"""
