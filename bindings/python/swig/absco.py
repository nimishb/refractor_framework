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
            fp, pathname, description = imp.find_module('_absco', [dirname(__file__)])
        except ImportError:
            import _absco
            return _absco
        if fp is not None:
            try:
                _mod = imp.load_module('_absco', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _absco = swig_import_helper()
    del swig_import_helper
else:
    import _absco
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
    __swig_destroy__ = _absco.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _absco.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _absco.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _absco.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _absco.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _absco.SwigPyIterator_equal(self, x)

    def copy(self):
        return _absco.SwigPyIterator_copy(self)

    def next(self):
        return _absco.SwigPyIterator_next(self)

    def __next__(self):
        return _absco.SwigPyIterator___next__(self)

    def previous(self):
        return _absco.SwigPyIterator_previous(self)

    def advance(self, n):
        return _absco.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _absco.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _absco.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _absco.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _absco.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _absco.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _absco.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _absco.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_absco.SHARED_PTR_DISOWN_swigconstant(_absco)
SHARED_PTR_DISOWN = _absco.SHARED_PTR_DISOWN

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

import full_physics_swig.gas_absorption
import full_physics_swig.generic_object
class Absco(full_physics_swig.gas_absorption.GasAbsorption):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.gas_absorption.GasAbsorption]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Absco, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.gas_absorption.GasAbsorption]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Absco, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def _v_number_broadener_vmr(self):
        return _absco.Absco__v_number_broadener_vmr(self)

    @property
    def number_broadener_vmr(self):
        return self._v_number_broadener_vmr()


    def _v_number_layer(self):
        return _absco.Absco__v_number_layer(self)

    @property
    def number_layer(self):
        return self._v_number_layer()


    def _v_number_temperature(self):
        return _absco.Absco__v_number_temperature(self)

    @property
    def number_temperature(self):
        return self._v_number_temperature()


    def _v_broadener_vmr_grid(self):
        return _absco.Absco__v_broadener_vmr_grid(self)

    @property
    def broadener_vmr_grid(self):
        return self._v_broadener_vmr_grid()


    def _v_pressure_grid(self):
        return _absco.Absco__v_pressure_grid(self)

    @property
    def pressure_grid(self):
        return self._v_pressure_grid()


    def _v_temperature_grid(self):
        return _absco.Absco__v_temperature_grid(self)

    @property
    def temperature_grid(self):
        return self._v_temperature_grid()


    def _v_broadener_name(self):
        return _absco.Absco__v_broadener_name(self)

    @property
    def broadener_name(self):
        return self._v_broadener_name()


    def table_scale(self, wn):
        return _absco.Absco_table_scale(self, wn)

    def absorption_cross_section(self, *args):
        return _absco.Absco_absorption_cross_section(self, *args)

    def read_double(self, wn):
        return _absco.Absco_read_double(self, wn)

    def read_float(self, wn):
        return _absco.Absco_read_float(self, wn)
    __swig_destroy__ = _absco.delete_Absco
    __del__ = lambda self: None
Absco_swigregister = _absco.Absco_swigregister
Absco_swigregister(Absco)

class vector_absco(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_absco, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_absco, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _absco.vector_absco_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _absco.vector_absco___nonzero__(self)

    def __bool__(self):
        return _absco.vector_absco___bool__(self)

    def __len__(self):
        return _absco.vector_absco___len__(self)

    def __getslice__(self, i, j):
        return _absco.vector_absco___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _absco.vector_absco___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _absco.vector_absco___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _absco.vector_absco___delitem__(self, *args)

    def __getitem__(self, *args):
        return _absco.vector_absco___getitem__(self, *args)

    def __setitem__(self, *args):
        return _absco.vector_absco___setitem__(self, *args)

    def pop(self):
        return _absco.vector_absco_pop(self)

    def append(self, x):
        return _absco.vector_absco_append(self, x)

    def empty(self):
        return _absco.vector_absco_empty(self)

    def size(self):
        return _absco.vector_absco_size(self)

    def swap(self, v):
        return _absco.vector_absco_swap(self, v)

    def begin(self):
        return _absco.vector_absco_begin(self)

    def end(self):
        return _absco.vector_absco_end(self)

    def rbegin(self):
        return _absco.vector_absco_rbegin(self)

    def rend(self):
        return _absco.vector_absco_rend(self)

    def clear(self):
        return _absco.vector_absco_clear(self)

    def get_allocator(self):
        return _absco.vector_absco_get_allocator(self)

    def pop_back(self):
        return _absco.vector_absco_pop_back(self)

    def erase(self, *args):
        return _absco.vector_absco_erase(self, *args)

    def __init__(self, *args):
        this = _absco.new_vector_absco(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _absco.vector_absco_push_back(self, x)

    def front(self):
        return _absco.vector_absco_front(self)

    def back(self):
        return _absco.vector_absco_back(self)

    def assign(self, n, x):
        return _absco.vector_absco_assign(self, n, x)

    def resize(self, *args):
        return _absco.vector_absco_resize(self, *args)

    def insert(self, *args):
        return _absco.vector_absco_insert(self, *args)

    def reserve(self, n):
        return _absco.vector_absco_reserve(self, n)

    def capacity(self):
        return _absco.vector_absco_capacity(self)
    __swig_destroy__ = _absco.delete_vector_absco
    __del__ = lambda self: None
vector_absco_swigregister = _absco.vector_absco_swigregister
vector_absco_swigregister(vector_absco)

# This file is compatible with both classic and new-style classes.


