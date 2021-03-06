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
            fp, pathname, description = imp.find_module('_radiative_transfer_imp_base', [dirname(__file__)])
        except ImportError:
            import _radiative_transfer_imp_base
            return _radiative_transfer_imp_base
        if fp is not None:
            try:
                _mod = imp.load_module('_radiative_transfer_imp_base', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _radiative_transfer_imp_base = swig_import_helper()
    del swig_import_helper
else:
    import _radiative_transfer_imp_base
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



_radiative_transfer_imp_base.SHARED_PTR_DISOWN_swigconstant(_radiative_transfer_imp_base)
SHARED_PTR_DISOWN = _radiative_transfer_imp_base.SHARED_PTR_DISOWN

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

import full_physics_swig.radiative_transfer_retrievable
import full_physics_swig.radiative_transfer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
import full_physics_swig.sub_state_vector_array
class RadiativeTransferImpBase(full_physics_swig.radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer):
    """

    As a design principle, we have each base class with the absolutely
    minimum interface needed for use from the rest of the system.

    This allows us to support any future code that supports this minimum
    interface.

    However, almost always you will want to derive from this class
    instead. See PressureImpBase for a more complete discussion of this.

    C++ includes: radiative_transfer_imp_base.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RadiativeTransferImpBase, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.radiative_transfer_retrievable.SubStateVectorArrayRadiativeTransfer]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RadiativeTransferImpBase, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _radiative_transfer_imp_base.delete_RadiativeTransferImpBase
    __del__ = lambda self: None

    def clone(self):
        """

        virtual boost::shared_ptr<RadiativeTransferRetrievable> FullPhysics::RadiativeTransferImpBase::clone() const =0

        """
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_clone(self)


    def _v_number_stokes(self):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase__v_number_stokes(self)

    @property
    def number_stokes(self):
        return self._v_number_stokes()


    def _v_number_spectrometer(self):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase__v_number_spectrometer(self)

    @property
    def number_spectrometer(self):
        return self._v_number_spectrometer()


    def reflectance(self, Spec_domain, Spec_index, Skip_jacobian=False):
        """

        virtual boost::shared_ptr<Spectrum> FullPhysics::RadiativeTransferImpBase::reflectance_ptr(const SpectralDomain &Spec_domain, int Spec_index, bool
        Skip_jacobian=false) const =0
        For the sake of being able to return a Spectrum class from Python The
        reflectance_ptr method here serves the purpose that the radiance
        method normally would.

        The reflectance method in this implementation simply calls the
        reflectance_ptr method for doing the actual work. 
        """
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_reflectance(self, Spec_domain, Spec_index, Skip_jacobian)


    def stokes(self, Spec_domain, Spec_index):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_stokes(self, Spec_domain, Spec_index)

    def stokes_and_jacobian(self, Spec_domain, Spec_index):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_stokes_and_jacobian(self, Spec_domain, Spec_index)

    def add_observer(self, Obs):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_add_observer(self, Obs)

    def remove_observer(self, Obs):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_remove_observer(self, Obs)

    def update_sub_state_hook(self):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_update_sub_state_hook(self)

    def print_desc(self, Os):
        """

        virtual void FullPhysics::RadiativeTransferImpBase::print(std::ostream &Os, bool Short_form=false) const
        Print to stream.

        The default calls the function "desc" that returns a string. This
        gives cleaner interface for deriving from this class in python, but
        most C++ classes will want to override this function rather than using
        desc. 
        """
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_print_desc(self, Os)


    def _v_desc(self):
        """

        virtual std::string FullPhysics::RadiativeTransferImpBase::desc() const
        Description of object, to be printed to stream.

        This gives a cleaner interface for deriving from python. 
        """
        return _radiative_transfer_imp_base.RadiativeTransferImpBase__v_desc(self)


    @property
    def desc(self):
        return self._v_desc()


    def mark_used(self, Sv, Used):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_mark_used(self, Sv, Used)

    def state_vector_name(self, Sv, Sv_name):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_state_vector_name(self, Sv, Sv_name)

    def notify_update(self, Observed_object):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_notify_update(self, Observed_object)

    def notify_add(self, Observed_object):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_notify_add(self, Observed_object)

    def notify_remove(self, Observed_object):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_notify_remove(self, Observed_object)

    def update_sub_state(self, Sv_sub, Cov_sub):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_update_sub_state(self, Sv_sub, Cov_sub)

    def state_vector_name_i(self, i):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_state_vector_name_i(self, i)

    def state_vector_name_sub(self, Sv_name):
        return _radiative_transfer_imp_base.RadiativeTransferImpBase_state_vector_name_sub(self, Sv_name)

    def __init__(self, *args):
        if self.__class__ == RadiativeTransferImpBase:
            _self = None
        else:
            _self = self
        this = _radiative_transfer_imp_base.new_RadiativeTransferImpBase(_self, *args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    def __disown__(self):
        self.this.disown()
        _radiative_transfer_imp_base.disown_RadiativeTransferImpBase(self)
        return weakref_proxy(self)
RadiativeTransferImpBase_swigregister = _radiative_transfer_imp_base.RadiativeTransferImpBase_swigregister
RadiativeTransferImpBase_swigregister(RadiativeTransferImpBase)

# This file is compatible with both classic and new-style classes.


