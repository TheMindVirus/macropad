# Electronic Prefix - TheMindVirus
# This sketch combines well known prefixes and suffixes from the field of electronics
# and combines them to form new words describing components which are potentially missing.

prefixes = \
[
    "Res", "Cap", "Trans", "Mem", "Neg",
    "Null", "Mon", "Di", "Tri", "Pent", "Hex", "Sept", "Oct", "Non", "Dec",
    "Var", "Vari"
]

suffixes = \
[
    "istor", "acitor", "ducer", "ode"
]

components = []
for prefix in prefixes:
    for suffix in suffixes:
        components.append(str(prefix) + str(suffix))

print(", ".join(components))
#for component in components:
#    print(component)

"""
Resistor, Resacitor, Resducer, Resode, Capistor, Capacitor, Capducer, Capode,
Transistor, Transacitor, Transducer, Transode, Memistor, Memacitor, Memducer,
Memode, Negistor, Negacitor, Negducer, Negode, Nullistor, Nullacitor, Nullducer,
Nullode, Monistor, Monacitor, Monducer, Monode, Diistor, Diacitor, Diducer,
Diode, Triistor, Triacitor, Triducer, Triode, Pentistor, Pentacitor, Pentducer,
Pentode, Hexistor, Hexacitor, Hexducer, Hexode, Septistor, Septacitor, Septducer,
Septode, Octistor, Octacitor, Octducer, Octode, Nonistor, Nonacitor, Nonducer,
Nonode, Decistor, Decacitor, Decducer, Decode, Varistor, Varacitor, Varducer,
Varode, Variistor, Variacitor, Variducer, Variode
"""
