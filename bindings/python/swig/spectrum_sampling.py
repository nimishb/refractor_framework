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
            fp, pathname, description = imp.find_module('_spectrum_sampling', [dirname(__file__)])
        except ImportError:
            import _spectrum_sampling
            return _spectrum_sampling
        if fp is not None:
            try:
                _mod = imp.load_module('_spectrum_sampling', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _spectrum_sampling = swig_import_helper()
    del swig_import_helper
else:
    import _spectrum_sampling
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



_spectrum_sampling.SHARED_PTR_DISOWN_swigconstant(_spectrum_sampling)
SHARED_PTR_DISOWN = _spectrum_sampling.SHARED_PTR_DISOWN

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
class SpectrumSampling(full_physics_swig.generic_object.GenericObject):
    """

    This determines the sampling of the spectrum that should be used for
    each of the spectrum indexes.

    Note that there are a few closely related classes, with similar
    sounding names. See spectrum_doxygen for a description of each of
    these.

    C++ includes: spectrum_sampling.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpectrumSampling, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SpectrumSampling, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _spectrum_sampling.delete_SpectrumSampling
    __del__ = lambda self: None

    def __str__(self):
        return _spectrum_sampling.SpectrumSampling___str__(self)

    def _v_number_spectrometer(self):
        """

        int FullPhysics::SpectrumSampling::number_spectrometer() const
        Number of spectrometers we have. 
        """
        return _spectrum_sampling.SpectrumSampling__v_number_spectrometer(self)


    @property
    def number_spectrometer(self):
        return self._v_number_spectrometer()


    def spectral_domain(self, spec_index, Lowres_grid, Ils_half_width):
        """

        virtual SpectralDomain FullPhysics::SpectrumSampling::spectral_domain(int spec_index, const SpectralDomain &Lowres_grid, const
        DoubleWithUnit &Ils_half_width) const =0
        Wavenumbers/Wavelengths to use for the given spectrometer.

        We pass in the low resolution grid that we are going to generate after
        the ILS convolution, along with the ILS half width so we can generate
        the high resolution points needed to supply the ILS. 
        """
        return _spectrum_sampling.SpectrumSampling_spectral_domain(self, spec_index, Lowres_grid, Ils_half_width)


    def spectral_domain_interpolated(self, Spec_index, Lowres_grid, Ils_half_width):
        """

        virtual SpectralDomain FullPhysics::SpectrumSampling::spectral_domain_interpolated(int Spec_index, const SpectralDomain &Lowres_grid, const
        DoubleWithUnit &Ils_half_width) const
        The interpolated spectral domain.

        The default is that this is just the same as spectral_domain, but
        derived classes can supply a different implementation if it is doing
        nonuniform sampling. 
        """
        return _spectrum_sampling.SpectrumSampling_spectral_domain_interpolated(self, Spec_index, Lowres_grid, Ils_half_width)


    def need_interpolation(self, Spec_index):
        """

        virtual bool FullPhysics::SpectrumSampling::need_interpolation(int Spec_index) const
        Indicate if spectral_domain and spectral_domain_interpolated are
        different at all. 
        """
        return _spectrum_sampling.SpectrumSampling_need_interpolation(self, Spec_index)

SpectrumSampling_swigregister = _spectrum_sampling.SpectrumSampling_swigregister
SpectrumSampling_swigregister(SpectrumSampling)

# This file is compatible with both classic and new-style classes.


