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
            fp, pathname, description = imp.find_module('_absorber_vmr_level', [dirname(__file__)])
        except ImportError:
            import _absorber_vmr_level
            return _absorber_vmr_level
        if fp is not None:
            try:
                _mod = imp.load_module('_absorber_vmr_level', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _absorber_vmr_level = swig_import_helper()
    del swig_import_helper
else:
    import _absorber_vmr_level
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



_absorber_vmr_level.SHARED_PTR_DISOWN_swigconstant(_absorber_vmr_level)
SHARED_PTR_DISOWN = _absorber_vmr_level.SHARED_PTR_DISOWN

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

import full_physics_swig.absorber_vmr_imp_base
import full_physics_swig.state_vector
import full_physics_swig.generic_object
import full_physics_swig.sub_state_vector_array
import full_physics_swig.absorber_vmr
class AbsorberVmrLevel(full_physics_swig.absorber_vmr_imp_base.AbsorberVmrImpBase):
    """

    This class maps the state vector to the absorber VMR on each level.

    This particular implementation uses the state vector values as the VMR
    for each pressure level.

    C++ includes: absorber_vmr_level.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.absorber_vmr_imp_base.AbsorberVmrImpBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, AbsorberVmrLevel, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.absorber_vmr_imp_base.AbsorberVmrImpBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, AbsorberVmrLevel, name)
    __repr__ = _swig_repr

    def __init__(self, Press, Vmr, Vmr_flag, Gas_name):
        """

        FullPhysics::AbsorberVmrLevel::AbsorberVmrLevel(const boost::shared_ptr< Pressure > &Press, const blitz::Array<
        double, 1 > &Vmr, const blitz::Array< bool, 1 > &Vmr_flag, const
        std::string &Gas_name)

        """
        this = _absorber_vmr_level.new_AbsorberVmrLevel(Press, Vmr, Vmr_flag, Gas_name)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def clone(self, *args):
        """

        virtual boost::shared_ptr<AbsorberVmr> FullPhysics::AbsorberVmrLevel::clone(const boost::shared_ptr< Pressure > &Press) const

        """
        return _absorber_vmr_level.AbsorberVmrLevel_clone(self, *args)


    def state_vector_name_i(self, i):
        """

        virtual std::string FullPhysics::AbsorberVmrLevel::state_vector_name_i(int i) const

        """
        return _absorber_vmr_level.AbsorberVmrLevel_state_vector_name_i(self, i)


    def _v_vmr_profile(self):
        """

        blitz::Array<double, 1> FullPhysics::AbsorberVmrLevel::vmr_profile() const
        VMR on the pressure grid.

        This is just coeff.value, but this is useful for generating output. 
        """
        return _absorber_vmr_level.AbsorberVmrLevel__v_vmr_profile(self)


    @property
    def vmr_profile(self):
        return self._v_vmr_profile()


    def _v_vmr_covariance(self):
        """

        blitz::Array<double, 2> FullPhysics::AbsorberVmrLevel::vmr_covariance() const
        Covariance of vmr profile. 
        """
        return _absorber_vmr_level.AbsorberVmrLevel__v_vmr_covariance(self)


    @property
    def vmr_covariance(self):
        return self._v_vmr_covariance()


    def _v_vmr_uncertainty(self):
        """

        blitz::Array<double, 1> FullPhysics::AbsorberVmrLevel::vmr_uncertainty() const
        Uncertainty of VMR. 
        """
        return _absorber_vmr_level.AbsorberVmrLevel__v_vmr_uncertainty(self)


    @property
    def vmr_uncertainty(self):
        return self._v_vmr_uncertainty()

    __swig_destroy__ = _absorber_vmr_level.delete_AbsorberVmrLevel
    __del__ = lambda self: None
AbsorberVmrLevel_swigregister = _absorber_vmr_level.AbsorberVmrLevel_swigregister
AbsorberVmrLevel_swigregister(AbsorberVmrLevel)

# This file is compatible with both classic and new-style classes.


