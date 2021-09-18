# Lego Macropad CP2077 Data Term - Alastair Cota, Adafruit Industries, Arasaka Corporation
# This layout is for playing CD_PROJEKT_RED Cyberpunk_2077 Data Terminal Jack-In Minigame.
# Arrow keys are the bottom row in portrait orientation, key 7 for Up and key 4 for Space.
# _________________ #
#||Macropad|======||#
#||________|==|F|=||#
#||===============||#
#||=[E]==[E]==[P]=||#
#||===============||#
#||=[T]==[_]==[G]=||#
#||===============||#
#||=[C]==[^]==[A]=||#
#||===============||#
#||=[<]==[v]==[>]=||#
#||_______________||#
#'''''''''''''''''''#

from adafruit_macropad import MacroPad
import random, time

macropad = MacroPad()

keys = \
{
    "0"  : (macropad.Keycode.ESCAPE,       0xFF0000, 0x330000, "ESCAPE"),
    "1"  : (macropad.Keycode.ENTER,        0xFF0000, 0x330000, "ENTER"),
    "2"  : (macropad.Keycode.P,            0xFF0000, 0x330000, "MENU"),
    "3"  : (macropad.Keycode.TAB,          0xFF0000, 0x330000, "SCOPE"),
    "4"  : (macropad.Keycode.SPACE,        0xFF0000, 0x330000, "SPACE"),
    "5"  : (macropad.Keycode.N,            0xFF0000, 0x330000, "GRAB"),
    "6"  : (macropad.Keycode.CONTROL,      0xFF0000, 0x330000, "CROUCH"),
    "8"  : (macropad.Keycode.ALT,          0xFF0000, 0x330000, "ALT_CUNNINGHAM"),
    "7"  : (macropad.Keycode.UP_ARROW,     0xFF0000, 0x330000, "UP_ARROW"),
    "9"  : (macropad.Keycode.LEFT_ARROW,   0xFF0000, 0x330000, "LEFT_ARROW"),
    "10" : (macropad.Keycode.DOWN_ARROW,   0xFF0000, 0x330000, "DOWN_ARROW"),
    "11" : (macropad.Keycode.RIGHT_ARROW,  0xFF0000, 0x330000, "RIGHT_ARROW"),
}

text_lines = macropad.display_text(title = "\\\\\\\\[7DATA7TERM7]////")
last_pressed = ""
last_position = 0
encoder_lock = False
interval = 10.0
t = 0.0

#define DECEMBER   12
DECEMBER = 12

def update_display(data_entry = ""):
    global text_lines
    time_seed = time.monotonic_ns()
    random.seed(time_seed)
    text_lines[0].text = "$> " + str(data_entry)
    text_lines[1].text = str(time_seed)
    text_lines[2].text = " ".join(["{:02X}".format(int(random.random() * 100.0)) for i in range(20, 77, DECEMBER)])
    text_lines.show()
update_display()

for key in keys:
    macropad.pixels[int(key)] = keys[key][2];

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        data = keys[str(key_event.key_number)]
        if key_event.pressed:
            macropad.keyboard.press(data[0])
            macropad.pixels[key_event.key_number] = data[1];
            macropad.start_tone(5000);
        else:
            macropad.keyboard.release(data[0])
            macropad.pixels[key_event.key_number] = data[2];
        last_pressed = data[3]
    if not encoder_lock and macropad.encoder_switch:
        macropad.keyboard.press(macropad.Keycode.F)
        encoder_lock = True
    elif encoder_lock and not macropad.encoder_switch:
        macropad.keyboard.release(macropad.Keycode.F)
        encoder_lock = False
    current_position = macropad.encoder
    if macropad.encoder < last_position:
        macropad.keyboard.send(macropad.Keycode.ONE)
        last_pressed = "ONE"
        last_position = current_position
    elif macropad.encoder > last_position:
        macropad.keyboard.send(macropad.Keycode.THREE)
        last_pressed = "THREE"
        last_position = current_position
    t = (time.monotonic_ns() / 1000.0) % (interval * 2)
    if (t < interval):
        update_display(last_pressed)
        macropad.stop_tone();
    

"""
#STR =  "                                           .--::////:--.\r\n"
#STR += "                                       `-/ydmNNNmmmmNNNmdy/-`\r\n"
#STR += "                                     .+dNNmyo/+shddhs+/oymNNd+.\r\n"
#STR += "                                   .sNMdo-` .yNMMMMMMNy. `-omMNs.\r\n"
#STR += "                                 `+NMd/`    hMMMMMMMMMMh    `/dMN+`\r\n"
#STR += "                                `yMNo`     `MMMMMMMMMMMM`     `oNMy`\r\n"
#STR += "                                yMN/`.:/+/.`yMMMMMMMMMMy`./+/:.`/NMy\r\n"
#STR += "                               +MM+/dNMMMMMdosmMMMMMMmsodMMMMMNd/+MM+\r\n"
#STR += "                              `NMdoMMMMMMMMMMy`:hMMh:`yMMMMMMMMMModMN`\r\n"
#STR += "                              :MMoNMMMMMMMMMMM. oMMo .MMMMMMMMMMMNoMM:\r\n"
#STR += "                              /MM/dMMMMMMMMMMm` oMMo `mMMMMMMMMMMd/MM/\r\n"
#STR += "                              :MMo.hMMMMMMMMMh. oMMo .hMMMMMMMMMh.oMM:\r\n"
#STR += "                              `NMd  -ohddhssNMNsyMMysNMNsshddho-  dMN`\r\n"
#STR += "                               +MM+         .sNMMMMMMNs`         +MM+\r\n"
#STR += "                                yMM/          .sNMMNs.          /MMh\r\n"
#STR += "                                  +NMm/`        oMMo        `/mMN+\r\n"
#STR += "                                   .sNMmo-      oMMo      -omMNs.\r\n"
#STR += "                                     `+hMNmho/-.+dd+.-/ohNMMh+`\r\n"
#STR += "                                       `./sdmNNNNNNNNNNmds/.`\r\n"
#STR += "                                           ``.-:////:-.``\r\n"
#STR += "         `....     ............`      `....`         `....         `....     ...    `.....``....\r\n"
#STR += "      :sdmNNNNs-   mNNNNNNNNNNNm/  `/ymNNNNm+`     mM+NNNmy:    -sdmNNNNs- . NNN``:smNNd  dddmNNNNh:\r\n"
#STR += "    `yNMNhsohNMNs. NMMhssssssdMMd -dMMmyssdMMmo` ///yyMMmyyy. `yNMNhsoyNMNy /MMMymMMNh +yNMNhsoyNMNh-\r\n"
#STR += "    oMMd.    -mMMo NMMo`     :hhs dMMs`   `/MMM- `:ymMMm        MMd.    -mMM hMMMMNh+.  /MMN-`   .hMMh\r\n"
#STR += "    yMMy      dMMo dMMNdo-`       NMM+      MMM: ///./ymMMmy: `yMM       hMM hmMMMm+    +MMm`     oMMh\r\n"
#STR += "    -mMMh+:--`dMMo dNMmNMNdo-`    +NMNy/---`MMM/ MM+   +yNMMMm smMM  :--`hMM hmMMmMMNh+ -dMMdo:--`oMMh\r\n"
#STR += "     .smNMMMNsdMMo ---.-odNMNdo-`  :hmMMMMN/MMM: dMMMMMMMMMMMM s.smNMMMMyhMM s---`:smMMN dmNNMMMMdoMMh\r\n"
#STR += "      `-////:://-      `-/////.    .:////-///`` :///////////-  `-////:://-  ///    ////   ::////-//:/\r\n"
"""
