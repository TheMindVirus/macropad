# Braille

![screenshot](/blob/archive/sketches/Braille/screenshot.png)

```py
# Braille Transposition - Alastair Cota - 14:42 24/08/2022
# This sketch makes use of the 8-dot pattern to represent braille in logic puzzles.
# However, in many cases the dots are numbered awkwardly and can be displayed upside-down right-left.

# https://www.unicode.org/charts/PDF/U2800.pdf

def check(dm):
    for i in dm:
        if (dm.count(i) != 1):
            return False
    return True

# Unicode starts at 0x2800 in hexadecimal and counts in braille format breaking from binary at 0x2808
# UTF-8 encodes this in 3 bytes starting from 0xE2A07F Big Endian, in 4 banks spaced by 193 steps
# This order is illogical for binary counting and graphics/mathematics but it's in the specification

dotmap = ""
for i in range(0, 256):
    dotmap += eval("\"\\u{:04X}\"".format(0x2800 + i))
print(dotmap)
print("A:", len(dotmap.encode()), check(dotmap))

# CD PROJEKT RED recently presented everyone with a puzzle involving a pattern of dots in a 2x4 grid
# Their numbering was different from braille and transposed from what you might call a logical order
# They start from the bottom right hand corner, then left, then diagonally up and right etc...

dotmap = "⠀⢀⡀⣀⠠⢠⡠⣠⠄⢄⡄⣄⠤⢤⡤⣤⠐⢐⡐⣐⠰⢰⡰⣰⠔⢔⡔⣔⠴⢴⡴⣴⠂⢂⡂⣂⠢⢢⡢⣢⠆⢆⡆⣆⠦⢦⡦⣦⠒⢒⡒⣒⠲⢲⡲⣲⠖⢖⡖⣖⠶⢶⡶⣶⠈⢈⡈⣈⠨⢨⡨⣨⠌⢌⡌⣌⠬⢬⡬⣬⠘⢘⡘⣘⠸⢸⡸⣸⠜⢜⡜⣜⠼⢼⡼⣼⠊⢊⡊⣊⠪⢪⡪⣪⠎⢎⡎⣎⠮⢮⡮⣮⠚⢚⡚⣚⠺⢺⡺⣺⠞⢞⡞⣞⠾⢾⡾⣾⠁⢁⡁⣁⠡⢡⡡⣡⠅⢅⡅⣅⠥⢥⡥⣥⠑⢑⡑⣑⠱⢱⡱⣱⠕⢕⡕⣕⠵⢵⡵⣵⠃⢃⡃⣃⠣⢣⡣⣣⠇⢇⡇⣇⠧⢧⡧⣧⠓⢓⡓⣓⠳⢳⡳⣳⠗⢗⡗⣗⠷⢷⡷⣷⠉⢉⡉⣉⠩⢩⡩⣩⠍⢍⡍⣍⠭⢭⡭⣭⠙⢙⡙⣙⠹⢹⡹⣹⠝⢝⡝⣝⠽⢽⡽⣽⠋⢋⡋⣋⠫⢫⡫⣫⠏⢏⡏⣏⠯⢯⡯⣯⠛⢛⡛⣛⠻⢻⡻⣻⠟⢟⡟⣟⠿⢿⡿⣿"
print(dotmap)
print("B:", len(dotmap.encode()), check(dotmap))

# Each digit in UTF-8 takes 3 bytes instead of perhaps using just 1 byte from 0->255
# It was found that using an underscore as 0 makes it more readable and saves 2 bytes for every 0
# However, using it throws off the alignment for programs expecting 3 bytes for each digit

dotmap = "_⢀⡀⣀⠠⢠⡠⣠⠄⢄⡄⣄⠤⢤⡤⣤⠐⢐⡐⣐⠰⢰⡰⣰⠔⢔⡔⣔⠴⢴⡴⣴⠂⢂⡂⣂⠢⢢⡢⣢⠆⢆⡆⣆⠦⢦⡦⣦⠒⢒⡒⣒⠲⢲⡲⣲⠖⢖⡖⣖⠶⢶⡶⣶⠈⢈⡈⣈⠨⢨⡨⣨⠌⢌⡌⣌⠬⢬⡬⣬⠘⢘⡘⣘⠸⢸⡸⣸⠜⢜⡜⣜⠼⢼⡼⣼⠊⢊⡊⣊⠪⢪⡪⣪⠎⢎⡎⣎⠮⢮⡮⣮⠚⢚⡚⣚⠺⢺⡺⣺⠞⢞⡞⣞⠾⢾⡾⣾⠁⢁⡁⣁⠡⢡⡡⣡⠅⢅⡅⣅⠥⢥⡥⣥⠑⢑⡑⣑⠱⢱⡱⣱⠕⢕⡕⣕⠵⢵⡵⣵⠃⢃⡃⣃⠣⢣⡣⣣⠇⢇⡇⣇⠧⢧⡧⣧⠓⢓⡓⣓⠳⢳⡳⣳⠗⢗⡗⣗⠷⢷⡷⣷⠉⢉⡉⣉⠩⢩⡩⣩⠍⢍⡍⣍⠭⢭⡭⣭⠙⢙⡙⣙⠹⢹⡹⣹⠝⢝⡝⣝⠽⢽⡽⣽⠋⢋⡋⣋⠫⢫⡫⣫⠏⢏⡏⣏⠯⢯⡯⣯⠛⢛⡛⣛⠻⢻⡻⣻⠟⢟⡟⣟⠿⢿⡿⣿"
print(dotmap)
lendotmap = len(dotmap.encode())
print("C:", lendotmap, "+ 2 =", lendotmap + 2, check(dotmap))

# In Computer Graphics rows are scanned from the top-left, then right, then diagonally down and left
# This was decided by display manufacturers and has stuck in the design for a long time without change
# This is somewhat contrary to how you may plot a graph in Mathematics or any Scientific Subject

dotmap = "⠀⠁⠈⠉⠂⠃⠊⠋⠐⠑⠘⠙⠒⠓⠚⠛⠄⠅⠌⠍⠆⠇⠎⠏⠔⠕⠜⠝⠖⠗⠞⠟⠠⠡⠨⠩⠢⠣⠪⠫⠰⠱⠸⠹⠲⠳⠺⠻⠤⠥⠬⠭⠦⠧⠮⠯⠴⠵⠼⠽⠶⠷⠾⠿⡀⡁⡈⡉⡂⡃⡊⡋⡐⡑⡘⡙⡒⡓⡚⡛⡄⡅⡌⡍⡆⡇⡎⡏⡔⡕⡜⡝⡖⡗⡞⡟⡠⡡⡨⡩⡢⡣⡪⡫⡰⡱⡸⡹⡲⡳⡺⡻⡤⡥⡬⡭⡦⡧⡮⡯⡴⡵⡼⡽⡶⡷⡾⡿⢀⢁⢈⢉⢂⢃⢊⢋⢐⢑⢘⢙⢒⢓⢚⢛⢄⢅⢌⢍⢆⢇⢎⢏⢔⢕⢜⢝⢖⢗⢞⢟⢠⢡⢨⢩⢢⢣⢪⢫⢰⢱⢸⢹⢲⢳⢺⢻⢤⢥⢬⢭⢦⢧⢮⢯⢴⢵⢼⢽⢶⢷⢾⢿⣀⣁⣈⣉⣂⣃⣊⣋⣐⣑⣘⣙⣒⣓⣚⣛⣄⣅⣌⣍⣆⣇⣎⣏⣔⣕⣜⣝⣖⣗⣞⣟⣠⣡⣨⣩⣢⣣⣪⣫⣰⣱⣸⣹⣲⣳⣺⣻⣤⣥⣬⣭⣦⣧⣮⣯⣴⣵⣼⣽⣶⣷⣾⣿"
print(dotmap)
print("D:", len(dotmap.encode()), check(dotmap))

# Why start from the top-left or the bottom-right when everything else starts from the bottom-left?
# When you plot an X/Y graph you have X on the horizontal axis and Y on the vertical axis
# It is natural to start counting upwards in bars

dotmap = "_⡀⠄⡄⠂⡂⠆⡆⠁⡁⠅⡅⠃⡃⠇⡇⢀⣀⢄⣄⢂⣂⢆⣆⢁⣁⢅⣅⢃⣃⢇⣇⠠⡠⠤⡤⠢⡢⠦⡦⠡⡡⠥⡥⠣⡣⠧⡧⢠⣠⢤⣤⢢⣢⢦⣦⢡⣡⢥⣥⢣⣣⢧⣧⠐⡐⠔⡔⠒⡒⠖⡖⠑⡑⠕⡕⠓⡓⠗⡗⢐⣐⢔⣔⢒⣒⢖⣖⢑⣑⢕⣕⢓⣓⢗⣗⠰⡰⠴⡴⠲⡲⠶⡶⠱⡱⠵⡵⠳⡳⠷⡷⢰⣰⢴⣴⢲⣲⢶⣶⢱⣱⢵⣵⢳⣳⢷⣷⠈⡈⠌⡌⠊⡊⠎⡎⠉⡉⠍⡍⠋⡋⠏⡏⢈⣈⢌⣌⢊⣊⢎⣎⢉⣉⢍⣍⢋⣋⢏⣏⠨⡨⠬⡬⠪⡪⠮⡮⠩⡩⠭⡭⠫⡫⠯⡯⢨⣨⢬⣬⢪⣪⢮⣮⢩⣩⢭⣭⢫⣫⢯⣯⠘⡘⠜⡜⠚⡚⠞⡞⠙⡙⠝⡝⠛⡛⠟⡟⢘⣘⢜⣜⢚⣚⢞⣞⢙⣙⢝⣝⢛⣛⢟⣟⠸⡸⠼⡼⠺⡺⠾⡾⠹⡹⠽⡽⠻⡻⠿⡿⢸⣸⢼⣼⢺⣺⢾⣾⢹⣹⢽⣽⢻⣻⢿⣿"
print(dotmap)
print("E:", len(dotmap.encode()), "+ 2 =", len(dotmap.encode()) + 2, check(dotmap))

# There are many more encodings, transpositions and compression optimisations yet to be explained here
# Try some of these first and then try making your own dotmap with a custom ordering to suit yourself
# Maybe also see if you can display it on a device that a blind person can put their hand on and read

dotmap = \
{
      0:"_",   1:"⡀",   2:"⠄",   3:"⡄",   4:"⠂",   5:"⡂",   6:"⠆",   7:"⡆",
      8:"⠁",   9:"⡁",  10:"⠅",  11:"⡅",  12:"⠃",  13:"⡃",  14:"⠇",  15:"⡇",
     16:"⢀",  17:"⣀",  18:"⢄",  19:"⣄",  20:"⢂",  21:"⣂",  22:"⢆",  23:"⣆",
     24:"⢁",  25:"⣁",  26:"⢅",  27:"⣅",  28:"⢃",  29:"⣃",  30:"⢇",  31:"⣇",
     32:"⠠",  33:"⡠",  34:"⠤",  35:"⡤",  36:"⠢",  37:"⡢",  38:"⠦",  39:"⡦",
     40:"⠡",  41:"⡡",  42:"⠥",  43:"⡥",  44:"⠣",  45:"⡣",  46:"⠧",  47:"⡧",
     48:"⢠",  49:"⣠",  50:"⢤",  51:"⣤",  52:"⢢",  53:"⣢",  54:"⢦",  55:"⣦",
     56:"⢡",  57:"⣡",  58:"⢥",  59:"⣥",  60:"⢣",  61:"⣣",  62:"⢧",  63:"⣧",
     64:"⠐",  65:"⡐",  66:"⠔",  67:"⡔",  68:"⠒",  69:"⡒",  70:"⠖",  71:"⡖",
     72:"⠑",  73:"⡑",  74:"⠕",  75:"⡕",  76:"⠓",  77:"⡓",  78:"⠗",  79:"⡗",
     80:"⢐",  81:"⣐",  82:"⢔",  83:"⣔",  84:"⢒",  85:"⣒",  86:"⢖",  87:"⣖",
     88:"⢑",  89:"⣑",  90:"⢕",  91:"⣕",  92:"⢓",  93:"⣓",  94:"⢗",  95:"⣗",
     96:"⠰",  97:"⡰",  98:"⠴",  99:"⡴", 100:"⠲", 101:"⡲", 102:"⠶", 103:"⡶",
    104:"⠱", 105:"⡱", 106:"⠵", 107:"⡵", 108:"⠳", 109:"⡳", 110:"⠷", 111:"⡷",
    112:"⢰", 113:"⣰", 114:"⢴", 115:"⣴", 116:"⢲", 117:"⣲", 118:"⢶", 119:"⣶",
    120:"⢱", 121:"⣱", 122:"⢵", 123:"⣵", 124:"⢳", 125:"⣳", 126:"⢷", 127:"⣷",
    128:"⠈", 129:"⡈", 130:"⠌", 131:"⡌", 132:"⠊", 133:"⡊", 134:"⠎", 135:"⡎",
    136:"⠉", 137:"⡉", 138:"⠍", 139:"⡍", 140:"⠋", 141:"⡋", 142:"⠏", 143:"⡏",
    144:"⢈", 145:"⣈", 146:"⢌", 147:"⣌", 148:"⢊", 149:"⣊", 150:"⢎", 151:"⣎",
    152:"⢉", 153:"⣉", 154:"⢍", 155:"⣍", 156:"⢋", 157:"⣋", 158:"⢏", 159:"⣏",
    160:"⠨", 161:"⡨", 162:"⠬", 163:"⡬", 164:"⠪", 165:"⡪", 166:"⠮", 167:"⡮",
    168:"⠩", 169:"⡩", 170:"⠭", 171:"⡭", 172:"⠫", 173:"⡫", 174:"⠯", 175:"⡯",
    176:"⢨", 177:"⣨", 178:"⢬", 179:"⣬", 180:"⢪", 181:"⣪", 182:"⢮", 183:"⣮",
    184:"⢩", 185:"⣩", 186:"⢭", 187:"⣭", 188:"⢫", 189:"⣫", 190:"⢯", 191:"⣯",
    192:"⠘", 193:"⡘", 194:"⠜", 195:"⡜", 196:"⠚", 197:"⡚", 198:"⠞", 199:"⡞",
    200:"⠙", 201:"⡙", 202:"⠝", 203:"⡝", 204:"⠛", 205:"⡛", 206:"⠟", 207:"⡟",
    208:"⢘", 209:"⣘", 210:"⢜", 211:"⣜", 212:"⢚", 213:"⣚", 214:"⢞", 215:"⣞",
    216:"⢙", 217:"⣙", 218:"⢝", 219:"⣝", 220:"⢛", 221:"⣛", 222:"⢟", 223:"⣟",
    224:"⠸", 225:"⡸", 226:"⠼", 227:"⡼", 228:"⠺", 229:"⡺", 230:"⠾", 231:"⡾",
    232:"⠹", 233:"⡹", 234:"⠽", 235:"⡽", 236:"⠻", 237:"⡻", 238:"⠿", 239:"⡿",
    240:"⢸", 241:"⣸", 242:"⢼", 243:"⣼", 244:"⢺", 245:"⣺", 246:"⢾", 247:"⣾",
    248:"⢹", 249:"⣹", 250:"⢽", 251:"⣽", 252:"⢻", 253:"⣻", 254:"⢿", 255:"⣿",
}
dotmap = "".join([dotmap[i] for i in dotmap])
print(dotmap)
print("F:", len(dotmap.encode()))

# Drink Water and Take Regular Eye and RSI Breaks!
```