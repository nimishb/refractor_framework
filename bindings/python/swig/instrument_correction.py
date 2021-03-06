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
            fp, pathname, description = imp.find_module('_instrument_correction', [dirname(__file__)])
        except ImportError:
            import _instrument_correction
            return _instrument_correction
        if fp is not None:
            try:
                _mod = imp.load_module('_instrument_correction', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _instrument_correction = swig_import_helper()
    del swig_import_helper
else:
    import _instrument_correction
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



_instrument_correction.SHARED_PTR_DISOWN_swigconstant(_instrument_correction)
SHARED_PTR_DISOWN = _instrument_correction.SHARED_PTR_DISOWN

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
class ObservableInstrumentCorrection(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObservableInstrumentCorrection, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObservableInstrumentCorrection, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _instrument_correction.delete_ObservableInstrumentCorrection
    __del__ = lambda self: None

    def add_observer_and_keep_reference(self, Obs):
        return _instrument_correction.ObservableInstrumentCorrection_add_observer_and_keep_reference(self, Obs)

    def add_observer(self, Obs):
        return _instrument_correction.ObservableInstrumentCorrection_add_observer(self, Obs)

    def remove_observer(self, Obs):
        return _instrument_correction.ObservableInstrumentCorrection_remove_observer(self, Obs)
ObservableInstrumentCorrection_swigregister = _instrument_correction.ObservableInstrumentCorrection_swigregister
ObservableInstrumentCorrection_swigregister(ObservableInstrumentCorrection)

class ObserverInstrumentCorrection(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObserverInstrumentCorrection, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObserverInstrumentCorrection, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _instrument_correction.new_ObserverInstrumentCorrection()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _instrument_correction.delete_ObserverInstrumentCorrection
    __del__ = lambda self: None

    def notify_update(self, Observed_object):
        return _instrument_correction.ObserverInstrumentCorrection_notify_update(self, Observed_object)

    def notify_add(self, Observed_object):
        return _instrument_correction.ObserverInstrumentCorrection_notify_add(self, Observed_object)

    def notify_remove(self, Observed_object):
        return _instrument_correction.ObserverInstrumentCorrection_notify_remove(self, Observed_object)
ObserverInstrumentCorrection_swigregister = _instrument_correction.ObserverInstrumentCorrection_swigregister
ObserverInstrumentCorrection_swigregister(ObserverInstrumentCorrection)

class InstrumentCorrection(full_physics_swig.state_vector.StateVectorObserver, ObservableInstrumentCorrection):
    """

    This class models an Instrument correction.

    This is used by IlsConvolution, and it applies zero or more
    corrections that allow the radiance results to be modified. Examples
    are a zero level offset correction, and a continuum correction.

    C++ includes: instrument_correction.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.state_vector.StateVectorObserver, ObservableInstrumentCorrection]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, InstrumentCorrection, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.state_vector.StateVectorObserver, ObservableInstrumentCorrection]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, InstrumentCorrection, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _instrument_correction.delete_InstrumentCorrection
    __del__ = lambda self: None

    def __str__(self):
        return _instrument_correction.InstrumentCorrection___str__(self)

    def apply_correction(self, Pixel_grid, Pixel_list, Radiance):
        """

        virtual void FullPhysics::InstrumentCorrection::apply_correction(const SpectralDomain &Pixel_grid, const std::vector< int >
        &Pixel_list, SpectralRange &Radiance) const =0
        Apply correction to radiance values, in place.

        If Radiance includes a Jacobian, then we include the Jacobian
        calculation. Otherwise we don't include the Jacobian in the
        calculation.

        Parameters:
        -----------

        Pixel_grid:  - The grid point of each pixel. We only use a subset of
        these points, but the full list is passed in for use by the class.

        Pixel_list:  - List of pixels that actually appear in Radiance, in the
        order that they appear.

        Radiance:  - Radiance values, that will be corrected in place. 
        """
        return _instrument_correction.InstrumentCorrection_apply_correction(self, Pixel_grid, Pixel_list, Radiance)


    def clone(self):
        """

        virtual boost::shared_ptr<InstrumentCorrection> FullPhysics::InstrumentCorrection::clone() const =0
        Clone an InstrumentCorrection object.

        Note that the cloned version will not be attached to and StateVector
        or Observer<InstrumentCorrection>, although you can of course attach
        them after receiving the cloned object.

        Because this isn't attached to the StateVector, one use of the clone
        operator is to create a "frozen" InstrumentCorrection object. 
        """
        return _instrument_correction.InstrumentCorrection_clone(self)

InstrumentCorrection_swigregister = _instrument_correction.InstrumentCorrection_swigregister
InstrumentCorrection_swigregister(InstrumentCorrection)

class SubStateVectorArrayInstrumentCorrection(InstrumentCorrection, full_physics_swig.state_vector.SubStateVectorObserver):
    __swig_setmethods__ = {}
    for _s in [InstrumentCorrection, full_physics_swig.state_vector.SubStateVectorObserver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SubStateVectorArrayInstrumentCorrection, name, value)
    __swig_getmethods__ = {}
    for _s in [InstrumentCorrection, full_physics_swig.state_vector.SubStateVectorObserver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SubStateVectorArrayInstrumentCorrection, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def init(self, *args):
        return _instrument_correction.SubStateVectorArrayInstrumentCorrection_init(self, *args)
    __swig_destroy__ = _instrument_correction.delete_SubStateVectorArrayInstrumentCorrection
    __del__ = lambda self: None

    def mark_used_sub(self, Used):
        return _instrument_correction.SubStateVectorArrayInstrumentCorrection_mark_used_sub(self, Used)

    def state_vector_name_i(self, i):
        return _instrument_correction.SubStateVectorArrayInstrumentCorrection_state_vector_name_i(self, i)

    def state_vector_name_sub(self, Sv_name):
        return _instrument_correction.SubStateVectorArrayInstrumentCorrection_state_vector_name_sub(self, Sv_name)

    def update_sub_state(self, Sv_sub, Cov):
        return _instrument_correction.SubStateVectorArrayInstrumentCorrection_update_sub_state(self, Sv_sub, Cov)

    def update_sub_state_hook(self):
        return _instrument_correction.SubStateVectorArrayInstrumentCorrection_update_sub_state_hook(self)

    def _v_coefficient(self):
        return _instrument_correction.SubStateVectorArrayInstrumentCorrection__v_coefficient(self)

    @property
    def coefficient(self):
        return self._v_coefficient()


    def _v_used_flag_value(self):
        return _instrument_correction.SubStateVectorArrayInstrumentCorrection__v_used_flag_value(self)

    @property
    def used_flag_value(self):
        return self._v_used_flag_value()


    def _v_statevector_covariance(self):
        return _instrument_correction.SubStateVectorArrayInstrumentCorrection__v_statevector_covariance(self)

    @property
    def statevector_covariance(self):
        return self._v_statevector_covariance()


    def _v_pressure(self):
        return _instrument_correction.SubStateVectorArrayInstrumentCorrection__v_pressure(self)

    @property
    def pressure(self):
        return self._v_pressure()

SubStateVectorArrayInstrumentCorrection_swigregister = _instrument_correction.SubStateVectorArrayInstrumentCorrection_swigregister
SubStateVectorArrayInstrumentCorrection_swigregister(SubStateVectorArrayInstrumentCorrection)

# This file is compatible with both classic and new-style classes.


