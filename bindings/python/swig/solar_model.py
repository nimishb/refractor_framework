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
            fp, pathname, description = imp.find_module('_solar_model', [dirname(__file__)])
        except ImportError:
            import _solar_model
            return _solar_model
        if fp is not None:
            try:
                _mod = imp.load_module('_solar_model', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _solar_model = swig_import_helper()
    del swig_import_helper
else:
    import _solar_model
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


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _solar_model.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _solar_model.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _solar_model.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _solar_model.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _solar_model.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _solar_model.SwigPyIterator_equal(self, x)

    def copy(self):
        return _solar_model.SwigPyIterator_copy(self)

    def next(self):
        return _solar_model.SwigPyIterator_next(self)

    def __next__(self):
        return _solar_model.SwigPyIterator___next__(self)

    def previous(self):
        return _solar_model.SwigPyIterator_previous(self)

    def advance(self, n):
        return _solar_model.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _solar_model.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _solar_model.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _solar_model.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _solar_model.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _solar_model.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _solar_model.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _solar_model.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_solar_model.SHARED_PTR_DISOWN_swigconstant(_solar_model)
SHARED_PTR_DISOWN = _solar_model.SHARED_PTR_DISOWN

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

import full_physics_swig.spectrum_effect
import full_physics_swig.generic_object
import full_physics_swig.state_vector
class SolarModel(full_physics_swig.spectrum_effect.SpectrumEffect):
    """

    This applies a solar model to reflectance to model the incoming solar
    irradiance.

    C++ includes: solar_model.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.spectrum_effect.SpectrumEffect]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SolarModel, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.spectrum_effect.SpectrumEffect]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SolarModel, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _solar_model.delete_SolarModel
    __del__ = lambda self: None

    def apply_solar_model(self, Spec):
        """

        virtual Spectrum FullPhysics::SolarModel::apply_solar_model(const Spectrum &Spec) const

        """
        return _solar_model.SolarModel_apply_solar_model(self, Spec)


    def solar_spectrum(self, Spec_domain):
        """

        virtual Spectrum FullPhysics::SolarModel::solar_spectrum(const SpectralDomain &Spec_domain) const =0
        Calculate solar spectrum.

        Parameters:
        -----------

        Spec_domain:  Wavenumber/Wavelength reflectance is given

        Solar spectrum. This should have units commensurate with something
        like W / m^2 / cm^-1.  Note that the wavenumber/frequency are in the
        earth rest frame. The solar model may need to work in the solar rest
        frame, bu the conversion to this is internal. The input and output
        from this function should be in the earth rest frame. 
        """
        return _solar_model.SolarModel_solar_spectrum(self, Spec_domain)


    def apply_effect(self, Spec, Forward_model_grid):
        """

        virtual void FullPhysics::SolarModel::apply_effect(Spectrum &Spec, const ForwardModelSpectralGrid &Forward_model_grid)
        const

        """
        return _solar_model.SolarModel_apply_effect(self, Spec, Forward_model_grid)

SolarModel_swigregister = _solar_model.SolarModel_swigregister
SolarModel_swigregister(SolarModel)

class vector_solar_model(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_solar_model, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_solar_model, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _solar_model.vector_solar_model_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _solar_model.vector_solar_model___nonzero__(self)

    def __bool__(self):
        return _solar_model.vector_solar_model___bool__(self)

    def __len__(self):
        return _solar_model.vector_solar_model___len__(self)

    def __getslice__(self, i, j):
        return _solar_model.vector_solar_model___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _solar_model.vector_solar_model___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _solar_model.vector_solar_model___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _solar_model.vector_solar_model___delitem__(self, *args)

    def __getitem__(self, *args):
        return _solar_model.vector_solar_model___getitem__(self, *args)

    def __setitem__(self, *args):
        return _solar_model.vector_solar_model___setitem__(self, *args)

    def pop(self):
        return _solar_model.vector_solar_model_pop(self)

    def append(self, x):
        return _solar_model.vector_solar_model_append(self, x)

    def empty(self):
        return _solar_model.vector_solar_model_empty(self)

    def size(self):
        return _solar_model.vector_solar_model_size(self)

    def swap(self, v):
        return _solar_model.vector_solar_model_swap(self, v)

    def begin(self):
        return _solar_model.vector_solar_model_begin(self)

    def end(self):
        return _solar_model.vector_solar_model_end(self)

    def rbegin(self):
        return _solar_model.vector_solar_model_rbegin(self)

    def rend(self):
        return _solar_model.vector_solar_model_rend(self)

    def clear(self):
        return _solar_model.vector_solar_model_clear(self)

    def get_allocator(self):
        return _solar_model.vector_solar_model_get_allocator(self)

    def pop_back(self):
        return _solar_model.vector_solar_model_pop_back(self)

    def erase(self, *args):
        return _solar_model.vector_solar_model_erase(self, *args)

    def __init__(self, *args):
        this = _solar_model.new_vector_solar_model(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _solar_model.vector_solar_model_push_back(self, x)

    def front(self):
        return _solar_model.vector_solar_model_front(self)

    def back(self):
        return _solar_model.vector_solar_model_back(self)

    def assign(self, n, x):
        return _solar_model.vector_solar_model_assign(self, n, x)

    def resize(self, *args):
        return _solar_model.vector_solar_model_resize(self, *args)

    def insert(self, *args):
        return _solar_model.vector_solar_model_insert(self, *args)

    def reserve(self, n):
        return _solar_model.vector_solar_model_reserve(self, n)

    def capacity(self):
        return _solar_model.vector_solar_model_capacity(self)
    __swig_destroy__ = _solar_model.delete_vector_solar_model
    __del__ = lambda self: None
vector_solar_model_swigregister = _solar_model.vector_solar_model_swigregister
vector_solar_model_swigregister(vector_solar_model)

# This file is compatible with both classic and new-style classes.


