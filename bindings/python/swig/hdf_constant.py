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
            fp, pathname, description = imp.find_module('_hdf_constant', [dirname(__file__)])
        except ImportError:
            import _hdf_constant
            return _hdf_constant
        if fp is not None:
            try:
                _mod = imp.load_module('_hdf_constant', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _hdf_constant = swig_import_helper()
    del swig_import_helper
else:
    import _hdf_constant
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



_hdf_constant.SHARED_PTR_DISOWN_swigconstant(_hdf_constant)
SHARED_PTR_DISOWN = _hdf_constant.SHARED_PTR_DISOWN

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
class HdfConstant(full_physics_swig.constant.Constant):
    """

    C++ includes: hdf_constant.h

    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.constant.Constant]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HdfConstant, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.constant.Constant]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HdfConstant, name)
    __repr__ = _swig_repr

    def __init__(self, Hdf_file):
        """

        FullPhysics::HdfConstant::HdfConstant(const boost::shared_ptr< HdfFile > &Hdf_file)

        """
        this = _hdf_constant.new_HdfConstant(Hdf_file)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def _v_rayleigh_depolarization_factor(self):
        """

        virtual double FullPhysics::HdfConstant::rayleigh_depolarization_factor() const
        Rayleigh depolarization factor. 
        """
        return _hdf_constant.HdfConstant__v_rayleigh_depolarization_factor(self)


    def _v_rayleigh_a(self):
        """

        virtual DoubleWithUnit FullPhysics::HdfConstant::rayleigh_a() const
        Rayleigh "a" value.

        This along with "b" are the wavelength dependence coefficients for
        the refractive index. 
        """
        return _hdf_constant.HdfConstant__v_rayleigh_a(self)


    def _v_rayleigh_b(self):
        """

        virtual DoubleWithUnit FullPhysics::HdfConstant::rayleigh_b() const
        Rayleigh "b" value.

        This along with "a" are the wavelength dependence coefficients for
        the refractive index. 
        """
        return _hdf_constant.HdfConstant__v_rayleigh_b(self)


    def _v_molar_weight_dry_air(self):
        """

        virtual DoubleWithUnit FullPhysics::HdfConstant::molar_weight_dry_air() const
        Molar weight of dry air. 
        """
        return _hdf_constant.HdfConstant__v_molar_weight_dry_air(self)


    def _v_molar_weight_water(self):
        """

        virtual DoubleWithUnit FullPhysics::HdfConstant::molar_weight_water() const
        Molar weight of water. 
        """
        return _hdf_constant.HdfConstant__v_molar_weight_water(self)


    def _v_avogadro_constant(self):
        """

        virtual DoubleWithUnit FullPhysics::HdfConstant::avogadro_constant() const
        Avogadro constant. 
        """
        return _hdf_constant.HdfConstant__v_avogadro_constant(self)

    __swig_destroy__ = _hdf_constant.delete_HdfConstant
    __del__ = lambda self: None
HdfConstant_swigregister = _hdf_constant.HdfConstant_swigregister
HdfConstant_swigregister(HdfConstant)

# This file is compatible with both classic and new-style classes.


