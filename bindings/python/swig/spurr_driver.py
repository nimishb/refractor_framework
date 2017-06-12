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
            fp, pathname, description = imp.find_module('_spurr_driver', [dirname(__file__)])
        except ImportError:
            import _spurr_driver
            return _spurr_driver
        if fp is not None:
            try:
                _mod = imp.load_module('_spurr_driver', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _spurr_driver = swig_import_helper()
    del swig_import_helper
else:
    import _spurr_driver
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



_spurr_driver.SHARED_PTR_DISOWN_swigconstant(_spurr_driver)
SHARED_PTR_DISOWN = _spurr_driver.SHARED_PTR_DISOWN

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
class SpurrBrdfDriver(_object):
    """

    Abstracts away set up of BRDF kernel interfaces.

    The arrays needing setting for the initialization steps are done
    through methods because it is often the case that boolean arrays
    passed to Fortran will need to be copied and can not be set directly
    into the memory read by Fortran. Since this step is only done once
    this is probably acceptable.

    For the setup of the values for the surface to be calculated, three
    double arrays are exposed so that this interface might copy values
    into the memory used by Fortran once instead of twice if method calls
    were used to do the setting.

    The public inteface only exposes the two main initialization and setup
    routines. However, most of the protected interface needs to be
    implemented by implementing classes. These are mostly methods to link
    a parameter to the location it is stored by the specific incarnation
    of Spurr BRDF code.

    C++ includes: spurr_driver.h 
    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpurrBrdfDriver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SpurrBrdfDriver, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def initialize_brdf_inputs(self, surface_type):
        """

        virtual void FullPhysics::SpurrBrdfDriver::initialize_brdf_inputs(int surface_type)

        """
        return _spurr_driver.SpurrBrdfDriver_initialize_brdf_inputs(self, surface_type)


    def setup_geometry(self, sza, azm, zen):
        """

        virtual void FullPhysics::SpurrBrdfDriver::setup_geometry(double sza, double azm, double zen) const =0

        """
        return _spurr_driver.SpurrBrdfDriver_setup_geometry(self, sza, azm, zen)


    def setup_brdf_inputs(self, surface_type, surface_parameters):
        """

        virtual ArrayAd<double, 1> FullPhysics::SpurrBrdfDriver::setup_brdf_inputs(int surface_type, const ArrayAd< double, 1 > &surface_parameters)
        const

        """
        return _spurr_driver.SpurrBrdfDriver_setup_brdf_inputs(self, surface_type, surface_parameters)


    def set_lambertian_albedo(self, albedo_array):
        """

        void FullPhysics::SpurrBrdfDriver::set_lambertian_albedo(const blitz::Array< double, 1 > &albedo_array)
        Initialize lambertian albedo from array that might be external to the
        BrdfDriver. 
        """
        return _spurr_driver.SpurrBrdfDriver_set_lambertian_albedo(self, albedo_array)


    def _v_n_brdf_kernels(self):
        """

        virtual int FullPhysics::SpurrBrdfDriver::n_brdf_kernels() const =0

        """
        return _spurr_driver.SpurrBrdfDriver__v_n_brdf_kernels(self)


    @property
    def n_brdf_kernels(self):
        return self._v_n_brdf_kernels()


    def _v_n_kernel_factor_wfs(self):
        """

        virtual int FullPhysics::SpurrBrdfDriver::n_kernel_factor_wfs() const =0

        """
        return _spurr_driver.SpurrBrdfDriver__v_n_kernel_factor_wfs(self)


    @property
    def n_kernel_factor_wfs(self):
        return self._v_n_kernel_factor_wfs()


    def _v_n_kernel_params_wfs(self):
        """

        virtual int FullPhysics::SpurrBrdfDriver::n_kernel_params_wfs() const =0

        """
        return _spurr_driver.SpurrBrdfDriver__v_n_kernel_params_wfs(self)


    @property
    def n_kernel_params_wfs(self):
        return self._v_n_kernel_params_wfs()


    def _v_n_surface_wfs(self):
        """

        virtual int FullPhysics::SpurrBrdfDriver::n_surface_wfs() const =0

        """
        return _spurr_driver.SpurrBrdfDriver__v_n_surface_wfs(self)


    @property
    def n_surface_wfs(self):
        return self._v_n_surface_wfs()


    def _v_do_shadow_effect(self):
        """

        virtual bool FullPhysics::SpurrBrdfDriver::do_shadow_effect() const =0

        """
        return _spurr_driver.SpurrBrdfDriver__v_do_shadow_effect(self)


    @property
    def do_shadow_effect(self):
        return self._v_do_shadow_effect()

    __swig_destroy__ = _spurr_driver.delete_SpurrBrdfDriver
    __del__ = lambda self: None
SpurrBrdfDriver_swigregister = _spurr_driver.SpurrBrdfDriver_swigregister
SpurrBrdfDriver_swigregister(SpurrBrdfDriver)

class SpurrRtDriver(_object):
    """

    Abstracts away set up of Radiative Transfer software from Rob Spurr
    into a simpler common inteface used by the L2 software.

    This interface should be independent of the L2 Atmosphere class to
    make unit testing easier.

    C++ includes: spurr_driver.h 
    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpurrRtDriver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SpurrRtDriver, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def reflectance_calculate(self, height_grid, sza, azm, zen, surface_type, surface_parameters, od, ssa, pf):
        """

        virtual double FullPhysics::SpurrRtDriver::reflectance_calculate(const blitz::Array< double, 1 > &height_grid, double sza, double azm,
        double zen, int surface_type, const blitz::Array< double, 1 >
        &surface_parameters, const blitz::Array< double, 1 > &od, const
        blitz::Array< double, 1 > &ssa, const blitz::Array< double, 2 > &pf)
        Computes reflectance without jacobians. 
        """
        return _spurr_driver.SpurrRtDriver_reflectance_calculate(self, height_grid, sza, azm, zen, surface_type, surface_parameters, od, ssa, pf)


    def reflectance_and_jacobian_calculate(self, height_grid, sza, azm, zen, surface_type, surface_parameters, od, ssa, pf, reflectance, jac_atm, jac_surf):
        """

        virtual void FullPhysics::SpurrRtDriver::reflectance_and_jacobian_calculate(const blitz::Array< double, 1 > &height_grid, double sza, double azm,
        double zen, int surface_type, ArrayAd< double, 1 >
        &surface_parameters, const ArrayAd< double, 1 > &od, const ArrayAd<
        double, 1 > &ssa, const ArrayAd< double, 2 > &pf, double &reflectance,
        blitz::Array< double, 2 > &jac_atm, blitz::Array< double, 1 >
        &jac_surf)

        """
        return _spurr_driver.SpurrRtDriver_reflectance_and_jacobian_calculate(self, height_grid, sza, azm, zen, surface_type, surface_parameters, od, ssa, pf, reflectance, jac_atm, jac_surf)


    def _v_brdf_driver(self):
        """

        const boost::shared_ptr<SpurrBrdfDriver> FullPhysics::SpurrRtDriver::brdf_driver() const
        Access to BRDF driver. 
        """
        return _spurr_driver.SpurrRtDriver__v_brdf_driver(self)


    @property
    def brdf_driver(self):
        return self._v_brdf_driver()


    def setup_height_grid(self, height_grid):
        """

        virtual void FullPhysics::SpurrRtDriver::setup_height_grid(const blitz::Array< double, 1 > &height_grid) const =0
        Setup height grid, should only be called once per instance or if the
        height grid changes. 
        """
        return _spurr_driver.SpurrRtDriver_setup_height_grid(self, height_grid)


    def setup_geometry(self, sza, azm, zen):
        """

        virtual void FullPhysics::SpurrRtDriver::setup_geometry(double sza, double azm, double zen) const =0
        Setup viewing geometry, should only be called once per instance or if
        the viewing geometry changes. 
        """
        return _spurr_driver.SpurrRtDriver_setup_geometry(self, sza, azm, zen)


    def setup_optical_inputs(self, od, ssa, pf):
        """

        virtual void FullPhysics::SpurrRtDriver::setup_optical_inputs(const blitz::Array< double, 1 > &od, const blitz::Array< double, 1 >
        &ssa, const blitz::Array< double, 2 > &pf) const =0
        Set up optical depth, single scattering albedo and phase function
        Should be called per spectral point. 
        """
        return _spurr_driver.SpurrRtDriver_setup_optical_inputs(self, od, ssa, pf)


    def clear_linear_inputs(self):
        """

        virtual void FullPhysics::SpurrRtDriver::clear_linear_inputs() const =0
        Mark that we are not retrieving weighting functions. 
        """
        return _spurr_driver.SpurrRtDriver_clear_linear_inputs(self)


    def setup_linear_inputs(self, od, ssa, pf, do_surface_linearization):
        """

        virtual void FullPhysics::SpurrRtDriver::setup_linear_inputs(const ArrayAd< double, 1 > &od, const ArrayAd< double, 1 > &ssa,
        const ArrayAd< double, 2 > &pf, bool do_surface_linearization) const
        =0
        Set up linearization, weighting functions. 
        """
        return _spurr_driver.SpurrRtDriver_setup_linear_inputs(self, od, ssa, pf, do_surface_linearization)


    def calculate_rt(self):
        """

        virtual void FullPhysics::SpurrRtDriver::calculate_rt() const =0
        Perform radiative transfer calculation with the values setup by
        setup_optical_inputs and setup_linear_inputs. 
        """
        return _spurr_driver.SpurrRtDriver_calculate_rt(self)


    def get_intensity(self):
        """

        virtual double FullPhysics::SpurrRtDriver::get_intensity() const =0
        Retrieve the intensity value calculated. 
        """
        return _spurr_driver.SpurrRtDriver_get_intensity(self)


    def copy_jacobians(self, jac_atm, jac_surf):
        """

        virtual void FullPhysics::SpurrRtDriver::copy_jacobians(blitz::Array< double, 2 > &jac_atm, blitz::Array< double, 1 >
        &jac_surf) const =0
        Copy jacobians out of internal xdata structures. 
        """
        return _spurr_driver.SpurrRtDriver_copy_jacobians(self, jac_atm, jac_surf)

    __swig_destroy__ = _spurr_driver.delete_SpurrRtDriver
    __del__ = lambda self: None
SpurrRtDriver_swigregister = _spurr_driver.SpurrRtDriver_swigregister
SpurrRtDriver_swigregister(SpurrRtDriver)

# This file is compatible with both classic and new-style classes.


