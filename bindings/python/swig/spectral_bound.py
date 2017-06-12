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
            fp, pathname, description = imp.find_module('_spectral_bound', [dirname(__file__)])
        except ImportError:
            import _spectral_bound
            return _spectral_bound
        if fp is not None:
            try:
                _mod = imp.load_module('_spectral_bound', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _spectral_bound = swig_import_helper()
    del swig_import_helper
else:
    import _spectral_bound
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



_spectral_bound.SHARED_PTR_DISOWN_swigconstant(_spectral_bound)
SHARED_PTR_DISOWN = _spectral_bound.SHARED_PTR_DISOWN

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
class SpectralBound(full_physics_swig.generic_object.GenericObject):
    """

    This gives the upper and lower bounds of the SpectralWindow.

    Lower_bound and upper_bound are just meant to give a rough idea of the
    band covered by a spectral window, there is no guarantee that
    lower_bound() + delta or upper_band() - delta will pass the
    grid_indexes test of the SpectralWindow. But the reverse is
    guaranteed, any value < lower_bound or >= upper_bound will certainly
    not pass grid_indexes test.

    Note that there are a few closely related classes, with similar
    sounding names. See spectrum_doxygen for a description of each of
    these.

    C++ includes: spectral_bound.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpectralBound, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SpectralBound, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """

        FullPhysics::SpectralBound::SpectralBound(const ArrayWithUnit< double, 2 > &Bound)

        """
        this = _spectral_bound.new_SpectralBound(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __str__(self):
        return _spectral_bound.SpectralBound___str__(self)

    def _v_number_spectrometer(self):
        """

        int FullPhysics::SpectralBound::number_spectrometer() const
        Number of spectrometers. 
        """
        return _spectral_bound.SpectralBound__v_number_spectrometer(self)


    @property
    def number_spectrometer(self):
        return self._v_number_spectrometer()


    def center(self, Spec_index, U):
        """

        DoubleWithUnit FullPhysics::SpectralBound::center(int Spec_index, const Unit &U) const
        Center between lower_bound and upper_bound.

        Turns out we need this often enough to be worth wrapping in a
        function. 
        """
        return _spectral_bound.SpectralBound_center(self, Spec_index, U)


    def lower_bound(self, *args):
        """

        DoubleWithUnit FullPhysics::SpectralBound::lower_bound(int Spec_index, const Unit &U) const
        Lower bound but with a unit conversion first in case the conversion
        reverses ordering. 
        """
        return _spectral_bound.SpectralBound_lower_bound(self, *args)


    def upper_bound(self, *args):
        """

        DoubleWithUnit FullPhysics::SpectralBound::upper_bound(int Spec_index, const Unit &U) const
        Upper bound but with a unit conversion first in case the conversion
        reverses ordering. 
        """
        return _spectral_bound.SpectralBound_upper_bound(self, *args)


    def spectral_index(self, W):
        """

        int FullPhysics::SpectralBound::spectral_index(const DoubleWithUnit &W) const

        """
        return _spectral_bound.SpectralBound_spectral_index(self, W)

    __swig_destroy__ = _spectral_bound.delete_SpectralBound
    __del__ = lambda self: None
SpectralBound_swigregister = _spectral_bound.SpectralBound_swigregister
SpectralBound_swigregister(SpectralBound)

# This file is compatible with both classic and new-style classes.


