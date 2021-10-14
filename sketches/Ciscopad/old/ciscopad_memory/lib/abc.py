def abstractmethod(funcobj):
    #setattr(funcobj, "__isabstractmethod__", True) #Class does not behave like Object
    return funcobj

class abstractclassmethod(classmethod):
    __isabstractmethod__ = True

    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super().__init__(callable)


class abstractstaticmethod(staticmethod):
    __isabstractmethod__ = True

    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super().__init__(callable)


class abstractproperty(property):
    __isabstractmethod__ = True

try:
    from ciscopad.lib._abc import (get_cache_token, _abc_init, _abc_register,
                      _abc_instancecheck, _abc_subclasscheck, _get_dump,
                      _reset_registry, _reset_caches)
except ImportError:
    from ciscopad.lib._py_abc import ABCMeta, get_cache_token
    ABCMeta.__module__ = 'abc'
else:
    class ABCMeta(type):
        def __init__(cls, *args, **kwargs):
            pass

        def __new__(mcls, name, bases, namespace, **kwargs):
            cls = super().__new__(mcls, name, bases, namespace, **kwargs)
            _abc_init(cls)
            return cls

        def register(cls, subclass):
            return _abc_register(cls, subclass)

        def __instancecheck__(cls, instance):
            return _abc_instancecheck(cls, instance)

        def __subclasscheck__(cls, subclass):
            return _abc_subclasscheck(cls, subclass)

        def _dump_registry(cls, file=None):
            print("Class: {}.{}".format(cls.__module__, cls.__qualname__), file=file)
            print("Inv. counter: {}".format(get_cache_token()), file=file)
            (_abc_registry, _abc_cache, _abc_negative_cache,
             _abc_negative_cache_version) = _get_dump(cls)
            print("_abc_registry: '{}'".format(_abc_registry), file=file)
            print("_abc_cache: '{}'".format(_abc_cache), file=file)
            print("_abc_negative_cache: '{}'".format(_abc_negative_cache), file=file)
            print("_abc_negative_cache_version: '{}'.format(_abc_negative_cache_version)",
                  file=file)

        def _abc_registry_clear(cls):
            _reset_registry(cls)

        def _abc_caches_clear(cls):
            _reset_caches(cls)


def update_abstractmethods(cls):
    if not hasattr(cls, '__abstractmethods__'):
        # We check for __abstractmethods__ here because cls might by a C
        # implementation or a python implementation (especially during
        # testing), and we want to handle both cases.
        return cls

    abstracts = set()
    # Check the existing abstract methods of the parents, keep only the ones
    # that are not implemented.
    for scls in cls.__bases__:
        for name in getattr(scls, '__abstractmethods__', ()):
            value = getattr(cls, name, None)
            if getattr(value, "__isabstractmethod__", False):
                abstracts.add(name)
    # Also add any other newly added abstract methods.
    for name, value in cls.__dict__.items():
        if getattr(value, "__isabstractmethod__", False):
            abstracts.add(name)
    cls.__abstractmethods__ = frozenset(abstracts)
    return cls

#Helper class that provides a standard way to create an ABC using inheritance.
#class ABC(MetaClass = ABCMeta):
class ABC(ABCMeta):
    def __init__(self, *args, **kwargs):
        self.__slots__ = ()