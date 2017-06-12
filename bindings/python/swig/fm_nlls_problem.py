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
            fp, pathname, description = imp.find_module('_fm_nlls_problem', [dirname(__file__)])
        except ImportError:
            import _fm_nlls_problem
            return _fm_nlls_problem
        if fp is not None:
            try:
                _mod = imp.load_module('_fm_nlls_problem', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _fm_nlls_problem = swig_import_helper()
    del swig_import_helper
else:
    import _fm_nlls_problem
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



_fm_nlls_problem.SHARED_PTR_DISOWN_swigconstant(_fm_nlls_problem)
SHARED_PTR_DISOWN = _fm_nlls_problem.SHARED_PTR_DISOWN

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
class FmNLLSProblem(_object):
    """

    This is the forward model cost function, rewritten to match the
    standard format used in nonlinear least squares solvers.

    C++ includes: fm_nlls_problem.h 
    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FmNLLSProblem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FmNLLSProblem, name)
    __repr__ = _swig_repr

    def __init__(self, Fm, Rad, Rad_uncer, X_apriori, Apriori_cov):
        """

        FullPhysics::FmNLLSProblem::FmNLLSProblem(const boost::shared_ptr< ForwardModel > &Fm, const blitz::Array<
        double, 1 > &Rad, const blitz::Array< double, 1 > &Rad_uncer, const
        blitz::Array< double, 1 > X_apriori, const blitz::Array< double, 2 >
        Apriori_cov)

        """
        this = _fm_nlls_problem.new_FmNLLSProblem(Fm, Rad, Rad_uncer, X_apriori, Apriori_cov)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _fm_nlls_problem.delete_FmNLLSProblem
    __del__ = lambda self: None

    def _v_residual_size(self):
        """

        virtual int FullPhysics::FmNLLSProblem::residual_size() const

        """
        return _fm_nlls_problem.FmNLLSProblem__v_residual_size(self)


    @property
    def residual_size(self):
        return self._v_residual_size()


    def _v_parameter_size(self):
        return _fm_nlls_problem.FmNLLSProblem__v_parameter_size(self)

    @property
    def parameter_size(self):
        return self._v_parameter_size()


    def _v_residual(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::FmNLLSProblem::residual()

        """
        return _fm_nlls_problem.FmNLLSProblem__v_residual(self)


    @property
    def residual(self):
        return self._v_residual()


    def _v_jacobian(self):
        """

        virtual blitz::Array<double, 2> FullPhysics::FmNLLSProblem::jacobian()

        """
        return _fm_nlls_problem.FmNLLSProblem__v_jacobian(self)


    @property
    def jacobian(self):
        return self._v_jacobian()

FmNLLSProblem_swigregister = _fm_nlls_problem.FmNLLSProblem_swigregister
FmNLLSProblem_swigregister(FmNLLSProblem)

# This file is compatible with both classic and new-style classes.


