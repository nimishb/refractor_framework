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
            fp, pathname, description = imp.find_module('_array_ad', [dirname(__file__)])
        except ImportError:
            import _array_ad
            return _array_ad
        if fp is not None:
            try:
                _mod = imp.load_module('_array_ad', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _array_ad = swig_import_helper()
    del swig_import_helper
else:
    import _array_ad
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



_array_ad.SHARED_PTR_DISOWN_swigconstant(_array_ad)
SHARED_PTR_DISOWN = _array_ad.SHARED_PTR_DISOWN

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

import numpy as np

def np_to_array_ad(a):
    '''Convert a numpy array of AutoDerivatives to a ArrayAd'''
    nvar = 0
    for i in a.flat:
        if(i.number_variable > 0):
            nvar = i.number_variable
            break
    if(len(a.shape) == 1):
        res = ArrayAd_double_1(a.shape[0], nvar)
        for i1 in range(res.rows):
            res[i1]  = a[i1]
    elif(len(a.shape) == 2):
        res = ArrayAd_double_2(a.shape[0], a.shape[1], nvar)
        for i1 in range(res.rows):
            for i2 in range(res.cols):
                res[i1,i2]  = a[i1, i2]
    elif(len(a.shape) == 3):
        res = ArrayAd_double_3(a.shape[0], a.shape[1], a.shape[2], nvar)
        for i1 in range(res.rows):
            for i2 in range(res.cols):
                for i3 in range(res.depth):
                    res[i1,i2, i3]  = a[i1, i2, i3]
    else:
        raise IndexError("np_to_array_ad only implemented for dimension <= 3")
    return res

class ArrayAd_double_1(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ArrayAd_double_1, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ArrayAd_double_1, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """

        FullPhysics::ArrayAd< T, D >::ArrayAd(const blitz::TinyVector< int, D > &Shape, int nvar)

        """
        this = _array_ad.new_ArrayAd_double_1(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def resize_number_variable(self, nvar):
        """

        void FullPhysics::ArrayAd< T, D >::resize_number_variable(int nvar)

        """
        return _array_ad.ArrayAd_double_1_resize_number_variable(self, nvar)


    def resize(self, *args):
        """

        void FullPhysics::ArrayAd< T, D >::resize(int n1, int n2, int n3, int n4, int n5, int nvar)

        """
        return _array_ad.ArrayAd_double_1_resize(self, *args)


    def _v_value(self):
        """

        blitz::Array<T, D>& FullPhysics::ArrayAd< T, D >::value()

        """
        return _array_ad.ArrayAd_double_1__v_value(self)


    @property
    def value(self):
        return self._v_value()


    def _v_jacobian(self):
        """

        blitz::Array<T, D+1>& FullPhysics::ArrayAd< T, D >::jacobian()

        """
        return _array_ad.ArrayAd_double_1__v_jacobian(self)


    @property
    def jacobian(self):
        return self._v_jacobian()


    def _v_rows(self):
        """

        int FullPhysics::ArrayAd< T, D >::rows() const

        """
        return _array_ad.ArrayAd_double_1__v_rows(self)


    @property
    def rows(self):
        return self._v_rows()


    def _v_cols(self):
        """

        int FullPhysics::ArrayAd< T, D >::cols() const

        """
        return _array_ad.ArrayAd_double_1__v_cols(self)


    @property
    def cols(self):
        return self._v_cols()


    def _v_depth(self):
        """

        int FullPhysics::ArrayAd< T, D >::depth() const

        """
        return _array_ad.ArrayAd_double_1__v_depth(self)


    @property
    def depth(self):
        return self._v_depth()


    def _v_is_constant(self):
        """

        bool FullPhysics::ArrayAd< T, D >::is_constant() const

        """
        return _array_ad.ArrayAd_double_1__v_is_constant(self)


    @property
    def is_constant(self):
        return self._v_is_constant()


    def _v_number_variable(self):
        """

        int FullPhysics::ArrayAd< T, D >::number_variable() const

        """
        return _array_ad.ArrayAd_double_1__v_number_variable(self)


    @property
    def number_variable(self):
        return self._v_number_variable()


    def reference(self, V):
        """

        void FullPhysics::ArrayAd< T, D >::reference(const ArrayAd< T, D > &V)

        """
        return _array_ad.ArrayAd_double_1_reference(self, V)


    def copy(self):
        """

        ArrayAd<T, D> FullPhysics::ArrayAd< T, D >::copy() const

        """
        return _array_ad.ArrayAd_double_1_copy(self)


    def __array__(self):
        if(1 == 1):
            res = np.empty([self.rows], np.object)
            for i1 in range(self.rows):
                res[i1] = self[i1]
        elif(1 ==2):
            res = np.empty([self.rows, self.cols], np.object)
            for i1 in range(self.rows):
                for i2 in range(self.cols):
                    res[i1,i2] = self[i1, i2]
        elif(1 ==3):
            res = np.empty([self.rows, self.cols, self.depth], np.object)
            for i1 in range(self.rows):
                for i2 in range(self.cols):
                    for i3 in range(self.depth):
                        res[i1,i2, i3] = self[i1, i2, i3]
        else:
          raise IndexError("__array__ only implemented to dimensions <= 3")
        return res

    def slice_data(self, key):
      if not type(key) is tuple:
        key = (key,)

      ad_val = self.value[key]
      ad_jac = self.jacobian[key + (slice(None),)]

      num_dim = len(ad_val.shape)

      return eval("ArrayAd_double_%d" % num_dim)(ad_val, ad_jac)

    def __getitem__(self, index):
      if(1 == 1):
        if type(index) is slice:
          return self.slice_data(index)
        else:
          return self.read(index)
      else:
        if any(type(x) is slice for x in index):
          return self.slice_data(index)
        else:
          return self.read(*index)

    def __setitem__(self, index, val):
      if(1 == 1):
        if type(index) is slice:
          raise NotImplementedError("__setitem__ can not be used for setting values to slices")
        self.write(index, val)
      else:
        if any(type(x) is slice for x in index):
          raise NotImplementedError("__setitem__ can not be used for setting values to slices")
        t = list(index)
        t.append(val)
        self.write(*t)


    def read(self, *args):
        return _array_ad.ArrayAd_double_1_read(self, *args)

    def write(self, *args):
        return _array_ad.ArrayAd_double_1_write(self, *args)

    @classmethod
    def pickle_format_version(cls):
      return 1

    def __reduce__(self):
      return _new_from_init, (self.__class__, 1, self.value,self.jacobian,self.is_constant)

    __swig_destroy__ = _array_ad.delete_ArrayAd_double_1
    __del__ = lambda self: None
ArrayAd_double_1_swigregister = _array_ad.ArrayAd_double_1_swigregister
ArrayAd_double_1_swigregister(ArrayAd_double_1)

class ArrayAd_double_2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ArrayAd_double_2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ArrayAd_double_2, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """

        FullPhysics::ArrayAd< T, D >::ArrayAd(const blitz::TinyVector< int, D > &Shape, int nvar)

        """
        this = _array_ad.new_ArrayAd_double_2(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def resize_number_variable(self, nvar):
        """

        void FullPhysics::ArrayAd< T, D >::resize_number_variable(int nvar)

        """
        return _array_ad.ArrayAd_double_2_resize_number_variable(self, nvar)


    def resize(self, *args):
        """

        void FullPhysics::ArrayAd< T, D >::resize(int n1, int n2, int n3, int n4, int n5, int nvar)

        """
        return _array_ad.ArrayAd_double_2_resize(self, *args)


    def _v_value(self):
        """

        blitz::Array<T, D>& FullPhysics::ArrayAd< T, D >::value()

        """
        return _array_ad.ArrayAd_double_2__v_value(self)


    @property
    def value(self):
        return self._v_value()


    def _v_jacobian(self):
        """

        blitz::Array<T, D+1>& FullPhysics::ArrayAd< T, D >::jacobian()

        """
        return _array_ad.ArrayAd_double_2__v_jacobian(self)


    @property
    def jacobian(self):
        return self._v_jacobian()


    def _v_rows(self):
        """

        int FullPhysics::ArrayAd< T, D >::rows() const

        """
        return _array_ad.ArrayAd_double_2__v_rows(self)


    @property
    def rows(self):
        return self._v_rows()


    def _v_cols(self):
        """

        int FullPhysics::ArrayAd< T, D >::cols() const

        """
        return _array_ad.ArrayAd_double_2__v_cols(self)


    @property
    def cols(self):
        return self._v_cols()


    def _v_depth(self):
        """

        int FullPhysics::ArrayAd< T, D >::depth() const

        """
        return _array_ad.ArrayAd_double_2__v_depth(self)


    @property
    def depth(self):
        return self._v_depth()


    def _v_is_constant(self):
        """

        bool FullPhysics::ArrayAd< T, D >::is_constant() const

        """
        return _array_ad.ArrayAd_double_2__v_is_constant(self)


    @property
    def is_constant(self):
        return self._v_is_constant()


    def _v_number_variable(self):
        """

        int FullPhysics::ArrayAd< T, D >::number_variable() const

        """
        return _array_ad.ArrayAd_double_2__v_number_variable(self)


    @property
    def number_variable(self):
        return self._v_number_variable()


    def reference(self, V):
        """

        void FullPhysics::ArrayAd< T, D >::reference(const ArrayAd< T, D > &V)

        """
        return _array_ad.ArrayAd_double_2_reference(self, V)


    def copy(self):
        """

        ArrayAd<T, D> FullPhysics::ArrayAd< T, D >::copy() const

        """
        return _array_ad.ArrayAd_double_2_copy(self)


    def __array__(self):
        if(2 == 1):
            res = np.empty([self.rows], np.object)
            for i1 in range(self.rows):
                res[i1] = self[i1]
        elif(2 ==2):
            res = np.empty([self.rows, self.cols], np.object)
            for i1 in range(self.rows):
                for i2 in range(self.cols):
                    res[i1,i2] = self[i1, i2]
        elif(2 ==3):
            res = np.empty([self.rows, self.cols, self.depth], np.object)
            for i1 in range(self.rows):
                for i2 in range(self.cols):
                    for i3 in range(self.depth):
                        res[i1,i2, i3] = self[i1, i2, i3]
        else:
          raise IndexError("__array__ only implemented to dimensions <= 3")
        return res

    def slice_data(self, key):
      if not type(key) is tuple:
        key = (key,)

      ad_val = self.value[key]
      ad_jac = self.jacobian[key + (slice(None),)]

      num_dim = len(ad_val.shape)

      return eval("ArrayAd_double_%d" % num_dim)(ad_val, ad_jac)

    def __getitem__(self, index):
      if(2 == 1):
        if type(index) is slice:
          return self.slice_data(index)
        else:
          return self.read(index)
      else:
        if any(type(x) is slice for x in index):
          return self.slice_data(index)
        else:
          return self.read(*index)

    def __setitem__(self, index, val):
      if(2 == 1):
        if type(index) is slice:
          raise NotImplementedError("__setitem__ can not be used for setting values to slices")
        self.write(index, val)
      else:
        if any(type(x) is slice for x in index):
          raise NotImplementedError("__setitem__ can not be used for setting values to slices")
        t = list(index)
        t.append(val)
        self.write(*t)


    def read(self, *args):
        return _array_ad.ArrayAd_double_2_read(self, *args)

    def write(self, *args):
        return _array_ad.ArrayAd_double_2_write(self, *args)

    @classmethod
    def pickle_format_version(cls):
      return 1

    def __reduce__(self):
      return _new_from_init, (self.__class__, 1, self.value,self.jacobian,self.is_constant)

    __swig_destroy__ = _array_ad.delete_ArrayAd_double_2
    __del__ = lambda self: None
ArrayAd_double_2_swigregister = _array_ad.ArrayAd_double_2_swigregister
ArrayAd_double_2_swigregister(ArrayAd_double_2)

class ArrayAd_double_3(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ArrayAd_double_3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ArrayAd_double_3, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """

        FullPhysics::ArrayAd< T, D >::ArrayAd(const blitz::TinyVector< int, D > &Shape, int nvar)

        """
        this = _array_ad.new_ArrayAd_double_3(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def resize_number_variable(self, nvar):
        """

        void FullPhysics::ArrayAd< T, D >::resize_number_variable(int nvar)

        """
        return _array_ad.ArrayAd_double_3_resize_number_variable(self, nvar)


    def resize(self, *args):
        """

        void FullPhysics::ArrayAd< T, D >::resize(int n1, int n2, int n3, int n4, int n5, int nvar)

        """
        return _array_ad.ArrayAd_double_3_resize(self, *args)


    def _v_value(self):
        """

        blitz::Array<T, D>& FullPhysics::ArrayAd< T, D >::value()

        """
        return _array_ad.ArrayAd_double_3__v_value(self)


    @property
    def value(self):
        return self._v_value()


    def _v_jacobian(self):
        """

        blitz::Array<T, D+1>& FullPhysics::ArrayAd< T, D >::jacobian()

        """
        return _array_ad.ArrayAd_double_3__v_jacobian(self)


    @property
    def jacobian(self):
        return self._v_jacobian()


    def _v_rows(self):
        """

        int FullPhysics::ArrayAd< T, D >::rows() const

        """
        return _array_ad.ArrayAd_double_3__v_rows(self)


    @property
    def rows(self):
        return self._v_rows()


    def _v_cols(self):
        """

        int FullPhysics::ArrayAd< T, D >::cols() const

        """
        return _array_ad.ArrayAd_double_3__v_cols(self)


    @property
    def cols(self):
        return self._v_cols()


    def _v_depth(self):
        """

        int FullPhysics::ArrayAd< T, D >::depth() const

        """
        return _array_ad.ArrayAd_double_3__v_depth(self)


    @property
    def depth(self):
        return self._v_depth()


    def _v_is_constant(self):
        """

        bool FullPhysics::ArrayAd< T, D >::is_constant() const

        """
        return _array_ad.ArrayAd_double_3__v_is_constant(self)


    @property
    def is_constant(self):
        return self._v_is_constant()


    def _v_number_variable(self):
        """

        int FullPhysics::ArrayAd< T, D >::number_variable() const

        """
        return _array_ad.ArrayAd_double_3__v_number_variable(self)


    @property
    def number_variable(self):
        return self._v_number_variable()


    def reference(self, V):
        """

        void FullPhysics::ArrayAd< T, D >::reference(const ArrayAd< T, D > &V)

        """
        return _array_ad.ArrayAd_double_3_reference(self, V)


    def copy(self):
        """

        ArrayAd<T, D> FullPhysics::ArrayAd< T, D >::copy() const

        """
        return _array_ad.ArrayAd_double_3_copy(self)


    def __array__(self):
        if(3 == 1):
            res = np.empty([self.rows], np.object)
            for i1 in range(self.rows):
                res[i1] = self[i1]
        elif(3 ==2):
            res = np.empty([self.rows, self.cols], np.object)
            for i1 in range(self.rows):
                for i2 in range(self.cols):
                    res[i1,i2] = self[i1, i2]
        elif(3 ==3):
            res = np.empty([self.rows, self.cols, self.depth], np.object)
            for i1 in range(self.rows):
                for i2 in range(self.cols):
                    for i3 in range(self.depth):
                        res[i1,i2, i3] = self[i1, i2, i3]
        else:
          raise IndexError("__array__ only implemented to dimensions <= 3")
        return res

    def slice_data(self, key):
      if not type(key) is tuple:
        key = (key,)

      ad_val = self.value[key]
      ad_jac = self.jacobian[key + (slice(None),)]

      num_dim = len(ad_val.shape)

      return eval("ArrayAd_double_%d" % num_dim)(ad_val, ad_jac)

    def __getitem__(self, index):
      if(3 == 1):
        if type(index) is slice:
          return self.slice_data(index)
        else:
          return self.read(index)
      else:
        if any(type(x) is slice for x in index):
          return self.slice_data(index)
        else:
          return self.read(*index)

    def __setitem__(self, index, val):
      if(3 == 1):
        if type(index) is slice:
          raise NotImplementedError("__setitem__ can not be used for setting values to slices")
        self.write(index, val)
      else:
        if any(type(x) is slice for x in index):
          raise NotImplementedError("__setitem__ can not be used for setting values to slices")
        t = list(index)
        t.append(val)
        self.write(*t)


    def read(self, *args):
        return _array_ad.ArrayAd_double_3_read(self, *args)

    def write(self, *args):
        return _array_ad.ArrayAd_double_3_write(self, *args)

    @classmethod
    def pickle_format_version(cls):
      return 1

    def __reduce__(self):
      return _new_from_init, (self.__class__, 1, self.value,self.jacobian,self.is_constant)

    __swig_destroy__ = _array_ad.delete_ArrayAd_double_3
    __del__ = lambda self: None
ArrayAd_double_3_swigregister = _array_ad.ArrayAd_double_3_swigregister
ArrayAd_double_3_swigregister(ArrayAd_double_3)

class ArrayAd_double_4(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ArrayAd_double_4, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ArrayAd_double_4, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """

        FullPhysics::ArrayAd< T, D >::ArrayAd(const blitz::TinyVector< int, D > &Shape, int nvar)

        """
        this = _array_ad.new_ArrayAd_double_4(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def resize_number_variable(self, nvar):
        """

        void FullPhysics::ArrayAd< T, D >::resize_number_variable(int nvar)

        """
        return _array_ad.ArrayAd_double_4_resize_number_variable(self, nvar)


    def resize(self, *args):
        """

        void FullPhysics::ArrayAd< T, D >::resize(int n1, int n2, int n3, int n4, int n5, int nvar)

        """
        return _array_ad.ArrayAd_double_4_resize(self, *args)


    def _v_value(self):
        """

        blitz::Array<T, D>& FullPhysics::ArrayAd< T, D >::value()

        """
        return _array_ad.ArrayAd_double_4__v_value(self)


    @property
    def value(self):
        return self._v_value()


    def _v_jacobian(self):
        """

        blitz::Array<T, D+1>& FullPhysics::ArrayAd< T, D >::jacobian()

        """
        return _array_ad.ArrayAd_double_4__v_jacobian(self)


    @property
    def jacobian(self):
        return self._v_jacobian()


    def _v_rows(self):
        """

        int FullPhysics::ArrayAd< T, D >::rows() const

        """
        return _array_ad.ArrayAd_double_4__v_rows(self)


    @property
    def rows(self):
        return self._v_rows()


    def _v_cols(self):
        """

        int FullPhysics::ArrayAd< T, D >::cols() const

        """
        return _array_ad.ArrayAd_double_4__v_cols(self)


    @property
    def cols(self):
        return self._v_cols()


    def _v_depth(self):
        """

        int FullPhysics::ArrayAd< T, D >::depth() const

        """
        return _array_ad.ArrayAd_double_4__v_depth(self)


    @property
    def depth(self):
        return self._v_depth()


    def _v_is_constant(self):
        """

        bool FullPhysics::ArrayAd< T, D >::is_constant() const

        """
        return _array_ad.ArrayAd_double_4__v_is_constant(self)


    @property
    def is_constant(self):
        return self._v_is_constant()


    def _v_number_variable(self):
        """

        int FullPhysics::ArrayAd< T, D >::number_variable() const

        """
        return _array_ad.ArrayAd_double_4__v_number_variable(self)


    @property
    def number_variable(self):
        return self._v_number_variable()


    def reference(self, V):
        """

        void FullPhysics::ArrayAd< T, D >::reference(const ArrayAd< T, D > &V)

        """
        return _array_ad.ArrayAd_double_4_reference(self, V)


    def copy(self):
        """

        ArrayAd<T, D> FullPhysics::ArrayAd< T, D >::copy() const

        """
        return _array_ad.ArrayAd_double_4_copy(self)


    def __array__(self):
        if(4 == 1):
            res = np.empty([self.rows], np.object)
            for i1 in range(self.rows):
                res[i1] = self[i1]
        elif(4 ==2):
            res = np.empty([self.rows, self.cols], np.object)
            for i1 in range(self.rows):
                for i2 in range(self.cols):
                    res[i1,i2] = self[i1, i2]
        elif(4 ==3):
            res = np.empty([self.rows, self.cols, self.depth], np.object)
            for i1 in range(self.rows):
                for i2 in range(self.cols):
                    for i3 in range(self.depth):
                        res[i1,i2, i3] = self[i1, i2, i3]
        else:
          raise IndexError("__array__ only implemented to dimensions <= 3")
        return res

    def slice_data(self, key):
      if not type(key) is tuple:
        key = (key,)

      ad_val = self.value[key]
      ad_jac = self.jacobian[key + (slice(None),)]

      num_dim = len(ad_val.shape)

      return eval("ArrayAd_double_%d" % num_dim)(ad_val, ad_jac)

    def __getitem__(self, index):
      if(4 == 1):
        if type(index) is slice:
          return self.slice_data(index)
        else:
          return self.read(index)
      else:
        if any(type(x) is slice for x in index):
          return self.slice_data(index)
        else:
          return self.read(*index)

    def __setitem__(self, index, val):
      if(4 == 1):
        if type(index) is slice:
          raise NotImplementedError("__setitem__ can not be used for setting values to slices")
        self.write(index, val)
      else:
        if any(type(x) is slice for x in index):
          raise NotImplementedError("__setitem__ can not be used for setting values to slices")
        t = list(index)
        t.append(val)
        self.write(*t)


    def read(self, *args):
        return _array_ad.ArrayAd_double_4_read(self, *args)

    def write(self, *args):
        return _array_ad.ArrayAd_double_4_write(self, *args)

    @classmethod
    def pickle_format_version(cls):
      return 1

    def __reduce__(self):
      return _new_from_init, (self.__class__, 1, self.value,self.jacobian,self.is_constant)

    __swig_destroy__ = _array_ad.delete_ArrayAd_double_4
    __del__ = lambda self: None
ArrayAd_double_4_swigregister = _array_ad.ArrayAd_double_4_swigregister
ArrayAd_double_4_swigregister(ArrayAd_double_4)

# This file is compatible with both classic and new-style classes.


