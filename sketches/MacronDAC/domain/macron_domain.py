class reprdoc:
    __indent__ = 20
    def __iter__(self):
        return iter(dir(self))
    def __repr__(self):
        data = ""
        for i in self:
            if not i.startswith("__"):
                indentation = " " * (self.__indent__ - len(str(i)))
                data += str(i) + ":" + indentation \
                      + str(eval("self." + str(i))) + "\n"
        return data

def diff(a, b, macron = "\u0303", micron = "\u0330"):
    a_float = float(a)
    b_float = float(b) ; c = a_float - b_float
    c_float = float(c)
    a_abs = abs(a_float)
    b_abs = abs(b_float)
    c_abs = abs(c_float)
    a_str = str(a_abs)
    b_str = str(b_abs)
    c_str = str(c_abs)
    a_len = len(a_str)
    b_len = len(b_str)
    c_len = len(c_str)
    a_bool = bool(a_float < 0.0)
    b_bool = bool(b_float < 0.0)
    c_bool = bool(c_float < 0.0)
    a_sign = "-" if a_bool else " "
    b_sign = "-" if b_bool else " "
    c_sign = "-" if c_bool else " "
    d_sign = "-" if not c_bool else "+"
    ap = a_str.find(".")
    bp = b_str.find(".")
    cp = ap - bp
    dp = abs(cp)
    if ap < bp:
        a_str = ("0" * dp) + a_str
        a_len = len(a_str)
    elif ap > bp:
        b_str = ("0" * dp) + b_str
        b_len = len(b_str)
    d_len = abs(a_len - b_len)
    if a_len < b_len:
        a_str += ("0" * d_len)
        a_len = len(a_str)
    elif a_len > b_len:
        b_str += ("0" * d_len)
        b_len = len(b_str)
    print(a_sign + a_str)
    print(b_sign + b_str)
    sz = max(a_len, b_len)
    d_str = ""
    for i in range(0, sz):
        if a_str[i] == "." or b_str[i] == ".":
            if ap < bp:
                d_str += macron
            elif ap > bp:
                d_str += micron
            d_str += "."
        else:
            ax = int(a_str[i])
            bx = int(b_str[i])
            cx = abs(ax - bx)
            if ax <= bx:
                d_str += macron
            if ax >= bx:
                d_str += micron
            d_str += str(cx)
    print(c_sign + c_str)
    print(d_sign + d_str)
    d = d_float = c_float
    d_bool = bool(d_float < 0.0)
    d_abs = abs(d_float)
    d_len = len(d_str)
    data = reprdoc()
    data.sz = sz
    data.a = a ; data.b = b ; data.c = c ; data.d = d
    data.ap = ap ; data.bp = bp ; data.cp = cp ; data.dp = dp
    data.a_float = a_float ; data.b_float = b_float
    data.c_float = c_float ; data.d_float = d_float
    data.a_abs = a_abs ; data.b_abs = b_abs
    data.c_abs = c_abs ; data.d_abs = d_abs
    data.a_str = a_str ; data.b_str = b_str
    data.c_str = c_str ; data.d_str = d_str
    data.a_len = a_len ; data.b_len = b_len
    data.c_len = c_len ; data.d_len = d_len
    data.a_bool = a_bool ; data.b_bool = b_bool
    data.c_bool = c_bool ; data.d_bool = d_bool
    data.a_sign = a_sign ; data.b_sign = b_sign
    data.c_sign = c_sign ; data.d_sign = d_sign
    return data

data = diff("-62.105", "+132.29")
print()
print(data)
