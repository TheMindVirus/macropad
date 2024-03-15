```py
# RepetitiveRepetitive - TheMindVirus
# This sketch looks for repeating patterns in a block of text that it generates from a wordlist.
# An augment in the text changes the integrity of the results by showing up different numbers of counts.

text = \
"""
Lorem Ipsum Ipsum Lorem Lorem Ipsum Ipsum Ipsum Lorem Lorem Lorem ...
"""

def repetitive_generate(length = 11, wordlist = ["Lorem", "Ipsum"]):
    text = ""
    for i in range(0, length):
        for j in range(0, len(wordlist)):
            if ((i % 2) == j):
                continue
            text += (wordlist[j] + " ") * i
    return text

text = repetitive_generate()
print(text, end = "\n\n")

def repetitive_augment(text):
    text = text[:100] + "Something"# + text[100:]
    return text

text = repetitive_augment(text)
print(text, end = "\n\n")

class repetitive_completion:
    repetitive_methods = {}
    repetitive_arguments = {}
    repetitive_verbosity = False
    def repetitive_dummy(method, *args, **kwargs):
        print("[WARN]: Method Not Implemented (\"" + str(method) + "(" + str(kwargs) + ")\")") 
    def repetitive_calling(method, *args, **kwargs):
        #nonlocal repetitive_methods
        if repetitive_completion.repetitive_verbosity:
            print("[_DBG]: ", repetitive_completion.repetitive_methods, repetitive_completion.repetitive_arguments)
            print("[_DBG]: ", dir(repetitive_completion.repetitive_methods))
            print("[_DBG]: ", dir(repetitive_completion.repetitive_arguments))
            print("[_DBG]: ", repetitive_completion.repetitive_methods.keys())
            print("[_DBG]: ", repetitive_completion.repetitive_arguments.keys())
            print("[_DBG]: ", repetitive_completion.repetitive_methods.values())
            print("[_DBG]: ", repetitive_completion.repetitive_arguments.values())
            print("[_DBG]: ", dir(list(repetitive_completion.repetitive_methods.values())[0]))
            #print("[_DBG]: ", list(repetitive_completion.repetitive_methods.values())[0].values())
        if method in repetitive_completion.repetitive_methods.keys() and repetitive_completion.repetitive_methods[method]:
            try:
                return repetitive_completion.repetitive_methods[method](*args, **kwargs)
            except:
                return repetitive_completion.repetitive_dummy(method, *args, **kwargs) #pass
        else:
            #repetitive_dummy(method, *args, **kwargs)
            return repetitive_completion.repetitive_dummy(method, *args, **kwargs)

def repetitive_patterns(text, length = -1, offset = 0, max_length = 10, min_length = 4, min_count = 2, *args, **kwargs):
    global repetitive_completion
    #.__kwargs__ = None #repetitive_patterns.__kwargs__ = None
    __kwargs__ = "text, length = -1, offset = 0, max_length = 10, min_length = 4, min_count = 2, *args, **kwargs"
    repetitive_completion.repetitive_arguments["repetitive_patterns"] = __kwargs__
    counts = {}
    if length < 0:
        length = len(text)
    max_length = max_length + 1
    errors = 0
    errors_prev = 0
    errors_limit = 10
    errors_threshold = 50
    progress = 0 # %
    progress_current = 0
    progress_lock = False
    progress_threshold = 75
    progress_total = length * (max_length - min_length)
    print("[INFO]: Please Wait...")
    #return
    def repetitive_handling(error = None, modeswitch = False):
        nonlocal errors, errors_prev, errors_limit, errors_threshold
        if modeswitch:
            raise
            return
        errors += 1
        if errors >= errors_limit and errors_prev < errors_limit:
            print("\033[2K\r[WARN]: Further Errors Suppressed")
        if errors < errors_limit:
            print("\033[2K\r[WARN]: Error: \"{}\"".format(str(error)))
        errors_prev = errors
    repetitive_completion.repetitive_methods["repetitive_handling"] = repetitive_handling
    def repetitive_printing(modeswitch = 0):
        nonlocal progress, progress_current, progress_lock, progress_threshold, progress_total
        if modeswitch == 1:
            if not progress_lock and progress > progress_threshold:
                print("\033[2K\r[INFO]: This might take a little while...")
                progress_lock = True
            return
        print("\033[2K\r[INFO]: Progress: {}% ({}/{})".format(int(progress), progress_current, progress_total), end = "" if modeswitch not in [2, 3] else "\n")
        if modeswitch == 3:
            print("[INFO]: Done!")
    repetitive_completion.repetitive_methods["repetitive_printing"] = repetitive_printing
    try:
        for i in range(min_length, max_length):
            try:
                for j in range(offset, length):
                    pattern = text[j:j+i]
                    counts[pattern] = 0
                    for k in range(offset, length):
                        try:
                            if (text[k:k+i] == pattern):
                                counts[pattern] += 1
                                if (j > errors_threshold):
                                    repetitive_handling(modeswitch = True)
                        except Exception as error:
                            repetitive_handling(error)
                    progress_current = (j - offset) + ((i - min_length) * length)
                    progress = (progress_current / progress_total) * 100
                    repetitive_printing()
                    repetitive_printing(modeswitch = 1)
            except Exception as error:
                repetitive_handling(error)
    except Exception as error:
        repetitive_handling(error)
    else:
        progress = 100
        progress_current = progress_total
    finally:
        repetitive_printing(modeswitch = 2)
    patterns = [key for key in counts.keys()]
    for i in range(0, len(patterns)):
        if (counts[patterns[i]] < min_count):
            counts.pop(patterns[i])
    return counts

counts = repetitive_patterns(text)
print(counts)

#repetitive_printing()
#repetitive_patterns.repetitive_printing(modeswitch = 1)
#repetitive_completion.repetitive_printing(modeswitch = 2)
repetitive_completion.repetitive_calling("repetitive_printing", modeswitch = 3)
```
```py
Adafruit CircuitPython 7.0.0-rc.1 on 2021-09-02; Adafruit Macropad RP2040 with rp2040
>>>
>>>
soft reboot

Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
code.py output:
Lorem Ipsum Ipsum Lorem Lorem Lorem Ipsum Ipsum Ipsum Ipsum Lorem Lorem Lorem Lorem Lorem Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum Lorem Lorem Lorem Lorem Lorem Lorem Lorem Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum

Lorem Ipsum Ipsum Lorem Lorem Lorem Ipsum Ipsum Ipsum Ipsum Lorem Lorem Lorem Lorem Lorem Ipsum IpsuSomething

[INFO]: Please Wait...
[WARN]: Error: "no active exception to reraise"
[WARN]: Error: "no active exception to reraise"
[WARN]: Error: "no active exception to reraise"
[WARN]: Error: "no active exception to reraise"
[WARN]: Error: "no active exception to reraise"
[WARN]: Error: "no active exception to reraise"
[WARN]: Error: "no active exception to reraise"
[WARN]: Error: "no active exception to reraise"
[WARN]: Error: "no active exception to reraise"
[WARN]: Further Errors Suppressed
[INFO]: This might take a little while...
[INFO]: Progress: 100% (763/763)
{'orem Ipsum': 3, 'um Lorem': 2, 'Lorem Ip': 3, 'psum Ip': 5, 'Lorem Ipsu': 3, 'em Lo': 6, 'rem Lor': 6, 'orem ': 9, 'rem L': 6, 'um Ipsum': 4, 'rem Ips': 3, 'rem I': 3, ' Ipsum': 7, 'Lorem ': 9, 'rem Lo': 6, 'psum ': 7, 'um Lo': 2, 'm Ipsum': 7, ' Ipsum I': 5, 'em Ipsum': 3, ' Ipsum L': 2, 'em Lorem': 6, 'em Ipsum ': 3, 'm Ipsum I': 5, 'um Ipsum ': 4, 'm Ipsum L': 2, 'psum Lor': 2, ' Lore': 8, 'sum Ipsu': 5, ' Ipsum Lo': 2, 'sum Lorem': 2, 'Lorem Lor': 6, ' Ipsu': 8, ' Lorem': 8, 'sum Lore': 2, 'sum Ipsum': 4, ' Lorem Lo': 6, 'em L': 6, 'um Ipsu': 5, 'm Ipsum Ip': 5, 'em I': 3, ' Ipsum Ips': 5, 'Ipsum Lor': 2, 'em Ips': 3, 'rem Lorem': 6, 'um Lore': 2, 'm Lo': 8, 'Ipsum Ip': 5, 'psum Ipsum': 4, ' Lorem L': 6, 'um L': 2, 'em Ipsu': 3, 'orem Lo': 6, 'um I': 5, ' Lorem I': 2, 'Ipsum ': 7, 'um Ips': 5, 'em Lore': 6, 'm Lorem Lo': 6, 'Lorem Lore': 6, 'rem Lorem ': 6, 'm Lorem Ip': 2, ' Lorem Ips': 2, 'psum Ipsu': 5, 'Ipsum Lore': 2, 'Ipsum Ipsu': 5, 'um Lorem L': 2, 'psum Lore': 2, 'orem Lorem': 6, 'sum Lo': 2, 'rem Ipsum ': 3, ' Ips': 8, ' Lorem Lor': 6, 'm Lorem': 8, 'em Lorem L': 4, 'm Ipsum ': 7, 'Ipsum L': 2, 'Ipsum Ips': 5, 'Ipsum I': 5, 'rem ': 9, 'sum Lor': 2, 'psum': 7, 'orem Lore': 6, ' Lorem Ip': 2, 'um Ipsum L': 2, 'em Lorem I': 2, 'um Ipsum I': 2, 'orem Ipsu': 3, 'psum L': 2, 'psum Ips': 5, 'em Ipsum I': 3, 'Ipsum': 7, 'm Ipsu': 8, 'psum I': 5, 'm Lorem I': 2, 'm Lore': 8, ' Lorem ': 8, 'm Lorem L': 6, 'sum Ipsum ': 4, 'm Ips': 8, 'um Ip': 5, 'um Lorem ': 2, 'rem Ip': 3, 'orem Ip': 3, 'um Lor': 2, 'rem Ipsum': 3, 'm Lorem ': 8, 'm Ip': 8, 'Lore': 9, 'em Ip': 3, 'Ipsum Lo': 2, 'em Lorem ': 6, 'orem I': 3, 'Ipsu': 8, 'Lorem': 9, 'psum Lo': 2, 'orem L': 6, 'Lorem Lo': 6, 'orem Lor': 6, 'sum L': 2, 'sum Ips': 5, 'em Lor': 6, 'sum I': 5, 'orem Ips': 3, 'rem Ipsu': 3, 'rem Lore': 6, ' Ipsum Lor': 2, 'sum ': 7, ' Ipsum Ip': 5, 'Lorem L': 6, 'orem': 9, ' Lor': 8, 'Lorem I': 3, 'Lorem Ips': 3, 'sum Ip': 5, ' Ipsum ': 7, 'm Lor': 8, 'm Ipsum Lo': 2, 'psum Lorem': 2, 'sum Lorem ': 2}
[INFO]: Progress: 100% (763/763)
[INFO]: Done!

Code done running.

Press any key to enter the REPL. Use CTRL-D to reload.
```