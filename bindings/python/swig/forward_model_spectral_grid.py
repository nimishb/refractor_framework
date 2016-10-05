# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _forward_model_spectral_grid.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_forward_model_spectral_grid', [dirname(__file__)])
        except ImportError:
            import _forward_model_spectral_grid
            return _forward_model_spectral_grid
        if fp is not None:
            try:
                _mod = imp.load_module('_forward_model_spectral_grid', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _forward_model_spectral_grid = swig_import_helper()
    del swig_import_helper
else:
    import _forward_model_spectral_grid
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


SHARED_PTR_DISOWN = _forward_model_spectral_grid.SHARED_PTR_DISOWN
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
import full_physics_swig.state_vector
class ForwardModelSpectralGrid(full_physics_swig.generic_object.GenericObject):
    """
    This is the Forward Model spectral grid.

    This is in a separate class because this is a bit complicated. We have
    3 grids to worry about

    The low resolution grid, which is the ultimate output of the
    ForwardModel.

    The high resolution grid, which is where we calculate the RT on. This
    is the spectrum before we have convolved it with Ils. Depending on the
    options used, this grid might be nonuniform.

    The high resolution grid we interpolate to. If we are not doing
    nonuniform sampling, then this is the same as the high resolution
    grid.

    Note that there are a few closely related classes, with similar
    sounding names. See spectrum_doxygen for a description of each of
    these.

    C++ includes: forward_model_spectral_grid.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        FullPhysics::ForwardModelSpectralGrid::ForwardModelSpectralGrid()

        """
        _forward_model_spectral_grid.ForwardModelSpectralGrid_swiginit(self,_forward_model_spectral_grid.new_ForwardModelSpectralGrid(*args))
    def _v_number_spectrometer(self):
        """
        int FullPhysics::ForwardModelSpectralGrid::number_spectrometer() const
        Number of spectrometer. 
        """
        return _forward_model_spectral_grid.ForwardModelSpectralGrid__v_number_spectrometer(self)

    @property
    def number_spectrometer(self):
        return self._v_number_spectrometer()

    def low_resolution_grid(self, *args):
        """
        const SpectralDomain& FullPhysics::ForwardModelSpectralGrid::low_resolution_grid(int Spec_index) const
        The low resolution grid. 
        """
        return _forward_model_spectral_grid.ForwardModelSpectralGrid_low_resolution_grid(self, *args)

    def high_resolution_grid(self, *args):
        """
        const SpectralDomain& FullPhysics::ForwardModelSpectralGrid::high_resolution_grid(int Spec_index) const
        The high resolution grid, possibly nonuniform. 
        """
        return _forward_model_spectral_grid.ForwardModelSpectralGrid_high_resolution_grid(self, *args)

    def high_resolution_interpolated_grid(self, *args):
        """
        const SpectralDomain& FullPhysics::ForwardModelSpectralGrid::high_resolution_interpolated_grid(int Spec_index) const
        The high resolution grid, interpolated to be uniform. 
        """
        return _forward_model_spectral_grid.ForwardModelSpectralGrid_high_resolution_interpolated_grid(self, *args)

    def interpolate_spectrum(self, *args):
        """
        Spectrum ForwardModelSpectralGrid::interpolate_spectrum(const Spectrum &Spec_in, int Spec_index) const
        Interpolate a spectrum to the high_resolution_interpolated_grid()
        sampling. 
        """
        return _forward_model_spectral_grid.ForwardModelSpectralGrid_interpolate_spectrum(self, *args)

    def pixel_list(self, *args):
        """
        const std::vector<int>& FullPhysics::ForwardModelSpectralGrid::pixel_list(int Spec_index) const
        Pixel indexes to use for low resolution grid. 
        """
        return _forward_model_spectral_grid.ForwardModelSpectralGrid_pixel_list(self, *args)

    __swig_destroy__ = _forward_model_spectral_grid.delete_ForwardModelSpectralGrid
ForwardModelSpectralGrid.__str__ = new_instancemethod(_forward_model_spectral_grid.ForwardModelSpectralGrid___str__,None,ForwardModelSpectralGrid)
ForwardModelSpectralGrid._v_number_spectrometer = new_instancemethod(_forward_model_spectral_grid.ForwardModelSpectralGrid__v_number_spectrometer,None,ForwardModelSpectralGrid)
ForwardModelSpectralGrid.low_resolution_grid = new_instancemethod(_forward_model_spectral_grid.ForwardModelSpectralGrid_low_resolution_grid,None,ForwardModelSpectralGrid)
ForwardModelSpectralGrid.high_resolution_grid = new_instancemethod(_forward_model_spectral_grid.ForwardModelSpectralGrid_high_resolution_grid,None,ForwardModelSpectralGrid)
ForwardModelSpectralGrid.high_resolution_interpolated_grid = new_instancemethod(_forward_model_spectral_grid.ForwardModelSpectralGrid_high_resolution_interpolated_grid,None,ForwardModelSpectralGrid)
ForwardModelSpectralGrid.interpolate_spectrum = new_instancemethod(_forward_model_spectral_grid.ForwardModelSpectralGrid_interpolate_spectrum,None,ForwardModelSpectralGrid)
ForwardModelSpectralGrid.pixel_list = new_instancemethod(_forward_model_spectral_grid.ForwardModelSpectralGrid_pixel_list,None,ForwardModelSpectralGrid)
ForwardModelSpectralGrid_swigregister = _forward_model_spectral_grid.ForwardModelSpectralGrid_swigregister
ForwardModelSpectralGrid_swigregister(ForwardModelSpectralGrid)



