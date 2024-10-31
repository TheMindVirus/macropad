```py
# Snake Oil Test Hypocule - TheMindVirus
# Snake Oil is a Test Hypocule written in Python and ported to CircuitPython
# Snake Oil contains a bunch of Test Programs which all use Shared Utilities

def main():
    print("\n<<<Snake Oil Test Hypocule>>>\n")
    test_sipo_chip_select()
    test_binary_rotation_compressor()
    test_message_diff_extraction()
    test_checksum_decoder_parity()
    print("\n<<<Snake Oil Test Hypocule>>>\n")

# Shared Utilities

def str2bin(data):
    buffer = ""
    for i in range(0, len(data)):
        buffer += "{:08b}".format(ord(data[i]))
    return buffer

def bin2str(data):
    buffer = ""
    for i in range(0, len(data), 8):
        buffer += chr(int(data[i:i+8], 2))
    return buffer

class bus():
    def __init__(self):
        self.labels = []
        self.values = []

    def __getitem__(self, item):
        idx = self.labels.index(item)
        return self.values[idx]

    def __setitem__(self, item, value):      
        if self.labels.count(item):
            idx = self.labels.index(item)
            self.values[idx] = value
        else:
            self.labels.append(item)
            self.values.append(value)

    def __add__(self, _bus):
        labels = []
        labels += self.labels
        labels += _bus.labels
        c = bus()
        for i in range(0, len(self.labels)):
            c[self.labels[i]] = self.values[i]
        for i in range(0, len(_bus.labels)):
            c[_bus.labels[i]] = _bus.values[i]
        return c

    def __sub__(self, item):
        idx = self.labels.index(item)
        self.labels.pop(idx)
        self.values.pop(idx)

    def __repr__(self):
        data = "{ "
        size = len(self.labels)
        for i in range(0, size):
            data += "\""
            data += self.labels[i]
            data += "\": "
            data += str(self.values[i])
            if i != size - 1:
                data += ", "
        data += " }"
        return data

def test_track(data, stack = [], verbose = True):
    if len(stack) > 0:
        stack[0].append(data)
    if verbose:
        print("{} ({})".format(data, len(data)))

# Address Peripheral Data Bus

def address_bus(n = 3, init = 1):
    selector = bus() # dict()
    for i in range(0, n):
        selector["S" + str(i)] = init
    return selector

def peripheral_bus(n = 5, offset = 3, init = 2):
    peripheral = bus() # dict()
    for i in range(0, n):
        peripheral["B" + str(i + offset)] = init
    return peripheral

def data_bus(n = 1, m = 3, k = 8):
    data = bus()
    for i in range(0, n):
        raw = bus()
        raw += address_bus(m, 0)
        raw += peripheral_bus(k - m, m, 0)
        data["D" + str(i)] = raw
    return data

# SIPO Chip Select

def set_label(_bus, label, _label = None):
    _bus[label] = _bus[_label]
    _bus -= _label

def set_channel(_bus, ch = 0, nch = 3, label = None):
    ch %= pow(2, nch)
    for i in range(0, nch):
        _bus[label]["S" + str(i)] = 1 if ((ch >> (nch - i - 1)) & 1) > 0 else 0

def set_info(_bus, dat = 0, ndat = 5, nch = 3, label = None):
    dat %= pow(2, ndat)
    for i in range(0, ndat):
        _bus[label]["B" + str(i + nch)] = 1 if ((dat >> (ndat - i - 1)) & 1) > 0 else 0

def get_info(_bus, nch = 3, ndat = 5, label = None):
    ch = 0
    dat = 0
    _label = _bus.labels[0]
    if label:
        _label = label
    for i in range(0, nch):
        ch += _bus[_label]["S" + str(nch - i - 1)] << i
    for i in range(0, ndat):
        dat += _bus[_label]["B" + str(ndat - i - 1 + nch)] << i
    return [ch, dat]

def set_data(_bus, ch = 0, dat = 0, nch = 3, ndat = 5, label = None):
    ch %= pow(2, nch)
    dat %= pow(2, ndat)
    for i in _bus:
        _ch, _dat = get_info(i)
        if ch == _ch:
            _label = i.labels[0]
            if label:
                _label = label
            set_info(i, dat, label = _label)

def show_data(_bus):
    for i in _bus:
         print(i, end = "\n", sep = "")

def test_sipo_chip_select():
    print("_SIPO_Chip_Select_")

    C = []
    for i in range(0, 4):
        C.append(data_bus())
        label = "C" + str(i)
        set_label(C[i], label, "D0")
        set_channel(C[i], i, label = label)
        set_info(C[i], 0, label = label)

    set_data(C, 2, 31)
    set_data(C, 0, 30)
    show_data(C)
    
    print()

# Binary Rotation Compressor

def rotary(stream, n = 8):
    stream = "".join([x if x == "0" or x == "1" else "" for x in stream])
    stream = "0" * ((n - len(stream)) % n) + stream
    diffs = []
    prev = 0
    mod = pow(2, n)
    for i in range(0, len(stream), n):
        curr = int(stream[i:i+n], 2)
        diff = (curr - prev) % mod
        diffs.append(diff)
        prev = curr
    return diffs

def respin(diffs, n = 8):
    stream = ""
    prev = 0
    mod = pow(2, n)
    for i in range(0, len(diffs)):
        diff = (prev + diffs[i]) % mod
        curr = ("{:0" + str(n) + "b}").format(diff)
        stream += curr
        prev = diff
    return stream

def test_binary_rotation_compressor():
    print("_Binary_Rotation_Compressor_")

    mod = 3
    a = "000 111 000 111"
    b = a.count("1")
    c = a.count("0")
    d = "".join([x if x == "0" or x == "1" else "" for x in a])
    d = len(d.replace(" ", ""))
    print(a, "\n", b, " ones ", c, " zeros ", "\n",
          d, " bytes encoding ", d, " bits", sep = "")

    e = rotary(a, mod)
    print(str(e) + ", " + str(mod))
    print((str(e) + "_" + str(mod)).replace(",", "-").replace(" ", "").replace("[", "").replace("]", ""))

    f = respin(e, mod)
    print(f)
    print(" ".join([f[i:i+3] for i in range(0, len(f), mod)]))
    
    print()

# Message Diff Extraction

def forward(msg):
    sz = len(msg)
    return rotary(str2bin(msg), sz), sz

def backward(count, diffs):
    pos = len(diffs) - count - 1
    return bin2str(respin(*diffs[pos]))

def test_message_diff_extraction():
    print("_Message_Diff_Extraction_")

    msg_stack = []

    msg_stack.append(forward("Some Sample Text. "))
    msg_stack.append(forward("Even More Sample Text. "))
    msg_stack.append(forward("A bit less text. "))

    msg_stack.append(forward("Some Sample Text2. "))
    msg_stack.append(forward("Even More Sample Text2. "))
    msg_stack.append(forward("A bit less text2. "))

    #print(msg_stack)
    print("\n".join([str(i) for i in msg_stack]))

    msg_track = []

    for i in range(len(msg_stack) -1, -1, -1):
        msg_track.append(backward(i, msg_stack))

    #print(msg_track)
    print("\n".join([i for i in msg_track]))
    
    print()

# Checksum Decoder Parity

class md5_context:
    standard = "RFC_1321"
    c0 = 0
    c1 = 0
    s0 = -1
    s1 = -1
    sz = 64
    buffer = [0] * sz
    digest = [0] * 16
    stack = pow(2, 32)

def md5_bit(F = "F", x = 0, y = 0, z = 0):
    if F == "F":
        return (((x) & (y)) | ((~x) & (z)))
    if F == "G":
        return (((x) & (z)) | ((y) & (~z)))
    if F == "H":
        return ((x) ^ (y) ^ (z))
    if F == "I":
        return ((y) ^ ((x) | (~z)))
    if F == "R":
        x %= pow(2, 32)
        rol = ((x) << (y)) | ((x) >> (32 - (y)))
        rol2 = rol % pow(2, 32)
        return rol2 #!!!

def md5_bit_bit(F = "F", a = 0, b = 0, c = 0, d = 0, x = 0, s = 0, ac = 0):
    a += md5_bit(F, b, c, d) + x + ac
    a = md5_bit("R", a, s)
    a += b
    return a

def md5_splice(a, az = 0, idx = 0, b = [], sz = 0):
    buffer = []
    buffer += a[:idx]
    buffer += b[:sz]
    buffer += a[idx:]
    buffer = buffer[:az]
    return buffer

def md5_clamp(a, stack = pow(2, 32)):
    for x in range(0, len(a)):
        a[x] %= stack
    return a

def md5_rotor(a):
    b = a[:]
    for x in range(1, len(a)):
        b[x] = a[x - 1]
    b[0] = a[-1]
    return b

def md5_pad(data, sz = 64):
    buffer = [0] * sz
    nsz = min(sz, len(data))
    for i in range(0, nsz):
        buffer[i] = data[i]
    return buffer

def md5_transform(ctx):
    H = \
    [
        0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
        0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
        0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
        0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
        0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
        0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
        0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
        0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
        0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
        0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
        0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
        0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
        0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
        0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391,
    ]
    
    K = \
    [
         7, 12, 17, 22,   7, 12, 17, 22,   7, 12, 17, 22,   7, 12, 17, 22,
         5,  9, 14, 20,   5,  9, 14, 20,   5,  9, 14, 20,   5,  9, 14, 20,
         4, 11, 16, 23,   4, 11, 16, 23,   4, 11, 16, 23,   4, 11, 16, 23,
         6, 10, 15, 21,   6, 10, 15, 21,   6, 10, 15, 21,   6, 10, 15, 21,
    ]

    P = [ "A", "B", "C", "D" ]
    F = [ "F", "G", "H", "I" ]
    S = [ 0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476 ]

    X = \
    [
         0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,
         1,  6, 11,  0,  5, 10, 15,  4,  9, 14,  3,  8, 13,  2,  7, 12,
         5,  8, 11, 14,  1,  4,  7, 10, 13,  0,  3,  6,  9, 12, 15,  2,
         0,  7, 14,  5, 12,  3, 10,  1,  8, 15,  6, 13,  4, 11,  2,  9,
    ]

    s0 = ctx.s0 if ctx.s0 != -1 else S[:] # deep copy required for correct function
    s1 = S[:] #ctx.s1 if ctx.s1 != -1 else S
    
    t = md5_pad(ctx.buffer, ctx.sz)
    x = md5_decode(t, ctx.sz)
    #x = t
    #print(x)

    f = 0
    p = P[:]
    for i in range(0, 64):
        f = int(i / 16)
        #print(F[f], *p, "\t", X[i], "\t", K[i], "\t", "0x{:08X}".format(H[i]))
        #s0[0] = md5_bit_bit(F[f], *s0, x[X[i]], K[i], H[i]) #!!!
        s0[0] = md5_bit_bit(F[f], s0[0], s0[1], s0[2], s0[3], x[X[i]], K[i], H[i]) #!!!
        s0 = md5_clamp(s0)
        #print(i, s0, ctx.stack)
        p = md5_rotor(p)
        s0 = md5_rotor(s0)
    for i in range(0, len(s0)):
        s1[i] += s0[i]
        s1 = md5_clamp(s1)

    ctx.s0 = s0
    ctx.s1 = s1
    return ctx

def md5_encode(data, sz):
    i = 0
    buffer = [0] * sz
    for j in range(0, sz, 4):
        buffer[j    ] = (data[i]      ) & 0xFF
        buffer[j + 1] = (data[i] >>  8) & 0xFF
        buffer[j + 2] = (data[i] >> 16) & 0xFF
        buffer[j + 3] = (data[i] >> 24) & 0xFF
        i += 1
    return buffer

def md5_decode(data, sz):
    i = 0
    buffer = [0] * sz
    for j in range(0, sz, 4):
        buffer[i] = (data[j    ]      ) \
                  | (data[j + 1] <<  8) \
                  | (data[j + 2] << 16) \
                  | (data[j + 3] << 24)
        i += 1
    return buffer

def md5_process(ctx, data, sz):
    ii = 0
    idx = 0
    part = 0

    idx = (ctx.c0 >> 3) & 0x3F
    ctx.c0 += (sz << 3)
    if ctx.c0 < (sz << 3):
        ctx.c1 += 1

    ctx.c1 += sz >> 29
    part = 64 - idx
    if sz >= part:
        #print(len(ctx.buffer))
        ctx.buffer = md5_splice(ctx.buffer, ctx.sz, idx, data[:part], part)
        ctx = md5_transform(ctx)
        ii = part
        for i in range(part, sz - 63, 64):
            ii = i
            ctx = md5_transform(ctx)
        idx = 0
    else:
        #print(sz, part)
        ii = 0
    
    part2 = sz - ii
    #print("PART2:", part2, idx)
    ctx.buffer = md5_splice(ctx.buffer, ctx.sz, idx, data[ii:ii+part2], part2)
    #print("BUFFER:", ctx.buffer, len(ctx.buffer))
    return ctx

def md5_final(ctx):
    bits = "0" * 8
    idx2 = 0
    pad = 0
    padding = md5_pad([0x80], 64)
    count = [ctx.c0, ctx.c1]
    bits = md5_encode(count, 8)
    idx2 = (ctx.c0 >> 3) & 0x3F
    pad = (56 - idx2) if (idx2 < 56) else (120 - idx2)
    ctx = md5_process(ctx, padding, pad)
    ctx = md5_process(ctx, bits, 8)
    state = ctx.s1 # not ctx.s0
    ctx.digest = md5_encode(state, 16)
    hex_digest = ""
    for i in range(0, 16):
        hex_digest += "{:02x}".format(ctx.digest[i])
    return hex_digest

def md5_checksum(data = ""):
    txt = data.encode()
    ctx = md5_context()
    ctx = md5_process(ctx, txt, len(txt))
    return md5_final(ctx)

def test_checksum_decoder_parity():
    print("_Checksum_Decoder_Parity_")
    
    _TXT_ = "Multiple of Four"
    _SZ_ = len(_TXT_)
    _RAW_ = md5_decode(_TXT_.encode(), _SZ_)
    _A_ = md5_encode(_RAW_, _SZ_)
    print("[ENCODE]:", ",".join([str(x) for x in _A_]))
    _B_ = md5_decode(_A_, _SZ_)
    _SZ2_ = int(_SZ_ / 4)
    _C_ = "".join([chr(i) for i in md5_encode(_B_, _SZ_)])
    print("[DECODE]:", _B_[:_SZ2_], _C_)

    test_stack = [[]]

    test_track("File.txt", test_stack)
    test_track(str2bin(test_stack[0][-1]), test_stack)
    test_track(rotary(test_stack[0][-1]), test_stack)
    test_track(respin(test_stack[0][-1]), test_stack)
    test_track(bin2str(test_stack[0][-1]), test_stack)
    test_track(md5_checksum(test_stack[0][-1]), test_stack)
    test_track(md5_checksum(test_stack[0][0]), test_stack)
    test_track(md5_checksum(""))
    test_track(md5_checksum())

    print()

expected_output = \
"""
_SIPO_Chip_Select_
{ "C0": { "S0": 0, "S1": 0, "S2": 0, "B3": 1, "B4": 1, "B5": 1, "B6": 1, "B7": 0 } }
{ "C1": { "S0": 0, "S1": 0, "S2": 1, "B3": 0, "B4": 0, "B5": 0, "B6": 0, "B7": 0 } }
{ "C2": { "S0": 0, "S1": 1, "S2": 0, "B3": 1, "B4": 1, "B5": 1, "B6": 1, "B7": 1 } }
{ "C3": { "S0": 0, "S1": 1, "S2": 1, "B3": 0, "B4": 0, "B5": 0, "B6": 0, "B7": 0 } }

_Binary_Rotation_Compressor_
000 111 000 111
6 ones 6 zeros 
12 bytes encoding 12 bits
[0, 7, 1, 7], 3
0-7-1-7_3
000111000111
000 111 000 111

_Message_Diff_Extraction_
([85437, 100501, 81542, 88216, 17444, 21426, 219351, 184323], 18)
([2276146, 3722465, 5400121, 2365162, 3761741, 2500862, 7812719, 4940592], 23)
([33344, 67429, 5982, 75092, 108557, 110261, 40737, 94694], 17)
([170875, 48589, 347514, 405572, 482186, 204549, 376049, 204698], 19)
([4552293, 2664936, 86552, 11591932, 5053707, 16232424, 22560, 13415852], 24)
([66689, 74262, 188804, 220504, 91918, 96726, 186037, 4372], 18)
Some Sample Text. 
Even More Sample Text. 
A bit less text. 
Some Sample Text2. 
Even More Sample Text2. 
A bit less text2. 

_Checksum_Decoder_Parity_
[ENCODE]: 77,117,108,116,105,112,108,101,32,111,102,32,70,111,117,114
[DECODE]: [1953264973, 1701605481, 543584032, 1920298822] Multiple of Four
File.txt (8)
0100011001101001011011000110010100101110011101000111100001110100 (64)
[70, 35, 3, 249, 201, 70, 4, 252] (8)
0100011001101001011011000110010100101110011101000111100001110100 (64)
File.txt (8)
0d7abe66c544c00a393b5697527be9b4 (32)
0d7abe66c544c00a393b5697527be9b4 (32)
d41d8cd98f00b204e9800998ecf8427e (32)
d41d8cd98f00b204e9800998ecf8427e (32)
"""

if __name__ == "__main__":
    main()
```