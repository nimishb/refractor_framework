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
            fp, pathname, description = imp.find_module('_error_analysis', [dirname(__file__)])
        except ImportError:
            import _error_analysis
            return _error_analysis
        if fp is not None:
            try:
                _mod = imp.load_module('_error_analysis', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _error_analysis = swig_import_helper()
    del swig_import_helper
else:
    import _error_analysis
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



_error_analysis.SHARED_PTR_DISOWN_swigconstant(_error_analysis)
SHARED_PTR_DISOWN = _error_analysis.SHARED_PTR_DISOWN

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
import full_physics_swig.observer
import full_physics_swig.model_measure
import full_physics_swig.model_state
import full_physics_swig.problem_state
import full_physics_swig.rt_atmosphere
import full_physics_swig.state_vector
import full_physics_swig.aerosol
class ErrorAnalysis(full_physics_swig.generic_object.GenericObject):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ErrorAnalysis, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ErrorAnalysis, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _error_analysis.new_ErrorAnalysis(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def residual_sum_sq(self, Band):
        return _error_analysis.ErrorAnalysis_residual_sum_sq(self, Band)

    def residual_mean_sq(self, Band):
        return _error_analysis.ErrorAnalysis_residual_mean_sq(self, Band)

    def reduced_chisq(self, Band):
        return _error_analysis.ErrorAnalysis_reduced_chisq(self, Band)

    def relative_residual_mean_sq(self, Band):
        return _error_analysis.ErrorAnalysis_relative_residual_mean_sq(self, Band)

    def signal(self, band):
        return _error_analysis.ErrorAnalysis_signal(self, band)

    def noise(self, band):
        return _error_analysis.ErrorAnalysis_noise(self, band)

    def chisq_measure_norm(self, Residual, Residual_cov_diag):
        return _error_analysis.ErrorAnalysis_chisq_measure_norm(self, Residual, Residual_cov_diag)

    def _v_xco2_measurement_error(self):
        return _error_analysis.ErrorAnalysis__v_xco2_measurement_error(self)

    @property
    def xco2_measurement_error(self):
        return self._v_xco2_measurement_error()


    def _v_xco2_smoothing_error(self):
        return _error_analysis.ErrorAnalysis__v_xco2_smoothing_error(self)

    @property
    def xco2_smoothing_error(self):
        return self._v_xco2_smoothing_error()


    def _v_xco2_uncertainty(self):
        return _error_analysis.ErrorAnalysis__v_xco2_uncertainty(self)

    @property
    def xco2_uncertainty(self):
        return self._v_xco2_uncertainty()


    def _v_xco2_interference_error(self):
        return _error_analysis.ErrorAnalysis__v_xco2_interference_error(self)

    @property
    def xco2_interference_error(self):
        return self._v_xco2_interference_error()


    def _v_xco2_gain_vector(self):
        return _error_analysis.ErrorAnalysis__v_xco2_gain_vector(self)

    @property
    def xco2_gain_vector(self):
        return self._v_xco2_gain_vector()


    def _v_xco2_uncert_noise(self):
        return _error_analysis.ErrorAnalysis__v_xco2_uncert_noise(self)

    @property
    def xco2_uncert_noise(self):
        return self._v_xco2_uncert_noise()


    def _v_xco2_uncert_smooth(self):
        return _error_analysis.ErrorAnalysis__v_xco2_uncert_smooth(self)

    @property
    def xco2_uncert_smooth(self):
        return self._v_xco2_uncert_smooth()


    def _v_xco2_uncert_interf(self):
        return _error_analysis.ErrorAnalysis__v_xco2_uncert_interf(self)

    @property
    def xco2_uncert_interf(self):
        return self._v_xco2_uncert_interf()


    def _v_degrees_of_freedom_full_vector(self):
        return _error_analysis.ErrorAnalysis__v_degrees_of_freedom_full_vector(self)

    @property
    def degrees_of_freedom_full_vector(self):
        return self._v_degrees_of_freedom_full_vector()


    def _v_degrees_of_freedom_xco2(self):
        return _error_analysis.ErrorAnalysis__v_degrees_of_freedom_xco2(self)

    @property
    def degrees_of_freedom_xco2(self):
        return self._v_degrees_of_freedom_xco2()


    def _v_xco2_avg_kernel(self):
        return _error_analysis.ErrorAnalysis__v_xco2_avg_kernel(self)

    @property
    def xco2_avg_kernel(self):
        return self._v_xco2_avg_kernel()


    def _v_co2_averaging_kernel(self):
        return _error_analysis.ErrorAnalysis__v_co2_averaging_kernel(self)

    @property
    def co2_averaging_kernel(self):
        return self._v_co2_averaging_kernel()


    def _v_xco2_avg_kernel_full(self):
        return _error_analysis.ErrorAnalysis__v_xco2_avg_kernel_full(self)

    @property
    def xco2_avg_kernel_full(self):
        return self._v_xco2_avg_kernel_full()


    def _v_xco2_avg_kernel_norm(self):
        return _error_analysis.ErrorAnalysis__v_xco2_avg_kernel_norm(self)

    @property
    def xco2_avg_kernel_norm(self):
        return self._v_xco2_avg_kernel_norm()


    def _v_xco2_correlation_interf(self):
        return _error_analysis.ErrorAnalysis__v_xco2_correlation_interf(self)

    @property
    def xco2_correlation_interf(self):
        return self._v_xco2_correlation_interf()


    def _v_interference_smoothing_uncertainty(self):
        return _error_analysis.ErrorAnalysis__v_interference_smoothing_uncertainty(self)

    @property
    def interference_smoothing_uncertainty(self):
        return self._v_interference_smoothing_uncertainty()

    __swig_destroy__ = _error_analysis.delete_ErrorAnalysis
    __del__ = lambda self: None
ErrorAnalysis_swigregister = _error_analysis.ErrorAnalysis_swigregister
ErrorAnalysis_swigregister(ErrorAnalysis)

# This file is compatible with both classic and new-style classes.


