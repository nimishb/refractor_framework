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
            fp, pathname, description = imp.find_module('_default_constant', [dirname(__file__)])
        except ImportError:
            import _default_constant
            return _default_constant
        if fp is not None:
            try:
                _mod = imp.load_module('_default_constant', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _default_constant = swig_import_helper()
    del swig_import_helper
else:
    import _default_constant
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



_default_constant.SHARED_PTR_DISOWN_swigconstant(_default_constant)
SHARED_PTR_DISOWN = _default_constant.SHARED_PTR_DISOWN

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

import full_physics_swig.constant
import full_physics_swig.generic_object
class DefaultConstant(full_physics_swig.constant.Constant):
    """

    This class is an implementation of Constant that uses hard coded
    values suitable for Earth.

    This is useful for things like unit tests where we just need
    reasonable values.

    C++ includes: default_constant.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.constant.Constant]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DefaultConstant, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.constant.Constant]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DefaultConstant, name)
    __repr__ = _swig_repr

    def __init__(self):
        """

        FullPhysics::DefaultConstant::DefaultConstant()

        """
        this = _default_constant.new_DefaultConstant()
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def _v_rayleigh_depolarization_factor(self):
        """

        virtual double FullPhysics::DefaultConstant::rayleigh_depolarization_factor() const
        Rayleigh depolarization factor. 
        """
        return _default_constant.DefaultConstant__v_rayleigh_depolarization_factor(self)


    @property
    def rayleigh_depolarization_factor(self):
        return self._v_rayleigh_depolarization_factor()


    def _v_rayleigh_a(self):
        """

        virtual DoubleWithUnit FullPhysics::DefaultConstant::rayleigh_a() const
        Rayleigh "a" value.

        This along with "b" are the wavelength dependence coefficients for
        the refractive index. 
        """
        return _default_constant.DefaultConstant__v_rayleigh_a(self)


    @property
    def rayleigh_a(self):
        return self._v_rayleigh_a()


    def _v_rayleigh_b(self):
        """

        virtual DoubleWithUnit FullPhysics::DefaultConstant::rayleigh_b() const
        Rayleigh "b" value.

        This along with "a" are the wavelength dependence coefficients for
        the refractive index. 
        """
        return _default_constant.DefaultConstant__v_rayleigh_b(self)


    @property
    def rayleigh_b(self):
        return self._v_rayleigh_b()


    def _v_molar_weight_dry_air(self):
        """

        virtual DoubleWithUnit FullPhysics::DefaultConstant::molar_weight_dry_air() const
        Molar weight of dry air. 
        """
        return _default_constant.DefaultConstant__v_molar_weight_dry_air(self)


    @property
    def molar_weight_dry_air(self):
        return self._v_molar_weight_dry_air()


    def _v_molar_weight_water(self):
        """

        virtual DoubleWithUnit FullPhysics::DefaultConstant::molar_weight_water() const
        Molar weight of water. 
        """
        return _default_constant.DefaultConstant__v_molar_weight_water(self)


    @property
    def molar_weight_water(self):
        return self._v_molar_weight_water()


    def _v_avogadro_constant(self):
        """

        virtual DoubleWithUnit FullPhysics::DefaultConstant::avogadro_constant() const
        Avogadro constant. 
        """
        return _default_constant.DefaultConstant__v_avogadro_constant(self)


    @property
    def avogadro_constant(self):
        return self._v_avogadro_constant()

    __swig_destroy__ = _default_constant.delete_DefaultConstant
    __del__ = lambda self: None
DefaultConstant_swigregister = _default_constant.DefaultConstant_swigregister
DefaultConstant_swigregister(DefaultConstant)

# This file is compatible with both classic and new-style classes.


