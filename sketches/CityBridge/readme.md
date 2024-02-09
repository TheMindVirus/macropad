```py
# City Bridge - TheMindVirus
# This script uses a non-binary counter to collimate numbers into fields.
# It then uses the counter to reduce a list of city bridge names, filtered by a set of criteria.

print("[INFO]:", "\nNow Loading\nPlease Wait...") # ... ... This might take a little while :| ... ...

abc = "abcdefghijklmnopqrstuvwxyz"
aiu = "aeiou" + "yn"
aic = "bcdfghjklmnpqrstvwxz"
sz = len(abc)
vz = len(aiu)
nz = len(aic)
n = 5

#for i in range(0, 100):
#    print(i, int(i / (n * n)) % n, int(i / n) % n, i % n)

def counter(n = 100, m = 5, e = 3):
    ct = []
    for i in range(0, n + 1):
        t = [i]
        for j in range(e -1, -1, -1):
            t.append(int(i / pow(m, j)) % m)
        ct.append(t)
    return ct

def print_matrix(data, separator = "\n", delimeter = ", ", padding = " ", pad = 8):
    print(separator.join([str(delimeter.join([(padding * (pad - min(pad, len(str(item))))) + str(item) for item in record]) + delimeter) for record in data]))
"""
count = 0
total = pow(sz, n)
for i in range(0, total):
    city = ""
    for j in range(0, n):
        t = int(i / pow(sz, n - j - 2)) % sz
        c = abc[t]
        if j == (1) - 1:
            city += c.upper()
        elif j == (5) - 1:
            city += "a"
        else:
            city += c
    if city[(2) - 1] in aiu \
    and city[(4) - 1] in aic:
        #print(city)
        count += 1

print("[INFO]:", count, "City Bridge Names out of", end = " "              )
print(total, "in Total", "({} {})".format(total - count, "Entries Reduced"))
percentage = (count / total) * 100
preduction = 100 - percentage
print("[INFO]:", "{:.02f}%".format(percentage), "Fraction", end = " _|||_ ")
print(           "{:.02f}%".format(preduction), "Reduction"                )
"""
print("[INFO]: BEGIN_DATA")
print_matrix(counter())
print("[INFO]: END_DATA")

print("[INFO]: Done!")
```