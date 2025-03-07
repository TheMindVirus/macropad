```py
Adafruit CircuitPython 7.0.0-rc.1 on 2021-09-02; Adafruit Macropad RP2040 with rp2040
>>>
soft reboot

Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
code.py output:

(defun lisp ()
  "multiline
   comment"
  (with open file => ('code.py')
    (loop for line => (file)
      (when in line => ('=>')
        (print to stdout => (line)
        )
      )
    )
  )
)

def lisp():
    """multiline
     comment"""
    with open('code.py', 'r') as file:
        for line in file.read().split("\n"):
            if "=>" in line:
                print(line, file = sys.stdout)

 <function lisp at 0x20009d00> ### <function lisp at 0x0000029ADAD872E0>

  (with open file => ('code.py')
    (loop for line => (file)
      (when in line => ('=>')
        (print to stdout => (line)
code = code.replace(" file => ", "")
code = code.replace("=>", "in")
code = code.replace("('in')", "\"=>\" in line:")

Code done running.

Press any key to enter the REPL. Use CTRL-D to reload.
```