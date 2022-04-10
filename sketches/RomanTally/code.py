# Roman Numerals and Tally - Alastair Cota
# Minimal implementation of converting integers to Roman Numerals and ASCII Tally

numerals       = ["", "I", "V", "X", "L", "C", "D",  "M",  "V̅",   "X̅",   "L̅",    "C̅",    "D̅",     "M̅"]
numeral_values = [ 0,   1,   5,  10,  50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
numeral_separators = ["̅"]

tallies      = ["", "|", "||", "|||", "||||", "++++"]
tally_values = [ 0,   1,    2,     3,      4,      5]
tally_separators = [" ", "-"]

def main():
    print(number2roman(931094))
    print(roman2number("C̅M̅X̅X̅X̅MXCIV"))
    print(number2tally(6))
    print(tally2number("++++ |"))
    print(roman2tally("IX"))
    print(tally2roman("++++ ||||"))

def number2roman(number):
    if number <= 0:
        return ""
    roman = "";
    rem = number
    for i in range(len(numerals) -1, 0, -1):
        roman += (numerals[i] * int(rem / numeral_values[i]))
        rem = rem % numeral_values[i]
    for i in range(len(numerals) -3, -1, -2):
        #print(numerals[i + 1] + (numerals[i] * 4), numerals[i] + numerals[i + 2])
        #print(numerals[i] * 4, numerals[i] + numerals[i + 1])
        roman = roman.replace(numerals[i + 1] + (numerals[i] * 4), numerals[i] + numerals[i + 2])
        roman = roman.replace(numerals[i] * 4, numerals[i] + numerals[i + 1])
    return roman

def roman2number(roman):
    number = 0
    for i in range(len(numerals) -3, -1, -2):
        #print(numerals[i] + numerals[i + 2], numerals[i + 1] + (numerals[i] * 4))
        #print(numerals[i] + numerals[i + 1], numerals[i] * 4)
        roman = roman.replace(numerals[i] + numerals[i + 2], numerals[i + 1] + (numerals[i] * 4))
        roman = roman.replace(numerals[i] + numerals[i + 1], numerals[i] * 4)
    tmp = ""
    for i in range(len(roman) -1, -1, -1):
        tmp = roman[i] + tmp
        if roman[i] not in numeral_separators:
            number += numeral_values[numerals.index(tmp)]
            tmp = ""
    return number

def number2tally(number):
    tally = ""
    if number < 0:
        tally += (tally_separators[1] + tally_separators[0])
        number = abs(number)
    rem = int(number / 5)
    for i in range(rem -1, -1, -1):
        tally += tallies[tally_values.index(5)]
        if i != -1:
            tally += tally_separators[0]
    rem = number % 5
    tally += tallies[rem]
    return tally

def tally2number(tally):
    number = 0
    skip = 0
    for i in range(0, len(tally)):
        if skip == 0:
            if tally[i] == tallies[1]:
                number += 1
            elif tally[i] == tallies[5][0]:
                number += 5
                skip = len(tallies[5])
        else:
            skip -= 1
    if tally[:2] == (tally_separators[1] + tally_separators[0]):
        number *= -1
    return number

def roman2tally(roman):
    tally = number2tally(roman2number(roman))
    return tally

def tally2roman(tally):
    roman = number2roman(tally2number(tally))
    return roman

if __name__ == "__main__":
    main()
