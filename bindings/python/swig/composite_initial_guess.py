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
            fp, pathname, description = imp.find_module('_composite_initial_guess', [dirname(__file__)])
        except ImportError:
            import _composite_initial_guess
            return _composite_initial_guess
        if fp is not None:
            try:
                _mod = imp.load_module('_composite_initial_guess', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _composite_initial_guess = swig_import_helper()
    del swig_import_helper
else:
    import _composite_initial_guess
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



_composite_initial_guess.SHARED_PTR_DISOWN_swigconstant(_composite_initial_guess)
SHARED_PTR_DISOWN = _composite_initial_guess.SHARED_PTR_DISOWN

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
import full_physics_swig.initial_guess
class InitialGuessBuilder(full_physics_swig.generic_object.GenericObject):
    """

    Class that builds a portion of the state vector.

    We use a std::vector here rather than a blitz::Array just because it
    is easier to add something to the end of std::vector than
    blitz::Array. CompositeInitialGuess converts this to a blitz::Array
    before finishing the construction of the initial guess.

    C++ includes: composite_initial_guess.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, InitialGuessBuilder, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.generic_object.GenericObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, InitialGuessBuilder, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _composite_initial_guess.delete_InitialGuessBuilder
    __del__ = lambda self: None

    def _v_number_element(self):
        """

        virtual int FullPhysics::InitialGuessBuilder::number_element() const =0
        Number of elements we will be adding to the state vector.

        0 is a legal value, if we are changing elements but not adding any. 
        """
        return _composite_initial_guess.InitialGuessBuilder__v_number_element(self)


    @property
    def number_element(self):
        return self._v_number_element()


    def build_initial_value(self, v, index):
        """

        virtual void FullPhysics::InitialGuessBuilder::build_initial_value(blitz::Array< double, 1 > &v, int index) const =0
        Called when we need this class to do its part in setting up the
        initial state vector.

        Parameters:
        -----------

        v:  State vector that should be updated in place.

        index:  Since we are often adding to the end of the state vector,
        index is passed in. This is the sum of the number_elements() of all
        the InitialGuessBuilder that appear before this object in the list. 
        """
        return _composite_initial_guess.InitialGuessBuilder_build_initial_value(self, v, index)


    def build_apriori(self, v, index):
        """

        virtual void FullPhysics::InitialGuessBuilder::build_apriori(blitz::Array< double, 1 > &v, int index) const =0
        Called when we need this class to do its part in setting up the
        apriori state vector.

        Parameters:
        -----------

        v:  State vector that should be updated in place.

        index:  Since we are often adding to the end of the state vector,
        index is passed in. This is the sum of the number_elements() of all
        the InitialGuessBuilder that appear before this object in the list. 
        """
        return _composite_initial_guess.InitialGuessBuilder_build_apriori(self, v, index)


    def build_apriori_covariance(self, m, index):
        """

        virtual void FullPhysics::InitialGuessBuilder::build_apriori_covariance(blitz::Array< double, 2 > &m, int index) const =0
        Called when we need this class to do its part in setting up the
        covariance matrix for the a priori state vector.

        Parameters:
        -----------

        m:  State vector that should be updated in place.

        index:  Since we are often adding to the end of the state vector,
        index is passed in. This is the sum of the number_elements() of all
        the InitialGuessBuilder that appear before this object in the list. 
        """
        return _composite_initial_guess.InitialGuessBuilder_build_apriori_covariance(self, m, index)


    def __str__(self):
        return _composite_initial_guess.InitialGuessBuilder___str__(self)
InitialGuessBuilder_swigregister = _composite_initial_guess.InitialGuessBuilder_swigregister
InitialGuessBuilder_swigregister(InitialGuessBuilder)

class CompositeInitialGuess(full_physics_swig.initial_guess.InitialGuess, InitialGuessBuilder):
    """

    A common way to create an initial guess is to have other classes
    responsible for portions of the state vector (e.g., an Atmosphere
    class creates the portion of the initial guess that handles the
    description of the atmosphere layers).

    This class implements this division.

    This is an example of the "Builder" design pattern. This class is
    what is commonly called the "Director", and the InitialGuessBuilder
    classes are the "Builder" classes.

    Note that the InitialGuessBuilder objects are called in the order they
    are added to the CompositeInitialGuess object. A common
    InitialGuessBuilder adds additional values to the end state vector, so
    the order is important.

    A CompositeInitialGuess is also a InitialGuessBuilder, so you can use
    this to nest initial guess builders.

    C++ includes: composite_initial_guess.h 
    """

    __swig_setmethods__ = {}
    for _s in [full_physics_swig.initial_guess.InitialGuess, InitialGuessBuilder]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CompositeInitialGuess, name, value)
    __swig_getmethods__ = {}
    for _s in [full_physics_swig.initial_guess.InitialGuess, InitialGuessBuilder]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CompositeInitialGuess, name)
    __repr__ = _swig_repr

    def build_initial_value(self, v, index):
        """

        virtual void FullPhysics::CompositeInitialGuess::build_initial_value(blitz::Array< double, 1 > &v, int index) const
        Called when we need this class to do its part in setting up the
        initial state vector.

        Parameters:
        -----------

        v:  State vector that should be updated in place.

        index:  Since we are often adding to the end of the state vector,
        index is passed in. This is the sum of the number_elements() of all
        the InitialGuessBuilder that appear before this object in the list. 
        """
        return _composite_initial_guess.CompositeInitialGuess_build_initial_value(self, v, index)


    def build_apriori(self, v, index):
        """

        virtual void FullPhysics::CompositeInitialGuess::build_apriori(blitz::Array< double, 1 > &v, int index) const
        Called when we need this class to do its part in setting up the
        apriori state vector.

        Parameters:
        -----------

        v:  State vector that should be updated in place.

        index:  Since we are often adding to the end of the state vector,
        index is passed in. This is the sum of the number_elements() of all
        the InitialGuessBuilder that appear before this object in the list. 
        """
        return _composite_initial_guess.CompositeInitialGuess_build_apriori(self, v, index)


    def build_apriori_covariance(self, m, index):
        """

        virtual void FullPhysics::CompositeInitialGuess::build_apriori_covariance(blitz::Array< double, 2 > &m, int index) const
        Called when we need this class to do its part in setting up the
        covariance matrix for the a priori state vector.

        Parameters:
        -----------

        m:  State vector that should be updated in place.

        index:  Since we are often adding to the end of the state vector,
        index is passed in. This is the sum of the number_elements() of all
        the InitialGuessBuilder that appear before this object in the list. 
        """
        return _composite_initial_guess.CompositeInitialGuess_build_apriori_covariance(self, m, index)


    def _v_initial_guess(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::CompositeInitialGuess::initial_guess() const

        """
        return _composite_initial_guess.CompositeInitialGuess__v_initial_guess(self)


    @property
    def initial_guess(self):
        return self._v_initial_guess()


    def add_builder(self, B):
        """

        void FullPhysics::CompositeInitialGuess::add_builder(const boost::shared_ptr< InitialGuessBuilder > &B)
        Add a builder to the build list. 
        """
        return _composite_initial_guess.CompositeInitialGuess_add_builder(self, B)


    def remove_builder(self, B):
        """

        void FullPhysics::CompositeInitialGuess::remove_builder(const boost::shared_ptr< InitialGuessBuilder > &B)
        Remove a builder to the build list. 
        """
        return _composite_initial_guess.CompositeInitialGuess_remove_builder(self, B)


    def __init__(self):
        this = _composite_initial_guess.new_CompositeInitialGuess()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _composite_initial_guess.delete_CompositeInitialGuess
    __del__ = lambda self: None
CompositeInitialGuess_swigregister = _composite_initial_guess.CompositeInitialGuess_swigregister
CompositeInitialGuess_swigregister(CompositeInitialGuess)

# This file is compatible with both classic and new-style classes.


