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
            fp, pathname, description = imp.find_module('_ils', [dirname(__file__)])
        except ImportError:
            import _ils
            return _ils
        if fp is not None:
            try:
                _mod = imp.load_module('_ils', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ils = swig_import_helper()
    del swig_import_helper
else:
    import _ils
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
    __swig_destroy__ = _ils.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _ils.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _ils.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _ils.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _ils.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _ils.SwigPyIterator_equal(self, x)

    def copy(self):
        return _ils.SwigPyIterator_copy(self)

    def next(self):
        return _ils.SwigPyIterator_next(self)

    def __next__(self):
        return _ils.SwigPyIterator___next__(self)

    def previous(self):
        return _ils.SwigPyIterator_previous(self)

    def advance(self, n):
        return _ils.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _ils.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _ils.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _ils.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _ils.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _ils.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _ils.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _ils.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_ils.SHARED_PTR_DISOWN_swigconstant(_ils)
SHARED_PTR_DISOWN = _ils.SHARED_PTR_DISOWN

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

import full_physics_swig.state_vector
import full_physics_swig.generic_object
class Ils(full_physics_swig.state_vector.StateVectorObserver):
    """

    This class models an Instrument Line Shape (ILS).

    We convolve with high resolution data to produce a model of what we
    expect to observe in the Level 1b data.

    C++ includes: ils.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.state_vector.StateVectorObserver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Ils, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.state_vector.StateVectorObserver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Ils, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ils.delete_Ils
    __del__ = lambda self: None

    def __str__(self):
        return _ils.Ils___str__(self)

    def apply_ils(self, *args):
        """

        virtual ArrayAd<double, 1> FullPhysics::Ils::apply_ils(const blitz::Array< double, 1 > &High_resolution_wave_number, const
        ArrayAd< double, 1 > &High_resolution_radiance, const std::vector< int
        > &Pixel_list) const =0
        Apply the ILS.

        This includes propagating the Jacobian from the high resolution data,
        and adding in any dependence of the ILS on the state vector elements
        (e.g., dispersion state vector elements).

        Parameters:
        -----------

        High_resolution_wave_number:  The wave numbers going with the high
        resolution radiance data. This is in cm^-1, and should be ordered from
        smallest to largest wavenumber.

        High_resolution_radiance:  The high resolution radiance data and
        jacobian . This is in w/m^2 / sr / cm^-1

        Pixel_list:  List of instrument pixels to include in the results. The
        order of the pixels is the same order that we return our results in.

        Radiance with ILS applied, and Jacobian This is in w/m^2 / sr / cm^-1.

        """
        return _ils.Ils_apply_ils(self, *args)


    def clone(self):
        """

        virtual boost::shared_ptr<Ils> FullPhysics::Ils::clone() const =0
        Clone an Ils object.

        Note that the cloned version will not be attached to and StateVector
        or Observer<Ils>, although you can of course attach them after
        receiving the cloned object.

        Because this isn't attached to the StateVector, one use of the clone
        operator is to create a "frozen" Ils object. 
        """
        return _ils.Ils_clone(self)


    def _v_band_name(self):
        """

        virtual std::string FullPhysics::Ils::band_name() const =0
        Descriptive name of the band. 
        """
        return _ils.Ils__v_band_name(self)


    @property
    def band_name(self):
        return self._v_band_name()


    def _v_hdf_band_name(self):
        """

        virtual std::string FullPhysics::Ils::hdf_band_name() const
        In general, the name used in HDF files for a particular band is
        similar but not identical to the more human readable band_name.

        For example, with GOSAT we use the HDF field name "weak_co2", but
        the band name is "WC-Band". This gives the HDF name to use.

        The default implementation just returns the same string as the band
        name. 
        """
        return _ils.Ils__v_hdf_band_name(self)


    @property
    def hdf_band_name(self):
        return self._v_hdf_band_name()


    def _v_pixel_grid(self):
        """

        virtual SpectralDomain FullPhysics::Ils::pixel_grid() const =0
        This is the pixel grid for each pixel. 
        """
        return _ils.Ils__v_pixel_grid(self)


    @property
    def pixel_grid(self):
        return self._v_pixel_grid()


    def _v_ils_half_width(self, *args):
        """

        virtual void FullPhysics::Ils::ils_half_width(const DoubleWithUnit &half_width)=0
        Set the half width of the ILS. 
        """
        return _ils.Ils__v_ils_half_width(self, *args)


    @property
    def ils_half_width(self):
        return self._v_ils_half_width()

    @ils_half_width.setter
    def ils_half_width(self, value):
      self._v_ils_half_width(value)

Ils_swigregister = _ils.Ils_swigregister
Ils_swigregister(Ils)

class vector_ils(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_ils, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_ils, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _ils.vector_ils_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _ils.vector_ils___nonzero__(self)

    def __bool__(self):
        return _ils.vector_ils___bool__(self)

    def __len__(self):
        return _ils.vector_ils___len__(self)

    def __getslice__(self, i, j):
        return _ils.vector_ils___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _ils.vector_ils___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _ils.vector_ils___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _ils.vector_ils___delitem__(self, *args)

    def __getitem__(self, *args):
        return _ils.vector_ils___getitem__(self, *args)

    def __setitem__(self, *args):
        return _ils.vector_ils___setitem__(self, *args)

    def pop(self):
        return _ils.vector_ils_pop(self)

    def append(self, x):
        return _ils.vector_ils_append(self, x)

    def empty(self):
        return _ils.vector_ils_empty(self)

    def size(self):
        return _ils.vector_ils_size(self)

    def swap(self, v):
        return _ils.vector_ils_swap(self, v)

    def begin(self):
        return _ils.vector_ils_begin(self)

    def end(self):
        return _ils.vector_ils_end(self)

    def rbegin(self):
        return _ils.vector_ils_rbegin(self)

    def rend(self):
        return _ils.vector_ils_rend(self)

    def clear(self):
        return _ils.vector_ils_clear(self)

    def get_allocator(self):
        return _ils.vector_ils_get_allocator(self)

    def pop_back(self):
        return _ils.vector_ils_pop_back(self)

    def erase(self, *args):
        return _ils.vector_ils_erase(self, *args)

    def __init__(self, *args):
        this = _ils.new_vector_ils(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _ils.vector_ils_push_back(self, x)

    def front(self):
        return _ils.vector_ils_front(self)

    def back(self):
        return _ils.vector_ils_back(self)

    def assign(self, n, x):
        return _ils.vector_ils_assign(self, n, x)

    def resize(self, *args):
        return _ils.vector_ils_resize(self, *args)

    def insert(self, *args):
        return _ils.vector_ils_insert(self, *args)

    def reserve(self, n):
        return _ils.vector_ils_reserve(self, n)

    def capacity(self):
        return _ils.vector_ils_capacity(self)
    __swig_destroy__ = _ils.delete_vector_ils
    __del__ = lambda self: None
vector_ils_swigregister = _ils.vector_ils_swigregister
vector_ils_swigregister(vector_ils)

# This file is compatible with both classic and new-style classes.


