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
            fp, pathname, description = imp.find_module('_lidort_driver', [dirname(__file__)])
        except ImportError:
            import _lidort_driver
            return _lidort_driver
        if fp is not None:
            try:
                _mod = imp.load_module('_lidort_driver', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _lidort_driver = swig_import_helper()
    del swig_import_helper
else:
    import _lidort_driver
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



_lidort_driver.SHARED_PTR_DISOWN_swigconstant(_lidort_driver)
SHARED_PTR_DISOWN = _lidort_driver.SHARED_PTR_DISOWN

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
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpurrBrdfDriver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SpurrBrdfDriver, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def initialize_brdf_inputs(self, surface_type):
        return _lidort_driver.SpurrBrdfDriver_initialize_brdf_inputs(self, surface_type)

    def setup_geometry(self, sza, azm, zen):
        return _lidort_driver.SpurrBrdfDriver_setup_geometry(self, sza, azm, zen)

    def setup_brdf_inputs(self, surface_type, surface_parameters):
        return _lidort_driver.SpurrBrdfDriver_setup_brdf_inputs(self, surface_type, surface_parameters)

    def set_lambertian_albedo(self, albedo_array):
        return _lidort_driver.SpurrBrdfDriver_set_lambertian_albedo(self, albedo_array)

    def _v_n_brdf_kernels(self):
        return _lidort_driver.SpurrBrdfDriver__v_n_brdf_kernels(self)

    @property
    def n_brdf_kernels(self):
        return self._v_n_brdf_kernels()


    def _v_n_kernel_factor_wfs(self):
        return _lidort_driver.SpurrBrdfDriver__v_n_kernel_factor_wfs(self)

    @property
    def n_kernel_factor_wfs(self):
        return self._v_n_kernel_factor_wfs()


    def _v_n_kernel_params_wfs(self):
        return _lidort_driver.SpurrBrdfDriver__v_n_kernel_params_wfs(self)

    @property
    def n_kernel_params_wfs(self):
        return self._v_n_kernel_params_wfs()


    def _v_n_surface_wfs(self):
        return _lidort_driver.SpurrBrdfDriver__v_n_surface_wfs(self)

    @property
    def n_surface_wfs(self):
        return self._v_n_surface_wfs()


    def _v_do_shadow_effect(self):
        return _lidort_driver.SpurrBrdfDriver__v_do_shadow_effect(self)

    @property
    def do_shadow_effect(self):
        return self._v_do_shadow_effect()

    __swig_destroy__ = _lidort_driver.delete_SpurrBrdfDriver
    __del__ = lambda self: None
SpurrBrdfDriver_swigregister = _lidort_driver.SpurrBrdfDriver_swigregister
SpurrBrdfDriver_swigregister(SpurrBrdfDriver)

class SpurrRtDriver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SpurrRtDriver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SpurrRtDriver, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def reflectance_calculate(self, height_grid, sza, azm, zen, surface_type, surface_parameters, od, ssa, pf):
        return _lidort_driver.SpurrRtDriver_reflectance_calculate(self, height_grid, sza, azm, zen, surface_type, surface_parameters, od, ssa, pf)

    def reflectance_and_jacobian_calculate(self, height_grid, sza, azm, zen, surface_type, surface_parameters, od, ssa, pf, reflectance, jac_atm, jac_surf):
        return _lidort_driver.SpurrRtDriver_reflectance_and_jacobian_calculate(self, height_grid, sza, azm, zen, surface_type, surface_parameters, od, ssa, pf, reflectance, jac_atm, jac_surf)

    def _v_brdf_driver(self):
        return _lidort_driver.SpurrRtDriver__v_brdf_driver(self)

    @property
    def brdf_driver(self):
        return self._v_brdf_driver()


    def setup_height_grid(self, height_grid):
        return _lidort_driver.SpurrRtDriver_setup_height_grid(self, height_grid)

    def setup_geometry(self, sza, azm, zen):
        return _lidort_driver.SpurrRtDriver_setup_geometry(self, sza, azm, zen)

    def setup_optical_inputs(self, od, ssa, pf):
        return _lidort_driver.SpurrRtDriver_setup_optical_inputs(self, od, ssa, pf)

    def clear_linear_inputs(self):
        return _lidort_driver.SpurrRtDriver_clear_linear_inputs(self)

    def setup_linear_inputs(self, od, ssa, pf, do_surface_linearization):
        return _lidort_driver.SpurrRtDriver_setup_linear_inputs(self, od, ssa, pf, do_surface_linearization)

    def calculate_rt(self):
        return _lidort_driver.SpurrRtDriver_calculate_rt(self)

    def get_intensity(self):
        return _lidort_driver.SpurrRtDriver_get_intensity(self)

    def copy_jacobians(self, jac_atm, jac_surf):
        return _lidort_driver.SpurrRtDriver_copy_jacobians(self, jac_atm, jac_surf)
    __swig_destroy__ = _lidort_driver.delete_SpurrRtDriver
    __del__ = lambda self: None
SpurrRtDriver_swigregister = _lidort_driver.SpurrRtDriver_swigregister
SpurrRtDriver_swigregister(SpurrRtDriver)

class LidortBrdfDriver(SpurrBrdfDriver):
    """

    LIDORT specific BRDF driver implementation.

    C++ includes: lidort_driver.h 
    """

    __swig_setmethods__ = {}
    for _s in [SpurrBrdfDriver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, LidortBrdfDriver, name, value)
    __swig_getmethods__ = {}
    for _s in [SpurrBrdfDriver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, LidortBrdfDriver, name)
    __repr__ = _swig_repr

    def __init__(self, nstream, nmoment):
        """

        FullPhysics::LidortBrdfDriver::LidortBrdfDriver(int nstream, int nmoment)

        """
        this = _lidort_driver.new_LidortBrdfDriver(nstream, nmoment)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _lidort_driver.delete_LidortBrdfDriver
    __del__ = lambda self: None

    def _v_brdf_interface(self):
        """

        const boost::shared_ptr<Brdf_Linsup_Masters> FullPhysics::LidortBrdfDriver::brdf_interface() const
        Interface to BRDF interface to allow changing configuration to values.

        """
        return _lidort_driver.LidortBrdfDriver__v_brdf_interface(self)


    @property
    def brdf_interface(self):
        return self._v_brdf_interface()


    def setup_geometry(self, sza, azm, zen):
        """

        virtual void FullPhysics::LidortBrdfDriver::setup_geometry(double sza, double azm, double zen) const

        """
        return _lidort_driver.LidortBrdfDriver_setup_geometry(self, sza, azm, zen)


    def _v_n_brdf_kernels(self):
        """

        virtual int FullPhysics::LidortBrdfDriver::n_brdf_kernels() const

        """
        return _lidort_driver.LidortBrdfDriver__v_n_brdf_kernels(self)


    @property
    def n_brdf_kernels(self):
        return self._v_n_brdf_kernels()


    def _v_n_kernel_factor_wfs(self):
        """

        virtual int FullPhysics::LidortBrdfDriver::n_kernel_factor_wfs() const

        """
        return _lidort_driver.LidortBrdfDriver__v_n_kernel_factor_wfs(self)


    @property
    def n_kernel_factor_wfs(self):
        return self._v_n_kernel_factor_wfs()


    def _v_n_kernel_params_wfs(self):
        """

        virtual int FullPhysics::LidortBrdfDriver::n_kernel_params_wfs() const

        """
        return _lidort_driver.LidortBrdfDriver__v_n_kernel_params_wfs(self)


    @property
    def n_kernel_params_wfs(self):
        return self._v_n_kernel_params_wfs()


    def _v_n_surface_wfs(self):
        """

        virtual int FullPhysics::LidortBrdfDriver::n_surface_wfs() const

        """
        return _lidort_driver.LidortBrdfDriver__v_n_surface_wfs(self)


    @property
    def n_surface_wfs(self):
        return self._v_n_surface_wfs()


    def _v_do_shadow_effect(self):
        """

        virtual bool FullPhysics::LidortBrdfDriver::do_shadow_effect() const

        """
        return _lidort_driver.LidortBrdfDriver__v_do_shadow_effect(self)


    @property
    def do_shadow_effect(self):
        return self._v_do_shadow_effect()


    def do_kparams_derivs(self, kernel_index):
        """

        virtual bool FullPhysics::LidortBrdfDriver::do_kparams_derivs(const int kernel_index) const

        """
        return _lidort_driver.LidortBrdfDriver_do_kparams_derivs(self, kernel_index)

LidortBrdfDriver_swigregister = _lidort_driver.LidortBrdfDriver_swigregister
LidortBrdfDriver_swigregister(LidortBrdfDriver)

class LidortRtDriver(SpurrRtDriver):
    """

    LIDORT specific Radiative transfer interface implementation.

    C++ includes: lidort_driver.h 
    """

    __swig_setmethods__ = {}
    for _s in [SpurrRtDriver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, LidortRtDriver, name, value)
    __swig_getmethods__ = {}
    for _s in [SpurrRtDriver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, LidortRtDriver, name)
    __repr__ = _swig_repr

    def __init__(self, nstream, nmoment, do_multi_scatt_only, surface_type, zen, pure_nadir):
        """

        FullPhysics::LidortRtDriver::LidortRtDriver(int nstream, int nmoment, bool do_multi_scatt_only, int surface_type,
        const blitz::Array< double, 1 > &zen, bool pure_nadir)

        """
        this = _lidort_driver.new_LidortRtDriver(nstream, nmoment, do_multi_scatt_only, surface_type, zen, pure_nadir)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def _v_number_moment(self):
        """

        int FullPhysics::LidortRtDriver::number_moment() const

        """
        return _lidort_driver.LidortRtDriver__v_number_moment(self)


    @property
    def number_moment(self):
        return self._v_number_moment()


    def _v_number_stream(self):
        """

        int FullPhysics::LidortRtDriver::number_stream() const

        """
        return _lidort_driver.LidortRtDriver__v_number_stream(self)


    @property
    def number_stream(self):
        return self._v_number_stream()


    def setup_sphericity(self, zen):
        """

        void FullPhysics::LidortRtDriver::setup_sphericity(double zen) const

        """
        return _lidort_driver.LidortRtDriver_setup_sphericity(self, zen)


    def set_plane_parallel(self):
        """

        void FullPhysics::LidortRtDriver::set_plane_parallel() const

        """
        return _lidort_driver.LidortRtDriver_set_plane_parallel(self)


    def set_pseudo_spherical(self):
        """

        void FullPhysics::LidortRtDriver::set_pseudo_spherical() const

        """
        return _lidort_driver.LidortRtDriver_set_pseudo_spherical(self)


    def set_plane_parallel_plus_ss_correction(self):
        """

        void FullPhysics::LidortRtDriver::set_plane_parallel_plus_ss_correction() const

        """
        return _lidort_driver.LidortRtDriver_set_plane_parallel_plus_ss_correction(self)


    def set_line_of_sight(self):
        """

        void FullPhysics::LidortRtDriver::set_line_of_sight() const

        """
        return _lidort_driver.LidortRtDriver_set_line_of_sight(self)


    def _v_do_multi_scatt_only(self):
        """

        bool FullPhysics::LidortRtDriver::do_multi_scatt_only() const

        """
        return _lidort_driver.LidortRtDriver__v_do_multi_scatt_only(self)


    @property
    def do_multi_scatt_only(self):
        return self._v_do_multi_scatt_only()


    def _v_pure_nadir(self):
        """

        bool FullPhysics::LidortRtDriver::pure_nadir() const

        """
        return _lidort_driver.LidortRtDriver__v_pure_nadir(self)


    @property
    def pure_nadir(self):
        return self._v_pure_nadir()


    def _v_lidort_brdf_driver(self):
        """

        const boost::shared_ptr<LidortBrdfDriver> FullPhysics::LidortRtDriver::lidort_brdf_driver() const
        Access to BRDF driver. 
        """
        return _lidort_driver.LidortRtDriver__v_lidort_brdf_driver(self)


    @property
    def lidort_brdf_driver(self):
        return self._v_lidort_brdf_driver()


    def _v_brdf_interface(self):
        """

        const boost::shared_ptr<Brdf_Linsup_Masters> FullPhysics::LidortRtDriver::brdf_interface() const

        """
        return _lidort_driver.LidortRtDriver__v_brdf_interface(self)


    @property
    def brdf_interface(self):
        return self._v_brdf_interface()


    def _v_lidort_interface(self):
        """

        const boost::shared_ptr<Lidort_Lps_Masters> FullPhysics::LidortRtDriver::lidort_interface() const
        Interface to LIDORT RT software inputs to allow changing LIDORT
        configuration to values other than default. 
        """
        return _lidort_driver.LidortRtDriver__v_lidort_interface(self)


    @property
    def lidort_interface(self):
        return self._v_lidort_interface()


    def setup_height_grid(self, height_grid):
        """

        void FullPhysics::LidortRtDriver::setup_height_grid(const blitz::Array< double, 1 > &height_grid) const

        """
        return _lidort_driver.LidortRtDriver_setup_height_grid(self, height_grid)


    def setup_geometry(self, sza, azm, zen):
        """

        void FullPhysics::LidortRtDriver::setup_geometry(double sza, double azm, double zen) const

        """
        return _lidort_driver.LidortRtDriver_setup_geometry(self, sza, azm, zen)


    def setup_optical_inputs(self, od, ssa, pf):
        """

        void FullPhysics::LidortRtDriver::setup_optical_inputs(const blitz::Array< double, 1 > &od, const blitz::Array< double, 1 >
        &ssa, const blitz::Array< double, 2 > &pf) const

        """
        return _lidort_driver.LidortRtDriver_setup_optical_inputs(self, od, ssa, pf)


    def clear_linear_inputs(self):
        """

        void FullPhysics::LidortRtDriver::clear_linear_inputs() const

        """
        return _lidort_driver.LidortRtDriver_clear_linear_inputs(self)


    def setup_linear_inputs(self, od, ssa, pf, do_surface_linearization):
        """

        void FullPhysics::LidortRtDriver::setup_linear_inputs(const ArrayAd< double, 1 > &od, const ArrayAd< double, 1 > &ssa,
        const ArrayAd< double, 2 > &pf, bool do_surface_linearization) const

        """
        return _lidort_driver.LidortRtDriver_setup_linear_inputs(self, od, ssa, pf, do_surface_linearization)


    def calculate_rt(self):
        """

        void FullPhysics::LidortRtDriver::calculate_rt() const

        """
        return _lidort_driver.LidortRtDriver_calculate_rt(self)


    def get_intensity(self):
        """

        double FullPhysics::LidortRtDriver::get_intensity() const

        """
        return _lidort_driver.LidortRtDriver_get_intensity(self)


    def copy_jacobians(self, jac_atm, jac_surf):
        """

        void FullPhysics::LidortRtDriver::copy_jacobians(blitz::Array< double, 2 > &jac_atm, blitz::Array< double, 1 >
        &jac_surf) const

        """
        return _lidort_driver.LidortRtDriver_copy_jacobians(self, jac_atm, jac_surf)

    __swig_destroy__ = _lidort_driver.delete_LidortRtDriver
    __del__ = lambda self: None
LidortRtDriver_swigregister = _lidort_driver.LidortRtDriver_swigregister
LidortRtDriver_swigregister(LidortRtDriver)

# This file is compatible with both classic and new-style classes.


