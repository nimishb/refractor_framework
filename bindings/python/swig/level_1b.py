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
            fp, pathname, description = imp.find_module('_level_1b', [dirname(__file__)])
        except ImportError:
            import _level_1b
            return _level_1b
        if fp is not None:
            try:
                _mod = imp.load_module('_level_1b', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _level_1b = swig_import_helper()
    del swig_import_helper
else:
    import _level_1b
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



_level_1b.SHARED_PTR_DISOWN_swigconstant(_level_1b)
SHARED_PTR_DISOWN = _level_1b.SHARED_PTR_DISOWN

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
class Level1b(full_physics_swig.generic_object.GenericObject):
    """

    This is used to read a Level 1B file.

    C++ includes: level_1b.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Level1b, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Level1b, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _level_1b.delete_Level1b
    __del__ = lambda self: None

    def __str__(self):
        return _level_1b.Level1b___str__(self)

    def _v_number_spectrometer(self):
        """

        virtual int FullPhysics::Level1b::number_spectrometer() const =0
        Number of spectrometers. 
        """
        return _level_1b.Level1b__v_number_spectrometer(self)


    @property
    def number_spectrometer(self):
        return self._v_number_spectrometer()


    def latitude(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1b::latitude(int i) const =0
        Latitude.

        Parameters:
        -----------

        i:  Spectrometer index (between 0 and number_spectrometer() - 1)

        Latitude. 
        """
        return _level_1b.Level1b_latitude(self, i)


    def longitude(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1b::longitude(int i) const =0
        Longitude.

        Parameters:
        -----------

        i:  Spectrometer index (between 0 and number_spectrometer() - 1)

        Longitude 
        """
        return _level_1b.Level1b_longitude(self, i)


    def sounding_zenith(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1b::sounding_zenith(int i) const =0
        Sounding zenith.

        Parameters:
        -----------

        i:  Spectrometer index (between 0 and number_spectrometer() - 1)

        Sounding zenith 
        """
        return _level_1b.Level1b_sounding_zenith(self, i)


    def sounding_azimuth(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1b::sounding_azimuth(int i) const =0
        Sounding azimuth.

        Parameters:
        -----------

        i:  Spectrometer index (between 0 and number_spectrometer() - 1)

        Sounding azimuth 
        """
        return _level_1b.Level1b_sounding_azimuth(self, i)


    def stokes_coefficient(self, i):
        """

        virtual blitz::Array<double, 1> FullPhysics::Level1b::stokes_coefficient(int i) const =0
        Return stokes coefficients.

        Parameters:
        -----------

        i:  Spectrometer index (between 0 and number_spectrometer() - 1)

        Stokes coefficients, with size 4. 
        """
        return _level_1b.Level1b_stokes_coefficient(self, i)


    def solar_zenith(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1b::solar_zenith(int i) const =0
        Solar zenith.

        Parameters:
        -----------

        i:  Spectrometer index (between 0 and number_spectrometer() - 1)

        Solar zenith angle 
        """
        return _level_1b.Level1b_solar_zenith(self, i)


    def solar_azimuth(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1b::solar_azimuth(int i) const =0
        Solar azimuth.

        Parameters:
        -----------

        i:  Spectrometer index (between 0 and number_spectrometer() - 1)

        Solar azimuth angle 
        """
        return _level_1b.Level1b_solar_azimuth(self, i)


    def relative_azimuth(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1b::relative_azimuth(int i) const
        Realtive azimuth.

        Parameters:
        -----------

        i:  Spectrometer index (between 0 and number_spectrometer() - 1)

        Relative azimuth angle between solar and sounding azimuth 
        """
        return _level_1b.Level1b_relative_azimuth(self, i)


    def altitude(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1b::altitude(int i) const =0
        Altitude.

        Parameters:
        -----------

        i:  Spectrometer index (between 0 and number_spectrometer() - 1)

        Altitude 
        """
        return _level_1b.Level1b_altitude(self, i)


    def relative_velocity(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1b::relative_velocity(int Spec_index) const =0
        Relative velocity.

        Relative velocity 
        """
        return _level_1b.Level1b_relative_velocity(self, i)


    def spectral_coefficient(self, Spec_index):
        """

        virtual ArrayWithUnit<double, 1> FullPhysics::Level1b::spectral_coefficient(int Spec_index) const =0
        Returns coefficients for an equation describing the special domain
        used to translate radiance value indexes to their corresponding
        spectral grid.

        (ie wavenumber, wavelength, etc) The meaning of these coefficients
        will be specific to the instrument that measured the data. 
        """
        return _level_1b.Level1b_spectral_coefficient(self, Spec_index)


    def time(self, Spec_index):
        """

        virtual Time FullPhysics::Level1b::time(int Spec_index) const =0
        Time of sounding. 
        """
        return _level_1b.Level1b_time(self, Spec_index)


    def _v_sounding_id(self):
        """

        virtual int64_t FullPhysics::Level1b::sounding_id() const =0
        Sounding ID. By convention this is a 64 bit integer. 
        """
        return _level_1b.Level1b__v_sounding_id(self)


    @property
    def sounding_id(self):
        return self._v_sounding_id()


    def _v_exposure_index(self):
        """

        virtual int FullPhysics::Level1b::exposure_index() const =0
        Exposure index. By convention this is 1 based. 
        """
        return _level_1b.Level1b__v_exposure_index(self)


    @property
    def exposure_index(self):
        return self._v_exposure_index()


    def radiance(self, Spec_index):
        """

        virtual SpectralRange FullPhysics::Level1b::radiance(int Spec_index) const =0
        Radiance, for given spectral band.

        This returns the radiance with associated units. It may or may not
        have a uncertainity with the radiance. 
        """
        return _level_1b.Level1b_radiance(self, Spec_index)

Level1b_swigregister = _level_1b.Level1b_swigregister
Level1b_swigregister(Level1b)

# This file is compatible with both classic and new-style classes.


