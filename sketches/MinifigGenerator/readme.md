```py
# Lego Minifig Generator - Alastair Cota
# A simple curated random number selector for generating combinations of Lego Minifigs
# For BrickLink, type in the part number that shows up on the macropad into the search box

from adafruit_macropad import MacroPad
import random, time
macropad = MacroPad()

keys = \
{
    "0"  : (macropad.Keycode.ONE,       0x00FFFF, 0x003333),
    "1"  : (macropad.Keycode.TWO,       0x00FFFF, 0x003333),
    "2"  : (macropad.Keycode.THREE,     0x00FFFF, 0x003333),
    "3"  : (macropad.Keycode.FOUR,      0x00FFFF, 0x003333),
    "4"  : (macropad.Keycode.FIVE,      0x00FFFF, 0x003333),
    "5"  : (macropad.Keycode.SIX,       0x00FFFF, 0x003333),
    "6"  : (macropad.Keycode.SEVEN,     0x00FFFF, 0x003333),
    "7"  : (macropad.Keycode.EIGHT,     0x00FFFF, 0x003333),
    "8"  : (macropad.Keycode.NINE,      0x00FFFF, 0x003333),
    "9"  : (macropad.Keycode.BACKSPACE, 0x00FFFF, 0x003333),
    "10" : (macropad.Keycode.ZERO,      0x00FFFF, 0x003333),
    "11" : (macropad.Keycode.ENTER,     0x00FFFF, 0x003333),
}

hair = \
[
    "53982", "53981", "87995", "28551", "92081", "61196",
    "12889", "4530", "15503", "53126", "41612", "12890",
    "17346", "92083", "x161", "20595", "13784", "13750",
    "40251", "23187", "15499", "59363", "85974", "3625",
    "20596", "x104", "13785", "87990", "88286", "17347",
    "62696", "15427", "21777", "20877", "64807", "11256",
    "99240", "29634", "30409", "92758", "13251", "27186",
    "93562", "29633", "30608", "25379", "6025", "40239",
    "30114", "24072", "36806", "34316", "3901", "21778",
    "35699", "88283", "25409", "87572", "30410", "32969",
    "99930", "15500", "21787", "21268", "40233", "62810",
    "20597", "26139", "15443", "59362", "62711", "x219",
    "35701", "98385", "15705", "24792", "17630", "43753",
    "98371", "95226", "25972", "64798", "21269", "24791",
    "23186", "98726", "93217", "10048", "92746", "25411",
    "25412", "25378", "87991", "43751", "32602",
]

face = \
[
    "3626cpb2922", "3626cpb2651", "3626cpb3197", "3626bpx105",
    "3626cpb3215", "3626cpb3224", "3626cpb1349", "3626cpb3225",
    "3626cpb3229", "3626cpb3216", "3626cpb1699", "3626bpx104",
    "3626bpb0442",
]

body = \
[
    "973pb3899", "973pb5103", "973pb5053", "973pb3624", "973pb3596",
    "973pb1558", "973pb3162", "973pb3163", "973pb2347", "973pb2818",
    "973pb4627", "973pb0b", "973pb0314", "973pb5004", "973pb0298",
    "973pb5016", "973pb5037", "973pb4739", "973pb4535",
]

random.seed(int(time.monotonic()))

buffer = []
def generate(n = 64):
    global buffer
    buffer = []
    for i in range(0, n):
        buffer.append(
        {
            "hair": int(random.random() * len(hair)),
            "face": int(random.random() * len(face)),
            "body": int(random.random() * len(body)),
        });

index = 0
def display():
    global index, buffer
    data = buffer[index]
    #macropad.display_sleep = True
    #macropad.display.freeze()
    print("\n\n\n\n")
    print("hair: " + hair[data["hair"]])
    print("face: " + face[data["face"]])
    print("body: " + body[data["body"]])
    #macropad.display.resume()
    #macropad.display_sleep = False

generate()
display()

encoder_position = 0
for key in keys:
    macropad.pixels[int(key)] = keys[key][2]

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        data = keys[str(key_event.key_number)]
        if key_event.pressed:
            macropad.keyboard.press(data[0]) if data[0] else None #pass
            macropad.pixels[key_event.key_number] = data[1]
        else:
            macropad.keyboard.release(data[0]) if data[0] else None #pass
            macropad.pixels[key_event.key_number] = data[2]

    current_position = macropad.encoder
    if current_position < encoder_position:
        index -= 1
        if index < 0:
            index = len(buffer) - 1
        display()
        encoder_position = current_position
    if current_position > encoder_position:
        index -= 1
        if index < 0:
            index = len(buffer) - 1
        display()
        encoder_position = current_position
```