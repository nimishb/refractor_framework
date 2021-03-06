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
            fp, pathname, description = imp.find_module('_gas_absorption', [dirname(__file__)])
        except ImportError:
            import _gas_absorption
            return _gas_absorption
        if fp is not None:
            try:
                _mod = imp.load_module('_gas_absorption', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gas_absorption = swig_import_helper()
    del swig_import_helper
else:
    import _gas_absorption
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


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _gas_absorption.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _gas_absorption.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _gas_absorption.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _gas_absorption.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _gas_absorption.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _gas_absorption.SwigPyIterator_equal(self, x)

    def copy(self):
        return _gas_absorption.SwigPyIterator_copy(self)

    def next(self):
        return _gas_absorption.SwigPyIterator_next(self)

    def __next__(self):
        return _gas_absorption.SwigPyIterator___next__(self)

    def previous(self):
        return _gas_absorption.SwigPyIterator_previous(self)

    def advance(self, n):
        return _gas_absorption.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _gas_absorption.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _gas_absorption.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _gas_absorption.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _gas_absorption.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _gas_absorption.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _gas_absorption.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _gas_absorption.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_gas_absorption.SHARED_PTR_DISOWN_swigconstant(_gas_absorption)
SHARED_PTR_DISOWN = _gas_absorption.SHARED_PTR_DISOWN

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
class GasAbsorption(full_physics_swig.generic_object.GenericObject):
    """

    This class determine the gaseous absorption coefficient for a given
    wave number, temperature and pressure.

    C++ includes: gas_absorption.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GasAbsorption, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GasAbsorption, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _gas_absorption.delete_GasAbsorption
    __del__ = lambda self: None

    def __str__(self):
        return _gas_absorption.GasAbsorption___str__(self)

    def have_data(self, wn):
        """

        virtual bool FullPhysics::GasAbsorption::have_data(double wn) const =0
        Return true if we have data for the given wave number.

        A particular gas might not have absorption coefficients for all
        spectral bands, e.g., ABSCO tables. 
        """
        return _gas_absorption.GasAbsorption_have_data(self, wn)


    def _v_broadener_name(self):
        """

        virtual std::string FullPhysics::GasAbsorption::broadener_name() const =0
        For some tables, we might have a broadener (e.g., "h2o").

        This returns the name of the broadener, if any. 
        """
        return _gas_absorption.GasAbsorption__v_broadener_name(self)


    @property
    def broadener_name(self):
        return self._v_broadener_name()


    def absorption_cross_section(self, *args):
        """

        virtual AutoDerivativeWithUnit<double> FullPhysics::GasAbsorption::absorption_cross_section(double Wn, const DoubleWithUnit &Press, const AutoDerivativeWithUnit<
        double > &Temp, const AutoDerivativeWithUnit< double > &Broadener_vmr)
        const =0
        This interpolates the ABSCO data to give absorption cross section for
        a given pressure, temperature, and broadener VMR.

        Parameters:
        -----------

        Wn:  wave number

        Press:  Pressure

        Temp:  Temperature

        Broadener_vmr:  Broadner VMR (e.g., H2O VMR). Not all tables will make
        use of this information.

        Absorption cross section in cm^2 / molecule 
        """
        return _gas_absorption.GasAbsorption_absorption_cross_section(self, *args)

GasAbsorption_swigregister = _gas_absorption.GasAbsorption_swigregister
GasAbsorption_swigregister(GasAbsorption)

class vector_gas_absorption(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector_gas_absorption, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector_gas_absorption, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _gas_absorption.vector_gas_absorption_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _gas_absorption.vector_gas_absorption___nonzero__(self)

    def __bool__(self):
        return _gas_absorption.vector_gas_absorption___bool__(self)

    def __len__(self):
        return _gas_absorption.vector_gas_absorption___len__(self)

    def __getslice__(self, i, j):
        return _gas_absorption.vector_gas_absorption___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _gas_absorption.vector_gas_absorption___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _gas_absorption.vector_gas_absorption___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _gas_absorption.vector_gas_absorption___delitem__(self, *args)

    def __getitem__(self, *args):
        return _gas_absorption.vector_gas_absorption___getitem__(self, *args)

    def __setitem__(self, *args):
        return _gas_absorption.vector_gas_absorption___setitem__(self, *args)

    def pop(self):
        return _gas_absorption.vector_gas_absorption_pop(self)

    def append(self, x):
        return _gas_absorption.vector_gas_absorption_append(self, x)

    def empty(self):
        return _gas_absorption.vector_gas_absorption_empty(self)

    def size(self):
        return _gas_absorption.vector_gas_absorption_size(self)

    def swap(self, v):
        return _gas_absorption.vector_gas_absorption_swap(self, v)

    def begin(self):
        return _gas_absorption.vector_gas_absorption_begin(self)

    def end(self):
        return _gas_absorption.vector_gas_absorption_end(self)

    def rbegin(self):
        return _gas_absorption.vector_gas_absorption_rbegin(self)

    def rend(self):
        return _gas_absorption.vector_gas_absorption_rend(self)

    def clear(self):
        return _gas_absorption.vector_gas_absorption_clear(self)

    def get_allocator(self):
        return _gas_absorption.vector_gas_absorption_get_allocator(self)

    def pop_back(self):
        return _gas_absorption.vector_gas_absorption_pop_back(self)

    def erase(self, *args):
        return _gas_absorption.vector_gas_absorption_erase(self, *args)

    def __init__(self, *args):
        this = _gas_absorption.new_vector_gas_absorption(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _gas_absorption.vector_gas_absorption_push_back(self, x)

    def front(self):
        return _gas_absorption.vector_gas_absorption_front(self)

    def back(self):
        return _gas_absorption.vector_gas_absorption_back(self)

    def assign(self, n, x):
        return _gas_absorption.vector_gas_absorption_assign(self, n, x)

    def resize(self, *args):
        return _gas_absorption.vector_gas_absorption_resize(self, *args)

    def insert(self, *args):
        return _gas_absorption.vector_gas_absorption_insert(self, *args)

    def reserve(self, n):
        return _gas_absorption.vector_gas_absorption_reserve(self, n)

    def capacity(self):
        return _gas_absorption.vector_gas_absorption_capacity(self)
    __swig_destroy__ = _gas_absorption.delete_vector_gas_absorption
    __del__ = lambda self: None
vector_gas_absorption_swigregister = _gas_absorption.vector_gas_absorption_swigregister
vector_gas_absorption_swigregister(vector_gas_absorption)

# This file is compatible with both classic and new-style classes.


