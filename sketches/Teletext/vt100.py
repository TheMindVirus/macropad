reset = "\033[0m"
bell = "\007"

black = "\033[38;5;0m"
white = "\033[38;5;15m"

red = "\033[38;5;1m"
green = "\033[38;5;2m"
yellow = "\033[38;5;3m"
blue = "\033[38;5;4m"

bg_black = "\033[48;5;0m"
bg_white = "\033[48;5;15m"

bg_red = "\033[48;5;1m"
bg_green = "\033[48;5;2m"
bg_yellow = "\033[48;5;3m"
bg_blue = "\033[48;5;4m"

def cursor(x, y):
    return "\033[" + str(y) + ";" + str(x) + "H"
