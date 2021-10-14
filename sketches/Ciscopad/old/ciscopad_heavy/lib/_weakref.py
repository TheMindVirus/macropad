class ref:
    def __init__(self, *args):
        pass

def _weakref_supported(*args):
    return False

def getweakrefcount(*args):
    return 0

def _weakref_getweakrefcount_impl(module, object):
    return None

def is_dead_weakref(value):
    return True

def _remove_dead_weakref(*args):
    return True

def _weakref__remove_dead_weakref_impl(module, dct, key):
    return None

def getweakrefs(*args):
    return None

def weakref_getweakrefs(self, obj):
    return None

def proxy(*args):
    return None

def weakref_proxy(self, *args):
    return None

CallableProxyType = None
ProxyType = None
ReferenceType = None

weakref_functions = []

def weakref_exec(module):
    return None
