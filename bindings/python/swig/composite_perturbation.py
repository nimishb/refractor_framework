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
            fp, pathname, description = imp.find_module('_composite_perturbation', [dirname(__file__)])
        except ImportError:
            import _composite_perturbation
            return _composite_perturbation
        if fp is not None:
            try:
                _mod = imp.load_module('_composite_perturbation', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _composite_perturbation = swig_import_helper()
    del swig_import_helper
else:
    import _composite_perturbation
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



_composite_perturbation.SHARED_PTR_DISOWN_swigconstant(_composite_perturbation)
SHARED_PTR_DISOWN = _composite_perturbation.SHARED_PTR_DISOWN

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

import full_physics_swig.perturbation
import full_physics_swig.generic_object
class PerturbationBuilder(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PerturbationBuilder, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PerturbationBuilder, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _composite_perturbation.delete_PerturbationBuilder
    __del__ = lambda self: None

    def _v_number_element(self):
        return _composite_perturbation.PerturbationBuilder__v_number_element(self)

    @property
    def number_element(self):
        return self._v_number_element()


    def build_perturbation(self, v, index):
        return _composite_perturbation.PerturbationBuilder_build_perturbation(self, v, index)
PerturbationBuilder_swigregister = _composite_perturbation.PerturbationBuilder_swigregister
PerturbationBuilder_swigregister(PerturbationBuilder)

class CompositePerturbation(full_physics_swig.perturbation.Perturbation):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.perturbation.Perturbation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CompositePerturbation, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.perturbation.Perturbation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CompositePerturbation, name)
    __repr__ = _swig_repr

    def _v_perturbation(self):
        return _composite_perturbation.CompositePerturbation__v_perturbation(self)

    @property
    def perturbation(self):
        return self._v_perturbation()


    def add_builder(self, B):
        return _composite_perturbation.CompositePerturbation_add_builder(self, B)

    def remove_builder(self, B):
        return _composite_perturbation.CompositePerturbation_remove_builder(self, B)

    def __init__(self):
        this = _composite_perturbation.new_CompositePerturbation()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _composite_perturbation.delete_CompositePerturbation
    __del__ = lambda self: None
CompositePerturbation_swigregister = _composite_perturbation.CompositePerturbation_swigregister
CompositePerturbation_swigregister(CompositePerturbation)

# This file is compatible with both classic and new-style classes.


