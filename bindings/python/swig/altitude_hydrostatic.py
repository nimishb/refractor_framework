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
            fp, pathname, description = imp.find_module('_altitude_hydrostatic', [dirname(__file__)])
        except ImportError:
            import _altitude_hydrostatic
            return _altitude_hydrostatic
        if fp is not None:
            try:
                _mod = imp.load_module('_altitude_hydrostatic', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _altitude_hydrostatic = swig_import_helper()
    del swig_import_helper
else:
    import _altitude_hydrostatic
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



_altitude_hydrostatic.SHARED_PTR_DISOWN_swigconstant(_altitude_hydrostatic)
SHARED_PTR_DISOWN = _altitude_hydrostatic.SHARED_PTR_DISOWN

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

import full_physics_swig.altitude
import full_physics_swig.generic_object
import full_physics_swig.state_vector
class AltitudeHydrostatic(full_physics_swig.altitude.Altitude):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.altitude.Altitude]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, AltitudeHydrostatic, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.altitude.Altitude]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, AltitudeHydrostatic, name)
    __repr__ = _swig_repr

    def __init__(self, P, T, Latitude, Surface_height):
        this = _altitude_hydrostatic.new_AltitudeHydrostatic(P, T, Latitude, Surface_height)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def altitude(self, P):
        return _altitude_hydrostatic.AltitudeHydrostatic_altitude(self, P)

    def gravity(self, P):
        return _altitude_hydrostatic.AltitudeHydrostatic_gravity(self, P)

    def notify_update(self, *args):
        return _altitude_hydrostatic.AltitudeHydrostatic_notify_update(self, *args)

    def clone(self, *args):
        return _altitude_hydrostatic.AltitudeHydrostatic_clone(self, *args)
    __swig_destroy__ = _altitude_hydrostatic.delete_AltitudeHydrostatic
    __del__ = lambda self: None
AltitudeHydrostatic_swigregister = _altitude_hydrostatic.AltitudeHydrostatic_swigregister
AltitudeHydrostatic_swigregister(AltitudeHydrostatic)

# This file is compatible with both classic and new-style classes.


