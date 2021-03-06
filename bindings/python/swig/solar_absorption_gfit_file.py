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
            fp, pathname, description = imp.find_module('_solar_absorption_gfit_file', [dirname(__file__)])
        except ImportError:
            import _solar_absorption_gfit_file
            return _solar_absorption_gfit_file
        if fp is not None:
            try:
                _mod = imp.load_module('_solar_absorption_gfit_file', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _solar_absorption_gfit_file = swig_import_helper()
    del swig_import_helper
else:
    import _solar_absorption_gfit_file
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



_solar_absorption_gfit_file.SHARED_PTR_DISOWN_swigconstant(_solar_absorption_gfit_file)
SHARED_PTR_DISOWN = _solar_absorption_gfit_file.SHARED_PTR_DISOWN

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

import full_physics_swig.solar_absorption_spectrum
import full_physics_swig.generic_object
class SolarAbsorptionGfitFile(full_physics_swig.solar_absorption_spectrum.SolarAbsorptionSpectrum):
    """

    This class calculates the solar absorption spectrum.

    This particular implementation reads the GFIT format absorption line
    list file. This is a fixed record file format that gives the
    absorption line list data.

    From the Fortran code:

    Calculates the solar optical thickness spectrum (SOT) at any
    wavelengths.

    Taking the exponential of SOT produces the solar spectrum as it would
    be observed at infinite spectral resolution.

    All solar lines are assumed to have a shape of the form

    \\[SOT = s \\exp\\left(-\\frac{x^2}{\\sqrt{d^4+x^2
    y^2}}\\right)\\] wheres is the line-center optical thickness
    (dimensionless) x is the frequency from line center (cm-1) y is the
    1/e folding width (cm-1) d is the Doppler width (cm-1)

    In the doppler limit, i.e. $ d^2 \\gg x.y $ \\[SOT = s
    \\exp\\left(-{\\frac{x}{d}}^2\\right)\\]

    In the far line wing limit, i.e. $x y \\gg d^2$, \\[SOT = s
    \\exp\\left(- \\left|\\frac{x}{y}\\right|\\right)\\]

    So near the line center, the lineshape is Doppler, but in the line
    wings it decays exponentially (if y>0).

    This choice of lineshape has no physical basis. It just seems to give
    a reasonable representation is nearly all cases. The only cases in
    which this lineshape does not give an adequate representation of the
    absorption are the extremely broad lines of light atmos such as H
    (atomic hydrogen) or Mg. However, by representing the H absorptions as
    superpositions of two lines, one narrow and the other broad, adequate
    results were obtained.

    Molecular absorptions (e.g. CO, OH, NH, CN) tend to have narrow,
    Doppler lineshapes because they are confined to a relatively narrow
    layer in the cooler, upper, part of the solar atmosphere. In the
    hotter depths they are dissociated.

    Atomic transitions, on the other hand, are formed over a much wider
    range of solar altitudes, and hence temperatures. This gives rise to
    line shapes whose wings decay in an approximately exponential manner
    with the distance from line center. The line shape of equation (1)
    does a reasonable job in both cases.

    This subroutine also makes allowances for the effect of the finite FOV
    of the observing instrument, which gives rise to:

    broadening of the solar lines due to the linear variation of the
    Doppler shift from solar rotation across the solar disk.

    deepening of the solar lines due to limb darkening. It assumes that an
    instrument which observes the entire solar disk will observe lines
    which are, on average, twice the strength of an instrument just
    observing the center of the disk.

    C++ includes: solar_absorption_gfit_file.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.solar_absorption_spectrum.SolarAbsorptionSpectrum]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SolarAbsorptionGfitFile, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.solar_absorption_spectrum.SolarAbsorptionSpectrum]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SolarAbsorptionGfitFile, name)
    __repr__ = _swig_repr

    def __init__(self, Line_list_file, Fraction_solar_diameter):
        """

        FullPhysics::SolarAbsorptionGfitFile::SolarAbsorptionGfitFile(const std::string &Line_list_file, double
        Fraction_solar_diameter=1.0)

        """
        this = _solar_absorption_gfit_file.new_SolarAbsorptionGfitFile(Line_list_file, Fraction_solar_diameter)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def solar_absorption_spectrum(self, spec_domain):
        """

        virtual Spectrum FullPhysics::SolarAbsorptionGfitFile::solar_absorption_spectrum(const SpectralDomain &spec_domain) const

        """
        return _solar_absorption_gfit_file.SolarAbsorptionGfitFile_solar_absorption_spectrum(self, spec_domain)


    def _v_fraction_solar_diameter(self):
        """

        double FullPhysics::SolarAbsorptionGfitFile::fraction_solar_diameter() const
        Fraction of solar diameter that we view. 
        """
        return _solar_absorption_gfit_file.SolarAbsorptionGfitFile__v_fraction_solar_diameter(self)


    @property
    def fraction_solar_diameter(self):
        return self._v_fraction_solar_diameter()

    __swig_destroy__ = _solar_absorption_gfit_file.delete_SolarAbsorptionGfitFile
    __del__ = lambda self: None
SolarAbsorptionGfitFile_swigregister = _solar_absorption_gfit_file.SolarAbsorptionGfitFile_swigregister
SolarAbsorptionGfitFile_swigregister(SolarAbsorptionGfitFile)

# This file is compatible with both classic and new-style classes.


