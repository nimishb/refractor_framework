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
            fp, pathname, description = imp.find_module('_solar_absorption_and_continuum', [dirname(__file__)])
        except ImportError:
            import _solar_absorption_and_continuum
            return _solar_absorption_and_continuum
        if fp is not None:
            try:
                _mod = imp.load_module('_solar_absorption_and_continuum', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _solar_absorption_and_continuum = swig_import_helper()
    del swig_import_helper
else:
    import _solar_absorption_and_continuum
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



_solar_absorption_and_continuum.SHARED_PTR_DISOWN_swigconstant(_solar_absorption_and_continuum)
SHARED_PTR_DISOWN = _solar_absorption_and_continuum.SHARED_PTR_DISOWN

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

import full_physics_swig.solar_model
import full_physics_swig.spectrum_effect
import full_physics_swig.generic_object
import full_physics_swig.state_vector
class SolarAbsorptionAndContinuum(full_physics_swig.solar_model.SolarModel):
    """

    This applies a solar model to radiances to model the incoming solar
    irradiance.

    This implementation is a common division of the solar model into

    A Doppler correction

    A solar absorption spectrum

    A solar continuum spectrum

    This uses 3 objects to do the work, a SolarDopplerShift, a
    SolarAbsorptionSpectrum, and a SolarContinuumSpectrum object. This
    class stitches these objects together to create the full spectrum.

    C++ includes: solar_absorption_and_continuum.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.solar_model.SolarModel]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SolarAbsorptionAndContinuum, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.solar_model.SolarModel]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SolarAbsorptionAndContinuum, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _solar_absorption_and_continuum.delete_SolarAbsorptionAndContinuum
    __del__ = lambda self: None

    def __init__(self, doppler_shiftv, absorption_spectrumv, continuum_spectrumv):
        """

        FullPhysics::SolarAbsorptionAndContinuum::SolarAbsorptionAndContinuum(const boost::shared_ptr< SolarDopplerShift > &doppler_shiftv, const
        boost::shared_ptr< SolarAbsorptionSpectrum > &absorption_spectrumv,
        const boost::shared_ptr< SolarContinuumSpectrum >
        &continuum_spectrumv)
        Create a SolarModel that uses the given doppler shift, absorption
        spectrum, and continuum spectrum. 
        """
        this = _solar_absorption_and_continuum.new_SolarAbsorptionAndContinuum(doppler_shiftv, absorption_spectrumv, continuum_spectrumv)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def clone(self):
        """

        virtual boost::shared_ptr<SpectrumEffect> FullPhysics::SolarAbsorptionAndContinuum::clone() const
        Clone a SolarAbsorptionAndContinuum object. 
        """
        return _solar_absorption_and_continuum.SolarAbsorptionAndContinuum_clone(self)


    def _v_doppler_shift(self):
        """

        const boost::shared_ptr<SolarDopplerShift>& FullPhysics::SolarAbsorptionAndContinuum::doppler_shift_ptr() const
        The SolarDopplerShift object used by this class, as a ptr. 
        """
        return _solar_absorption_and_continuum.SolarAbsorptionAndContinuum__v_doppler_shift(self)


    @property
    def doppler_shift(self):
        return self._v_doppler_shift()


    def _v_absorption_spectrum(self):
        """

        const boost::shared_ptr<SolarAbsorptionSpectrum>& FullPhysics::SolarAbsorptionAndContinuum::absorption_spectrum_ptr() const
        The SolarAbsorptionSpectrum object used by this class, as a ptr. 
        """
        return _solar_absorption_and_continuum.SolarAbsorptionAndContinuum__v_absorption_spectrum(self)


    @property
    def absorption_spectrum(self):
        return self._v_absorption_spectrum()


    def _v_continuum_spectrum(self):
        """

        const boost::shared_ptr<SolarContinuumSpectrum>& FullPhysics::SolarAbsorptionAndContinuum::continuum_spectrum_ptr() const
        The SolarContinuumSpectrum object used by this class, as a ptr. 
        """
        return _solar_absorption_and_continuum.SolarAbsorptionAndContinuum__v_continuum_spectrum(self)


    @property
    def continuum_spectrum(self):
        return self._v_continuum_spectrum()


    def solar_spectrum(self, Spec_domain):
        """

        virtual Spectrum FullPhysics::SolarAbsorptionAndContinuum::solar_spectrum(const SpectralDomain &Spec_domain) const

        """
        return _solar_absorption_and_continuum.SolarAbsorptionAndContinuum_solar_spectrum(self, Spec_domain)

SolarAbsorptionAndContinuum_swigregister = _solar_absorption_and_continuum.SolarAbsorptionAndContinuum_swigregister
SolarAbsorptionAndContinuum_swigregister(SolarAbsorptionAndContinuum)

# This file is compatible with both classic and new-style classes.


