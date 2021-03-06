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
            fp, pathname, description = imp.find_module('_connor_solver_map', [dirname(__file__)])
        except ImportError:
            import _connor_solver_map
            return _connor_solver_map
        if fp is not None:
            try:
                _mod = imp.load_module('_connor_solver_map', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _connor_solver_map = swig_import_helper()
    del swig_import_helper
else:
    import _connor_solver_map
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



_connor_solver_map.SHARED_PTR_DISOWN_swigconstant(_connor_solver_map)
SHARED_PTR_DISOWN = _connor_solver_map.SHARED_PTR_DISOWN

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

import full_physics_swig.nlls_solver
import full_physics_swig.iterative_solver_der
import full_physics_swig.iterative_solver
import full_physics_swig.generic_object
import full_physics_swig.cost_func_diff
import full_physics_swig.cost_func
import full_physics_swig.problem_state
import full_physics_swig.nlls_problem_state
import full_physics_swig.model_measure
import full_physics_swig.model_state
class ConnorSolverMAP(full_physics_swig.nlls_solver.NLLSSolver):
    """

    This solves a nonlinear least squares problem using Levenberg-
    Marquardt.

    This is the code that was originally written by Brian Connor.

    We've rewritten the code in C++. This in entirely a matter a
    convenience, the wrapper code for calling the older Fortran code was
    bigger than the routine we were calling, so it made more sense just to
    duplicate the algorithm. We can revisit this if there is a reason to
    move this back to Fortran.

    This solver is able to handle rank deficient Jacobians (e.g., we have
    parameters that are ignored).

    At each iteration, this solves

    \\[ \\left((1+\\gamma) \\mathbf{S}_a^{-1} + \\mathbf{K}_i^T
    \\mathbf{S}_{\\epsilon}^{-1} \\mathbf{K}_i\\right)
    d\\mathbf{x}_{i+1} = \\left[\\mathbf{K}_i^T
    \\mathbf{S}_{\\epsilon}^{-1} \\left(\\mathbf{y} -
    \\mathbf{F}(\\mathbf{x}_i)\\right) +
    \\mathbf{S}_a^{-1}(\\mathbf{x}_a - \\mathbf{x}_i)\\right]
    \\]

    This class has a "do_inversion" private member that is a bit
    difficult to test. As an aid to testing, the constructor takes a
    optional file name. If that name is passed, then we dump the state of
    this class in the first iteration of the solver to that file. We can
    then rerun the do_inversion by passing this file name to
    "test_do_inversion", which sets up the state, calls, do_inversion,
    and returns the results. This is entirely for use in unit testing, you
    wouldn't call this in normal operation.

    This class is an Observable, any registered Observer will get notified
    after each iteration of the solver. This can be used to do things like
    add iteration output or extra logging.

    C++ includes: connor_solver_map.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.nlls_solver.NLLSSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ConnorSolverMAP, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.nlls_solver.NLLSSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ConnorSolverMAP, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """

        FullPhysics::ConnorSolverMAP::ConnorSolverMAP(int max_cost_function_calls, double dx_tol_abs, double dx_tol_rel,
        double g_tol_abs, const boost::shared_ptr< NLLSMaxAPosteriori >
        &NLLS_MAP, const boost::shared_ptr< ConvergenceCheck >
        &Convergence_check, bool vrbs=false, double Gamma_initial=0.0, const
        std::string &Fname_test_data="")
        and optionally an initial value for gamma.

        See the comments above this class for the "save_test_data" argument.

        """
        this = _connor_solver_map.new_ConnorSolverMAP(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _connor_solver_map.delete_ConnorSolverMAP
    __del__ = lambda self: None

    def solve(self):
        """

        void FullPhysics::ConnorSolverMAP::solve()

        """
        return _connor_solver_map.ConnorSolverMAP_solve(self)


    def _v_convergence_check(self):
        """

        boost::shared_ptr<ConvergenceCheck> FullPhysics::ConnorSolverMAP::convergence_check() const
        The convergence check object. 
        """
        return _connor_solver_map.ConnorSolverMAP__v_convergence_check(self)


    @property
    def convergence_check(self):
        return self._v_convergence_check()


    def _v_gamma_last_step(self):
        """

        double FullPhysics::ConnorSolverMAP::gamma_last_step() const
        Levenberg-Marquardt parameter for last step we processed. 
        """
        return _connor_solver_map.ConnorSolverMAP__v_gamma_last_step(self)


    @property
    def gamma_last_step(self):
        return self._v_gamma_last_step()


    def _v_number_iteration(self):
        """

        int FullPhysics::ConnorSolverMAP::number_iteration() const
        Number of iterations for the last problem solved. 
        """
        return _connor_solver_map.ConnorSolverMAP__v_number_iteration(self)


    @property
    def number_iteration(self):
        return self._v_number_iteration()


    def _v_number_divergent(self):
        """

        int FullPhysics::ConnorSolverMAP::number_divergent() const
        Number of divergent steps for the last problem solved. 
        """
        return _connor_solver_map.ConnorSolverMAP__v_number_divergent(self)


    @property
    def number_divergent(self):
        return self._v_number_divergent()


    def _v_outcome_flag(self):
        """

        int FullPhysics::ConnorSolverMAP::outcome_flag() const
        Outcome flag. This is an integer version of FitStatistic::OUTCOME. 
        """
        return _connor_solver_map.ConnorSolverMAP__v_outcome_flag(self)


    @property
    def outcome_flag(self):
        return self._v_outcome_flag()


    def _v_x_update(self):
        """

        blitz::Array<double, 1> FullPhysics::ConnorSolverMAP::x_update() const
        Return the a priori of the last problem solved. 
        """
        return _connor_solver_map.ConnorSolverMAP__v_x_update(self)


    @property
    def x_update(self):
        return self._v_x_update()


    def _v_fit_statistic(self):
        """

        virtual FitStatistic FullPhysics::ConnorSolverMAP::fit_statistic() const
        Return fit results for solution to last problem solved. 
        """
        return _connor_solver_map.ConnorSolverMAP__v_fit_statistic(self)


    @property
    def fit_statistic(self):
        return self._v_fit_statistic()

ConnorSolverMAP_swigregister = _connor_solver_map.ConnorSolverMAP_swigregister
ConnorSolverMAP_swigregister(ConnorSolverMAP)

# This file is compatible with both classic and new-style classes.


