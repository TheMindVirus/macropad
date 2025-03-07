# DefunLisp - TheMindVirus
# This sketch is highly experimental but when it functions correctly it's self referencing and reflective
# Edge Case Keywords from lisp and micro lisp are replaced with the corresponding python and micro python

# and replaces edge case keywords from lisp and micro lisp with the corresponding python keywords

code = \
"""
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
"""

import sys

print(code)

code = code.replace("  ", "    ")
code = code.replace("(defun", "def")
code = code.replace("lisp ()", "lisp():")
code = code.replace("\"", "\"\"\"")
code = code.replace("(with", "with")
code = code.replace(" file => ", "")
code = code.replace("std", "file = sys.std")
code = code.replace("(loop for line", "for line")
code = code.replace("=>", "in")
code = code.replace("('in')", "\"=>\" in line:")
code = code.replace("(when in line in", "if")
code = code.replace("line in (file)", "line in file.read().split(\"\\n\"):")
code = code.replace("(print to ", "print(line, ")
code = code.replace(" in (line)", ")")
code = code.replace("')", "', 'r') as file:")
code = code.replace(" )", "")
code = code.replace("\n)", "")
code = code.strip()

print(code)
"""
exec(code)

entry = lisp

print("\n", entry, "\n")

entry()
"""
