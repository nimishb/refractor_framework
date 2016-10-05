# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _logger.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_logger', [dirname(__file__)])
        except ImportError:
            import _logger
            return _logger
        if fp is not None:
            try:
                _mod = imp.load_module('_logger', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _logger = swig_import_helper()
    del swig_import_helper
else:
    import _logger
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


SHARED_PTR_DISOWN = _logger.SHARED_PTR_DISOWN
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

class LogImp(object):
    """
    The actual implementation of the Logger.

    C++ includes: logger.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _logger.delete_LogImp
    DEBUG = _logger.LogImp_DEBUG
    INFO = _logger.LogImp_INFO
    WARNING = _logger.LogImp_WARNING
    ERROR = _logger.LogImp_ERROR
    FATAL = _logger.LogImp_FATAL
    def write(self, *args):
        """
        void FullPhysics::LogImp::write(log_level l, const char *v)

        """
        return _logger.LogImp_write(self, *args)

    def flush(self, *args):
        """
        virtual void FullPhysics::LogImp::flush(log_level l)=0
        Flush data to the log, at the given level. 
        """
        return _logger.LogImp_flush(self, *args)

LogImp.write = new_instancemethod(_logger.LogImp_write,None,LogImp)
LogImp.flush = new_instancemethod(_logger.LogImp_flush,None,LogImp)
LogImp_swigregister = _logger.LogImp_swigregister
LogImp_swigregister(LogImp)

class Logger(object):
    """
    This is a simple logger.

    The logger depends on a specific implementation being set by
    set_implementation. If we don't have an implementation set, then the
    logger doesn't do anything.

    The logger is a singleton, there is just one global logger. You can
    directly access it through instance, but normally you just do things
    like "Logger::debug() << 'My debug message\\n'". Data is flushed
    when a "\\n" is encountered, you should end all messages with
    "\\n".

    C++ includes: logger.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def set_implementation(*args):
        """
        static void FullPhysics::Logger::set_implementation(LogImp *imp)
        Set the implementation.

        It is perfectly legal for this to be a null pointer, in that case we
        just don't send log messages anywhere. 
        """
        return _logger.Logger_set_implementation(*args)

    set_implementation = staticmethod(set_implementation)
    __swig_destroy__ = _logger.delete_Logger
Logger_swigregister = _logger.Logger_swigregister
Logger_swigregister(Logger)

def Logger_set_implementation(*args):
  """
    static void FullPhysics::Logger::set_implementation(LogImp *imp)
    Set the implementation.

    It is perfectly legal for this to be a null pointer, in that case we
    just don't send log messages anywhere. 
    """
  return _logger.Logger_set_implementation(*args)



