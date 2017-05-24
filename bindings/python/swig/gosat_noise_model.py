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
            fp, pathname, description = imp.find_module('_gosat_noise_model', [dirname(__file__)])
        except ImportError:
            import _gosat_noise_model
            return _gosat_noise_model
        if fp is not None:
            try:
                _mod = imp.load_module('_gosat_noise_model', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gosat_noise_model = swig_import_helper()
    del swig_import_helper
else:
    import _gosat_noise_model
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



_gosat_noise_model.SHARED_PTR_DISOWN_swigconstant(_gosat_noise_model)
SHARED_PTR_DISOWN = _gosat_noise_model.SHARED_PTR_DISOWN

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

import full_physics_swig.noise_model
import full_physics_swig.generic_object
import full_physics_swig.hdf_sounding_id
import full_physics_swig.state_vector
class GosatNoiseModel(full_physics_swig.noise_model.NoiseModel):
    __swig_setmethods__ = {}
    for _s in [full_physics_swig.noise_model.NoiseModel]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GosatNoiseModel, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.noise_model.NoiseModel]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GosatNoiseModel, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _gosat_noise_model.new_GosatNoiseModel(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def uncertainty(self, Spec_index, Radiance):
        return _gosat_noise_model.GosatNoiseModel_uncertainty(self, Spec_index, Radiance)
    __swig_destroy__ = _gosat_noise_model.delete_GosatNoiseModel
    __del__ = lambda self: None
GosatNoiseModel_swigregister = _gosat_noise_model.GosatNoiseModel_swigregister
GosatNoiseModel_swigregister(GosatNoiseModel)

# This file is compatible with both classic and new-style classes.


