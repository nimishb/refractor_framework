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
            fp, pathname, description = imp.find_module('_l_rad_driver', [dirname(__file__)])
        except ImportError:
            import _l_rad_driver
            return _l_rad_driver
        if fp is not None:
            try:
                _mod = imp.load_module('_l_rad_driver', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _l_rad_driver = swig_import_helper()
    del swig_import_helper
else:
    import _l_rad_driver
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



_l_rad_driver.SHARED_PTR_DISOWN_swigconstant(_l_rad_driver)
SHARED_PTR_DISOWN = _l_rad_driver.SHARED_PTR_DISOWN

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
class LRadDriver(_object):
    """

    This class drives the LRAD code, which gives a polarization correction
    to scalar intensity and jacobians.

    The correction used here is described in the paper "A fast linearized
    pseudo-spherical two orders of scattering model to account for
    polarization in vertically inhomogeneous scattering-absorbing media"
    by Vijah Natrah and Robert Spurr in Journal of Quantitative
    Spectroscopy & Radiative Transfer 107 (2007) 263-293 (a copy of this
    paper can be found in the source tree at 'doc/LRAD Paper.pdf').

    C++ includes: l_rad_driver.h 
    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LRadDriver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LRadDriver, name)
    __repr__ = _swig_repr
    REGULAR = _l_rad_driver.LRadDriver_REGULAR
    ENHANCED = _l_rad_driver.LRadDriver_ENHANCED
    PLANE_PARALLEL = _l_rad_driver.LRadDriver_PLANE_PARALLEL
    DETECT = _l_rad_driver.LRadDriver_DETECT

    def __init__(self, *args):
        """

        FullPhysics::LRadDriver::LRadDriver(int Number_stream, int Number_stokes, int surface_type, bool
        Tms_Correction=false, bool Pure_nadir=false, const PsMode
        ps_mode=DETECT)

        """
        this = _l_rad_driver.new_LRadDriver(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def _v_number_stokes(self):
        """

        virtual int FullPhysics::LRadDriver::number_stokes() const

        """
        return _l_rad_driver.LRadDriver__v_number_stokes(self)


    @property
    def number_stokes(self):
        return self._v_number_stokes()


    def _v_number_stream(self):
        """

        virtual int FullPhysics::LRadDriver::number_stream() const

        """
        return _l_rad_driver.LRadDriver__v_number_stream(self)


    @property
    def number_stream(self):
        return self._v_number_stream()


    def z_matrix(self, pf):
        """

        ArrayAd<double, 2> FullPhysics::LRadDriver::z_matrix(const ArrayAd< double, 3 > &pf) const

        """
        return _l_rad_driver.LRadDriver_z_matrix(self, pf)


    def setup_geometry(self, alt, sza, zen, azm):
        """

        virtual void FullPhysics::LRadDriver::setup_geometry(blitz::Array< double, 1 > alt, double sza, double zen, double azm)
        const
        Setup viewing geometry, should only be called once per instance or if
        the viewing geometry changes. 
        """
        return _l_rad_driver.LRadDriver_setup_geometry(self, alt, sza, zen, azm)


    def setup_surface_params(self, surface_param):
        """

        virtual void FullPhysics::LRadDriver::setup_surface_params(const blitz::Array< double, 1 > &surface_param)
        Set up surface parameters for spectral point. 
        """
        return _l_rad_driver.LRadDriver_setup_surface_params(self, surface_param)


    def setup_optical_inputs(self, od, ssa, pf, zmat):
        """

        virtual void FullPhysics::LRadDriver::setup_optical_inputs(const blitz::Array< double, 1 > &od, const blitz::Array< double, 1 >
        &ssa, const blitz::Array< double, 3 > &pf, const blitz::Array< double,
        2 > &zmat)
        Set up optical depth, single scattering albedo and scattering matrix
        Should be called per spectral point. 
        """
        return _l_rad_driver.LRadDriver_setup_optical_inputs(self, od, ssa, pf, zmat)


    def clear_linear_inputs(self):
        """

        virtual void FullPhysics::LRadDriver::clear_linear_inputs()
        Mark that we are not retrieving weighting functions. 
        """
        return _l_rad_driver.LRadDriver_clear_linear_inputs(self)


    def setup_linear_inputs(self, od, ssa, pf, zmat):
        """

        virtual void FullPhysics::LRadDriver::setup_linear_inputs(const ArrayAd< double, 1 > &od, const ArrayAd< double, 1 > &ssa,
        const ArrayAd< double, 3 > &pf, const ArrayAd< double, 2 > &zmat)
        Set up linearization, weighting functions. 
        """
        return _l_rad_driver.LRadDriver_setup_linear_inputs(self, od, ssa, pf, zmat)


    def calculate_first_order(self):
        """

        virtual void FullPhysics::LRadDriver::calculate_first_order()
        Perform radiative transfer calculation with the values setup by
        setup_optical_inputs and setup_linear_inputs for the first order of
        scattering. 
        """
        return _l_rad_driver.LRadDriver_calculate_first_order(self)


    def calculate_second_order(self):
        """

        virtual void FullPhysics::LRadDriver::calculate_second_order()
        Perform radiative transfer calculation with the values setup by
        setup_optical_inputs and setup_linear_inputs for the second order of
        scattering. 
        """
        return _l_rad_driver.LRadDriver_calculate_second_order(self)


    def stokes(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::LRadDriver::stokes() const
        Retrieve the stokes values calculated. 
        """
        return _l_rad_driver.LRadDriver_stokes(self)


    def atmospheric_jacobian(self):
        """

        virtual blitz::Array<double, 3> FullPhysics::LRadDriver::atmospheric_jacobian() const
        Atmospheric jacobian from last calculation. 
        """
        return _l_rad_driver.LRadDriver_atmospheric_jacobian(self)


    def surface_jacobian(self):
        """

        virtual blitz::Array<double, 2> FullPhysics::LRadDriver::surface_jacobian() const
        Surface jacobian. 
        """
        return _l_rad_driver.LRadDriver_surface_jacobian(self)


    def print_desc(self, Os, Short_form=False):
        """

        virtual void FullPhysics::LRadDriver::print(std::ostream &Os, bool Short_form=false) const

        """
        return _l_rad_driver.LRadDriver_print_desc(self, Os, Short_form)

    __swig_destroy__ = _l_rad_driver.delete_LRadDriver
    __del__ = lambda self: None
LRadDriver_swigregister = _l_rad_driver.LRadDriver_swigregister
LRadDriver_swigregister(LRadDriver)

# This file is compatible with both classic and new-style classes.


