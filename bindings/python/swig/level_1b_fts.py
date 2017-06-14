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
            fp, pathname, description = imp.find_module('_level_1b_fts', [dirname(__file__)])
        except ImportError:
            import _level_1b_fts
            return _level_1b_fts
        if fp is not None:
            try:
                _mod = imp.load_module('_level_1b_fts', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _level_1b_fts = swig_import_helper()
    del swig_import_helper
else:
    import _level_1b_fts
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



_level_1b_fts.SHARED_PTR_DISOWN_swigconstant(_level_1b_fts)
SHARED_PTR_DISOWN = _level_1b_fts.SHARED_PTR_DISOWN

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

import full_physics_swig.level_1b
import full_physics_swig.generic_object
class Level1bFts(full_physics_swig.level_1b.Level1b):
    """

    This is the Level 1B data for a FTS.

    C++ includes: level_1b_fts.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.level_1b.Level1b]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Level1bFts, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.level_1b.Level1b]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Level1bFts, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def latitude(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1bFts::latitude(int i) const

        """
        return _level_1b_fts.Level1bFts_latitude(self, i)


    def longitude(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1bFts::longitude(int i) const

        """
        return _level_1b_fts.Level1bFts_longitude(self, i)


    def sounding_zenith(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1bFts::sounding_zenith(int i) const

        """
        return _level_1b_fts.Level1bFts_sounding_zenith(self, i)


    def sounding_azimuth(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1bFts::sounding_azimuth(int i) const

        """
        return _level_1b_fts.Level1bFts_sounding_azimuth(self, i)


    def stokes_coefficient(self, i):
        """

        virtual blitz::Array<double, 1> FullPhysics::Level1bFts::stokes_coefficient(int i) const

        """
        return _level_1b_fts.Level1bFts_stokes_coefficient(self, i)


    def solar_zenith(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1bFts::solar_zenith(int i) const

        """
        return _level_1b_fts.Level1bFts_solar_zenith(self, i)


    def solar_azimuth(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1bFts::solar_azimuth(int i) const

        """
        return _level_1b_fts.Level1bFts_solar_azimuth(self, i)


    def altitude(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1bFts::altitude(int i) const

        """
        return _level_1b_fts.Level1bFts_altitude(self, i)


    def relative_velocity(self, i):
        """

        virtual DoubleWithUnit FullPhysics::Level1bFts::relative_velocity(int Spec_index) const

        """
        return _level_1b_fts.Level1bFts_relative_velocity(self, i)


    def spectral_coefficient(self, Spec_index):
        """

        virtual ArrayWithUnit<double, 1> FullPhysics::Level1bFts::spectral_coefficient(int Spec_index) const

        """
        return _level_1b_fts.Level1bFts_spectral_coefficient(self, Spec_index)


    def time(self, Spec_index):
        """

        virtual Time FullPhysics::Level1bFts::time(int Spec_index) const

        """
        return _level_1b_fts.Level1bFts_time(self, Spec_index)


    def radiance(self, Spec_index):
        """

        virtual SpectralRange FullPhysics::Level1bFts::radiance(int Spec_index) const

        """
        return _level_1b_fts.Level1bFts_radiance(self, Spec_index)

    __swig_destroy__ = _level_1b_fts.delete_Level1bFts
    __del__ = lambda self: None
Level1bFts_swigregister = _level_1b_fts.Level1bFts_swigregister
Level1bFts_swigregister(Level1bFts)

# This file is compatible with both classic and new-style classes.


