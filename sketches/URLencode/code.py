# URL Escape Sequences - Alastair Cota
# There are certain symbols which browsers do not encode directly (e.g. %20 for space)
# and instead use a variant of Windows-1252/UTF-8/E-ASCII encoding to escape these symbols.

# https://www.w3schools.com/tags/ref_urlencode.ASP
# ENG[UK] (British English / United Kingdom / Great Britain) Keyboard Layout is assumed

from adafruit_macropad import MacroPad

macropad = MacroPad()

kc = macropad.Keycode

index = \
{
    0x00 : { "ESC": "%20", "ALT": "%20", "SEQ": " " , "KEY" : (kc.SPACE,)              },
    0x01 : { "ESC": "%21", "ALT": "%21", "SEQ": "!" , "KEY" : (kc.SHIFT, kc.ONE)       },
    0x02 : { "ESC": "%22", "ALT": "%22", "SEQ": "\"", "KEY" : (kc.SHIFT, kc.TWO)       },
    0x03 : { "ESC": "%23", "ALT": "%23", "SEQ": "#" , "KEY" : (kc.POUND,)              },
    0x04 : { "ESC": "%24", "ALT": "%24", "SEQ": "$" , "KEY" : (kc.SHIFT, kc.FOUR)      },
    0x05 : { "ESC": "%25", "ALT": "%25", "SEQ": "%" , "KEY" : (kc.SHIFT, kc.FIVE)      },
    0x06 : { "ESC": "%26", "ALT": "%26", "SEQ": "&" , "KEY" : (kc.SHIFT, kc.SEVEN)     },
    0x07 : { "ESC": "%27", "ALT": "%27", "SEQ": "'" , "KEY" : (kc.QUOTE,)              },
    0x08 : { "ESC": "%28", "ALT": "%28", "SEQ": "(" , "KEY" : (kc.SHIFT, kc.NINE)      },
    0x09 : { "ESC": "%29", "ALT": "%29", "SEQ": ")" , "KEY" : (kc.SHIFT, kc.ZERO)      },
    0x0A : { "ESC": "%2A", "ALT": "%2A", "SEQ": "*" , "KEY" : (kc.SHIFT, kc.EIGHT)     },
    0x0B : { "ESC": "%2B", "ALT": "%2B", "SEQ": "+" , "KEY" : (kc.SHIFT, kc.EQUALS)    },
    0x0C : { "ESC": "%2C", "ALT": "%2C", "SEQ": "," , "KEY" : (kc.COMMA,)              },
    0x0D : { "ESC": "%2D", "ALT": "%2D", "SEQ": "-" , "KEY" : (kc.MINUS,)              },
    0x0E : { "ESC": "%2E", "ALT": "%2E", "SEQ": "." , "KEY" : (kc.PERIOD,)             },
    0x0F : { "ESC": "%2F", "ALT": "%2F", "SEQ": "/" , "KEY" : (kc.FORWARD_SLASH,)      },
    0x10 : { "ESC": "%30", "ALT": "%30", "SEQ": "0" , "KEY" : (kc.ZERO,)               },
    0x11 : { "ESC": "%31", "ALT": "%31", "SEQ": "1" , "KEY" : (kc.ONE,)                },
    0x12 : { "ESC": "%32", "ALT": "%32", "SEQ": "2" , "KEY" : (kc.TWO,)                },
    0x13 : { "ESC": "%33", "ALT": "%33", "SEQ": "3" , "KEY" : (kc.THREE,)              },
    0x14 : { "ESC": "%34", "ALT": "%34", "SEQ": "4" , "KEY" : (kc.FOUR,)               },
    0x15 : { "ESC": "%35", "ALT": "%35", "SEQ": "5" , "KEY" : (kc.FIVE,)               },
    0x16 : { "ESC": "%36", "ALT": "%36", "SEQ": "6" , "KEY" : (kc.SIX,)                },
    0x17 : { "ESC": "%37", "ALT": "%37", "SEQ": "7" , "KEY" : (kc.SEVEN,)              },
    0x18 : { "ESC": "%38", "ALT": "%38", "SEQ": "8" , "KEY" : (kc.EIGHT,)              },
    0x19 : { "ESC": "%39", "ALT": "%39", "SEQ": "9" , "KEY" : (kc.NINE,)               },
    0x1A : { "ESC": "%3A", "ALT": "%3A", "SEQ": ":" , "KEY" : (kc.SHIFT, kc.SEMICOLON) },
    0x1B : { "ESC": "%3B", "ALT": "%3B", "SEQ": ";" , "KEY" : (kc.SEMICOLON,)          },
    0x1C : { "ESC": "%3C", "ALT": "%3C", "SEQ": "<" , "KEY" : (kc.SHIFT, kc.COMMA)     },
    0x1D : { "ESC": "%3D", "ALT": "%3D", "SEQ": "=" , "KEY" : (kc.EQUALS,)             },
    0x1E : { "ESC": "%3E", "ALT": "%3E", "SEQ": ">" , "KEY" : (kc.SHIFT, kc.PERIOD)    },
    0x1F : { "ESC": "%3F", "ALT": "%3F", "SEQ": "?" , "KEY" : (kc.SHIFT, kc.FORWARD_SLASH) },
    0x20 : { "ESC": "%40", "ALT": "%40", "SEQ": "@" , "KEY" : (kc.SHIFT, kc.QUOTE) },
    0x21 : { "ESC": "%41", "ALT": "%41", "SEQ": "A" , "KEY" : (kc.SHIFT, kc.A) },
    0x22 : { "ESC": "%42", "ALT": "%42", "SEQ": "B" , "KEY" : (kc.SHIFT, kc.B) },
    0x23 : { "ESC": "%43", "ALT": "%43", "SEQ": "C" , "KEY" : (kc.SHIFT, kc.C) },
    0x24 : { "ESC": "%44", "ALT": "%44", "SEQ": "D" , "KEY" : (kc.SHIFT, kc.D) },
    0x25 : { "ESC": "%45", "ALT": "%45", "SEQ": "E" , "KEY" : (kc.SHIFT, kc.E) },
    0x26 : { "ESC": "%46", "ALT": "%46", "SEQ": "F" , "KEY" : (kc.SHIFT, kc.F) },
    0x27 : { "ESC": "%47", "ALT": "%47", "SEQ": "G" , "KEY" : (kc.SHIFT, kc.G) },
    0x28 : { "ESC": "%48", "ALT": "%48", "SEQ": "H" , "KEY" : (kc.SHIFT, kc.H) },
    0x29 : { "ESC": "%49", "ALT": "%49", "SEQ": "I" , "KEY" : (kc.SHIFT, kc.I) },
    0x2A : { "ESC": "%4A", "ALT": "%4A", "SEQ": "J" , "KEY" : (kc.SHIFT, kc.J) },
    0x2B : { "ESC": "%4B", "ALT": "%4B", "SEQ": "K" , "KEY" : (kc.SHIFT, kc.K) },
    0x2C : { "ESC": "%4C", "ALT": "%4C", "SEQ": "L" , "KEY" : (kc.SHIFT, kc.L) },
    0x2D : { "ESC": "%4D", "ALT": "%4D", "SEQ": "M" , "KEY" : (kc.SHIFT, kc.M) },
    0x2E : { "ESC": "%4E", "ALT": "%4E", "SEQ": "N" , "KEY" : (kc.SHIFT, kc.N) },
    0x2F : { "ESC": "%4F", "ALT": "%4F", "SEQ": "O" , "KEY" : (kc.SHIFT, kc.O) },
    0x30 : { "ESC": "%50", "ALT": "%50", "SEQ": "P" , "KEY" : (kc.SHIFT, kc.P) },
    0x31 : { "ESC": "%51", "ALT": "%51", "SEQ": "Q" , "KEY" : (kc.SHIFT, kc.Q) },
    0x32 : { "ESC": "%52", "ALT": "%52", "SEQ": "R" , "KEY" : (kc.SHIFT, kc.R) },
    0x33 : { "ESC": "%53", "ALT": "%53", "SEQ": "S" , "KEY" : (kc.SHIFT, kc.S) },
    0x34 : { "ESC": "%54", "ALT": "%54", "SEQ": "T" , "KEY" : (kc.SHIFT, kc.T) },
    0x35 : { "ESC": "%55", "ALT": "%55", "SEQ": "U" , "KEY" : (kc.SHIFT, kc.U) },
    0x36 : { "ESC": "%56", "ALT": "%56", "SEQ": "V" , "KEY" : (kc.SHIFT, kc.V) },
    0x37 : { "ESC": "%57", "ALT": "%57", "SEQ": "W" , "KEY" : (kc.SHIFT, kc.W) },
    0x38 : { "ESC": "%58", "ALT": "%58", "SEQ": "X" , "KEY" : (kc.SHIFT, kc.X) },
    0x39 : { "ESC": "%59", "ALT": "%59", "SEQ": "Y" , "KEY" : (kc.SHIFT, kc.Y) },
    0x3A : { "ESC": "%5A", "ALT": "%5A", "SEQ": "Z" , "KEY" : (kc.SHIFT, kc.Z) },
    0x3B : { "ESC": "%5B", "ALT": "%5B", "SEQ": "[" , "KEY" : (kc.LEFT_BRACKET,) },
    0x3C : { "ESC": "%5C", "ALT": "%5C", "SEQ": "\\", "KEY" : (kc.KEYPAD_BACKSLASH,) },
    0x3D : { "ESC": "%5D", "ALT": "%5D", "SEQ": "]" , "KEY" : (kc.RIGHT_BRACKET,) },
    0x3E : { "ESC": "%5E", "ALT": "%5E", "SEQ": "^" , "KEY" : (kc.SHIFT, kc.SIX) },
    0x3F : { "ESC": "%5F", "ALT": "%5F", "SEQ": "_" , "KEY" : (kc.SHIFT, kc.MINUS) },
    0x40 : { "ESC": "%60", "ALT": "%60", "SEQ": "`" , "KEY" : (kc.GRAVE_ACCENT,) },
    0x41 : { "ESC": "%61", "ALT": "%61", "SEQ": "a" , "KEY" : (kc.A,) },
    0x42 : { "ESC": "%62", "ALT": "%62", "SEQ": "b" , "KEY" : (kc.B,) },
    0x43 : { "ESC": "%63", "ALT": "%63", "SEQ": "c" , "KEY" : (kc.C,) },
    0x44 : { "ESC": "%64", "ALT": "%64", "SEQ": "d" , "KEY" : (kc.D,) },
    0x45 : { "ESC": "%65", "ALT": "%65", "SEQ": "e" , "KEY" : (kc.E,) },
    0x46 : { "ESC": "%66", "ALT": "%66", "SEQ": "f" , "KEY" : (kc.F,) },
    0x47 : { "ESC": "%67", "ALT": "%67", "SEQ": "g" , "KEY" : (kc.G,) },
    0x48 : { "ESC": "%68", "ALT": "%68", "SEQ": "h" , "KEY" : (kc.H,) },
    0x49 : { "ESC": "%69", "ALT": "%69", "SEQ": "i" , "KEY" : (kc.I,) },
    0x4A : { "ESC": "%6A", "ALT": "%6A", "SEQ": "j" , "KEY" : (kc.J,) },
    0x4B : { "ESC": "%6B", "ALT": "%6B", "SEQ": "k" , "KEY" : (kc.K,) },
    0x4C : { "ESC": "%6C", "ALT": "%6C", "SEQ": "l" , "KEY" : (kc.L,) },
    0x4D : { "ESC": "%6D", "ALT": "%6D", "SEQ": "m" , "KEY" : (kc.M,) },
    0x4E : { "ESC": "%6E", "ALT": "%6E", "SEQ": "n" , "KEY" : (kc.N,) },
    0x4F : { "ESC": "%6F", "ALT": "%6F", "SEQ": "o" , "KEY" : (kc.O,) },
    0x50 : { "ESC": "%70", "ALT": "%70", "SEQ": "p" , "KEY" : (kc.P,) },
    0x51 : { "ESC": "%71", "ALT": "%71", "SEQ": "q" , "KEY" : (kc.Q,) },
    0x52 : { "ESC": "%72", "ALT": "%72", "SEQ": "r" , "KEY" : (kc.R,) },
    0x53 : { "ESC": "%73", "ALT": "%73", "SEQ": "s" , "KEY" : (kc.S,) },
    0x54 : { "ESC": "%74", "ALT": "%74", "SEQ": "t" , "KEY" : (kc.T,) },
    0x55 : { "ESC": "%75", "ALT": "%75", "SEQ": "u" , "KEY" : (kc.U,) },
    0x56 : { "ESC": "%76", "ALT": "%76", "SEQ": "v" , "KEY" : (kc.V,) },
    0x57 : { "ESC": "%77", "ALT": "%77", "SEQ": "w" , "KEY" : (kc.W,) },
    0x58 : { "ESC": "%78", "ALT": "%78", "SEQ": "x" , "KEY" : (kc.X,) },
    0x59 : { "ESC": "%79", "ALT": "%79", "SEQ": "y" , "KEY" : (kc.Y,) },
    0x5A : { "ESC": "%7A", "ALT": "%7A", "SEQ": "z" , "KEY" : (kc.Z,) },
    0x5B : { "ESC": "%7B", "ALT": "%7B", "SEQ": "{" , "KEY" : (kc.SHIFT, kc.LEFT_BRACKET) },
    0x5C : { "ESC": "%7C", "ALT": "%7C", "SEQ": "|" , "KEY" : (kc.SHIFT, kc.KEYPAD_BACKSLASH) },
    0x5D : { "ESC": "%7D", "ALT": "%7D", "SEQ": "}" , "KEY" : (kc.SHIFT, kc.RIGHT_BRACKET) },
    0x5E : { "ESC": "%7E", "ALT": "%7E", "SEQ": "~" , "KEY" : (kc.SHIFT, kc.POUND) },

    0x60 : { "ESC": "%80", "ALT": "%E2%82%AC", "SEQ": "€", "KEY": () },
    0x61 : { "ESC": "%81", "ALT": "%81"      , "SEQ": "" , "KEY": () },
    0x62 : { "ESC": "%82", "ALT": "%E2%80%9A", "SEQ": "‚", "KEY": () },
    0x63 : { "ESC": "%83", "ALT": "%C6%92"   , "SEQ": "ƒ", "KEY": () },
    0x64 : { "ESC": "%84", "ALT": "%E2%80%9E", "SEQ": "„", "KEY": () },
    0x65 : { "ESC": "%85", "ALT": "%E2%80%A6", "SEQ": "…", "KEY": () },
    0x66 : { "ESC": "%86", "ALT": "%E2%80%A0", "SEQ": "†", "KEY": () },
    0x67 : { "ESC": "%87", "ALT": "%E2%80%A1", "SEQ": "‡", "KEY": () },
    0x68 : { "ESC": "%88", "ALT": "%CB%86"   , "SEQ": "ˆ", "KEY": () },
    0x69 : { "ESC": "%89", "ALT": "%E2%80%B0", "SEQ": "‰", "KEY": () },
    0x6A : { "ESC": "%8A", "ALT": "%C5%A0"   , "SEQ": "Š", "KEY": () },
    0x6B : { "ESC": "%8B", "ALT": "%E2%80%B9", "SEQ": "‹", "KEY": () },
    0x6C : { "ESC": "%8C", "ALT": "%C5%92"   , "SEQ": "Œ", "KEY": () },
    0x6D : { "ESC": "%8D", "ALT": "%C5%8D"   , "SEQ": "" , "KEY": () },
    0x6E : { "ESC": "%8E", "ALT": "%C5%BD"   , "SEQ": "Ž", "KEY": () },
    0x6F : { "ESC": "%8F", "ALT": "%8F"      , "SEQ": "" , "KEY": () },
    0x70 : { "ESC": "%90", "ALT": "%C2%90"   , "SEQ": "" , "KEY": () },
    0x71 : { "ESC": "%91", "ALT": "%E2%80%98", "SEQ": "‘", "KEY": () },
    0x72 : { "ESC": "%92", "ALT": "%E2%80%99", "SEQ": "’", "KEY": () },
    0x73 : { "ESC": "%93", "ALT": "%E2%80%9C", "SEQ": "“", "KEY": () },
    0x74 : { "ESC": "%94", "ALT": "%E2%80%9D", "SEQ": "”", "KEY": () },
    0x75 : { "ESC": "%95", "ALT": "%E2%80%A2", "SEQ": "•", "KEY": () },
    0x76 : { "ESC": "%96", "ALT": "%E2%80%93", "SEQ": "–", "KEY": () },
    0x77 : { "ESC": "%97", "ALT": "%E2%80%94", "SEQ": "—", "KEY": () },
    0x78 : { "ESC": "%98", "ALT": "%CB%9C"   , "SEQ": "˜", "KEY": () },
    0x79 : { "ESC": "%99", "ALT": "%E2%84"   , "SEQ": "™", "KEY": () },
    0x7A : { "ESC": "%9A", "ALT": "%C5%A1"   , "SEQ": "š", "KEY": () },
    0x7B : { "ESC": "%9B", "ALT": "%E2%80"   , "SEQ": "›", "KEY": () },
    0x7C : { "ESC": "%9C", "ALT": "%C5%93"   , "SEQ": "œ", "KEY": () },
    0x7D : { "ESC": "%9D", "ALT": "%9D"      , "SEQ": "" , "KEY": () },
    0x7E : { "ESC": "%9E", "ALT": "%C5%BE"   , "SEQ": "ž", "KEY": () },
    0x7F : { "ESC": "%9F", "ALT": "%C5%B8"   , "SEQ": "Ÿ", "KEY": () },
    0x80 : { "ESC": "%A0", "ALT": "%C2%A0"   , "SEQ": " ", "KEY": () },
    0x81 : { "ESC": "%A1", "ALT": "%C2%A1"   , "SEQ": "¡", "KEY": () },
    0x82 : { "ESC": "%A2", "ALT": "%C2%A2"   , "SEQ": "¢", "KEY": () },
    0x83 : { "ESC": "%A3", "ALT": "%C2%A3"   , "SEQ": "£", "KEY": (kc.SHIFT, kc.THREE) },
    0x84 : { "ESC": "%A4", "ALT": "%C2%A4"   , "SEQ": "¤", "KEY": () },
    0x85 : { "ESC": "%A5", "ALT": "%C2%A5"   , "SEQ": "¥", "KEY": () },
    0x86 : { "ESC": "%A6", "ALT": "%C2%A6"   , "SEQ": "¦", "KEY": () },
    0x87 : { "ESC": "%A7", "ALT": "%C2%A7"   , "SEQ": "§", "KEY": () },
    0x88 : { "ESC": "%A8", "ALT": "%C2%A8"   , "SEQ": "¨", "KEY": () },
    0x89 : { "ESC": "%A9", "ALT": "%C2%A9"   , "SEQ": "©", "KEY": () },
    0x8A : { "ESC": "%AA", "ALT": "%C2%AA"   , "SEQ": "ª", "KEY": () },
    0x8B : { "ESC": "%AB", "ALT": "%C2%AB"   , "SEQ": "«", "KEY": () },
    0x8C : { "ESC": "%AC", "ALT": "%C2%AC"   , "SEQ": "¬", "KEY": (kc.SHIFT, kc.GRAVE_ACCENT) },
    0x8D : { "ESC": "%AD", "ALT": "%C2%AD"   , "SEQ": "­", "KEY": () },
    0x8E : { "ESC": "%AE", "ALT": "%C2%AE"   , "SEQ": "®", "KEY": () },
    0x8F : { "ESC": "%AF", "ALT": "%C2%AF"   , "SEQ": "¯", "KEY": () },
    0x90 : { "ESC": "%B0", "ALT": "%C2%B0"   , "SEQ": "°", "KEY": () },
    0x91 : { "ESC": "%B1", "ALT": "%C2%B1"   , "SEQ": "±", "KEY": () },
    0x92 : { "ESC": "%B2", "ALT": "%C2%B2"   , "SEQ": "²", "KEY": () },
    0x93 : { "ESC": "%B3", "ALT": "%C2%B3"   , "SEQ": "³", "KEY": () },
    0x94 : { "ESC": "%B4", "ALT": "%C2%B4"   , "SEQ": "´", "KEY": () },
    0x95 : { "ESC": "%B5", "ALT": "%C2%B5"   , "SEQ": "µ", "KEY": () },
    0x96 : { "ESC": "%B6", "ALT": "%C2%B6"   , "SEQ": "¶", "KEY": () },
    0x97 : { "ESC": "%B7", "ALT": "%C2%B7"   , "SEQ": "·", "KEY": () },
    0x98 : { "ESC": "%B8", "ALT": "%C2%B8"   , "SEQ": "¸", "KEY": () },
    0x99 : { "ESC": "%B9", "ALT": "%C2%B9"   , "SEQ": "¹", "KEY": () },
    0x9A : { "ESC": "%BA", "ALT": "%C2%BA"   , "SEQ": "º", "KEY": () },
    0x9B : { "ESC": "%BB", "ALT": "%C2%BB"   , "SEQ": "»", "KEY": () },
    0x9C : { "ESC": "%BC", "ALT": "%C2%BC"   , "SEQ": "¼", "KEY": () },
    0x9D : { "ESC": "%BD", "ALT": "%C2%BD"   , "SEQ": "½", "KEY": () },
    0x9E : { "ESC": "%BE", "ALT": "%C2%BE"   , "SEQ": "¾", "KEY": () },
    0x9F : { "ESC": "%BF", "ALT": "%C2%BF"   , "SEQ": "¿", "KEY": () },
    0xA0 : { "ESC": "%C0", "ALT": "%C3%80"   , "SEQ": "À", "KEY": () },
    0xA1 : { "ESC": "%C1", "ALT": "%C3%81"   , "SEQ": "Á", "KEY": () },
    0xA2 : { "ESC": "%C2", "ALT": "%C3%82"   , "SEQ": "Â", "KEY": () },
    0xA3 : { "ESC": "%C3", "ALT": "%C3%83"   , "SEQ": "Ã", "KEY": () },
    0xA4 : { "ESC": "%C4", "ALT": "%C3%84"   , "SEQ": "Ä", "KEY": () },
    0xA5 : { "ESC": "%C5", "ALT": "%C3%85"   , "SEQ": "Å", "KEY": () },
    0xA6 : { "ESC": "%C6", "ALT": "%C3%86"   , "SEQ": "Æ", "KEY": () },
    0xA7 : { "ESC": "%C7", "ALT": "%C3%87"   , "SEQ": "Ç", "KEY": () },
    0xA8 : { "ESC": "%C8", "ALT": "%C3%88"   , "SEQ": "È", "KEY": () },
    0xA9 : { "ESC": "%C9", "ALT": "%C3%89"   , "SEQ": "É", "KEY": () },
    0xAA : { "ESC": "%CA", "ALT": "%C3%8A"   , "SEQ": "Ê", "KEY": () },
    0xAB : { "ESC": "%CB", "ALT": "%C3%8B"   , "SEQ": "Ë", "KEY": () },
    0xAC : { "ESC": "%CC", "ALT": "%C3%8C"   , "SEQ": "Ì", "KEY": () },
    0xAD : { "ESC": "%CD", "ALT": "%C3%8D"   , "SEQ": "Í", "KEY": () },
    0xAE : { "ESC": "%CE", "ALT": "%C3%8E"   , "SEQ": "Î", "KEY": () },
    0xAF : { "ESC": "%CF", "ALT": "%C3%8F"   , "SEQ": "Ï", "KEY": () },
    0xB0 : { "ESC": "%D0", "ALT": "%C3%90"   , "SEQ": "Ð", "KEY": () },
    0xB1 : { "ESC": "%D1", "ALT": "%C3%91"   , "SEQ": "Ñ", "KEY": () },
    0xB2 : { "ESC": "%D2", "ALT": "%C3%92"   , "SEQ": "Ò", "KEY": () },
    0xB3 : { "ESC": "%D3", "ALT": "%C3%93"   , "SEQ": "Ó", "KEY": () },
    0xB4 : { "ESC": "%D4", "ALT": "%C3%94"   , "SEQ": "Ô", "KEY": () },
    0xB5 : { "ESC": "%D5", "ALT": "%C3%95"   , "SEQ": "Õ", "KEY": () },
    0xB6 : { "ESC": "%D6", "ALT": "%C3%96"   , "SEQ": "Ö", "KEY": () },
    0xB7 : { "ESC": "%D7", "ALT": "%C3%97"   , "SEQ": "×", "KEY": () },
    0xB8 : { "ESC": "%D8", "ALT": "%C3%98"   , "SEQ": "Ø", "KEY": () },
    0xB9 : { "ESC": "%D9", "ALT": "%C3%99"   , "SEQ": "Ù", "KEY": () },
    0xBA : { "ESC": "%DA", "ALT": "%C3%9A"   , "SEQ": "Ú", "KEY": () },
    0xBB : { "ESC": "%DB", "ALT": "%C3%9B"   , "SEQ": "Û", "KEY": () },
    0xBC : { "ESC": "%DC", "ALT": "%C3%9C"   , "SEQ": "Ü", "KEY": () },
    0xBD : { "ESC": "%DD", "ALT": "%C3%9D"   , "SEQ": "Ý", "KEY": () },
    0xBE : { "ESC": "%DE", "ALT": "%C3%9E"   , "SEQ": "Þ", "KEY": () },
    0xBF : { "ESC": "%DF", "ALT": "%C3%9F"   , "SEQ": "ß", "KEY": () },
    0xC0 : { "ESC": "%E0", "ALT": "%C3%A0"   , "SEQ": "à", "KEY": () },
    0xC1 : { "ESC": "%E1", "ALT": "%C3%A1"   , "SEQ": "á", "KEY": () },
    0xC2 : { "ESC": "%E2", "ALT": "%C3%A2"   , "SEQ": "â", "KEY": () },
    0xC3 : { "ESC": "%E3", "ALT": "%C3%A3"   , "SEQ": "ã", "KEY": () },
    0xC4 : { "ESC": "%E4", "ALT": "%C3%A4"   , "SEQ": "ä", "KEY": () },
    0xC5 : { "ESC": "%E5", "ALT": "%C3%A5"   , "SEQ": "å", "KEY": () },
    0xC6 : { "ESC": "%E6", "ALT": "%C3%A6"   , "SEQ": "æ", "KEY": () },
    0xC7 : { "ESC": "%E7", "ALT": "%C3%A7"   , "SEQ": "ç", "KEY": () },
    0xC8 : { "ESC": "%E8", "ALT": "%C3%A8"   , "SEQ": "è", "KEY": () },
    0xC9 : { "ESC": "%E9", "ALT": "%C3%A9"   , "SEQ": "é", "KEY": () },
    0xCA : { "ESC": "%EA", "ALT": "%C3%AA"   , "SEQ": "ê", "KEY": () },
    0xCB : { "ESC": "%EB", "ALT": "%C3%AB"   , "SEQ": "ë", "KEY": () },
    0xCC : { "ESC": "%EC", "ALT": "%C3%AC"   , "SEQ": "ì", "KEY": () },
    0xCD : { "ESC": "%ED", "ALT": "%C3%AD"   , "SEQ": "í", "KEY": () },
    0xCE : { "ESC": "%EE", "ALT": "%C3%AE"   , "SEQ": "î", "KEY": () },
    0xCF : { "ESC": "%EF", "ALT": "%C3%AF"   , "SEQ": "ï", "KEY": () },
    0xD0 : { "ESC": "%F0", "ALT": "%C3%B0"   , "SEQ": "ð", "KEY": () },
    0xD1 : { "ESC": "%F1", "ALT": "%C3%B1"   , "SEQ": "ñ", "KEY": () },
    0xD2 : { "ESC": "%F2", "ALT": "%C3%B2"   , "SEQ": "ò", "KEY": () },
    0xD3 : { "ESC": "%F3", "ALT": "%C3%B3"   , "SEQ": "ó", "KEY": () },
    0xD4 : { "ESC": "%F4", "ALT": "%C3%B4"   , "SEQ": "ô", "KEY": () },
    0xD5 : { "ESC": "%F5", "ALT": "%C3%B5"   , "SEQ": "õ", "KEY": () },
    0xD6 : { "ESC": "%F6", "ALT": "%C3%B6"   , "SEQ": "ö", "KEY": () },
    0xD7 : { "ESC": "%F7", "ALT": "%C3%B7"   , "SEQ": "÷", "KEY": () },
    0xD8 : { "ESC": "%F8", "ALT": "%C3%B8"   , "SEQ": "ø", "KEY": () },
    0xD9 : { "ESC": "%F9", "ALT": "%C3%B9"   , "SEQ": "ù", "KEY": () },
    0xDA : { "ESC": "%FA", "ALT": "%C3%BA"   , "SEQ": "ú", "KEY": () },
    0xDB : { "ESC": "%FB", "ALT": "%C3%BB"   , "SEQ": "û", "KEY": () },
    0xDC : { "ESC": "%FC", "ALT": "%C3%BC"   , "SEQ": "ü", "KEY": () },
    0xDD : { "ESC": "%FD", "ALT": "%C3%BD"   , "SEQ": "ý", "KEY": () },
    0xDE : { "ESC": "%FE", "ALT": "%C3%BE"   , "SEQ": "þ", "KEY": () },
    0xDF : { "ESC": "%FF", "ALT": "%C3%BF"   , "SEQ": "ÿ", "KEY": () },

    0xE0 : { "ESC": "%00", "ALT": "%00", "SEQ": "[NUL]", "KEY": () },
    0xE1 : { "ESC": "%01", "ALT": "%01", "SEQ": "[SOH]", "KEY": () },
    0xE2 : { "ESC": "%02", "ALT": "%02", "SEQ": "[STX]", "KEY": () },
    0xE3 : { "ESC": "%03", "ALT": "%03", "SEQ": "[ETX]", "KEY": () },
    0xE4 : { "ESC": "%04", "ALT": "%04", "SEQ": "[EOT]", "KEY": () },
    0xE5 : { "ESC": "%05", "ALT": "%05", "SEQ": "[ENQ]", "KEY": () },
    0xE6 : { "ESC": "%06", "ALT": "%06", "SEQ": "[ACK]", "KEY": () },
    0xE7 : { "ESC": "%07", "ALT": "%07", "SEQ": "[BEL]", "KEY": () },
    0xE8 : { "ESC": "%08", "ALT": "%08", "SEQ": "[BS]" , "KEY": () },
    0xE9 : { "ESC": "%09", "ALT": "%09", "SEQ": "[HT]" , "KEY": () },
    0xEA : { "ESC": "%0A", "ALT": "%0A", "SEQ": "[LF]" , "KEY": () },
    0xEB : { "ESC": "%0B", "ALT": "%0B", "SEQ": "[VT]" , "KEY": () },
    0xEC : { "ESC": "%0C", "ALT": "%0C", "SEQ": "[FF]" , "KEY": () },
    0xED : { "ESC": "%0D", "ALT": "%0D", "SEQ": "[CR]" , "KEY": () },
    0xEE : { "ESC": "%0E", "ALT": "%0E", "SEQ": "[SO]" , "KEY": () },
    0xEF : { "ESC": "%0F", "ALT": "%0F", "SEQ": "[SI]" , "KEY": () },
    0xF0 : { "ESC": "%10", "ALT": "%10", "SEQ": "[DLE]", "KEY": () },
    0xF1 : { "ESC": "%11", "ALT": "%11", "SEQ": "[DC1]", "KEY": () },
    0xF2 : { "ESC": "%12", "ALT": "%12", "SEQ": "[DC2]", "KEY": () },
    0xF3 : { "ESC": "%13", "ALT": "%13", "SEQ": "[DC3]", "KEY": () },
    0xF4 : { "ESC": "%14", "ALT": "%14", "SEQ": "[DC4]", "KEY": () },
    0xF5 : { "ESC": "%15", "ALT": "%15", "SEQ": "[NAK]", "KEY": () },
    0xF6 : { "ESC": "%16", "ALT": "%16", "SEQ": "[SYN]", "KEY": () },
    0xF7 : { "ESC": "%17", "ALT": "%17", "SEQ": "[ETB]", "KEY": () },
    0xF8 : { "ESC": "%18", "ALT": "%18", "SEQ": "[CAN]", "KEY": () },
    0xF9 : { "ESC": "%19", "ALT": "%19", "SEQ": "[EM]" , "KEY": () },
    0xFA : { "ESC": "%1A", "ALT": "%1A", "SEQ": "[SUB]", "KEY": () },
    0xFB : { "ESC": "%1B", "ALT": "%1B", "SEQ": "[ESC]", "KEY": () },
    0xFC : { "ESC": "%1C", "ALT": "%1C", "SEQ": "[FS]" , "KEY": () },
    0xFD : { "ESC": "%1D", "ALT": "%1D", "SEQ": "[GS]" , "KEY": () },
    0xFE : { "ESC": "%1E", "ALT": "%1E", "SEQ": "[RS]" , "KEY": () },
    0xFF : { "ESC": "%1F", "ALT": "%1F", "SEQ": "[US]" , "KEY": () },

    0x5F : { "ESC": "%7F", "ALT": "%7F", "SEQ": "[DEL]" , "KEY" : () },
}

selected = 0
def display(i = 0):
    global index
    slide = macropad.display_text()
    slide[0].text = "ESC: " + str(index[i]["ESC"])
    slide[1].text = "ALT: " + str(index[i]["ALT"])
    slide[2].text = "SEQ: " + str(index[i]["SEQ"])
    slide[3].text = "KEY: " + str(index[i]["KEY"])
    slide.show()

encoder_position = 0
display(encoder_position)

while True:
    current_position = macropad.encoder
    if current_position > encoder_position:
        selected += 1
        if selected >= len(index):
            selected = 0
        display(selected)
        encoder_position = current_position
    elif current_position < encoder_position:
        selected -= 1
        if selected < 0:
            selected = len(index) - 1
        display(selected)
        encoder_position = current_position

    macropad.encoder_switch_debounced.update()
    if macropad.encoder_switch_debounced.pressed:
        caps = macropad.keyboard.led_on(macropad.keyboard.LED_CAPS_LOCK)
        if caps:
            macropad.keyboard.send(kc.CAPS_LOCK)
        macropad.keyboard.send(*(index[selected]["KEY"]))
        if caps:
            macropad.keyboard.send(kc.CAPS_LOCK)
    