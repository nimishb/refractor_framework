/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 3.0.8
 *
 * This file is not intended to be easily readable and contains a number of
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG
 * interface file instead.
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_absorber_WRAP_H_
#define SWIG_absorber_WRAP_H_

#include <map>
#include <string>


class SwigDirector_Absorber : public FullPhysics::Absorber, public Swig::Director {

public:
    SwigDirector_Absorber(PyObject *self);
    virtual ~SwigDirector_Absorber();
    virtual void notify_add(FullPhysics::StateVector &Observed_object);
    virtual void notify_remove(FullPhysics::StateVector &Observed_object);
    virtual void notify_update(FullPhysics::StateVector const &Sv);
    virtual void mark_used(FullPhysics::StateVector const &Sv, blitz::Array< bool,1 > &Used) const;
    virtual void state_vector_name(FullPhysics::StateVector const &Sv, blitz::Array< std::string,1 > &Sv_name) const;
    virtual void add_observer(FullPhysics::Observer< FullPhysics::Absorber > &Obs);
    virtual void remove_observer(FullPhysics::Observer< FullPhysics::Absorber > &Obs);
    virtual int number_species() const;
    virtual std::string gas_name(int Species_index) const;
    virtual int gas_index(std::string const &Name) const;
    virtual FullPhysics::ArrayAd< double,2 > optical_depth_each_layer(double wn, int spec_index) const;
    virtual FullPhysics::AutoDerivative< double > xgas(std::string const &Gas_name) const;
    virtual boost::shared_ptr< FullPhysics::AbsorberVmr > absorber_vmr(std::string const &gas_name) const;
    virtual boost::shared_ptr< FullPhysics::Absorber > clone() const;
    virtual boost::shared_ptr< FullPhysics::Absorber > clone(boost::shared_ptr< FullPhysics::Pressure > const &Press, boost::shared_ptr< FullPhysics::Temperature > const &Temp, std::vector< boost::shared_ptr< FullPhysics::Altitude >,std::allocator< boost::shared_ptr< FullPhysics::Altitude > > > const &Alt) const;
    virtual void print(std::ostream &Os) const;

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class Absorber doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[16];
#endif

};


class SwigDirector_SubStateVectorAbsorber : public FullPhysics::SubStateVectorArray< FullPhysics::Absorber >, public Swig::Director {

public:
    SwigDirector_SubStateVectorAbsorber(PyObject *self, blitz::Array< double,1 > const &Coeff, blitz::Array< bool,1 > const &Used_flag);
    SwigDirector_SubStateVectorAbsorber(PyObject *self, blitz::Array< double,1 > const &Coeff, blitz::Array< bool,1 > const &Used_flag, boost::shared_ptr< FullPhysics::Pressure > const &Press);
    SwigDirector_SubStateVectorAbsorber(PyObject *self);
    virtual ~SwigDirector_SubStateVectorAbsorber();
    virtual void notify_add(FullPhysics::StateVector &Observed_object);
    virtual void notify_remove(FullPhysics::StateVector &Observed_object);
    virtual void notify_update(FullPhysics::StateVector const &Sv);
    virtual void mark_used(FullPhysics::StateVector const &Sv, blitz::Array< bool,1 > &Used) const;
    virtual void state_vector_name(FullPhysics::StateVector const &Sv, blitz::Array< std::string,1 > &Sv_name) const;
    virtual void add_observer(FullPhysics::Observer< FullPhysics::Absorber > &Obs);
    virtual void remove_observer(FullPhysics::Observer< FullPhysics::Absorber > &Obs);
    virtual int number_species() const;
    virtual std::string gas_name(int Species_index) const;
    virtual int gas_index(std::string const &Name) const;
    virtual FullPhysics::ArrayAd< double,2 > optical_depth_each_layer(double wn, int spec_index) const;
    virtual FullPhysics::AutoDerivative< double > xgas(std::string const &Gas_name) const;
    virtual boost::shared_ptr< FullPhysics::AbsorberVmr > absorber_vmr(std::string const &gas_name) const;
    virtual boost::shared_ptr< FullPhysics::Absorber > clone() const;
    virtual boost::shared_ptr< FullPhysics::Absorber > clone(boost::shared_ptr< FullPhysics::Pressure > const &Press, boost::shared_ptr< FullPhysics::Temperature > const &Temp, std::vector< boost::shared_ptr< FullPhysics::Altitude >,std::allocator< boost::shared_ptr< FullPhysics::Altitude > > > const &Alt) const;
    virtual void print(std::ostream &Os) const;
    virtual void update_sub_state(FullPhysics::ArrayAd< double,1 > const &Sv_sub, blitz::Array< double,2 > const &Cov);
    virtual void mark_used_sub(blitz::Array< bool,1 > &Used) const;
    virtual void state_vector_name_sub(blitz::Array< std::string,1 > &Sv_name) const;
    virtual std::string state_vector_name_i(int i) const;
    virtual void update_sub_state_hook();

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class SubStateVectorAbsorber doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[21];
#endif

};


#endif
