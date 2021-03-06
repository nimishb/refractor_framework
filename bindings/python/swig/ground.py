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
            fp, pathname, description = imp.find_module('_ground', [dirname(__file__)])
        except ImportError:
            import _ground
            return _ground
        if fp is not None:
            try:
                _mod = imp.load_module('_ground', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ground = swig_import_helper()
    del swig_import_helper
else:
    import _ground
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



_ground.SHARED_PTR_DISOWN_swigconstant(_ground)
SHARED_PTR_DISOWN = _ground.SHARED_PTR_DISOWN

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

import full_physics_swig.observer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
class ObservableGround(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObservableGround, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObservableGround, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ground.delete_ObservableGround
    __del__ = lambda self: None

    def add_observer_and_keep_reference(self, Obs):
        return _ground.ObservableGround_add_observer_and_keep_reference(self, Obs)

    def add_observer(self, Obs):
        return _ground.ObservableGround_add_observer(self, Obs)

    def remove_observer(self, Obs):
        return _ground.ObservableGround_remove_observer(self, Obs)
ObservableGround_swigregister = _ground.ObservableGround_swigregister
ObservableGround_swigregister(ObservableGround)

class ObserverGround(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObserverGround, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObserverGround, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _ground.new_ObserverGround()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _ground.delete_ObserverGround
    __del__ = lambda self: None

    def notify_update(self, Observed_object):
        return _ground.ObserverGround_notify_update(self, Observed_object)

    def notify_add(self, Observed_object):
        return _ground.ObserverGround_notify_add(self, Observed_object)

    def notify_remove(self, Observed_object):
        return _ground.ObserverGround_notify_remove(self, Observed_object)
ObserverGround_swigregister = _ground.ObserverGround_swigregister
ObserverGround_swigregister(ObserverGround)

class Ground(ObservableGround):
    """

    This class maintains the ground portion of the state.

    Other objects may depend on the ground, and should be updated when the
    ground is updated. To facilitate that, this class in an Oberverable,
    and objects can add themselves as Observers to be notified when the
    ground is updated.

    This class is unfortunately a bit hard coded. The surface types are
    one of a set of enumerations. The surface parameters depend on exactly
    what the surface type is. These types and parameters map to types and
    parameters found in the LIDORT and LRAD code, so the hard coding is
    intrinsic.

    C++ includes: ground.h 
    """

    __swig_setmethods__ = {}
    for _s in [ObservableGround]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Ground, name, value)
    __swig_getmethods__ = {}
    for _s in [ObservableGround]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Ground, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _ground.delete_Ground
    __del__ = lambda self: None

    def add_observer(self, Obs):
        """

        virtual void FullPhysics::Ground::add_observer(Observer< Ground > &Obs)

        """
        return _ground.Ground_add_observer(self, Obs)


    def remove_observer(self, Obs):
        """

        virtual void FullPhysics::Ground::remove_observer(Observer< Ground > &Obs)

        """
        return _ground.Ground_remove_observer(self, Obs)


    def __str__(self):
        return _ground.Ground___str__(self)

    def surface_parameter(self, wn, spec_index):
        """

        virtual ArrayAd<double, 1> FullPhysics::Ground::surface_parameter(const double wn, const int spec_index) const =0
        Surface parmeters.

        What exactly these parameters mean is determined by the surface type,
        see the discussion in the comments before the Ground class. 
        """
        return _ground.Ground_surface_parameter(self, wn, spec_index)


    def clone(self):
        """

        virtual boost::shared_ptr<Ground> FullPhysics::Ground::clone() const =0
        Clone a Ground object.

        Note that the cloned version will not be attached to a StateVector,
        although you can of course attach them after receiving the cloned
        object.

        Because this isn't attached to the StateVector, one use of the clone
        operator is to create a "frozen" Ground object. 
        """
        return _ground.Ground_clone(self)


    def print_desc(self, Os):
        return _ground.Ground_print_desc(self, Os)
Ground_swigregister = _ground.Ground_swigregister
Ground_swigregister(Ground)

class SubStateVectorArrayGround(Ground, full_physics_swig.state_vector.SubStateVectorObserver):
    __swig_setmethods__ = {}
    for _s in [Ground, full_physics_swig.state_vector.SubStateVectorObserver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SubStateVectorArrayGround, name, value)
    __swig_getmethods__ = {}
    for _s in [Ground, full_physics_swig.state_vector.SubStateVectorObserver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SubStateVectorArrayGround, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def init(self, *args):
        return _ground.SubStateVectorArrayGround_init(self, *args)
    __swig_destroy__ = _ground.delete_SubStateVectorArrayGround
    __del__ = lambda self: None

    def mark_used_sub(self, Used):
        return _ground.SubStateVectorArrayGround_mark_used_sub(self, Used)

    def state_vector_name_i(self, i):
        return _ground.SubStateVectorArrayGround_state_vector_name_i(self, i)

    def state_vector_name_sub(self, Sv_name):
        return _ground.SubStateVectorArrayGround_state_vector_name_sub(self, Sv_name)

    def update_sub_state(self, Sv_sub, Cov):
        return _ground.SubStateVectorArrayGround_update_sub_state(self, Sv_sub, Cov)

    def update_sub_state_hook(self):
        return _ground.SubStateVectorArrayGround_update_sub_state_hook(self)

    def _v_coefficient(self):
        return _ground.SubStateVectorArrayGround__v_coefficient(self)

    @property
    def coefficient(self):
        return self._v_coefficient()


    def _v_used_flag_value(self):
        return _ground.SubStateVectorArrayGround__v_used_flag_value(self)

    @property
    def used_flag_value(self):
        return self._v_used_flag_value()


    def _v_statevector_covariance(self):
        return _ground.SubStateVectorArrayGround__v_statevector_covariance(self)

    @property
    def statevector_covariance(self):
        return self._v_statevector_covariance()


    def _v_pressure(self):
        return _ground.SubStateVectorArrayGround__v_pressure(self)

    @property
    def pressure(self):
        return self._v_pressure()

SubStateVectorArrayGround_swigregister = _ground.SubStateVectorArrayGround_swigregister
SubStateVectorArrayGround_swigregister(SubStateVectorArrayGround)

# This file is compatible with both classic and new-style classes.


