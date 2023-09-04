# UnoOnUno - TheMindVirus @ 23:29 03/09/2023
# This sketch is a port of the game UNO originally made for Arduino Uno Rev3 at the same time.
# While it is relatively stable, a few features might be missing or may need some tweaks.

import random, time

def TYPE(CARD):
    return (CARD & 0x0F)
def CHROMA(CARD):
    return (CARD & 0xF0)

def SET_RED(CARD):
    return (CARD + 0x10)
def SET_YLW(CARD):
    return (CARD + 0x20)
def SET_GRN(CARD):
    return (CARD + 0x40)
def SET_BLU(CARD):
    return (CARD + 0x80)
def SET_NUL(CARD):
    return (CARD & 0xF0)

def IS_RED(CARD):
    return ((CARD & 0x10) != 0)
def IS_YLW(CARD):
    return ((CARD & 0x20) != 0)
def IS_GRN(CARD):
    return ((CARD & 0x40) != 0)
def IS_BLU(CARD):
    return ((CARD & 0x80) != 0)
def IS_NUL(CARD):
    return (CHROMA(CARD) == 0)

CARD_0 = 0
CARD_1 = 1
CARD_2 = 2
CARD_3 = 3
CARD_4 = 4
CARD_5 = 5
CARD_6 = 6
CARD_7 = 7
CARD_8 = 8
CARD_9 = 9
CARD_SKIP = 10
CARD_SWAP = 11
CARD_ADD2 = 12
CARD_DRAW = 13
CARD_ADD4 = 14
CARD_NULL = 15

PILE = \
[
    SET_RED(CARD_0), SET_RED(CARD_1), SET_RED(CARD_2), SET_RED(CARD_3), SET_RED(CARD_4), SET_RED(CARD_5), SET_RED(CARD_6), SET_RED(CARD_7), SET_RED(CARD_8), SET_RED(CARD_9), SET_RED(CARD_SKIP), SET_RED(CARD_SWAP), SET_RED(CARD_ADD2), CARD_DRAW,
    SET_YLW(CARD_0), SET_YLW(CARD_1), SET_YLW(CARD_2), SET_YLW(CARD_3), SET_YLW(CARD_4), SET_YLW(CARD_5), SET_YLW(CARD_6), SET_YLW(CARD_7), SET_YLW(CARD_8), SET_YLW(CARD_9), SET_YLW(CARD_SKIP), SET_YLW(CARD_SWAP), SET_YLW(CARD_ADD2), CARD_DRAW,
    SET_GRN(CARD_0), SET_GRN(CARD_1), SET_GRN(CARD_2), SET_GRN(CARD_3), SET_GRN(CARD_4), SET_GRN(CARD_5), SET_GRN(CARD_6), SET_GRN(CARD_7), SET_GRN(CARD_8), SET_GRN(CARD_9), SET_GRN(CARD_SKIP), SET_GRN(CARD_SWAP), SET_GRN(CARD_ADD2), CARD_DRAW,
    SET_BLU(CARD_0), SET_BLU(CARD_1), SET_BLU(CARD_2), SET_BLU(CARD_3), SET_BLU(CARD_4), SET_BLU(CARD_5), SET_BLU(CARD_6), SET_BLU(CARD_7), SET_BLU(CARD_8), SET_BLU(CARD_9), SET_BLU(CARD_SKIP), SET_BLU(CARD_SWAP), SET_BLU(CARD_ADD2), CARD_DRAW,
    
    SET_RED(CARD_NULL), SET_RED(CARD_1), SET_RED(CARD_2), SET_RED(CARD_3), SET_RED(CARD_4), SET_RED(CARD_5), SET_RED(CARD_6), SET_RED(CARD_7), SET_RED(CARD_8), SET_RED(CARD_9), SET_RED(CARD_SKIP), SET_RED(CARD_SWAP), SET_RED(CARD_ADD2), CARD_ADD4,
    SET_YLW(CARD_NULL), SET_YLW(CARD_1), SET_YLW(CARD_2), SET_YLW(CARD_3), SET_YLW(CARD_4), SET_YLW(CARD_5), SET_YLW(CARD_6), SET_YLW(CARD_7), SET_YLW(CARD_8), SET_YLW(CARD_9), SET_YLW(CARD_SKIP), SET_YLW(CARD_SWAP), SET_YLW(CARD_ADD2), CARD_ADD4,
    SET_GRN(CARD_NULL), SET_GRN(CARD_1), SET_GRN(CARD_2), SET_GRN(CARD_3), SET_GRN(CARD_4), SET_GRN(CARD_5), SET_GRN(CARD_6), SET_GRN(CARD_7), SET_GRN(CARD_8), SET_GRN(CARD_9), SET_GRN(CARD_SKIP), SET_GRN(CARD_SWAP), SET_GRN(CARD_ADD2), CARD_ADD4,
    SET_BLU(CARD_NULL), SET_BLU(CARD_1), SET_BLU(CARD_2), SET_BLU(CARD_3), SET_BLU(CARD_4), SET_BLU(CARD_5), SET_BLU(CARD_6), SET_BLU(CARD_7), SET_BLU(CARD_8), SET_BLU(CARD_9), SET_BLU(CARD_SKIP), SET_BLU(CARD_SWAP), SET_BLU(CARD_ADD2), CARD_ADD4,
]

MAX_COUNT = len(PILE)
VARIANTS = 4
PLAYERS = 4
STARTING = 7

TIMEOUT = 10 #3000
TIMEOUT_HI = (TIMEOUT & 0xFF00) >> 8
TIMEOUT_LO = TIMEOUT & 0xFF

pile = []
hand = []

game = 0
turn = 0
reverse = False
skip = False
card = 0

def shuffle(n = 0):
    global pile
    for x in range(0, n):
        Z = len(pile)
        for i in range(0, Z):
            idx1, idx2 = [random.randrange(0, Z), random.randrange(0, Z)]
            pile[idx1], pile[idx2] = [pile[idx2], pile[idx1]]
    
        j = 0
        i = 0
        for x in range(Z - 1, -1, -1):
            i = x - 1
            pile[j], pile[i] = [pile[i], pile[j]]
            j += 1
            if (j >= Z / 2):
                break

def load_pile(n = 0):
    global pile
    j = 0
    pile = []
    for i in range(0, MAX_COUNT):
        if (TYPE(PILE[i]) != CARD_NULL):
            pile.append(PILE[i])
            j += 1
    return j

def empty_hands():
    global hand
    hand = []
    for i in range(0, PLAYERS):
        hand.append([])
    return PLAYERS

def fill_hands():
    for j in range(0, PLAYERS):
        for i in range(0, STARTING):
            draw_card(j)
    return PLAYERS

def draw_card(n = 0):
    global pile, hand, game
    if (len(pile) == 0):
        print("[INFO]: DRAW")
        game += 1
        setup()
        #return x
    x = n % PLAYERS
    #hand.append(pile[-1])
    #pile.pop()
    hand[x].append(pile.pop())
    return x

def place_card(n = 0):
    global card, skip, reverse, hand, game
    x = n % PLAYERS
    if (skip == True):
        skip = False
        next_turn()
        return x
    for i in range(0, len(hand[x])):
        if ((CHROMA(hand[x][i]) == CHROMA(card)) \
        or  (IS_NUL(hand[x][i]) or IS_NUL(card))):
            card = hand[x][i]
            if (TYPE(card) == CARD_SWAP):
                reverse = not reverse
            if (TYPE(card) == CARD_SKIP):
                skip = True
            if ((TYPE(card) == CARD_DRAW) or (TYPE(card) == CARD_ADD4)):
                c = random.randrange(0, VARIANTS) % VARIANTS
                if (c == 0):
                    card = SET_RED(card)
                elif (c == 1):
                    card = SET_YLW(card)
                elif (c == 2):
                    card = SET_GRN(card)
                elif (c == 3):
                    card = SET_BLU(card)
                elif (c == 3):
                    card = SET_NUL(card)
            hand[x].pop(i)
            if (len(hand[x]) == 0):
                print("[INFO]: Player ", end = "")
                print(x + 1, end = "")
                print(" Wins!")
                game += 1
                setup()
            return x
    if (TYPE(card) == CARD_ADD2):
        draw_card(x)
        #draw_card(x)
        #return x
    if (TYPE(card) == CARD_ADD4):
        draw_card(x)
        draw_card(x)
        draw_card(x)
        #draw_card(x)
        #return x
    draw_card(x)
    return x

def show_cards():
    print("[GAME]: ", end = "")
    print(game + 1)
    print("[TURN]: ", end = "")
    print(turn + 1)
    print("[CARD]: ", end = "")
    print(card + 0)
    print("[PILE]: ", end = "")
    for i in range(0, len(pile)):
        print(pile[i], end = "")
        print(", ", end = "")
    print()
    for j in range(0, PLAYERS):
        print("[HAND]: ", end = "")
        for i in range(0, len(hand[j])):
            print(hand[j][i], end = "")
            print(", ", end = "")
        print()
    return 0

def next_turn(n = 0):
    global turn
    if (not reverse):
        turn += 1
        if (turn >= PLAYERS):
            turn = 0
    else:
        if (turn > 0):
            turn -= 1
        else:
            turn = PLAYERS - 1
    return turn

def setup():
    global turn
    print("<<<UNO>>>")
    print("[INFO]: Game Now Loading...")
    print("[INFO]: (shuffling might need a few seconds)")
    time.sleep(3000 / 1000)
    #time.sleep(15000 / 1000)
    load_pile()
    shuffle(len(pile) / 2)
    empty_hands()
    fill_hands()
    turn = 0
    show_cards()
    time.sleep(((TIMEOUT_HI << 8) + TIMEOUT_LO) / 1000)

def loop():
    place_card(turn)
    show_cards()
    time.sleep(TIMEOUT / 1000)
    next_turn()

if __name__ == "__main__":
    setup()
    while (1):
        loop()