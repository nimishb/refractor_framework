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
            fp, pathname, description = imp.find_module('_aerosol', [dirname(__file__)])
        except ImportError:
            import _aerosol
            return _aerosol
        if fp is not None:
            try:
                _mod = imp.load_module('_aerosol', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _aerosol = swig_import_helper()
    del swig_import_helper
else:
    import _aerosol
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



_aerosol.SHARED_PTR_DISOWN_swigconstant(_aerosol)
SHARED_PTR_DISOWN = _aerosol.SHARED_PTR_DISOWN

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
import full_physics_swig.pressure
class ObserverAerosol(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObserverAerosol, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObserverAerosol, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _aerosol.new_ObserverAerosol()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _aerosol.delete_ObserverAerosol
    __del__ = lambda self: None

    def notify_update(self, Observed_object):
        return _aerosol.ObserverAerosol_notify_update(self, Observed_object)

    def notify_add(self, Observed_object):
        return _aerosol.ObserverAerosol_notify_add(self, Observed_object)

    def notify_remove(self, Observed_object):
        return _aerosol.ObserverAerosol_notify_remove(self, Observed_object)
ObserverAerosol_swigregister = _aerosol.ObserverAerosol_swigregister
ObserverAerosol_swigregister(ObserverAerosol)

class ObservableAerosol(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ObservableAerosol, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ObservableAerosol, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _aerosol.delete_ObservableAerosol
    __del__ = lambda self: None

    def add_observer_and_keep_reference(self, Obs):
        return _aerosol.ObservableAerosol_add_observer_and_keep_reference(self, Obs)

    def add_observer(self, Obs):
        return _aerosol.ObservableAerosol_add_observer(self, Obs)

    def remove_observer(self, Obs):
        return _aerosol.ObservableAerosol_remove_observer(self, Obs)
ObservableAerosol_swigregister = _aerosol.ObservableAerosol_swigregister
ObservableAerosol_swigregister(ObservableAerosol)

class Aerosol(full_physics_swig.state_vector.StateVectorObserver, ObservableAerosol):
    """

    This class maintains the aerosol portion of the state.

    Other objects may depend on the aerosol, and should be updated when
    the aerosol is updated. To facilitate that, this class in an
    Oberverable, and objects can add themselves as Observers to be
    notified when the aerosol is updated.

    I'm not really sure what the interface for this class should be. Right
    now it is used only by AtmosphereOco, and there is only one instance
    AerosolOptical, so the functions are what AtmosphereOco needs. But we
    may perhaps want to modify this in the future to be more general.

    C++ includes: aerosol.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.state_vector.StateVectorObserver, ObservableAerosol]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Aerosol, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.state_vector.StateVectorObserver, ObservableAerosol]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Aerosol, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def __str__(self):
        return _aerosol.Aerosol___str__(self)

    def add_observer(self, Obs):
        """

        virtual void FullPhysics::Aerosol::add_observer(Observer< Aerosol > &Obs)

        """
        return _aerosol.Aerosol_add_observer(self, Obs)


    def remove_observer(self, Obs):
        """

        virtual void FullPhysics::Aerosol::remove_observer(Observer< Aerosol > &Obs)

        """
        return _aerosol.Aerosol_remove_observer(self, Obs)


    def pf_mom(self, wn, frac_aer, nummom=-1, numscat=-1):
        """

        virtual ArrayAd<double, 3> FullPhysics::Aerosol::pf_mom(double wn, const ArrayAd< double, 2 > &frac_aer, int nummom=-1, int
        numscat=-1) const =0
        This calculates the portion of the phase function moments that come
        from the aerosol.

        Parameters:
        -----------

        wn:  The wave number.

        frac_aer:  This is number_active_layer() x number_particle()

        nummom:  Number of moments to fill in

        numscat:  Number of scatters to fill in 
        """
        return _aerosol.Aerosol_pf_mom(self, wn, frac_aer, nummom, numscat)


    def optical_depth_each_layer(self, wn):
        """

        virtual ArrayAd<double, 2> FullPhysics::Aerosol::optical_depth_each_layer(double wn) const =0
        This gives the optical depth for each layer, for the given wave
        number.

        Note this only includes the aerosol portion of this, Atmosphere class
        combines this with Absorbers and rayleigh scattering.

        This calculates the derivatives with respect to the state vector.

        This has size of number_active_layer() x number_particle(). 
        """
        return _aerosol.Aerosol_optical_depth_each_layer(self, wn)


    def ssa_each_layer(self, wn, particle_index, Od):
        """

        virtual ArrayAd<double, 1> FullPhysics::Aerosol::ssa_each_layer(double wn, int particle_index, const ArrayAd< double, 1 > &Od) const
        =0
        This gives the single scatter albedo for each layer, for the given
        wave number, for the given particle.

        Note this only includes the aerosol portion of this, Atmosphere class
        combines this with Rayleigh scattering.

        We take in the optical depth of each layer. This is just what is
        returned by optical_depth_each_layer(), we take this in because we can
        change what the derivative of optical_depth_each_layer is respect to,
        e.g. in AtmosphereOco we use taua_i.

        This calculates the derivative with respect to whatever variables Od
        is relative to.

        This has size of number_active_layer() 
        """
        return _aerosol.Aerosol_ssa_each_layer(self, wn, particle_index, Od)


    def _v_number_particle(self):
        """

        virtual int FullPhysics::Aerosol::number_particle() const =0
        Number of aerosol particles. 
        """
        return _aerosol.Aerosol__v_number_particle(self)


    @property
    def number_particle(self):
        return self._v_number_particle()


    def clone(self, *args):
        """

        virtual boost::shared_ptr<Aerosol> FullPhysics::Aerosol::clone(const boost::shared_ptr< Pressure > &Press, const boost::shared_ptr<
        RelativeHumidity > &Rh) const =0

        """
        return _aerosol.Aerosol_clone(self, *args)

    __swig_destroy__ = _aerosol.delete_Aerosol
    __del__ = lambda self: None
Aerosol_swigregister = _aerosol.Aerosol_swigregister
Aerosol_swigregister(Aerosol)

# This file is compatible with both classic and new-style classes.


