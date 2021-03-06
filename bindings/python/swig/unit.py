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
            fp, pathname, description = imp.find_module('_unit', [dirname(__file__)])
        except ImportError:
            import _unit
            return _unit
        if fp is not None:
            try:
                _mod = imp.load_module('_unit', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _unit = swig_import_helper()
    del swig_import_helper
else:
    import _unit
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



_unit.SHARED_PTR_DISOWN_swigconstant(_unit)
SHARED_PTR_DISOWN = _unit.SHARED_PTR_DISOWN

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
class Unit(full_physics_swig.generic_object.GenericObject):
    """

    Libraries such as boost::units allow unit handling where we know the
    units at compile time.

    This class provide the same sort of handling, but for instances where
    we know the units at runtime rather than compile time (e.g., based on
    input read).

    We do dimensional analysis based on the SI base units. In order, these
    are meter, kilogram, second, Kelvin, Ampere, mole, candela, steradian,
    radian, photon, sample_index

    Note that steradian, radian and sample_index are actually
    dimensionless, but it is useful to track them. Also photon is a photon
    count, which doesn't really have units either. But it is useful to
    track because we can determine the photon count at a particular
    wavelength to convert to cm^-1.

    C++ includes: unit.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Unit, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Unit, name)
    __repr__ = _swig_repr

    def __str__(self):
        return _unit.Unit___str__(self)
    __swig_getmethods__["number_base_unit"] = _unit.Unit_number_base_unit_get
    if _newclass:
        number_base_unit = _swig_property(_unit.Unit_number_base_unit_get)

    def __init__(self, *args):
        """

        FullPhysics::Unit::Unit()

        """
        this = _unit.new_Unit(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def _v_base_unit_powers(self):
        """

        const boost::array<boost::rational<int>, number_base_unit>& FullPhysics::Unit::base_unit_powers() const
        Array of the powers of the base units (so m^2 would return
        (1,0,0,0,0,0,0,0)) 
        """
        return _unit.Unit__v_base_unit_powers(self)


    @property
    def base_unit_powers(self):
        return self._v_base_unit_powers()


    def _v_conversion_to_si(self):
        """

        double FullPhysics::Unit::conversion_to_si() const
        Conversion factor to go to SI units. 
        """
        return _unit.Unit__v_conversion_to_si(self)


    @property
    def conversion_to_si(self):
        return self._v_conversion_to_si()


    def _v_name(self):
        """

        void FullPhysics::Unit::name(const std::string &V)
        Set name of unit. 
        """
        return _unit.Unit__v_name(self)


    @property
    def name(self):
        return self._v_name()


    def is_commensurate(self, Units):
        """

        bool FullPhysics::Unit::is_commensurate(const Unit &Units) const
        Test if this set of units is commensurate with another set.

        If this return true then conversion() would succeed, otherwise it
        would fail. 
        """
        return _unit.Unit_is_commensurate(self, Units)


    def __imul__(self, *args):
        return _unit.Unit___imul__(self, *args)

    def __idiv__(self, Dunit):
        return _unit.Unit___idiv__(self, Dunit)

    def __mul__(self, *args):
        return _unit.Unit___mul__(self, *args)

    def __rmul__(self, X):
        return _unit.Unit___rmul__(self, X)

    def __div__(self, Y):
        return _unit.Unit___div__(self, Y)

    def __truediv__(self, Y):
        return _unit.Unit___truediv__(self, Y)

    def __rdiv__(self, X):
        return _unit.Unit___rdiv__(self, X)

    def __pow__(self, X):
        return _unit.Unit___pow__(self, X)

    @classmethod
    def pickle_format_version(cls):
      return 1

    def __reduce__(self):
      return _new_from_init, (self.__class__, 1, self.name)

    __swig_destroy__ = _unit.delete_Unit
    __del__ = lambda self: None
Unit_swigregister = _unit.Unit_swigregister
Unit_swigregister(Unit)


def conversion(Dunit_from, Dunit_to):
    return _unit.conversion(Dunit_from, Dunit_to)
conversion = _unit.conversion
# This file is compatible with both classic and new-style classes.


