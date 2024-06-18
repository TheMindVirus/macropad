```
# MacronDAC - TheMindVirus
# A numeric system whereby each digit has a minus sign above (macron) and below (micron)
# Variants of Digital to Analog Converter for Audio Signals simulating PCM to PWM low-resolution conversion

n = 64.32 # "-64.32"
m = "32 10" # "332310"
macron = "\u0303"
micron = "\u0330"

def bar(n):
    return "".join([macron + micron + i for i in str(n)])

def double_sign(n, m, e = True):
    acc = ""
    dat = str(n)
    for i in range(0, len(dat)):
        if e:
            acc += dat[i]
        if m[i] == "1" or m[i] == "3":
            acc += macron
        if m[i] == "2" or m[i] == "3":
            acc += micron
        if not e:
            acc += dat[i]
    return acc

def DEC2PCM(dec_mid):
    return [abs(int(max(0, dec_mid))), abs(int(max(0, -dec_mid)))]

def PCM2DEC(dec_pos, dec_neg):
    return dec_pos - dec_neg

def PCM2PWM(adc_pos, adc_neg, adc_max = 1024, pwm_max = 127):
    adc_pos = abs(int(adc_pos))
    adc_neg = abs(int(adc_neg))
    adc_mid = abs(int(adc_max / 2))
    pwm_mid = abs(int(pwm_max / 2))
    pwm_mul = float(pwm_max / adc_max)
    return [abs(int(pwm_mid + int(adc_pos * pwm_mul) - int(adc_neg * pwm_mul)))]

def PWM2PCM(pwm_pos, adc_max = 1024, pwm_max = 127):
    pwm_pos = abs(int(pwm_pos - 0))
    adc_mid = abs(int(adc_max / 2))
    pwm_mid = abs(int(pwm_max / 2))
    pwm_div = float(adc_max / pwm_max)
    return DEC2PCM(int((pwm_pos * pwm_div) - adc_mid))

def test():
    print(bar(n), double_sign(n, m))
    print(-32.0, PCM2PWM(0, -32.0), PCM2DEC(*PWM2PCM(*PCM2PWM(*DEC2PCM(-32.0)))))
    print(-32.0, PCM2PWM(0, -32.0), PCM2DEC(*PWM2PCM(*PCM2PWM(*DEC2PCM(-32.0), adc_max = 65535, pwm_max = 65535), adc_max = 65535, pwm_max = 65535)))
    print()

import collections

class addict: #(dict):
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        self.data = collections.OrderedDict() # ++
        self.ref = 0
    def add(self, item):
        #self.__setitem__(self.ref, item)
        self.data[self.ref] = item # ++
        self.ref += 1
    def item(addict, item, default):
        try:
            return addict[item]
        except:
            return default

    def __iter__(self): # ++
        return iter(list(self.data.keys())) # ++
    def __getitem__(self, item): # ++
        try: # ++
            return self.data[item] # ++
        except: # ++
            return []
            #raise IndexError() # ++
    def __setitem__(self, item, value): # ++
        self.data[item] = value # ++
    def __repr__(self): # ++
        return str(self.data) # ++
        
mods = addict()

mod = \
{
    "names":
    {
        "Mod1",
    },
    "items":
    {
        0: "Converter", # Zero State Stream
        1: "Analog",    # One State Stream
        2: "Digital",   # Two State Stream
        3: "Ternary",   # Three State Stream
        4: "Pulse",     # N-State Stream
        5: "Granular",  # 0.N-State Stream
    },
    "augments":
    {
        "tween": " to ",
        "sep": " ",
    }
}
mods.add(mod)

mod = \
{
    "names":
    {
        "Mod2",
    },
    "items":
    {
        0:  "Nilary",  # Zero State Stream
        1:  "Unary",   # One State Stream
        2:  "Binary",  # Two State Stream
        3:  "Ternary", # Three State Stream
        4:  "Quantum", # Four State Stream
        5:  "Vintage", # Five State Stream
        6:  "Hexery",  # Six State Stream (ABCDEF)
        7:  "Septary", # Seven State Stream
        8:  "Octuary", # Eight State Stream
        9:  "Chinary", # Nine State Stream
        10: "Xeniary", # Ten State Stream
    },
    "augments":
    {
        "tween": "-",
        "sep": "-",
    }
}
mods.add(mod)

mod = \
{
    "names":
    {
        "Mod3",
    },
    "items":
    {
        0: "Zilla", # Zero State Stream
        1: "Una", # One State Stream
        2: "Dua", # Two State Stream
        3: "Tria", # Three State Stream
        4: "Quadra", # Four State Stream
        5: "Penta", # Five State Stream
        6: "Hexa", # Six State Stream
        7: "Septa", # Seven State Stream
        8: "Octa" , # Eight State Stream
        9: "Nona", # Nine State Stream
        10: "Xena", # Ten State Stream
    },
    "augments":
    {
        "sep": " ",
        "tween": " ",
        "suffix1": "gem",
        "suffix2": "gen",
    }
}
mods.add(mod)

mod = \
{
    "names":
    {
        "Mod4",
    },
    "items":
    {
        0: "en-ni-al", # Zero State Stream
        1: "Sept",     # Seven State Stream
        2: "Cent",     # Hundred State Stream
    },
    "augments":
    {
        "tween": "-u-a-",
        "sep": "-",
    }
}
mods.add(mod)

def detail_mod(mod):
    z = 0
    details = {}
    labels = []
    names = list(mod["names"])
    items = list(mod["items"].items())
    augments = mod["augments"]
    suffix1 = addict.item(augments, "suffix1", "")
    suffix2 = addict.item(augments, "suffix2", "")
    tween = addict.item(augments, "tween", "")
    sep = addict.item(augments, "sep", "")
    for j in range(0, len(items)):
        if j == 0:
            continue
        for i in range(0, len(items)):
            if i == 0:
                continue
            details[z] = "" + \
                items[j][1] + suffix1 + tween + \
                items[i][1] + suffix2 + sep + items[0][1]
            labels.append(items[j][1][0] + items[i][1][0] + items[0][1][0])
            z += 1
    return names, labels, details

def pad(data, insert = "0", indent = 4):
    return (str(insert) * (indent - len(str(data)))) + str(data)

def print_mods(mods):
    for mod in mods:
        names, labels, details = detail_mod(mods[mod])
        name = "[" + ", ".join([str(name) for name in names]) + "]"
        print(name)
        i = 0 # ++
        for item in details:
            print(pad(item), "-", labels[i], "-", details[item])
            i += 1 # ++
        print()

if __name__ == "__main__":
    test()
    print_mods(mods)
    pass
```