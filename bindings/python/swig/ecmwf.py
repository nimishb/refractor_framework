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
            fp, pathname, description = imp.find_module('_ecmwf', [dirname(__file__)])
        except ImportError:
            import _ecmwf
            return _ecmwf
        if fp is not None:
            try:
                _mod = imp.load_module('_ecmwf', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ecmwf = swig_import_helper()
    del swig_import_helper
else:
    import _ecmwf
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



_ecmwf.SHARED_PTR_DISOWN_swigconstant(_ecmwf)
SHARED_PTR_DISOWN = _ecmwf.SHARED_PTR_DISOWN

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
class Ecmwf(full_physics_swig.generic_object.GenericObject):
    """

    This class is used to read some of the fields from the ECMWF file,
    which can then be used for things such as the apriori.

    Since resampled ECMWF files can differ between instrument types, the
    read routines are pure virtual and need to be implemented for the
    specifics of the instrument specific ECMWF files.

    C++ includes: ecmwf.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Ecmwf, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Ecmwf, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _ecmwf.delete_Ecmwf
    __del__ = lambda self: None

    def specific_humidity(self, *args):
        """

        virtual ArrayAd<double, 1> FullPhysics::Ecmwf::specific_humidity(const ArrayAd< double, 1 > &Pressure_level) const =0

        """
        return _ecmwf.Ecmwf_specific_humidity(self, *args)


    def h2o_vmr(self, *args):
        """

        ArrayAd<double, 1> FullPhysics::Ecmwf::h2o_vmr(const ArrayAd< double, 1 > &Pressure_level) const

        """
        return _ecmwf.Ecmwf_h2o_vmr(self, *args)


    def ozone_mmr(self, *args):
        """

        virtual ArrayAd<double, 1> FullPhysics::Ecmwf::ozone_mmr(const ArrayAd< double, 1 > &Pressure_level) const

        """
        return _ecmwf.Ecmwf_ozone_mmr(self, *args)


    def ozone_vmr(self, *args):
        """

        ArrayAd<double, 1> FullPhysics::Ecmwf::ozone_vmr(const ArrayAd< double, 1 > &Pressure_level) const

        """
        return _ecmwf.Ecmwf_ozone_vmr(self, *args)


    def temperature_grid(self):
        """

        virtual void FullPhysics::Ecmwf::temperature_grid(blitz::Array< double, 1 > &Pressure, blitz::Array< double, 1 > &T)
        const =0
        Temperature grid on the ECMWF pressure grid.

        The temperature is in Kelvin, and the Pressure is in pascals. 
        """
        return _ecmwf.Ecmwf_temperature_grid(self)


    def specific_humidity_grid(self):
        """

        virtual void FullPhysics::Ecmwf::specific_humidity_grid(blitz::Array< double, 1 > &Pressure, blitz::Array< double, 1 > &H)
        const =0
        Humidity on the ECMWF pressure grid.

        Pressure is in pascals. 
        """
        return _ecmwf.Ecmwf_specific_humidity_grid(self)


    def ozone_mmr_grid(self):
        """

        virtual void FullPhysics::Ecmwf::ozone_mmr_grid(blitz::Array< double, 1 > &Pressure, blitz::Array< double, 1 > &H)
        const
        Ozone mass mixing ratio on the ECMWF pressure grid.

        Pressure is in pascals. 
        """
        return _ecmwf.Ecmwf_ozone_mmr_grid(self)


    def temperature(self, *args):
        """

        virtual ArrayAd<double, 1> FullPhysics::Ecmwf::temperature(const ArrayAd< double, 1 > &Pressure_level) const =0

        """
        return _ecmwf.Ecmwf_temperature(self, *args)


    def _v_surface_pressure(self):
        """

        virtual double FullPhysics::Ecmwf::surface_pressure() const =0
        Get the surface pressure from the Ecmwf file. 
        """
        return _ecmwf.Ecmwf__v_surface_pressure(self)


    @property
    def surface_pressure(self):
        return self._v_surface_pressure()


    def _v_windspeed(self):
        """

        virtual double FullPhysics::Ecmwf::windspeed() const
        Calculate windspeed magnitude from windspeed components. 
        """
        return _ecmwf.Ecmwf__v_windspeed(self)


    @property
    def windspeed(self):
        return self._v_windspeed()


    def _v_windspeed_u(self):
        """

        virtual double FullPhysics::Ecmwf::windspeed_u() const =0
        The U component windspeed from the Ecmwf file. 
        """
        return _ecmwf.Ecmwf__v_windspeed_u(self)


    @property
    def windspeed_u(self):
        return self._v_windspeed_u()


    def _v_windspeed_v(self):
        """

        virtual double FullPhysics::Ecmwf::windspeed_v() const =0
        The V component windspeed from the Ecmwf file. 
        """
        return _ecmwf.Ecmwf__v_windspeed_v(self)


    @property
    def windspeed_v(self):
        return self._v_windspeed_v()


    def __str__(self):
        return _ecmwf.Ecmwf___str__(self)
Ecmwf_swigregister = _ecmwf.Ecmwf_swigregister
Ecmwf_swigregister(Ecmwf)

# This file is compatible with both classic and new-style classes.


