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
            fp, pathname, description = imp.find_module('_rayleigh', [dirname(__file__)])
        except ImportError:
            import _rayleigh
            return _rayleigh
        if fp is not None:
            try:
                _mod = imp.load_module('_rayleigh', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _rayleigh = swig_import_helper()
    del swig_import_helper
else:
    import _rayleigh
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



_rayleigh.SHARED_PTR_DISOWN_swigconstant(_rayleigh)
SHARED_PTR_DISOWN = _rayleigh.SHARED_PTR_DISOWN

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

import full_physics_swig.pressure
import full_physics_swig.state_vector
import full_physics_swig.generic_object
import full_physics_swig.temperature
import full_physics_swig.altitude
class ObservableRayleigh(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObservableRayleigh, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObservableRayleigh, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _rayleigh.delete_ObservableRayleigh
    __del__ = lambda self: None

    def add_observer_and_keep_reference(self, Obs):
        return _rayleigh.ObservableRayleigh_add_observer_and_keep_reference(self, Obs)

    def add_observer(self, Obs):
        return _rayleigh.ObservableRayleigh_add_observer(self, Obs)

    def remove_observer(self, Obs):
        return _rayleigh.ObservableRayleigh_remove_observer(self, Obs)
ObservableRayleigh_swigregister = _rayleigh.ObservableRayleigh_swigregister
ObservableRayleigh_swigregister(ObservableRayleigh)

class ObserverRayleigh(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObserverRayleigh, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObserverRayleigh, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _rayleigh.new_ObserverRayleigh()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _rayleigh.delete_ObserverRayleigh
    __del__ = lambda self: None

    def notify_update(self, Observed_object):
        return _rayleigh.ObserverRayleigh_notify_update(self, Observed_object)

    def notify_add(self, Observed_object):
        return _rayleigh.ObserverRayleigh_notify_add(self, Observed_object)

    def notify_remove(self, Observed_object):
        return _rayleigh.ObserverRayleigh_notify_remove(self, Observed_object)
ObserverRayleigh_swigregister = _rayleigh.ObserverRayleigh_swigregister
ObserverRayleigh_swigregister(ObserverRayleigh)

class Rayleigh(full_physics_swig.pressure.ObserverPressure, full_physics_swig.altitude.ObserverAltitude):
    """

    This class calculates the Rayleigh portion of the optical depth.

    C++ includes: rayleigh.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.pressure.ObserverPressure, full_physics_swig.altitude.ObserverAltitude]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Rayleigh, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.pressure.ObserverPressure, full_physics_swig.altitude.ObserverAltitude]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Rayleigh, name)
    __repr__ = _swig_repr

    def __init__(self, Pres, Alt, C):
        """

        FullPhysics::Rayleigh::Rayleigh(const boost::shared_ptr< Pressure > &Pres, const std::vector<
        boost::shared_ptr< Altitude > > &Alt, const Constant &C)

        """
        this = _rayleigh.new_Rayleigh(Pres, Alt, C)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def notify_update(self, *args):
        """

        virtual void FullPhysics::Rayleigh::notify_update(const Altitude &A)

        """
        return _rayleigh.Rayleigh_notify_update(self, *args)


    def optical_depth_each_layer(self, wn, spec_index):
        """

        ArrayAd<double, 1> FullPhysics::Rayleigh::optical_depth_each_layer(double wn, int spec_index) const

        """
        return _rayleigh.Rayleigh_optical_depth_each_layer(self, wn, spec_index)


    def cross_section(*args):
        """

        static DoubleWithUnit FullPhysics::Rayleigh::cross_section(const DoubleWithUnit &W, const Constant &C=DefaultConstant())

        """
        return _rayleigh.Rayleigh_cross_section(*args)

    if _newclass:
        cross_section = staticmethod(cross_section)
    __swig_getmethods__["cross_section"] = lambda x: cross_section
    __swig_destroy__ = _rayleigh.delete_Rayleigh
    __del__ = lambda self: None
Rayleigh_swigregister = _rayleigh.Rayleigh_swigregister
Rayleigh_swigregister(Rayleigh)

def Rayleigh_cross_section(*args):
    """

    static DoubleWithUnit FullPhysics::Rayleigh::cross_section(const DoubleWithUnit &W, const Constant &C=DefaultConstant())

    """
    return _rayleigh.Rayleigh_cross_section(*args)

# This file is compatible with both classic and new-style classes.


