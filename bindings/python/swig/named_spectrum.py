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
            fp, pathname, description = imp.find_module('_named_spectrum', [dirname(__file__)])
        except ImportError:
            import _named_spectrum
            return _named_spectrum
        if fp is not None:
            try:
                _mod = imp.load_module('_named_spectrum', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _named_spectrum = swig_import_helper()
    del swig_import_helper
else:
    import _named_spectrum
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
    __swig_destroy__ = _named_spectrum.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _named_spectrum.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _named_spectrum.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _named_spectrum.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _named_spectrum.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _named_spectrum.SwigPyIterator_equal(self, x)

    def copy(self):
        return _named_spectrum.SwigPyIterator_copy(self)

    def next(self):
        return _named_spectrum.SwigPyIterator_next(self)

    def __next__(self):
        return _named_spectrum.SwigPyIterator___next__(self)

    def previous(self):
        return _named_spectrum.SwigPyIterator_previous(self)

    def advance(self, n):
        return _named_spectrum.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _named_spectrum.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _named_spectrum.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _named_spectrum.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _named_spectrum.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _named_spectrum.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _named_spectrum.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _named_spectrum.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_named_spectrum.SHARED_PTR_DISOWN_swigconstant(_named_spectrum)
SHARED_PTR_DISOWN = _named_spectrum.SHARED_PTR_DISOWN

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

import full_physics_swig.spectrum
import full_physics_swig.generic_object
class ObservableNamedSpectrum(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObservableNamedSpectrum, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObservableNamedSpectrum, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _named_spectrum.delete_ObservableNamedSpectrum
    __del__ = lambda self: None

    def add_observer_and_keep_reference(self, Obs):
        return _named_spectrum.ObservableNamedSpectrum_add_observer_and_keep_reference(self, Obs)

    def add_observer(self, Obs):
        return _named_spectrum.ObservableNamedSpectrum_add_observer(self, Obs)

    def remove_observer(self, Obs):
        return _named_spectrum.ObservableNamedSpectrum_remove_observer(self, Obs)
ObservableNamedSpectrum_swigregister = _named_spectrum.ObservableNamedSpectrum_swigregister
ObservableNamedSpectrum_swigregister(ObservableNamedSpectrum)

class ObservablePtrNamedSpectrum(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObservablePtrNamedSpectrum, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObservablePtrNamedSpectrum, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _named_spectrum.delete_ObservablePtrNamedSpectrum
    __del__ = lambda self: None

    def add_observer_and_keep_reference(self, Obs):
        return _named_spectrum.ObservablePtrNamedSpectrum_add_observer_and_keep_reference(self, Obs)

    def add_observer(self, Obs):
        return _named_spectrum.ObservablePtrNamedSpectrum_add_observer(self, Obs)

    def remove_observer(self, Obs):
        return _named_spectrum.ObservablePtrNamedSpectrum_remove_observer(self, Obs)
ObservablePtrNamedSpectrum_swigregister = _named_spectrum.ObservablePtrNamedSpectrum_swigregister
ObservablePtrNamedSpectrum_swigregister(ObservablePtrNamedSpectrum)

class ObserverNamedSpectrum(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObserverNamedSpectrum, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObserverNamedSpectrum, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _named_spectrum.new_ObserverNamedSpectrum()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _named_spectrum.delete_ObserverNamedSpectrum
    __del__ = lambda self: None

    def notify_update(self, Observed_object):
        return _named_spectrum.ObserverNamedSpectrum_notify_update(self, Observed_object)

    def notify_add(self, Observed_object):
        return _named_spectrum.ObserverNamedSpectrum_notify_add(self, Observed_object)

    def notify_remove(self, Observed_object):
        return _named_spectrum.ObserverNamedSpectrum_notify_remove(self, Observed_object)
ObserverNamedSpectrum_swigregister = _named_spectrum.ObserverNamedSpectrum_swigregister
ObserverNamedSpectrum_swigregister(ObserverNamedSpectrum)

class NamedSpectrum(full_physics_swig.spectrum.Spectrum):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.spectrum.Spectrum]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NamedSpectrum, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.spectrum.Spectrum]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, NamedSpectrum, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _named_spectrum.new_NamedSpectrum(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def _v_name(self):
        return _named_spectrum.NamedSpectrum__v_name(self)

    @property
    def name(self):
        return self._v_name()


    def _v_index(self):
        return _named_spectrum.NamedSpectrum__v_index(self)

    @property
    def index(self):
        return self._v_index()


    def __str__(self):
        return _named_spectrum.NamedSpectrum___str__(self)
    __swig_destroy__ = _named_spectrum.delete_NamedSpectrum
    __del__ = lambda self: None
NamedSpectrum_swigregister = _named_spectrum.NamedSpectrum_swigregister
NamedSpectrum_swigregister(NamedSpectrum)

class vector_named_spectrum(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_named_spectrum, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_named_spectrum, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _named_spectrum.vector_named_spectrum_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _named_spectrum.vector_named_spectrum___nonzero__(self)

    def __bool__(self):
        return _named_spectrum.vector_named_spectrum___bool__(self)

    def __len__(self):
        return _named_spectrum.vector_named_spectrum___len__(self)

    def __getslice__(self, i, j):
        return _named_spectrum.vector_named_spectrum___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _named_spectrum.vector_named_spectrum___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _named_spectrum.vector_named_spectrum___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _named_spectrum.vector_named_spectrum___delitem__(self, *args)

    def __getitem__(self, *args):
        return _named_spectrum.vector_named_spectrum___getitem__(self, *args)

    def __setitem__(self, *args):
        return _named_spectrum.vector_named_spectrum___setitem__(self, *args)

    def pop(self):
        return _named_spectrum.vector_named_spectrum_pop(self)

    def append(self, x):
        return _named_spectrum.vector_named_spectrum_append(self, x)

    def empty(self):
        return _named_spectrum.vector_named_spectrum_empty(self)

    def size(self):
        return _named_spectrum.vector_named_spectrum_size(self)

    def swap(self, v):
        return _named_spectrum.vector_named_spectrum_swap(self, v)

    def begin(self):
        return _named_spectrum.vector_named_spectrum_begin(self)

    def end(self):
        return _named_spectrum.vector_named_spectrum_end(self)

    def rbegin(self):
        return _named_spectrum.vector_named_spectrum_rbegin(self)

    def rend(self):
        return _named_spectrum.vector_named_spectrum_rend(self)

    def clear(self):
        return _named_spectrum.vector_named_spectrum_clear(self)

    def get_allocator(self):
        return _named_spectrum.vector_named_spectrum_get_allocator(self)

    def pop_back(self):
        return _named_spectrum.vector_named_spectrum_pop_back(self)

    def erase(self, *args):
        return _named_spectrum.vector_named_spectrum_erase(self, *args)

    def __init__(self, *args):
        this = _named_spectrum.new_vector_named_spectrum(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _named_spectrum.vector_named_spectrum_push_back(self, x)

    def front(self):
        return _named_spectrum.vector_named_spectrum_front(self)

    def back(self):
        return _named_spectrum.vector_named_spectrum_back(self)

    def assign(self, n, x):
        return _named_spectrum.vector_named_spectrum_assign(self, n, x)

    def resize(self, *args):
        return _named_spectrum.vector_named_spectrum_resize(self, *args)

    def insert(self, *args):
        return _named_spectrum.vector_named_spectrum_insert(self, *args)

    def reserve(self, n):
        return _named_spectrum.vector_named_spectrum_reserve(self, n)

    def capacity(self):
        return _named_spectrum.vector_named_spectrum_capacity(self)
    __swig_destroy__ = _named_spectrum.delete_vector_named_spectrum
    __del__ = lambda self: None
vector_named_spectrum_swigregister = _named_spectrum.vector_named_spectrum_swigregister
vector_named_spectrum_swigregister(vector_named_spectrum)

class ObservableStokesUpdate(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObservableStokesUpdate, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObservableStokesUpdate, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _named_spectrum.delete_ObservableStokesUpdate
    __del__ = lambda self: None

    def add_observer_and_keep_reference(self, Obs):
        return _named_spectrum.ObservableStokesUpdate_add_observer_and_keep_reference(self, Obs)

    def add_observer(self, Obs):
        return _named_spectrum.ObservableStokesUpdate_add_observer(self, Obs)

    def remove_observer(self, Obs):
        return _named_spectrum.ObservableStokesUpdate_remove_observer(self, Obs)
ObservableStokesUpdate_swigregister = _named_spectrum.ObservableStokesUpdate_swigregister
ObservableStokesUpdate_swigregister(ObservableStokesUpdate)

class ObserverStokesUpdate(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObserverStokesUpdate, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObserverStokesUpdate, name)
    __repr__ = _swig_repr

    def __init__(self):
        if self.__class__ == ObserverStokesUpdate:
            _self = None
        else:
            _self = self
        this = _named_spectrum.new_ObserverStokesUpdate(_self, )
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _named_spectrum.delete_ObserverStokesUpdate
    __del__ = lambda self: None

    def notify_update(self, Observed_object):
        return _named_spectrum.ObserverStokesUpdate_notify_update(self, Observed_object)

    def notify_add(self, Observed_object):
        return _named_spectrum.ObserverStokesUpdate_notify_add(self, Observed_object)

    def notify_remove(self, Observed_object):
        return _named_spectrum.ObserverStokesUpdate_notify_remove(self, Observed_object)
    def __disown__(self):
        self.this.disown()
        _named_spectrum.disown_ObserverStokesUpdate(self)
        return weakref_proxy(self)
ObserverStokesUpdate_swigregister = _named_spectrum.ObserverStokesUpdate_swigregister
ObserverStokesUpdate_swigregister(ObserverStokesUpdate)

# This file is compatible with both classic and new-style classes.


