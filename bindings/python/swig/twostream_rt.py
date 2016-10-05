# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _twostream_rt.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_twostream_rt', [dirname(__file__)])
        except ImportError:
            import _twostream_rt
            return _twostream_rt
        if fp is not None:
            try:
                _mod = imp.load_module('_twostream_rt', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _twostream_rt = swig_import_helper()
    del swig_import_helper
else:
    import _twostream_rt
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


SHARED_PTR_DISOWN = _twostream_rt.SHARED_PTR_DISOWN
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

import full_physics_swig.spurr_rt
import full_physics_swig.rt_atmosphere
import full_physics_swig.observer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
import full_physics_swig.radiative_transfer_single_wn
import full_physics_swig.radiative_transfer_fixed_stokes_coefficient
import full_physics_swig.radiative_transfer
import full_physics_swig.named_spectrum
class TwostreamRt(full_physics_swig.spurr_rt.SpurrRt):
    """
    Uses the Spurr interfaces to construct a radiative transfer class
    connecting L2 FP and TwoStream.

    C++ includes: twostream_rt.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    @property
    def number_stream(self):
        return self._v_number_stream()

    def _v_number_moment(self):
        """
        int FullPhysics::TwostreamRt::number_moment() const
        Number of moments for scattering matrix.

        2stream natuarally uses up to 3 moments 
        """
        return _twostream_rt.TwostreamRt__v_number_moment(self)

    @property
    def number_moment(self):
        return self._v_number_moment()

    def _v_brdf_driver(self):
        """
        const boost::shared_ptr<TwostreamBrdfDriver> FullPhysics::TwostreamRt::brdf_driver() const
        Convenience routine to get brdf driver object. 
        """
        return _twostream_rt.TwostreamRt__v_brdf_driver(self)

    @property
    def brdf_driver(self):
        return self._v_brdf_driver()

    def _v_rt_driver(self):
        """
        const boost::shared_ptr<TwostreamRtDriver> FullPhysics::TwostreamRt::rt_driver() const
        Convenience routine to get rt driver object. 
        """
        return _twostream_rt.TwostreamRt__v_rt_driver(self)

    @property
    def rt_driver(self):
        return self._v_rt_driver()

    def print_desc(self, *args):
        """
        void TwostreamRt::print(std::ostream &Os, bool Short_form=false) const
        Print to a stream. 
        """
        return _twostream_rt.TwostreamRt_print_desc(self, *args)

    __swig_destroy__ = _twostream_rt.delete_TwostreamRt
TwostreamRt._v_number_moment = new_instancemethod(_twostream_rt.TwostreamRt__v_number_moment,None,TwostreamRt)
TwostreamRt._v_brdf_driver = new_instancemethod(_twostream_rt.TwostreamRt__v_brdf_driver,None,TwostreamRt)
TwostreamRt._v_rt_driver = new_instancemethod(_twostream_rt.TwostreamRt__v_rt_driver,None,TwostreamRt)
TwostreamRt.print_desc = new_instancemethod(_twostream_rt.TwostreamRt_print_desc,None,TwostreamRt)
TwostreamRt_swigregister = _twostream_rt.TwostreamRt_swigregister
TwostreamRt_swigregister(TwostreamRt)



