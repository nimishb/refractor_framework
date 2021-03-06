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
            fp, pathname, description = imp.find_module('_aerosol_property_imp_base', [dirname(__file__)])
        except ImportError:
            import _aerosol_property_imp_base
            return _aerosol_property_imp_base
        if fp is not None:
            try:
                _mod = imp.load_module('_aerosol_property_imp_base', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _aerosol_property_imp_base = swig_import_helper()
    del swig_import_helper
else:
    import _aerosol_property_imp_base
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



_aerosol_property_imp_base.SHARED_PTR_DISOWN_swigconstant(_aerosol_property_imp_base)
SHARED_PTR_DISOWN = _aerosol_property_imp_base.SHARED_PTR_DISOWN

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

import full_physics_swig.aerosol_property
import full_physics_swig.observer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
class SubStateVectorArrayAerosolProperty(full_physics_swig.aerosol_property.AerosolProperty, full_physics_swig.state_vector.SubStateVectorObserver):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.aerosol_property.AerosolProperty, full_physics_swig.state_vector.SubStateVectorObserver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SubStateVectorArrayAerosolProperty, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.aerosol_property.AerosolProperty, full_physics_swig.state_vector.SubStateVectorObserver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SubStateVectorArrayAerosolProperty, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def init(self, *args):
        return _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_init(self, *args)
    __swig_destroy__ = _aerosol_property_imp_base.delete_SubStateVectorArrayAerosolProperty
    __del__ = lambda self: None

    def mark_used_sub(self, Used):
        return _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_mark_used_sub(self, Used)

    def state_vector_name_i(self, i):
        return _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_state_vector_name_i(self, i)

    def state_vector_name_sub(self, Sv_name):
        return _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_state_vector_name_sub(self, Sv_name)

    def update_sub_state(self, Sv_sub, Cov):
        return _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_update_sub_state(self, Sv_sub, Cov)

    def update_sub_state_hook(self):
        return _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_update_sub_state_hook(self)

    def _v_coefficient(self):
        return _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty__v_coefficient(self)

    @property
    def coefficient(self):
        return self._v_coefficient()


    def _v_used_flag_value(self):
        return _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty__v_used_flag_value(self)

    @property
    def used_flag_value(self):
        return self._v_used_flag_value()


    def _v_statevector_covariance(self):
        return _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty__v_statevector_covariance(self)

    @property
    def statevector_covariance(self):
        return self._v_statevector_covariance()


    def _v_pressure(self):
        return _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty__v_pressure(self)

    @property
    def pressure(self):
        return self._v_pressure()

SubStateVectorArrayAerosolProperty_swigregister = _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_swigregister
SubStateVectorArrayAerosolProperty_swigregister(SubStateVectorArrayAerosolProperty)

class AerosolPropertyImpBase(SubStateVectorArrayAerosolProperty):
    """

    As a design principle, we have each base class with the absolutely
    minimum interface needed for use from the rest of the system.

    This allows us to support any future code that supports this minimum
    interface.

    However, almost always you will want to derive from this class
    instead. See PressureImpBase for a more complete discussion of this.

    C++ includes: aerosol_property_imp_base.h 
    """

    __swig_setmethods__ = {}
    for _s in [SubStateVectorArrayAerosolProperty]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, AerosolPropertyImpBase, name, value)
    __swig_getmethods__ = {}
    for _s in [SubStateVectorArrayAerosolProperty]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, AerosolPropertyImpBase, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _aerosol_property_imp_base.delete_AerosolPropertyImpBase
    __del__ = lambda self: None

    def clone(self, *args):
        """

        virtual boost::shared_ptr<AerosolProperty> FullPhysics::AerosolPropertyImpBase::clone(const boost::shared_ptr< Pressure > &Press, const boost::shared_ptr<
        RelativeHumidity > &Rh) const =0

        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_clone(self, *args)


    def extinction_coefficient_each_layer(self, wn):
        """

        virtual ArrayAd<double,1> FullPhysics::AerosolPropertyImpBase::extinction_coefficient_each_layer(double wn) const =0

        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_extinction_coefficient_each_layer(self, wn)


    def scattering_coefficient_each_layer(self, wn):
        """

        virtual ArrayAd<double, 1> FullPhysics::AerosolPropertyImpBase::scattering_coefficient_each_layer(double wn) const =0

        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_scattering_coefficient_each_layer(self, wn)


    def phase_function_moment_each_layer(self, wn, nmom=-1, nscatt=-1):
        """

        virtual ArrayAd<double, 3> FullPhysics::AerosolPropertyImpBase::phase_function_moment_each_layer(double wn, int nmom=-1, int nscatt=-1) const =0

        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_phase_function_moment_each_layer(self, wn, nmom, nscatt)


    def desc(self):
        """

        virtual std::string FullPhysics::AerosolPropertyImpBase::desc() const
        Description of object, to be printed to stream.

        This gives a cleaner interface for deriving from python. 
        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_desc(self)


    def add_observer(self, Obs):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_add_observer(self, Obs)

    def remove_observer(self, Obs):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_remove_observer(self, Obs)

    def update_sub_state_hook(self):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_update_sub_state_hook(self)

    def print_desc(self, Os):
        """

        virtual void FullPhysics::AerosolPropertyImpBase::print(std::ostream &Os) const
        Print to stream.

        The default calls the function "desc" that returns a string. This
        gives cleaner interface for deriving from this class in python, but
        most C++ classes will want to override this function rather than using
        desc. 
        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_print_desc(self, Os)


    def _v_desc(self):
        """

        virtual std::string FullPhysics::AerosolPropertyImpBase::desc() const
        Description of object, to be printed to stream.

        This gives a cleaner interface for deriving from python. 
        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase__v_desc(self)


    @property
    def desc(self):
        return self._v_desc()


    def mark_used(self, Sv, Used):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_mark_used(self, Sv, Used)

    def state_vector_name(self, Sv, Sv_name):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_state_vector_name(self, Sv, Sv_name)

    def notify_update(self, Observed_object):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_notify_update(self, Observed_object)

    def notify_add(self, Observed_object):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_notify_add(self, Observed_object)

    def notify_remove(self, Observed_object):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_notify_remove(self, Observed_object)

    def update_sub_state(self, Sv_sub, Cov_sub):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_update_sub_state(self, Sv_sub, Cov_sub)

    def state_vector_name_i(self, i):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_state_vector_name_i(self, i)

    def state_vector_name_sub(self, Sv_name):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_state_vector_name_sub(self, Sv_name)

    def _v_aerosol_parameter(self):
        """

        blitz::Array<double, 1> FullPhysics::AerosolPropertyImpBase::aerosol_parameter() const
        Returns the value of the coefficients used to generate the aerosol
        property. 
        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase__v_aerosol_parameter(self)


    @property
    def aerosol_parameter(self):
        return self._v_aerosol_parameter()


    def _v_aerosol_parameter_uncertainty(self):
        """

        blitz::Array<double, 1> FullPhysics::AerosolPropertyImpBase::aerosol_parameter_uncertainty() const
        Returns the uncertainty of the aerosol type coefficients. 
        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase__v_aerosol_parameter_uncertainty(self)


    @property
    def aerosol_parameter_uncertainty(self):
        return self._v_aerosol_parameter_uncertainty()


    def init(self, Coeff, Used_flag):
        return _aerosol_property_imp_base.AerosolPropertyImpBase_init(self, Coeff, Used_flag)

    def __init__(self, *args):
        if self.__class__ == AerosolPropertyImpBase:
            _self = None
        else:
            _self = self
        this = _aerosol_property_imp_base.new_AerosolPropertyImpBase(_self, *args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    def __disown__(self):
        self.this.disown()
        _aerosol_property_imp_base.disown_AerosolPropertyImpBase(self)
        return weakref_proxy(self)
AerosolPropertyImpBase_swigregister = _aerosol_property_imp_base.AerosolPropertyImpBase_swigregister
AerosolPropertyImpBase_swigregister(AerosolPropertyImpBase)

# This file is compatible with both classic and new-style classes.


