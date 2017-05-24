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
            fp, pathname, description = imp.find_module('_fp_time', [dirname(__file__)])
        except ImportError:
            import _fp_time
            return _fp_time
        if fp is not None:
            try:
                _mod = imp.load_module('_fp_time', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _fp_time = swig_import_helper()
    del swig_import_helper
else:
    import _fp_time
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



_fp_time.SHARED_PTR_DISOWN_swigconstant(_fp_time)
SHARED_PTR_DISOWN = _fp_time.SHARED_PTR_DISOWN

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

import datetime
import time

def _new_time(pgs):
  return Time.time_pgs(pgs)

class Time(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Time, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Time, name)
    __repr__ = _swig_repr
    __swig_getmethods__["time_pgs"] = lambda x: _fp_time.Time_time_pgs
    if _newclass:
        time_pgs = staticmethod(_fp_time.Time_time_pgs)
    __swig_getmethods__["time_unix"] = lambda x: _fp_time.Time_time_unix
    if _newclass:
        time_unix = staticmethod(_fp_time.Time_time_unix)

    def _v_unix_time(self):
        return _fp_time.Time__v_unix_time(self)

    @property
    def unix_time(self):
        return self._v_unix_time()


    def _v_pgs_time(self):
        return _fp_time.Time__v_pgs_time(self)

    @property
    def pgs_time(self):
        return self._v_pgs_time()

    __swig_getmethods__["parse_time"] = lambda x: _fp_time.Time_parse_time
    if _newclass:
        parse_time = staticmethod(_fp_time.Time_parse_time)

    def __str__(self):
        return _fp_time.Time___str__(self)

    def __cmp__(self, T2):
        return _fp_time.Time___cmp__(self, T2)

    def __add__(self, T):
        return _fp_time.Time___add__(self, T)

    def __radd__(self, T):
        return _fp_time.Time___radd__(self, T)

    def __sub__(self, *args):
        return _fp_time.Time___sub__(self, *args)

    def __reduce__(self):
      return _new_time, (self.pgs(),)



    def __init__(self):
        this = _fp_time.new_Time()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _fp_time.delete_Time
    __del__ = lambda self: None
Time_swigregister = _fp_time.Time_swigregister
Time_swigregister(Time)

def Time_time_pgs(pgs):
    return _fp_time.Time_time_pgs(pgs)
Time_time_pgs = _fp_time.Time_time_pgs

def Time_time_unix(unix_time):
    return _fp_time.Time_time_unix(unix_time)
Time_time_unix = _fp_time.Time_time_unix

def Time_parse_time(Time_string):
    return _fp_time.Time_parse_time(Time_string)
Time_parse_time = _fp_time.Time_parse_time

# This file is compatible with both classic and new-style classes.


