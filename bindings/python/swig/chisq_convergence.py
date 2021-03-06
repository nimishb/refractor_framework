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
            fp, pathname, description = imp.find_module('_chisq_convergence', [dirname(__file__)])
        except ImportError:
            import _chisq_convergence
            return _chisq_convergence
        if fp is not None:
            try:
                _mod = imp.load_module('_chisq_convergence', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _chisq_convergence = swig_import_helper()
    del swig_import_helper
else:
    import _chisq_convergence
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



_chisq_convergence.SHARED_PTR_DISOWN_swigconstant(_chisq_convergence)
SHARED_PTR_DISOWN = _chisq_convergence.SHARED_PTR_DISOWN

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

import full_physics_swig.convergence_check
import full_physics_swig.generic_object
class ChisqConvergence(full_physics_swig.convergence_check.ConvergenceCheck):
    """

    This class tests for convergence of a Levenberg-Marquardt solver.

    This is a simple criteria based just on the chisq. If the chisq is
    below a given threshold and has changed less than Stopping_criteria,
    then we are done. If the chisq is larger than the chisq than the last
    iteration, we say the step has diverged and increase lambda by a boost
    factor. Otherwise, we reduce lambda by a drop factor.

    C++ includes: chisq_convergence.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.convergence_check.ConvergenceCheck]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ChisqConvergence, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.convergence_check.ConvergenceCheck]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ChisqConvergence, name)
    __repr__ = _swig_repr

    def __init__(self, stopping_criteria=0.001, dropf=0.1, boostf=10, min_chisq=0.01, max_iteration=50):
        """

        FullPhysics::ChisqConvergence::ChisqConvergence(double stopping_criteria=0.001, double dropf=0.1, double boostf=10,
        double min_chisq=0.01, int max_iteration=50)

        """
        this = _chisq_convergence.new_ChisqConvergence(stopping_criteria, dropf, boostf, min_chisq, max_iteration)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def convergence_check(self, fit_stat_last, fit_stat, has_converged, convergence_failed, gamma, step_diverged):
        """

        virtual void FullPhysics::ChisqConvergence::convergence_check(const FitStatistic &fit_stat_last, FitStatistic &fit_stat, bool
        &has_converged, bool &convergence_failed, double &gamma, bool
        &step_diverged)

        """
        return _chisq_convergence.ChisqConvergence_convergence_check(self, fit_stat_last, fit_stat, has_converged, convergence_failed, gamma, step_diverged)


    def evaluate_quality(self, fit_stat, Residual, Residual_cov_diag):
        """

        virtual void FullPhysics::ChisqConvergence::evaluate_quality(FitStatistic &fit_stat, const blitz::Array< double, 1 > &Residual,
        const blitz::Array< double, 1 > &Residual_cov_diag)

        """
        return _chisq_convergence.ChisqConvergence_evaluate_quality(self, fit_stat, Residual, Residual_cov_diag)

    __swig_destroy__ = _chisq_convergence.delete_ChisqConvergence
    __del__ = lambda self: None
ChisqConvergence_swigregister = _chisq_convergence.ChisqConvergence_swigregister
ChisqConvergence_swigregister(ChisqConvergence)

# This file is compatible with both classic and new-style classes.


