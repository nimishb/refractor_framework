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
            fp, pathname, description = imp.find_module('_level_1b_oco', [dirname(__file__)])
        except ImportError:
            import _level_1b_oco
            return _level_1b_oco
        if fp is not None:
            try:
                _mod = imp.load_module('_level_1b_oco', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _level_1b_oco = swig_import_helper()
    del swig_import_helper
else:
    import _level_1b_oco
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



_level_1b_oco.SHARED_PTR_DISOWN_swigconstant(_level_1b_oco)
SHARED_PTR_DISOWN = _level_1b_oco.SHARED_PTR_DISOWN

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

import full_physics_swig.level_1b_hdf
import full_physics_swig.level_1b
import full_physics_swig.generic_object
class Level1bOco(full_physics_swig.level_1b_hdf.Level1bHdf):
    """

    This reads a Level 1B file that is in the HDF format.

    C++ includes: level_1b_oco.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.level_1b_hdf.Level1bHdf]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Level1bOco, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.level_1b_hdf.Level1bHdf]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Level1bOco, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def radiance(self, Spec_index):
        return _level_1b_oco.Level1bOco_radiance(self, Spec_index)

    def has_spike_eof(self, Spec_index):
        """

        bool FullPhysics::Level1bOco::has_spike_eof(int Spec_index) const
        True if we have the SpikeEOF data available. 
        """
        return _level_1b_oco.Level1bOco_has_spike_eof(self, Spec_index)


    def spike_eof(self, Spec_index):
        """

        blitz::Array<double, 1> FullPhysics::Level1bOco::spike_eof(int Spec_index) const

        """
        return _level_1b_oco.Level1bOco_spike_eof(self, Spec_index)


    def _v_has_solar_relative_velocity(self):
        """

        bool FullPhysics::Level1bOco::has_solar_relative_velocity() const
        True if the Level 1 data has the solar relative velocity.

        Older versions of OCO and also the simulated data do not have this
        field, so this returns false. 
        """
        return _level_1b_oco.Level1bOco__v_has_solar_relative_velocity(self)


    @property
    def has_solar_relative_velocity(self):
        return self._v_has_solar_relative_velocity()


    def _v_land_fraction(self):
        """

        double FullPhysics::Level1bOco::land_fraction() const
        Return land fraction, as a percentage going from 0 to 100. 
        """
        return _level_1b_oco.Level1bOco__v_land_fraction(self)


    @property
    def land_fraction(self):
        return self._v_land_fraction()


    def _v_solar_distance(self):
        """

        DoubleWithUnit FullPhysics::Level1bOco::solar_distance() const
        Distance from sounding location to the sun. 
        """
        return _level_1b_oco.Level1bOco__v_solar_distance(self)


    @property
    def solar_distance(self):
        return self._v_solar_distance()


    def _v_solar_velocity(self):
        """

        DoubleWithUnit FullPhysics::Level1bOco::solar_velocity() const
        Velocity of sun along the sounding location/sun vector.

        Note this includes the rotation of the earth along with the earth/sun
        velocity, so we can take this directly to calculate the doppler shift.

        """
        return _level_1b_oco.Level1bOco__v_solar_velocity(self)


    @property
    def solar_velocity(self):
        return self._v_solar_velocity()


    def _v_acquisition_mode(self):
        """

        const std::string& FullPhysics::Level1bOco::acquisition_mode() const
        The acquisition mode.

        The data we process will be "Nadir", "Glint" or "Target". 
        """
        return _level_1b_oco.Level1bOco__v_acquisition_mode(self)


    @property
    def acquisition_mode(self):
        return self._v_acquisition_mode()

    __swig_destroy__ = _level_1b_oco.delete_Level1bOco
    __del__ = lambda self: None
Level1bOco_swigregister = _level_1b_oco.Level1bOco_swigregister
Level1bOco_swigregister(Level1bOco)

# This file is compatible with both classic and new-style classes.


