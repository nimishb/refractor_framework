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
            fp, pathname, description = imp.find_module('_ils_table', [dirname(__file__)])
        except ImportError:
            import _ils_table
            return _ils_table
        if fp is not None:
            try:
                _mod = imp.load_module('_ils_table', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ils_table = swig_import_helper()
    del swig_import_helper
else:
    import _ils_table
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



_ils_table.SHARED_PTR_DISOWN_swigconstant(_ils_table)
SHARED_PTR_DISOWN = _ils_table.SHARED_PTR_DISOWN

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

import full_physics_swig.ils_function
import full_physics_swig.generic_object
class IlsTableLinear(full_physics_swig.ils_function.IlsFunction):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.ils_function.IlsFunction]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IlsTableLinear, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.ils_function.IlsFunction]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, IlsTableLinear, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ils_table.new_IlsTableLinear(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def ils(self, wn_center, wn, OUTPUT):
        return _ils_table.IlsTableLinear_ils(self, wn_center, wn, OUTPUT)

    def _v_wavenumber(self):
        return _ils_table.IlsTableLinear__v_wavenumber(self)

    @property
    def wavenumber(self):
        return self._v_wavenumber()


    def _v_delta_lambda(self):
        return _ils_table.IlsTableLinear__v_delta_lambda(self)

    @property
    def delta_lambda(self):
        return self._v_delta_lambda()


    def _v_response(self):
        return _ils_table.IlsTableLinear__v_response(self)

    @property
    def response(self):
        return self._v_response()


    def create_delta_lambda_to_response(self, Wavenumber, Delta_lambda, Response):
        return _ils_table.IlsTableLinear_create_delta_lambda_to_response(self, Wavenumber, Delta_lambda, Response)
    __swig_destroy__ = _ils_table.delete_IlsTableLinear
    __del__ = lambda self: None
IlsTableLinear_swigregister = _ils_table.IlsTableLinear_swigregister
IlsTableLinear_swigregister(IlsTableLinear)

class IlsTableLog(full_physics_swig.ils_function.IlsFunction):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.ils_function.IlsFunction]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IlsTableLog, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.ils_function.IlsFunction]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, IlsTableLog, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ils_table.new_IlsTableLog(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def ils(self, wn_center, wn, OUTPUT):
        return _ils_table.IlsTableLog_ils(self, wn_center, wn, OUTPUT)

    def _v_wavenumber(self):
        return _ils_table.IlsTableLog__v_wavenumber(self)

    @property
    def wavenumber(self):
        return self._v_wavenumber()


    def _v_delta_lambda(self):
        return _ils_table.IlsTableLog__v_delta_lambda(self)

    @property
    def delta_lambda(self):
        return self._v_delta_lambda()


    def _v_response(self):
        return _ils_table.IlsTableLog__v_response(self)

    @property
    def response(self):
        return self._v_response()


    def create_delta_lambda_to_response(self, Wavenumber, Delta_lambda, Response):
        return _ils_table.IlsTableLog_create_delta_lambda_to_response(self, Wavenumber, Delta_lambda, Response)
    __swig_destroy__ = _ils_table.delete_IlsTableLog
    __del__ = lambda self: None
IlsTableLog_swigregister = _ils_table.IlsTableLog_swigregister
IlsTableLog_swigregister(IlsTableLog)

# This file is compatible with both classic and new-style classes.


