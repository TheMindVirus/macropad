# Abacus - TheMindVirus
# This sketch aims to simplify the nested counting structure often found in for loops
# whereby at each stage the next counter is incremented when the current one is full.

class abacus:
    def __init__(self, count = [], beads = []):
        self.count = count
        self.beads = beads

    def addBeads(self, count = 10):
        count = 1 if count == 0 else abs(count)
        self.count.append(count)
        self.beads.append(0)

    def getBeads(self):
        count = 0
        for i in range(0, len(self.count)):
            count += self.count[i]
        return count
    
    def getTotal(self):
        count = 1 if len(self.count) > 0 else 0
        for i in range(0, len(self.count)):
            count *= self.count[i]
        return count

    def rollBeads(self):
        for i in range(0, len(self.count)):
            self.beads[i] += 1
            if self.beads[i] < self.count[i]:
                break
            else:
                self.beads[i] = 0

    def __getitem__(self, value):
        return self.beads[value]

    def __add__(self, value):
        self.addBeads(value)
        return self

    def __call__(self, value = 1):
        for i in range(0, value):
            self.rollBeads()
        return self

    def __repr__(self):
        data = "["
        total = len(self.count)
        for i in range(0, total):
            data += str(self.beads[i] + 1) + "/" + str(self.count[i])
            if i < total - 1:
                data += ", "
        data += "]"
        return data

abc = "abcdefghijklmnopqrstuvwxyz"
cns = "bcdfghjklmnpqrstvwxyz"
vwl = "aeiou"

#sz = len(abc)
#t = pow(sz, 4)
#x = y = z = w = 0

szc = len(cns)
szv = len(vwl)

x = abacus()
x += szc
x += szv
x += szv
x += szc
#szt = x.getBeads()
szt = x.getTotal()

for i in range(0, szt):
    print(cns[x[0]] + vwl[x[1]] + "nn" + vwl[x[2]] + cns[x[3]])
    if i == szt - 1:
        print(x)
    x()

"""
szt = szc * szv * szv * szc
x = y = z = w = 0

for i in range(0, szt):
    print(cns[x] + vwl[y] + "nn" + vwl[z] + cns[w])
    x += 1
    if x >= szc:
        x = 0
        y += 1
        if y >= szv:
            y = 0
            z += 1
            if z >= szv:
                z = 0
                w += 1
                if w >= szc:
                    w = 0
"""
"""
arl = []
arl.append(szc)
arl.append(szv)
arl.append(szv)
arl.append(szc)
szl = len(arl)
arr = [0] * szl
szt = 1
for i in range(0, szl):
    szt *= arl[i]

for i in range(0, szt):
    print(cns[arr[0]] + vwl[arr[1]] + "nn" + vwl[arr[2]] + cns[arr[3]])
    for x in range(0, szl):
        arr[x] += 1
        if arr[x] < arl[x]:
            break
        else:
            arr[x] = 0
"""
"""
[0/21, 0/5, 0/5, 0/21]
[21/21, 5/5, 5/5, 21/21]
"""