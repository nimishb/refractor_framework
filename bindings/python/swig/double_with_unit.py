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
            fp, pathname, description = imp.find_module('_double_with_unit', [dirname(__file__)])
        except ImportError:
            import _double_with_unit
            return _double_with_unit
        if fp is not None:
            try:
                _mod = imp.load_module('_double_with_unit', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _double_with_unit = swig_import_helper()
    del swig_import_helper
else:
    import _double_with_unit
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



_double_with_unit.SHARED_PTR_DISOWN_swigconstant(_double_with_unit)
SHARED_PTR_DISOWN = _double_with_unit.SHARED_PTR_DISOWN

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
class DoubleWithUnit(full_physics_swig.generic_object.GenericObject):
    """

    We frequently have a double with units associated with it.

    This is a simple structure that just keeps these two things together.

    C++ includes: double_with_unit.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleWithUnit, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleWithUnit, name)
    __repr__ = _swig_repr

    def __str__(self):
        return _double_with_unit.DoubleWithUnit___str__(self)

    def __init__(self, *args):
        """

        FullPhysics::DoubleWithUnit::DoubleWithUnit(double V)

        """
        this = _double_with_unit.new_DoubleWithUnit(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __imul__(self, D):
        return _double_with_unit.DoubleWithUnit___imul__(self, D)

    def __idiv__(self, D):
        return _double_with_unit.DoubleWithUnit___idiv__(self, D)

    def __iadd__(self, D):
        return _double_with_unit.DoubleWithUnit___iadd__(self, D)

    def __isub__(self, D):
        return _double_with_unit.DoubleWithUnit___isub__(self, D)

    def convert(self, *args):
        """

        DoubleWithUnit FullPhysics::DoubleWithUnit::convert(const Unit &R) const
        Convert to the given units. 
        """
        return _double_with_unit.DoubleWithUnit_convert(self, *args)


    def convert_wave(self, *args):
        """

        DoubleWithUnit FullPhysics::DoubleWithUnit::convert_wave(const Unit &R, const SpectralDomain &Pixel_grid) const

        """
        return _double_with_unit.DoubleWithUnit_convert_wave(self, *args)


    def _value(self):
        return _double_with_unit.DoubleWithUnit__value(self)

    def _value_set(self, V):
        return _double_with_unit.DoubleWithUnit__value_set(self, V)

    def _units(self):
        return _double_with_unit.DoubleWithUnit__units(self)

    def _units_set(self, U):
        return _double_with_unit.DoubleWithUnit__units_set(self, U)

    def __mul__(self, Y):
        return _double_with_unit.DoubleWithUnit___mul__(self, Y)

    def __div__(self, Y):
        return _double_with_unit.DoubleWithUnit___div__(self, Y)

    def __truediv__(self, Y):
        return _double_with_unit.DoubleWithUnit___truediv__(self, Y)

    def __add__(self, Y):
        return _double_with_unit.DoubleWithUnit___add__(self, Y)

    def __sub__(self, Y):
        return _double_with_unit.DoubleWithUnit___sub__(self, Y)

    @property
    def value(self):
      return self._value()

    @value.setter
    def value(self, val):
      self._value_set(val)

    @property
    def units(self):
      return self._units()

    @units.setter
    def units(self,val):
        self._units_set(val)

    __swig_destroy__ = _double_with_unit.delete_DoubleWithUnit
    __del__ = lambda self: None
DoubleWithUnit_swigregister = _double_with_unit.DoubleWithUnit_swigregister
DoubleWithUnit_swigregister(DoubleWithUnit)

# This file is compatible with both classic and new-style classes.


