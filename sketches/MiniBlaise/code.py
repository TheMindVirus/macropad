# MiniBlaise - TheMindVirus @ 12:42 04/09/2023
# This sketch is an Early Language Model for transmogrifying python into Borland Delphi Pascal.
# The language was originally devised by French Mathematician, Blaise Pascal, in the 1650's. 

# VT100 - ^ replaced by \033
print("\033[48;5;230m", end = "") # Beige slof OpenBIOS background
print("\033[38;5;4m", end = "") # Optional blue text
print("\033[38;5;232m", end = "") # Compulsory black text
print("\033[1m", end = "") # Unsupported bold mode
# VT100 - CSI same as ESC, no extra [

# Enable PuTTY Option: Window->Colours:
# Indicated bolded text by changing: Both
# (The font and The colour)

pascal = \
"""
program Borland_Delphi;

uses time;

procedure main();
begin
    var a := readln("And again, please: ")
    halt
    writeln("You Wrote: " + a) { No Comment. }
end;
"""

#pascal = pascal.removeprefix("\n").removesuffix("\n")
pascal = pascal[1:-2]

pascal = pascal.replace(":=", "=")
pascal = pascal.replace(");", "):")
pascal = pascal.replace(";", "")
pascal = pascal.replace("{", "#")
pascal = pascal.replace("}", "#")
pascal = pascal.replace("program ", "# ")
pascal = pascal.replace("uses ", "import ")
pascal = pascal.replace("procedure ", "def ")
pascal = pascal.replace("begin", "    pass")
pascal = pascal.replace("var ", "")
pascal = pascal.replace("writeln", "print")
pascal = pascal.replace("readln", "input")
pascal = pascal.replace("halt", "time.sleep(1)")
pascal = pascal.replace("end", "    pass")

entry = "main"
param = ""
shim = "if __name__ == \"__main__\":\n    "
pascal = pascal + "\n\n" + shim + entry + "(" + param + ")"

print(pascal)
affirm = input("Please Enter Y to Continue: ")
if (affirm == "Y"):
    exec(pascal)

# VT100 - Reset
print("\033[0m")
# VT100 - Only applies after code completion