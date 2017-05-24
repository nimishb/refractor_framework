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
            fp, pathname, description = imp.find_module('_max_a_posteriori', [dirname(__file__)])
        except ImportError:
            import _max_a_posteriori
            return _max_a_posteriori
        if fp is not None:
            try:
                _mod = imp.load_module('_max_a_posteriori', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _max_a_posteriori = swig_import_helper()
    del swig_import_helper
else:
    import _max_a_posteriori
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



_max_a_posteriori.SHARED_PTR_DISOWN_swigconstant(_max_a_posteriori)
SHARED_PTR_DISOWN = _max_a_posteriori.SHARED_PTR_DISOWN

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

import full_physics_swig.model_measure
import full_physics_swig.model_state
import full_physics_swig.problem_state
import full_physics_swig.generic_object
class MaxAPosteriori(full_physics_swig.model_measure.ModelMeasure):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.model_measure.ModelMeasure]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MaxAPosteriori, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.model_measure.ModelMeasure]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MaxAPosteriori, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _max_a_posteriori.delete_MaxAPosteriori
    __del__ = lambda self: None

    def _v_a_priori_params(self):
        return _max_a_posteriori.MaxAPosteriori__v_a_priori_params(self)

    @property
    def a_priori_params(self):
        return self._v_a_priori_params()


    def _v_a_priori_cov(self):
        return _max_a_posteriori.MaxAPosteriori__v_a_priori_cov(self)

    @property
    def a_priori_cov(self):
        return self._v_a_priori_cov()


    def _v_param_a_priori_uncertainty(self):
        return _max_a_posteriori.MaxAPosteriori__v_param_a_priori_uncertainty(self)

    @property
    def param_a_priori_uncertainty(self):
        return self._v_param_a_priori_uncertainty()


    def _v_parameter_a_priori_diff(self):
        return _max_a_posteriori.MaxAPosteriori__v_parameter_a_priori_diff(self)

    @property
    def parameter_a_priori_diff(self):
        return self._v_parameter_a_priori_diff()


    def _v_cov_weighted_parameter_a_priori_diff(self):
        return _max_a_posteriori.MaxAPosteriori__v_cov_weighted_parameter_a_priori_diff(self)

    @property
    def cov_weighted_parameter_a_priori_diff(self):
        return self._v_cov_weighted_parameter_a_priori_diff()


    def _v_a_priori_cov_chol_inv(self):
        return _max_a_posteriori.MaxAPosteriori__v_a_priori_cov_chol_inv(self)

    @property
    def a_priori_cov_chol_inv(self):
        return self._v_a_priori_cov_chol_inv()


    def _v_weighted_model_measure_diff_aug(self):
        return _max_a_posteriori.MaxAPosteriori__v_weighted_model_measure_diff_aug(self)

    @property
    def weighted_model_measure_diff_aug(self):
        return self._v_weighted_model_measure_diff_aug()


    def _v_a_posteriori_covariance(self):
        return _max_a_posteriori.MaxAPosteriori__v_a_posteriori_covariance(self)

    @property
    def a_posteriori_covariance(self):
        return self._v_a_posteriori_covariance()


    def _v_a_priori_cov_chol(self):
        return _max_a_posteriori.MaxAPosteriori__v_a_priori_cov_chol(self)

    @property
    def a_priori_cov_chol(self):
        return self._v_a_priori_cov_chol()


    def _v_param_a_posteriori_uncertainty(self):
        return _max_a_posteriori.MaxAPosteriori__v_param_a_posteriori_uncertainty(self)

    @property
    def param_a_posteriori_uncertainty(self):
        return self._v_param_a_posteriori_uncertainty()

MaxAPosteriori_swigregister = _max_a_posteriori.MaxAPosteriori_swigregister
MaxAPosteriori_swigregister(MaxAPosteriori)

# This file is compatible with both classic and new-style classes.


