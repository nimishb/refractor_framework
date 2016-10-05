# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _absorber.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_absorber', [dirname(__file__)])
        except ImportError:
            import _absorber
            return _absorber
        if fp is not None:
            try:
                _mod = imp.load_module('_absorber', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _absorber = swig_import_helper()
    del swig_import_helper
else:
    import _absorber
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


SHARED_PTR_DISOWN = _absorber.SHARED_PTR_DISOWN
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

import full_physics_swig.state_vector
import full_physics_swig.generic_object
class ObservableAbsorber(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _absorber.delete_ObservableAbsorber
ObservableAbsorber.add_observer_and_keep_reference = new_instancemethod(_absorber.ObservableAbsorber_add_observer_and_keep_reference,None,ObservableAbsorber)
ObservableAbsorber.add_observer = new_instancemethod(_absorber.ObservableAbsorber_add_observer,None,ObservableAbsorber)
ObservableAbsorber.remove_observer = new_instancemethod(_absorber.ObservableAbsorber_remove_observer,None,ObservableAbsorber)
ObservableAbsorber_swigregister = _absorber.ObservableAbsorber_swigregister
ObservableAbsorber_swigregister(ObservableAbsorber)

class ObserverAbsorber(full_physics_swig.generic_object.GenericObject):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        _absorber.ObserverAbsorber_swiginit(self,_absorber.new_ObserverAbsorber())
    __swig_destroy__ = _absorber.delete_ObserverAbsorber
ObserverAbsorber.notify_update = new_instancemethod(_absorber.ObserverAbsorber_notify_update,None,ObserverAbsorber)
ObserverAbsorber.notify_add = new_instancemethod(_absorber.ObserverAbsorber_notify_add,None,ObserverAbsorber)
ObserverAbsorber.notify_remove = new_instancemethod(_absorber.ObserverAbsorber_notify_remove,None,ObserverAbsorber)
ObserverAbsorber_swigregister = _absorber.ObserverAbsorber_swigregister
ObserverAbsorber_swigregister(ObserverAbsorber)

class Absorber(full_physics_swig.state_vector.StateVectorObserver,ObservableAbsorber):
    """
    This class maintains the absorber portion of the state.

    Other objects may depend on the absorber, and should be updated when
    the absorber is updated. To facilitate that, this class in an
    Oberverable, and objects can add themselves as Observers to be
    notified when the absorber is updated.

    Because the absorber calculation tends to be a bottle neck, we keep a
    timer in this class. This class keeps track of the time used in the
    optical_depth_each_layer function. Other classes can make use of this
    information for logging if desired.

    C++ includes: absorber.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _absorber.delete_Absorber
    def add_observer(self, *args):
        """
        virtual void FullPhysics::Absorber::add_observer(Observer< Absorber > &Obs)

        """
        return _absorber.Absorber_add_observer(self, *args)

    def remove_observer(self, *args):
        """
        virtual void FullPhysics::Absorber::remove_observer(Observer< Absorber > &Obs)

        """
        return _absorber.Absorber_remove_observer(self, *args)

    def _v_number_species(self):
        """
        virtual int FullPhysics::Absorber::number_species() const
        Number of species. 
        """
        return _absorber.Absorber__v_number_species(self)

    @property
    def number_species(self):
        return self._v_number_species()

    def gas_name(self, *args):
        """
        virtual std::string FullPhysics::Absorber::gas_name(int Species_index) const =0
        Name of gases, in the order that optical_depth_each_layer returns
        them. 
        """
        return _absorber.Absorber_gas_name(self, *args)

    def gas_index(self, *args):
        """
        int Absorber::gas_index(const std::string &Name) const
        Map a gas name to the index number it appears in
        optical_depth_each_layer.

        This return -1 if the Name is not one of the gases. 
        """
        return _absorber.Absorber_gas_index(self, *args)

    def optical_depth_each_layer(self, *args):
        """
        virtual ArrayAd<double, 2> FullPhysics::Absorber::optical_depth_each_layer(double wn, int spec_index) const =0
        This gives the optical depth for each layer, for the given wave
        number.

        Note this only includes the Absorbers portion of this, Atmosphere
        class combines this with Rayleigh and Aerosol scattering.

        This has size of pres->number_active_layer() x number_species()

        We include the derivative of this with respect to the state vector. 
        """
        return _absorber.Absorber_optical_depth_each_layer(self, *args)

    def xgas(self, *args):
        """
        virtual AutoDerivative<double> FullPhysics::Absorber::xgas(const std::string &Gas_name) const =0
        This calculates the gas column, e.g., XCO2.

        This is the dry air mole fraction of the gas, see section 3.5.4 of the
        ATB

        We include the derivative of this with respect to the state vector. 
        """
        return _absorber.Absorber_xgas(self, *args)

    def absorber_vmr(self, *args):
        """
        virtual boost::shared_ptr<AbsorberVmr> FullPhysics::Absorber::absorber_vmr(const std::string &gas_name) const =0
        Returns the AbsorberVmr object for a given species index. 
        """
        return _absorber.Absorber_absorber_vmr(self, *args)

    def clone(self, *args):
        """
        virtual boost::shared_ptr<Absorber> FullPhysics::Absorber::clone(const boost::shared_ptr< Pressure > &Press, const boost::shared_ptr<
        Temperature > &Temp, const std::vector< boost::shared_ptr< Altitude >
        > &Alt) const =0
        This version of clone takes a Pressure, Altitude and Temperature to
        use.

        The intent is that the Pressure, Altitude and Temperature has been
        cloned from the original Pressure, Altitude and Temperature (although
        this class has no way to verify this). This allows sets of objects to
        be cloned using a common Pressure, Altitude and Temperature clones,
        e.g. Atmosphere. 
        """
        return _absorber.Absorber_clone(self, *args)

    def __init__(self): 
        if self.__class__ == Absorber:
            _self = None
        else:
            _self = self
        _absorber.Absorber_swiginit(self,_absorber.new_Absorber(_self, ))
    def __disown__(self):
        self.this.disown()
        _absorber.disown_Absorber(self)
        return weakref_proxy(self)
Absorber.add_observer = new_instancemethod(_absorber.Absorber_add_observer,None,Absorber)
Absorber.remove_observer = new_instancemethod(_absorber.Absorber_remove_observer,None,Absorber)
Absorber.__str__ = new_instancemethod(_absorber.Absorber___str__,None,Absorber)
Absorber._v_number_species = new_instancemethod(_absorber.Absorber__v_number_species,None,Absorber)
Absorber.gas_name = new_instancemethod(_absorber.Absorber_gas_name,None,Absorber)
Absorber.gas_index = new_instancemethod(_absorber.Absorber_gas_index,None,Absorber)
Absorber.optical_depth_each_layer = new_instancemethod(_absorber.Absorber_optical_depth_each_layer,None,Absorber)
Absorber.xgas = new_instancemethod(_absorber.Absorber_xgas,None,Absorber)
Absorber.absorber_vmr = new_instancemethod(_absorber.Absorber_absorber_vmr,None,Absorber)
Absorber.clone = new_instancemethod(_absorber.Absorber_clone,None,Absorber)
Absorber.print_desc = new_instancemethod(_absorber.Absorber_print_desc,None,Absorber)
Absorber.notify_update = new_instancemethod(_absorber.Absorber_notify_update,None,Absorber)
Absorber.mark_used = new_instancemethod(_absorber.Absorber_mark_used,None,Absorber)
Absorber.state_vector_name = new_instancemethod(_absorber.Absorber_state_vector_name,None,Absorber)
Absorber.notify_add = new_instancemethod(_absorber.Absorber_notify_add,None,Absorber)
Absorber.notify_remove = new_instancemethod(_absorber.Absorber_notify_remove,None,Absorber)
Absorber_swigregister = _absorber.Absorber_swigregister
Absorber_swigregister(Absorber)

class SubStateVectorAbsorber(Absorber,full_physics_swig.state_vector.SubStateVectorObserver):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        if self.__class__ == SubStateVectorAbsorber:
            _self = None
        else:
            _self = self
        _absorber.SubStateVectorAbsorber_swiginit(self,_absorber.new_SubStateVectorAbsorber(_self, *args))
    def _v_number_species(self):
        """
        virtual int FullPhysics::Absorber::number_species() const
        Number of species. 
        """
        return _absorber.SubStateVectorAbsorber__v_number_species(self)

    def gas_name(self, *args):
        """
        virtual std::string FullPhysics::Absorber::gas_name(int Species_index) const =0
        Name of gases, in the order that optical_depth_each_layer returns
        them. 
        """
        return _absorber.SubStateVectorAbsorber_gas_name(self, *args)

    def gas_index(self, *args):
        """
        int Absorber::gas_index(const std::string &Name) const
        Map a gas name to the index number it appears in
        optical_depth_each_layer.

        This return -1 if the Name is not one of the gases. 
        """
        return _absorber.SubStateVectorAbsorber_gas_index(self, *args)

    def optical_depth_each_layer(self, *args):
        """
        virtual ArrayAd<double, 2> FullPhysics::Absorber::optical_depth_each_layer(double wn, int spec_index) const =0
        This gives the optical depth for each layer, for the given wave
        number.

        Note this only includes the Absorbers portion of this, Atmosphere
        class combines this with Rayleigh and Aerosol scattering.

        This has size of pres->number_active_layer() x number_species()

        We include the derivative of this with respect to the state vector. 
        """
        return _absorber.SubStateVectorAbsorber_optical_depth_each_layer(self, *args)

    def add_observer(self, *args):
        """
        virtual void FullPhysics::Absorber::add_observer(Observer< Absorber > &Obs)

        """
        return _absorber.SubStateVectorAbsorber_add_observer(self, *args)

    def remove_observer(self, *args):
        """
        virtual void FullPhysics::Absorber::remove_observer(Observer< Absorber > &Obs)

        """
        return _absorber.SubStateVectorAbsorber_remove_observer(self, *args)

    def clone(self, *args):
        """
        virtual boost::shared_ptr<Absorber> FullPhysics::Absorber::clone(const boost::shared_ptr< Pressure > &Press, const boost::shared_ptr<
        Temperature > &Temp, const std::vector< boost::shared_ptr< Altitude >
        > &Alt) const =0
        This version of clone takes a Pressure, Altitude and Temperature to
        use.

        The intent is that the Pressure, Altitude and Temperature has been
        cloned from the original Pressure, Altitude and Temperature (although
        this class has no way to verify this). This allows sets of objects to
        be cloned using a common Pressure, Altitude and Temperature clones,
        e.g. Atmosphere. 
        """
        return _absorber.SubStateVectorAbsorber_clone(self, *args)

    __swig_destroy__ = _absorber.delete_SubStateVectorAbsorber
    def __disown__(self):
        self.this.disown()
        _absorber.disown_SubStateVectorAbsorber(self)
        return weakref_proxy(self)
SubStateVectorAbsorber._v_number_species = new_instancemethod(_absorber.SubStateVectorAbsorber__v_number_species,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.gas_name = new_instancemethod(_absorber.SubStateVectorAbsorber_gas_name,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.gas_index = new_instancemethod(_absorber.SubStateVectorAbsorber_gas_index,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.optical_depth_each_layer = new_instancemethod(_absorber.SubStateVectorAbsorber_optical_depth_each_layer,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.print_desc = new_instancemethod(_absorber.SubStateVectorAbsorber_print_desc,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.add_observer = new_instancemethod(_absorber.SubStateVectorAbsorber_add_observer,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.remove_observer = new_instancemethod(_absorber.SubStateVectorAbsorber_remove_observer,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.clone = new_instancemethod(_absorber.SubStateVectorAbsorber_clone,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.notify_update = new_instancemethod(_absorber.SubStateVectorAbsorber_notify_update,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.mark_used = new_instancemethod(_absorber.SubStateVectorAbsorber_mark_used,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.state_vector_name = new_instancemethod(_absorber.SubStateVectorAbsorber_state_vector_name,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.notify_add = new_instancemethod(_absorber.SubStateVectorAbsorber_notify_add,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.notify_remove = new_instancemethod(_absorber.SubStateVectorAbsorber_notify_remove,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.init = new_instancemethod(_absorber.SubStateVectorAbsorber_init,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.mark_used_sub = new_instancemethod(_absorber.SubStateVectorAbsorber_mark_used_sub,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.state_vector_name_i = new_instancemethod(_absorber.SubStateVectorAbsorber_state_vector_name_i,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.state_vector_name_sub = new_instancemethod(_absorber.SubStateVectorAbsorber_state_vector_name_sub,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.update_sub_state = new_instancemethod(_absorber.SubStateVectorAbsorber_update_sub_state,None,SubStateVectorAbsorber)
SubStateVectorAbsorber.update_sub_state_hook = new_instancemethod(_absorber.SubStateVectorAbsorber_update_sub_state_hook,None,SubStateVectorAbsorber)
SubStateVectorAbsorber._v_coefficient = new_instancemethod(_absorber.SubStateVectorAbsorber__v_coefficient,None,SubStateVectorAbsorber)
SubStateVectorAbsorber._v_used_flag_value = new_instancemethod(_absorber.SubStateVectorAbsorber__v_used_flag_value,None,SubStateVectorAbsorber)
SubStateVectorAbsorber._v_pressure = new_instancemethod(_absorber.SubStateVectorAbsorber__v_pressure,None,SubStateVectorAbsorber)
SubStateVectorAbsorber_swigregister = _absorber.SubStateVectorAbsorber_swigregister
SubStateVectorAbsorber_swigregister(SubStateVectorAbsorber)



