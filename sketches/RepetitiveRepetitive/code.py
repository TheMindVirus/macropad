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