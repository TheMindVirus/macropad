```py
import sys, random; n = 4444; sys.stdout.write(" ".join(["{:02X}".format(random.randint(0, 255)) if i != random.randint(0, n - 1) else "WI FI" for i in range(0, n)]));
```
Find `WI FI`:
![screenshot](https://github.com/themindvirus/macropad/blob/archive/sketches/HexSearchGame/screenshot.png)
![screenshot](https://github.com/themindvirus/macropad/blob/archive/sketches/HexSearchGame/repl.png)