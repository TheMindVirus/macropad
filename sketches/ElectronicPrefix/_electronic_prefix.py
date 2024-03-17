"""
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
"""

prefixes = \
[
    "Res", "Cap", "Trans", "Tran", "Thyr", "Therm", "Mem", "Memr", "Neg", "Surg", "Aud", "Vid", "Electr", "An", "Cath",
    "Null", "Mon", "Di", "Tri", "Tetr", "Pent", "Hex", "Sept", "Oct", "Non", "Dec", "Hen", "Ren", "Zen", "Red",
    "Var", "Vari", "Mod", "Und", "Acc", "Sole", "Solen", "Mo", "Ser", "Des", "Con", "Ins", "Entr", "Fl",
]

suffixes = \
[
    "istor", "ristor", "acitor", "citor", "ductor", "ducer", "former", "er",
    "ulator", "elerator", "noid", "ode", "eon", "ion", "oid", "tor", "vo", "ux", "ix",
]

components = []
for prefix in prefixes:
    for suffix in suffixes:
        components.append(str(prefix) + str(suffix))

print(", ".join(components))
#for component in components:
#    print(component)

"""Squeezed text (101 Lines)""" # Vibri

original = \
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

latest = \
"""
Resistor, Resristor, Resacitor, Rescitor, Resductor, Resducer, Resformer,
Reser, Resulator, Reselerator, Resnoid, Resode, Reseon, Resion, Resoid, Restor,
Resvo, Resux, Resix, Capistor, Capristor, Capacitor, Capcitor, Capductor,
Capducer, Capformer, Caper, Capulator, Capelerator, Capnoid, Capode, Capeon,
Capion, Capoid, Captor, Capvo, Capux, Capix, Transistor, Transristor,
Transacitor, Transcitor, Transductor, Transducer, Transformer, Transer,
Transulator, Transelerator, Transnoid, Transode, Transeon, Transion, Transoid,
Transtor, Transvo, Transux, Transix, Tranistor, Tranristor, Tranacitor,
Trancitor, Tranductor, Tranducer, Tranformer, Traner, Tranulator, Tranelerator,
Trannoid, Tranode, Traneon, Tranion, Tranoid, Trantor, Tranvo, Tranux, Tranix,
Thyristor, Thyrristor, Thyracitor, Thyrcitor, Thyrductor, Thyrducer,
Thyrformer, Thyrer, Thyrulator, Thyrelerator, Thyrnoid, Thyrode, Thyreon,
Thyrion, Thyroid, Thyrtor, Thyrvo, Thyrux, Thyrix, Thermistor, Thermristor,
Thermacitor, Thermcitor, Thermductor, Thermducer, Thermformer, Thermer,
Thermulator, Thermelerator, Thermnoid, Thermode, Thermeon, Thermion, Thermoid,
Thermtor, Thermvo, Thermux, Thermix, Memistor, Memristor, Memacitor, Memcitor,
Memductor, Memducer, Memformer, Memer, Memulator, Memelerator, Memnoid, Memode,
Memeon, Memion, Memoid, Memtor, Memvo, Memux, Memix, Memristor, Memrristor,
Memracitor, Memrcitor, Memrductor, Memrducer, Memrformer, Memrer, Memrulator,
Memrelerator, Memrnoid, Memrode, Memreon, Memrion, Memroid, Memrtor, Memrvo,
Memrux, Memrix, Negistor, Negristor, Negacitor, Negcitor, Negductor, Negducer,
Negformer, Neger, Negulator, Negelerator, Negnoid, Negode, Negeon, Negion,
Negoid, Negtor, Negvo, Negux, Negix, Surgistor, Surgristor, Surgacitor,
Surgcitor, Surgductor, Surgducer, Surgformer, Surger, Surgulator, Surgelerator,
Surgode, Surgeon, Surgion, Surgoid, Surgtor, Surgvo, Surgux, Surgix,
Audistor, Audristor, Audacitor, Audcitor, Audductor, Audducer, Audformer,
Auder, Audulator, Audelerator, Audnoid, Audode, Audeon, Audion, Audoid, Audtor,
Audvo, Audux, Audix, Vidistor, Vidristor, Vidacitor, Vidcitor, Vidductor,
Vidducer, Vidformer, Vider, Vidulator, Videlerator, Vidnoid, Vidode, Videon,
Vidion, Vidoid, Vidtor, Vidvo, Vidux, Vidix, Electristor, Electrristor,
Electracitor, Electrcitor, Electrductor, Electrducer, Electrformer, Electrer,
Electrulator, Electrelerator, Electrnoid, Electrode, Electreon, Electrion,
Electroid, Electrtor, Electrvo, Electrux, Electrix, Anistor, Anristor,
Anacitor, Ancitor, Anductor, Anducer, Anformer, Aner, Anulator, Anelerator,
Annoid, Anode, Aneon, Anion, Anoid, Antor, Anvo, Anux, Anix, Cathistor,
Cathristor, Cathacitor, Cathcitor, Cathductor, Cathducer, Cathformer, Cather,
Cathulator, Cathelerator, Cathnoid, Cathode, Catheon, Cathion, Cathoid,
Cathtor, Cathvo, Cathux, Cathix, Nullistor, Nullristor, Nullacitor, Nullcitor,
Nullductor, Nullducer, Nullformer, Nuller, Nullulator, Nullelerator, Nullnoid,
Nullode, Nulleon, Nullion, Nulloid, Nulltor, Nullvo, Nullux, Nullix, Monistor,
Monristor, Monacitor, Moncitor, Monductor, Monducer, Monformer, Moner,
Monulator, Monelerator, Monnoid, Monode, Moneon, Monion, Monoid, Montor,
Monvo, Monux, Monix, Diistor, Diristor, Diacitor, Dicitor, Diductor, Diducer,
Diformer, Dier, Diulator, Dielerator, Dinoid, Diode, Dieon, Diion, Dioid,
Ditor, Divo, Diux, Diix, Triistor, Triristor, Triacitor, Tricitor, Triductor,
Triducer, Triformer, Trier, Triulator, Trielerator, Trinoid, Triode, Trieon,
Triion, Trioid, Tritor, Trivo, Triux, Triix, Tetristor, Tetrristor, Tetracitor,
Tetrcitor, Tetrductor, Tetrducer, Tetrformer, Tetrer, Tetrulator, Tetrelerator,
Tetrode, Tetreon, Tetrion, Tetroid, Tetrtor, Tetrvo, Tetrux, Tetrix,
Pentistor, Pentristor, Pentacitor, Pentcitor, Pentductor, Pentducer,
Pentformer, Penter, Pentulator, Pentelerator, Pentnoid, Pentode, Penteon,
Pention, Pentoid, Penttor, Pentvo, Pentux, Pentix, Hexistor, Hexristor,
Hexacitor, Hexcitor, Hexductor, Hexducer, Hexformer, Hexer, Hexulator,
Hexelerator, Hexnoid, Hexode, Hexeon, Hexion, Hexoid, Hextor, Hexvo, Hexux,
Hexix, Septistor, Septristor, Septacitor, Septcitor, Septductor, Septducer,
Septformer, Septer, Septulator, Septelerator, Septnoid, Septode, Septeon,
Seption, Septoid, Septtor, Septvo, Septux, Septix, Octistor, Octristor,
Octacitor, Octcitor, Octductor, Octducer, Octformer, Octer, Octulator,
Octelerator, Octnoid, Octode, Octeon, Oction, Octoid, Octtor, Octvo, Octux,
Octix, Nonistor, Nonristor, Nonacitor, Noncitor, Nonductor, Nonducer,
Nonformer, Noner, Nonulator, Nonelerator, Nonnoid, Nonode, Noneon, Nonion,
Nonoid, Nontor, Nonvo, Nonux, Nonix, Decistor, Decristor, Decacitor, Deccitor,
Decductor, Decducer, Decformer, Decer, Deculator, Decelerator, Decnoid, Decode,
Deceon, Decion, Decoid, Dector, Decvo, Decux, Decix, Henistor, Henristor,
Henacitor, Hencitor, Henductor, Henducer, Henformer, Hener, Henulator,
Henelerator, Hennoid, Henode, Heneon, Henion, Henoid, Hentor, Henvo, Henux,
Henix, Renistor, Renristor, Renacitor, Rencitor, Renductor, Renducer,
Renformer, Rener, Renulator, Renelerator, Rennoid, Renode, Reneon, Renion,
Renoid, Rentor, Renvo, Renux, Renix, Zenistor, Zenristor, Zenacitor, Zencitor,
Zenductor, Zenducer, Zenformer, Zener, Zenulator, Zenelerator, Zennoid, Zenode,
Zeneon, Zenion, Zenoid, Zentor, Zenvo, Zenux, Zenix, Redistor, Redristor,
Redacitor, Redcitor, Redductor, Redducer, Redformer, Reder, Redulator,
Redelerator, Rednoid, Redode, Redeon, Redion, Redoid, Redtor, Redvo, Redux,
Redix, Varistor, Varristor, Varacitor, Varcitor, Varductor, Varducer,
Varformer, Varer, Varulator, Varelerator, Varnoid, Varode, Vareon, Varion,
Varoid, Vartor, Varvo, Varux, Varix, Variistor, Variristor, Variacitor,
Varicitor, Variductor, Variducer, Variformer, Varier, Variulator,
Varielerator, Varinoid, Variode, Varieon, Variion, Varioid, Varitor, Varivo,
Variux, Variix, Modistor, Modristor, Modacitor, Modcitor, Modductor, Modducer,
Modformer, Moder, Modulator, Modelerator, Modnoid, Modode, Modeon, Modion,
Modoid, Modtor, Modvo, Modux, Modix, Undistor, Undristor, Undacitor, Undcitor,
Undductor, Undducer, Undformer, Under, Undulator, Undelerator, Undnoid, Undode,
Undeon, Undion, Undoid, Undtor, Undvo, Undux, Undix, Accistor, Accristor,
Accacitor, Acccitor, Accductor, Accducer, Accformer, Accer, Acculator,
Accelerator, Accnoid, Accode, Acceon, Accion, Accoid, Acctor, Accvo, Accux,
Accix, Soleistor, Soleristor, Soleacitor, Solecitor, Soleductor, Soleducer,
Soleformer, Soleer, Soleulator, Soleelerator, Solenoid, Soleode, Soleeon,
Soleion, Soleoid, Soletor, Solevo, Soleux, Soleix, Solenistor, Solenristor,
Solenacitor, Solencitor, Solenductor, Solenducer, Solenformer, Solener,
Solenulator, Solenelerator, Solennoid, Solenode, Soleneon, Solenion, Solenoid,
Solentor, Solenvo, Solenux, Solenix, Moistor, Moristor, Moacitor, Mocitor,
Moductor, Moducer, Moformer, Moer, Moulator, Moelerator, Monoid, Moode, Moeon,
Moion, Mooid, Motor, Movo, Moux, Moix, Seristor, Serristor, Seracitor,
Sercitor, Serductor, Serducer, Serformer, Serer, Serulator, Serelerator,
Sernoid, Serode, Sereon, Serion, Seroid, Sertor, Servo, Serux, Serix,
Desistor, Desristor, Desacitor, Descitor, Desductor, Desducer, Desformer,
Deser, Desulator, Deselerator, Desnoid, Desode, Deseon, Desion, Desoid,
Destor, Desvo, Desux, Desix, Conistor, Conristor, Conacitor, Concitor,
Conductor, Conducer, Conformer, Coner, Conulator, Conelerator, Connoid,
Conode, Coneon, Conion, Conoid, Contor, Convo, Conux, Conix, Insistor,
Insristor, Insacitor, Inscitor, Insductor, Insducer, Insformer, Inser,
Insulator, Inselerator, Insnoid, Insode, Inseon, Insion, Insoid, Instor,
Insvo, Insux, Insix, Entristor, Entrristor, Entracitor, Entrcitor, Entrductor,
Entrducer, Entrformer, Entrer, Entrulator, Entrelerator, Entrnoid, Entrode,
Entreon, Entrion, Entroid, Entrtor, Entrvo, Entrux, Entrix, Flistor, Flristor,
Flacitor, Flcitor, Flductor, Flducer, Flformer, Fler, Flulator, Flelerator,
Flnoid, Flode, Fleon, Flion, Floid, Fltor, Flvo, Flux, Flix
"""

approved = \
"""
Resistor    : Buffers "Charge" Impedes "Voltage"
Capacitor   : Buffers "Voltage" Impedes "Charge"
Transistor  : Buffers "Charge" On "Voltage"
Transducer  : Buffers "Charge" On "Flux"
Transformer : Buffers "Voltage" And "Charge"
Trancitor   : Buffers "Transfer" "Resistance" On "Voltage"
Thyristor   : Buffers "Voltage" On "Charge"
Thermistor  : Buffers "Voltage" On "Thermals"
Memristor   : Buffers "Voltage" On "Flux"
Negistor    : Buffers Anti "Charge" Impedes Anti "Voltage"
Audion      : Buffers "Charge" On "Thermals"
Electrode   : Buffers "Voltage" And "Charge" And "Current" And "Flux" And Anti "Voltage" And Anti "Charge" And Anti "Current" And Anti "Flux"
Anode       : Buffers "Voltage" And "Charge" And "Current" And "Flux"
Cathode     : Buffers Anti "Voltage" And Anti "Charge" And Anti "Current" And Anti "Flux"
Monode      : Buffers "Current" On 1 "Voltage"
Diode       : Buffers "Current" On 2 "Voltage"
Triode      : Buffers "Current" On 3 "Voltage"
Tetrode     : Buffers "Current" On 4 "Voltage"
Pentode     : Buffers "Current" On 5 "Voltage"
Hexode      : Buffers "Current" On 6 "Voltage"
Septode     : Buffers "Current" On 7 "Voltage"
Octode      : Buffers "Current" On 8 "Voltage"
Nonode      : Buffers "Current" On 9 "Voltage"
Decelerator : Buffers "Inertia" Impedes "Velocity"
Decode      : Buffers "Current" On 10 "Voltage" "Remaps" "Unary"
Zener       : Impedes "Current" On 2 "Voltage"
Redux       : Buffers Anti And "Reduction" And "Minimalism" And "Simplicity"
Varistor    : Buffers "Voltage" On "Voltage"
Varacitor   : Buffers "Charge" On "Voltage"
Varier      : Buffers "Current" On "Voltage"
Modulator   : Buffers "Current2 On "Charge"
Under       : Impedes "Unary"
Undulator   : Buffers "Flux"
Accelerator : Buffers "Velocity"
Solenoid    : Buffers "Linear" "Flux" On "Voltage"
Motor       : Buffers "Rotary" "Flux" On "Voltage"
Servo       : Buffers "Rotary" "Flux" On 2 "Control" "Voltage"
Insulator   : Impedes "Voltage" "Conduction"
Flux        : Buffers "Flux"
"""

removed = \
"""
Desistor, Desristor, Desacitor, Descitor, Desductor, Desducer, Desformer,
Deser, Desulator, Deselerator, Desnoid, Desode, Deseon, Desion, Desoid,
Destor, Desvo, Desux, Desix,

Conistor, Conristor, Conacitor, Concitor,
Conductor, Conducer, Conformer, Coner, Conulator, Conelerator, Connoid,
Conode, Coneon, Conion, Conoid, Contor, Convo, Conux, Conix,

...
"""

cemented = \
"""
Thyracitor  : Buffers "Charge" On "Voltage"
Negode      : Buffers "Current" On 0 "Voltage"
Henode      : Buffers "Current" On 11 "Voltage"
Renode      : Buffers "Current" On 13 "Voltage"

Redristor   : Impedes "Resistance"
Redacitor   : Impedes "Capacitance"
Redductor   : Impedes "Transduction"
Redformer   : Impedes "Transformation"
Redulator   : Impedes "Undulation"
Redelerator : Buffers "Deceleration"
Redode      : Buffers "Current" On 14 "Voltage"

Zenristor   : Buffers "Resistance"
Zenacitor   : Buffers "Capacitance"
Zenductor   : Buffers "Transduction"
Zenformer   : Buffers "Transformation"
Zenulator   : Buffers "Undulation"
Zenelerator : Buffers "Acceleration"
Zenode      : Buffers "Current" On 15 "Voltage"
Zenvo       : Buffers "Velocity"

Variode     : Buffers "Current" On N# "Voltage"

Modistor    : Buffers "Transfer" "Resistance"
Modcitor    : Buffers "Transfer" "Capacitance"
Modducer    : Buffers "Transfer" "Transduction"
Mod(d)er    : Buffers "Transfer" "Transformation"
Modode      : Buffers "Transfer" "Current" On N# "Voltage"

Accistor    : Buffers "Transfer" "Transfer"
Acculator   : Buffers "Accumulation"
Accode      : Buffers "Current" On 10 "Voltage" "Remaps" "Unary"

Moistor     : Buffers "Moisture"

Seristor    : Buffers "Serial" "Resistance"
Seracitor   : Buffers "Serial" "Capacitance"
Serductor   : Buffers "Serial" "Transduction"
Serode      : Buffers "Current" On 1 1 "Voltage" "Remaps" "Unary"

Flix        : Buffers "Current" On M#(N# N#) "Voltage" "Remaps" "Unary"
"""
