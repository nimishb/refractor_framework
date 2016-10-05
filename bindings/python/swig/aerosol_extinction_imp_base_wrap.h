/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.9
 * 
 * This file is not intended to be easily readable and contains a number of 
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG 
 * interface file instead. 
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_aerosol_extinction_imp_base_WRAP_H_
#define SWIG_aerosol_extinction_imp_base_WRAP_H_

#include <map>
#include <string>


class SwigDirector_AerosolExtinctionImpBase : public FullPhysics::AerosolExtinctionImpBase, public Swig::Director {

public:
    SwigDirector_AerosolExtinctionImpBase(PyObject *self, std::string const &Aerosol_name, blitz::Array< double,1 > const &Coeff, blitz::Array< bool,1 > const &Used_flag, boost::shared_ptr< FullPhysics::Pressure > const &Press, bool Mark_according_to_press = true, int Pdep_start = 0);
    virtual ~SwigDirector_AerosolExtinctionImpBase();
    virtual void notify_add(FullPhysics::StateVector &Observed_object);
    virtual void notify_remove(FullPhysics::StateVector &Observed_object);
    virtual void notify_update(FullPhysics::StateVector const &Observed_object);
    virtual void mark_used(FullPhysics::StateVector const &Sv, blitz::Array< bool,1 > &Used) const;
    virtual void state_vector_name(FullPhysics::StateVector const &Sv, blitz::Array< std::string,1 > &Sv_name) const;
    virtual void add_observer(FullPhysics::Observer< FullPhysics::AerosolExtinction > &Obs);
    virtual void remove_observer(FullPhysics::Observer< FullPhysics::AerosolExtinction > &Obs);
    virtual boost::shared_ptr< FullPhysics::AerosolExtinction > clone() const;
    virtual boost::shared_ptr< FullPhysics::AerosolExtinction > clone(boost::shared_ptr< FullPhysics::Pressure > const &Press) const;
    virtual FullPhysics::AutoDerivative< double > extinction_for_layer(int i) const;
    virtual std::string aerosol_name() const;
    virtual void print(std::ostream &Os) const;
    virtual void update_sub_state(FullPhysics::ArrayAd< double,1 > const &Sv_sub, blitz::Array< double,2 > const &Cov_sub);
    virtual void mark_used_sub(blitz::Array< bool,1 > &Used) const;
    virtual void state_vector_name_sub(blitz::Array< std::string,1 > &Sv_name) const;
    virtual std::string state_vector_name_i(int i) const;
    virtual void update_sub_state_hook();
    virtual FullPhysics::ArrayAd< double,1 > aerosol_extinction() const;
    virtual std::string model_short_name() const;
    virtual void calc_aerosol_extinction() const;
    using FullPhysics::AerosolExtinctionImpBase::cache_stale;
    using FullPhysics::AerosolExtinctionImpBase::aext;
    using FullPhysics::AerosolExtinctionImpBase::total_aod;


/* Internal Director utilities */
public:
    bool swig_get_inner(const char* swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }

    void swig_set_inner(const char* swig_protected_method_name, bool val) const
    { swig_inner[swig_protected_method_name] = val;}

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
          std::string msg = "Method in class AerosolExtinctionImpBase doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[19];
#endif

};


#endif
