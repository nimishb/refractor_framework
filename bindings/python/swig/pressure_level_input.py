# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pressure_level_input', [dirname(__file__)])
        except ImportError:
            import _pressure_level_input
            return _pressure_level_input
        if fp is not None:
            try:
                _mod = imp.load_module('_pressure_level_input', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pressure_level_input = swig_import_helper()
    del swig_import_helper
else:
    import _pressure_level_input
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except Exception:
    weakref_proxy = lambda x: x



_pressure_level_input.SHARED_PTR_DISOWN_swigconstant(_pressure_level_input)
SHARED_PTR_DISOWN = _pressure_level_input.SHARED_PTR_DISOWN

def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

import full_physics_swig.generic_object
class PressureLevelInput(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PressureLevelInput, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PressureLevelInput, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pressure_level_input.new_PressureLevelInput(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def _v_pressure_level(self):
        return _pressure_level_input.PressureLevelInput__v_pressure_level(self)

    @property
    def pressure_level(self):
        return self._v_pressure_level()


    def __str__(self):
        return _pressure_level_input.PressureLevelInput___str__(self)
    __swig_destroy__ = _pressure_level_input.delete_PressureLevelInput
    __del__ = lambda self: None
PressureLevelInput_swigregister = _pressure_level_input.PressureLevelInput_swigregister
PressureLevelInput_swigregister(PressureLevelInput)

# This file is compatible with both classic and new-style classes.


