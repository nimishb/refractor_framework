# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _ground_breon.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ground_breon', [dirname(__file__)])
        except ImportError:
            import _ground_breon
            return _ground_breon
        if fp is not None:
            try:
                _mod = imp.load_module('_ground_breon', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ground_breon = swig_import_helper()
    del swig_import_helper
else:
    import _ground_breon
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


SHARED_PTR_DISOWN = _ground_breon.SHARED_PTR_DISOWN
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

import full_physics_swig.ground
import full_physics_swig.observer
import full_physics_swig.generic_object
import full_physics_swig.sub_state_vector_array
class GroundBreonVeg(full_physics_swig.ground.Ground):
    """
    C++ includes: ground_breon.h

    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        FullPhysics::GroundBreonVeg::GroundBreonVeg(const blitz::Array< double, 2 > &Rahman_params, const blitz::Array<
        bool, 2 > &Flag, const std::vector< std::string > &Desc_band_names)

        """
        _ground_breon.GroundBreonVeg_swiginit(self,_ground_breon.new_GroundBreonVeg(*args))
    def number_spectrometer(self):
        """
        virtual const int FullPhysics::GroundBreon::number_spectrometer() const

        """
        return _ground_breon.GroundBreonVeg_number_spectrometer(self)

    def overall_amplitude(self, *args):
        """
        void GroundBreon::overall_amplitude(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_breon.GroundBreonVeg_overall_amplitude(self, *args)

    def asymmetry_parameter(self, *args):
        """
        void GroundBreon::asymmetry_parameter(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_breon.GroundBreonVeg_asymmetry_parameter(self, *args)

    def geometric_factor(self, *args):
        """
        void GroundBreon::geometric_factor(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_breon.GroundBreonVeg_geometric_factor(self, *args)

    def refractive_index(self, *args):
        """
        virtual const double FullPhysics::GroundBreon::refractive_index(const int Spec_idx) const
        Returns hard coded value of 1.5 since that is the value hardcoded into
        LIDORT. 
        """
        return _ground_breon.GroundBreonVeg_refractive_index(self, *args)

    def breon_type(self):
        """
        virtual const std::string FullPhysics::GroundBreonVeg::breon_type() const
        String describing which type of Breon surface type, also makes this
        class abstract. 
        """
        return _ground_breon.GroundBreonVeg_breon_type(self)

    def state_vector_name_i(self, *args):
        """
        std::string GroundBreon::state_vector_name_i(int i) const

        """
        return _ground_breon.GroundBreonVeg_state_vector_name_i(self, *args)

    def desc(self):
        """
        virtual std::string FullPhysics::GroundBreon::desc() const

        """
        return _ground_breon.GroundBreonVeg_desc(self)

    __swig_destroy__ = _ground_breon.delete_GroundBreonVeg
GroundBreonVeg.number_spectrometer = new_instancemethod(_ground_breon.GroundBreonVeg_number_spectrometer,None,GroundBreonVeg)
GroundBreonVeg.overall_amplitude = new_instancemethod(_ground_breon.GroundBreonVeg_overall_amplitude,None,GroundBreonVeg)
GroundBreonVeg.asymmetry_parameter = new_instancemethod(_ground_breon.GroundBreonVeg_asymmetry_parameter,None,GroundBreonVeg)
GroundBreonVeg.geometric_factor = new_instancemethod(_ground_breon.GroundBreonVeg_geometric_factor,None,GroundBreonVeg)
GroundBreonVeg.refractive_index = new_instancemethod(_ground_breon.GroundBreonVeg_refractive_index,None,GroundBreonVeg)
GroundBreonVeg.breon_type = new_instancemethod(_ground_breon.GroundBreonVeg_breon_type,None,GroundBreonVeg)
GroundBreonVeg.state_vector_name_i = new_instancemethod(_ground_breon.GroundBreonVeg_state_vector_name_i,None,GroundBreonVeg)
GroundBreonVeg.desc = new_instancemethod(_ground_breon.GroundBreonVeg_desc,None,GroundBreonVeg)
GroundBreonVeg_swigregister = _ground_breon.GroundBreonVeg_swigregister
GroundBreonVeg_swigregister(GroundBreonVeg)

class GroundBreonSoil(full_physics_swig.ground.Ground):
    """
    C++ includes: ground_breon.h

    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        FullPhysics::GroundBreonSoil::GroundBreonSoil(const blitz::Array< double, 2 > &Rahman_params, const blitz::Array<
        bool, 2 > &Flag, const std::vector< std::string > &Desc_band_names)

        """
        _ground_breon.GroundBreonSoil_swiginit(self,_ground_breon.new_GroundBreonSoil(*args))
    def number_spectrometer(self):
        """
        virtual const int FullPhysics::GroundBreon::number_spectrometer() const

        """
        return _ground_breon.GroundBreonSoil_number_spectrometer(self)

    def overall_amplitude(self, *args):
        """
        void GroundBreon::overall_amplitude(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_breon.GroundBreonSoil_overall_amplitude(self, *args)

    def asymmetry_parameter(self, *args):
        """
        void GroundBreon::asymmetry_parameter(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_breon.GroundBreonSoil_asymmetry_parameter(self, *args)

    def geometric_factor(self, *args):
        """
        void GroundBreon::geometric_factor(const int spec_index, const AutoDerivative< double > &val)

        """
        return _ground_breon.GroundBreonSoil_geometric_factor(self, *args)

    def refractive_index(self, *args):
        """
        virtual const double FullPhysics::GroundBreon::refractive_index(const int Spec_idx) const
        Returns hard coded value of 1.5 since that is the value hardcoded into
        LIDORT. 
        """
        return _ground_breon.GroundBreonSoil_refractive_index(self, *args)

    def breon_type(self):
        """
        virtual const std::string FullPhysics::GroundBreonSoil::breon_type() const
        String describing which type of Breon surface type, also makes this
        class abstract. 
        """
        return _ground_breon.GroundBreonSoil_breon_type(self)

    def state_vector_name_i(self, *args):
        """
        std::string GroundBreon::state_vector_name_i(int i) const

        """
        return _ground_breon.GroundBreonSoil_state_vector_name_i(self, *args)

    def desc(self):
        """
        virtual std::string FullPhysics::GroundBreon::desc() const

        """
        return _ground_breon.GroundBreonSoil_desc(self)

    __swig_destroy__ = _ground_breon.delete_GroundBreonSoil
GroundBreonSoil.number_spectrometer = new_instancemethod(_ground_breon.GroundBreonSoil_number_spectrometer,None,GroundBreonSoil)
GroundBreonSoil.overall_amplitude = new_instancemethod(_ground_breon.GroundBreonSoil_overall_amplitude,None,GroundBreonSoil)
GroundBreonSoil.asymmetry_parameter = new_instancemethod(_ground_breon.GroundBreonSoil_asymmetry_parameter,None,GroundBreonSoil)
GroundBreonSoil.geometric_factor = new_instancemethod(_ground_breon.GroundBreonSoil_geometric_factor,None,GroundBreonSoil)
GroundBreonSoil.refractive_index = new_instancemethod(_ground_breon.GroundBreonSoil_refractive_index,None,GroundBreonSoil)
GroundBreonSoil.breon_type = new_instancemethod(_ground_breon.GroundBreonSoil_breon_type,None,GroundBreonSoil)
GroundBreonSoil.state_vector_name_i = new_instancemethod(_ground_breon.GroundBreonSoil_state_vector_name_i,None,GroundBreonSoil)
GroundBreonSoil.desc = new_instancemethod(_ground_breon.GroundBreonSoil_desc,None,GroundBreonSoil)
GroundBreonSoil_swigregister = _ground_breon.GroundBreonSoil_swigregister
GroundBreonSoil_swigregister(GroundBreonSoil)



