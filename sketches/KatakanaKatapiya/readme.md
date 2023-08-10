```py
# Katakana Katapiya - TheMindVirus
# Katakana is a Japanese method of writing and pronouncing words using syllables.
# Katapiya is CircuitPython written in Katakana, which might eventually become extended bytecode.

ji = \
"""
イ ソ # import audio # i so
イ ロ # import video # i ro

ク 一:        # while true scope # ku ichi
    ソ.ソに()  # run audio method # so sony
    ロ.タイト() # run video titles # ro taito

# katakana #
# katapiya #
"""

### BEGIN_EDGE_MOD ###

from adafruit_macropad import MacroPad

macropad = MacroPad()

def sony_audio():
    macropad.start_tone(1000)
    macropad.stop_tone()
    pass

def taito_video():
    print("カ・タ・カ・ナ  カ・タ・ピ・や")
    #text_lines = macropad.display_text()
    #text_lines[0].text = "カ・タ・カ・ナ"
    #text_lines[1].text = "カ・タ・ピ・や"
    #text_lines.show()
    pass

ji = ji[1:] # otherwise invalid syntax
ji = ji.replace("ソ.ソに", "sony_audio")
ji = ji.replace("ロ.タイト", "taito_video")

ji += "    break # "

### END_EDGE_MOD ###

ji = ji.replace("イ ", "import ")
ji = ji.replace("ソ", "synthio")
ji = ji.replace("ロ", "displayio")
ji = ji.replace("ク ", "while ")
ji = ji.replace("一", "1")

### BEGIN_EDGE ###

def bytecode(ji):
    i = 0
    code = ""
    for j in ji:
        code += "{:02x} ".format(ord(j))
        if i % 8 == 7:
            code += "\n"
        i += 1
    u = len(ji)
    v = int(u / 8) # int((u + 7) / 8)
    print("bytes: {}\nchunks: {}\n".format(u, v))
    return code
print(bytecode(ji))

print(ji)
loop = True
run = True
once = True
#exec(ji)

print()
while loop:
    try:
        if run:
            exec(ji)
        if once:
            loop = False
        pass
    except Exception as error:
        print(error)
        loop = False
        pass

### END_EDGE ###

# TRON: Table Row Object Notation
# Access-Control-Allow-Origin: *

# カ・タ・カ・ナ
# カ・タ・ピ・や

# コ・ナ・ミ
# コ・タ・ク

# ティク トク
# びィレィびィレィ

# アクリトピア
# リウガワカテキワクラヤ
```