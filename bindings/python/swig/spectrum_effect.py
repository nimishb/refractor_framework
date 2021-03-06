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
            fp, pathname, description = imp.find_module('_spectrum_effect', [dirname(__file__)])
        except ImportError:
            import _spectrum_effect
            return _spectrum_effect
        if fp is not None:
            try:
                _mod = imp.load_module('_spectrum_effect', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _spectrum_effect = swig_import_helper()
    del swig_import_helper
else:
    import _spectrum_effect
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
    __swig_destroy__ = _spectrum_effect.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _spectrum_effect.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _spectrum_effect.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _spectrum_effect.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _spectrum_effect.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _spectrum_effect.SwigPyIterator_equal(self, x)

    def copy(self):
        return _spectrum_effect.SwigPyIterator_copy(self)

    def next(self):
        return _spectrum_effect.SwigPyIterator_next(self)

    def __next__(self):
        return _spectrum_effect.SwigPyIterator___next__(self)

    def previous(self):
        return _spectrum_effect.SwigPyIterator_previous(self)

    def advance(self, n):
        return _spectrum_effect.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _spectrum_effect.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _spectrum_effect.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _spectrum_effect.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _spectrum_effect.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _spectrum_effect.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _spectrum_effect.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _spectrum_effect.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_spectrum_effect.SHARED_PTR_DISOWN_swigconstant(_spectrum_effect)
SHARED_PTR_DISOWN = _spectrum_effect.SHARED_PTR_DISOWN

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
import full_physics_swig.state_vector
class ObservableSpectrumEffect(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObservableSpectrumEffect, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObservableSpectrumEffect, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _spectrum_effect.delete_ObservableSpectrumEffect
    __del__ = lambda self: None

    def add_observer_and_keep_reference(self, Obs):
        return _spectrum_effect.ObservableSpectrumEffect_add_observer_and_keep_reference(self, Obs)

    def add_observer(self, Obs):
        return _spectrum_effect.ObservableSpectrumEffect_add_observer(self, Obs)

    def remove_observer(self, Obs):
        return _spectrum_effect.ObservableSpectrumEffect_remove_observer(self, Obs)
ObservableSpectrumEffect_swigregister = _spectrum_effect.ObservableSpectrumEffect_swigregister
ObservableSpectrumEffect_swigregister(ObservableSpectrumEffect)

class ObserverSpectrumEffect(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObserverSpectrumEffect, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObserverSpectrumEffect, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _spectrum_effect.new_ObserverSpectrumEffect()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _spectrum_effect.delete_ObserverSpectrumEffect
    __del__ = lambda self: None

    def notify_update(self, Observed_object):
        return _spectrum_effect.ObserverSpectrumEffect_notify_update(self, Observed_object)

    def notify_add(self, Observed_object):
        return _spectrum_effect.ObserverSpectrumEffect_notify_add(self, Observed_object)

    def notify_remove(self, Observed_object):
        return _spectrum_effect.ObserverSpectrumEffect_notify_remove(self, Observed_object)
ObserverSpectrumEffect_swigregister = _spectrum_effect.ObserverSpectrumEffect_swigregister
ObserverSpectrumEffect_swigregister(ObserverSpectrumEffect)

class SpectrumEffect(full_physics_swig.state_vector.StateVectorObserver, ObservableSpectrumEffect):
    """

    This class models models any effects that need to be applied to high
    resolution spectra after the radiative transfer model has finished its
    work.

    C++ includes: spectrum_effect.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.state_vector.StateVectorObserver, ObservableSpectrumEffect]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpectrumEffect, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.state_vector.StateVectorObserver, ObservableSpectrumEffect]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SpectrumEffect, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _spectrum_effect.delete_SpectrumEffect
    __del__ = lambda self: None

    def __str__(self):
        return _spectrum_effect.SpectrumEffect___str__(self)

    def apply_effect(self, Spec, Forward_model_grid):
        """

        virtual void FullPhysics::SpectrumEffect::apply_effect(Spectrum &Spec, const ForwardModelSpectralGrid &Forward_model_grid)
        const =0
        Apply correction to spectrum in place.

        We pass in the forward model grids used. A class can use this to
        optimize its calculation, see for example FluorescenceEffect. 
        """
        return _spectrum_effect.SpectrumEffect_apply_effect(self, Spec, Forward_model_grid)


    def clone(self):
        """

        virtual boost::shared_ptr<SpectrumEffect> FullPhysics::SpectrumEffect::clone() const =0
        Clone a SpectrumEffect object.

        Note that the cloned version will not be attached to and StateVector
        or Observer<SpectrumEffect>, although you can of course attach them
        after receiving the cloned object.

        Because this isn't attached to the StateVector, one use of the clone
        operator is to create a "frozen" SpectrumEffect object. 
        """
        return _spectrum_effect.SpectrumEffect_clone(self)


    def _v_name(self):
        """

        virtual std::string FullPhysics::SpectrumEffect::name() const =0
        Name of spectrum effect, for use when outputting effects of effect. 
        """
        return _spectrum_effect.SpectrumEffect__v_name(self)


    @property
    def name(self):
        return self._v_name()


    def add_observer(self, Obs):
        """

        virtual void FullPhysics::SpectrumEffect::add_observer(Observer< SpectrumEffect > &Obs)

        """
        return _spectrum_effect.SpectrumEffect_add_observer(self, Obs)


    def remove_observer(self, Obs):
        """

        virtual void FullPhysics::SpectrumEffect::remove_observer(Observer< SpectrumEffect > &Obs)

        """
        return _spectrum_effect.SpectrumEffect_remove_observer(self, Obs)

SpectrumEffect_swigregister = _spectrum_effect.SpectrumEffect_swigregister
SpectrumEffect_swigregister(SpectrumEffect)

class SubStateVectorArraySpectrumEffect(SpectrumEffect, full_physics_swig.state_vector.SubStateVectorObserver):
    __swig_setmethods__ = {}
    for _s in [SpectrumEffect, full_physics_swig.state_vector.SubStateVectorObserver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SubStateVectorArraySpectrumEffect, name, value)
    __swig_getmethods__ = {}
    for _s in [SpectrumEffect, full_physics_swig.state_vector.SubStateVectorObserver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SubStateVectorArraySpectrumEffect, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def init(self, *args):
        return _spectrum_effect.SubStateVectorArraySpectrumEffect_init(self, *args)
    __swig_destroy__ = _spectrum_effect.delete_SubStateVectorArraySpectrumEffect
    __del__ = lambda self: None

    def mark_used_sub(self, Used):
        return _spectrum_effect.SubStateVectorArraySpectrumEffect_mark_used_sub(self, Used)

    def state_vector_name_i(self, i):
        return _spectrum_effect.SubStateVectorArraySpectrumEffect_state_vector_name_i(self, i)

    def state_vector_name_sub(self, Sv_name):
        return _spectrum_effect.SubStateVectorArraySpectrumEffect_state_vector_name_sub(self, Sv_name)

    def update_sub_state(self, Sv_sub, Cov):
        return _spectrum_effect.SubStateVectorArraySpectrumEffect_update_sub_state(self, Sv_sub, Cov)

    def update_sub_state_hook(self):
        return _spectrum_effect.SubStateVectorArraySpectrumEffect_update_sub_state_hook(self)

    def _v_coefficient(self):
        return _spectrum_effect.SubStateVectorArraySpectrumEffect__v_coefficient(self)

    @property
    def coefficient(self):
        return self._v_coefficient()


    def _v_used_flag_value(self):
        return _spectrum_effect.SubStateVectorArraySpectrumEffect__v_used_flag_value(self)

    @property
    def used_flag_value(self):
        return self._v_used_flag_value()


    def _v_statevector_covariance(self):
        return _spectrum_effect.SubStateVectorArraySpectrumEffect__v_statevector_covariance(self)

    @property
    def statevector_covariance(self):
        return self._v_statevector_covariance()


    def _v_pressure(self):
        return _spectrum_effect.SubStateVectorArraySpectrumEffect__v_pressure(self)

    @property
    def pressure(self):
        return self._v_pressure()

SubStateVectorArraySpectrumEffect_swigregister = _spectrum_effect.SubStateVectorArraySpectrumEffect_swigregister
SubStateVectorArraySpectrumEffect_swigregister(SubStateVectorArraySpectrumEffect)

class vector_spectrum_effect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_spectrum_effect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_spectrum_effect, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _spectrum_effect.vector_spectrum_effect_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _spectrum_effect.vector_spectrum_effect___nonzero__(self)

    def __bool__(self):
        return _spectrum_effect.vector_spectrum_effect___bool__(self)

    def __len__(self):
        return _spectrum_effect.vector_spectrum_effect___len__(self)

    def __getslice__(self, i, j):
        return _spectrum_effect.vector_spectrum_effect___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _spectrum_effect.vector_spectrum_effect___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _spectrum_effect.vector_spectrum_effect___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _spectrum_effect.vector_spectrum_effect___delitem__(self, *args)

    def __getitem__(self, *args):
        return _spectrum_effect.vector_spectrum_effect___getitem__(self, *args)

    def __setitem__(self, *args):
        return _spectrum_effect.vector_spectrum_effect___setitem__(self, *args)

    def pop(self):
        return _spectrum_effect.vector_spectrum_effect_pop(self)

    def append(self, x):
        return _spectrum_effect.vector_spectrum_effect_append(self, x)

    def empty(self):
        return _spectrum_effect.vector_spectrum_effect_empty(self)

    def size(self):
        return _spectrum_effect.vector_spectrum_effect_size(self)

    def swap(self, v):
        return _spectrum_effect.vector_spectrum_effect_swap(self, v)

    def begin(self):
        return _spectrum_effect.vector_spectrum_effect_begin(self)

    def end(self):
        return _spectrum_effect.vector_spectrum_effect_end(self)

    def rbegin(self):
        return _spectrum_effect.vector_spectrum_effect_rbegin(self)

    def rend(self):
        return _spectrum_effect.vector_spectrum_effect_rend(self)

    def clear(self):
        return _spectrum_effect.vector_spectrum_effect_clear(self)

    def get_allocator(self):
        return _spectrum_effect.vector_spectrum_effect_get_allocator(self)

    def pop_back(self):
        return _spectrum_effect.vector_spectrum_effect_pop_back(self)

    def erase(self, *args):
        return _spectrum_effect.vector_spectrum_effect_erase(self, *args)

    def __init__(self, *args):
        this = _spectrum_effect.new_vector_spectrum_effect(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _spectrum_effect.vector_spectrum_effect_push_back(self, x)

    def front(self):
        return _spectrum_effect.vector_spectrum_effect_front(self)

    def back(self):
        return _spectrum_effect.vector_spectrum_effect_back(self)

    def assign(self, n, x):
        return _spectrum_effect.vector_spectrum_effect_assign(self, n, x)

    def resize(self, *args):
        return _spectrum_effect.vector_spectrum_effect_resize(self, *args)

    def insert(self, *args):
        return _spectrum_effect.vector_spectrum_effect_insert(self, *args)

    def reserve(self, n):
        return _spectrum_effect.vector_spectrum_effect_reserve(self, n)

    def capacity(self):
        return _spectrum_effect.vector_spectrum_effect_capacity(self)
    __swig_destroy__ = _spectrum_effect.delete_vector_spectrum_effect
    __del__ = lambda self: None
vector_spectrum_effect_swigregister = _spectrum_effect.vector_spectrum_effect_swigregister
vector_spectrum_effect_swigregister(vector_spectrum_effect)

class vector_vector_spectrum_effect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_vector_spectrum_effect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_vector_spectrum_effect, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _spectrum_effect.vector_vector_spectrum_effect_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _spectrum_effect.vector_vector_spectrum_effect___nonzero__(self)

    def __bool__(self):
        return _spectrum_effect.vector_vector_spectrum_effect___bool__(self)

    def __len__(self):
        return _spectrum_effect.vector_vector_spectrum_effect___len__(self)

    def __getslice__(self, i, j):
        return _spectrum_effect.vector_vector_spectrum_effect___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _spectrum_effect.vector_vector_spectrum_effect___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _spectrum_effect.vector_vector_spectrum_effect___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _spectrum_effect.vector_vector_spectrum_effect___delitem__(self, *args)

    def __getitem__(self, *args):
        return _spectrum_effect.vector_vector_spectrum_effect___getitem__(self, *args)

    def __setitem__(self, *args):
        return _spectrum_effect.vector_vector_spectrum_effect___setitem__(self, *args)

    def pop(self):
        return _spectrum_effect.vector_vector_spectrum_effect_pop(self)

    def append(self, x):
        return _spectrum_effect.vector_vector_spectrum_effect_append(self, x)

    def empty(self):
        return _spectrum_effect.vector_vector_spectrum_effect_empty(self)

    def size(self):
        return _spectrum_effect.vector_vector_spectrum_effect_size(self)

    def swap(self, v):
        return _spectrum_effect.vector_vector_spectrum_effect_swap(self, v)

    def begin(self):
        return _spectrum_effect.vector_vector_spectrum_effect_begin(self)

    def end(self):
        return _spectrum_effect.vector_vector_spectrum_effect_end(self)

    def rbegin(self):
        return _spectrum_effect.vector_vector_spectrum_effect_rbegin(self)

    def rend(self):
        return _spectrum_effect.vector_vector_spectrum_effect_rend(self)

    def clear(self):
        return _spectrum_effect.vector_vector_spectrum_effect_clear(self)

    def get_allocator(self):
        return _spectrum_effect.vector_vector_spectrum_effect_get_allocator(self)

    def pop_back(self):
        return _spectrum_effect.vector_vector_spectrum_effect_pop_back(self)

    def erase(self, *args):
        return _spectrum_effect.vector_vector_spectrum_effect_erase(self, *args)

    def __init__(self, *args):
        this = _spectrum_effect.new_vector_vector_spectrum_effect(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _spectrum_effect.vector_vector_spectrum_effect_push_back(self, x)

    def front(self):
        return _spectrum_effect.vector_vector_spectrum_effect_front(self)

    def back(self):
        return _spectrum_effect.vector_vector_spectrum_effect_back(self)

    def assign(self, n, x):
        return _spectrum_effect.vector_vector_spectrum_effect_assign(self, n, x)

    def resize(self, *args):
        return _spectrum_effect.vector_vector_spectrum_effect_resize(self, *args)

    def insert(self, *args):
        return _spectrum_effect.vector_vector_spectrum_effect_insert(self, *args)

    def reserve(self, n):
        return _spectrum_effect.vector_vector_spectrum_effect_reserve(self, n)

    def capacity(self):
        return _spectrum_effect.vector_vector_spectrum_effect_capacity(self)
    __swig_destroy__ = _spectrum_effect.delete_vector_vector_spectrum_effect
    __del__ = lambda self: None
vector_vector_spectrum_effect_swigregister = _spectrum_effect.vector_vector_spectrum_effect_swigregister
vector_vector_spectrum_effect_swigregister(vector_vector_spectrum_effect)

# This file is compatible with both classic and new-style classes.


