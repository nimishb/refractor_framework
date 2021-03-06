# Files in the current directory to include in the library
set(DIR_SOURCES
    l_rad_fortran/calc_geom_first_enh.F90
    l_rad_fortran/calc_geom_first_reg.F90
    l_rad_fortran/calc_geom_second.F90
    l_rad_fortran/l_calc_phase_first.F90
    l_rad_fortran/l_rad_first_enh.F90
    l_rad_fortran/l_rad_first_reg.F90
    l_rad_fortran/l_rad_second.F90
    l_rad_fortran/l_surface.F90
    l_rad_fortran/l_surface_fourier.F90
    l_rad_fortran/geometry_pool.F90
    l_rad_fortran/l_rad_first_pp.F90
    l_rad_fortran/l_sscorr_nadir.F90
    l_rad_fortran/l_sscorr_outgoing.F90
    l_rad_fortran/l_sscorr_pp.F90
    absco_hdf.cc
    absorber_absco.cc
    absorber_vmr_met.cc
    absorber_vmr_level.cc
    absorber_vmr_level_scaled.cc
    aerosol_extinction_linear.cc
    aerosol_extinction_log.cc
    aerosol_optical.cc
    aerosol_property_hdf.cc
    aerosol_property_rh_hdf.cc
    aerosol_shape_gaussian.cc
    altitude_hydrostatic.cc
    atmosphere_oco.cc
    bad_sample_noise_model.cc
    bard_ml_problem.cc
    bard_nlls_problem.cc
    brdf_functions.F90
    brown_nlls_problem.cc
    chapman_boa.cc
    chapman_boa_rt.cc
    chisq_convergence.cc
    composite_perturbation.cc
    connor_convergence.cc
    connor_solver.cc
    connor_solver_map.cc
    cost_minimizer_gsl.cc
    dispersion_fit.cc
    dispersion_polynomial.cc
    empirical_orthogonal_function.cc
    error_analysis.cc
    fd_forward_model.cc
    # Disabled due to incompatibility with GSL >= 2.0 due to change in interface it uses
    #    fdf_nlls_solver.cc
    fluorescence_effect.cc
    fm_nlls_problem.cc
    forward_model_cost_function.cc
    fp_logger.cc
    freudenstein_roth_nlls_problem.cc
    gas_vmr_apriori.cc
    gosat_noise_model.cc
    ground_brdf.cc
    ground_coxmunk.cc
    ground_coxmunk_plus_lambertian.cc
    ground_lambertian.cc
    gsl_lsp.cc
    gsl_mdm.cc
    hdf_constant.cc
    helical_valley_nlls_problem.cc
    ils_convolution.cc
    ils_fts.cc
    ils_fts_f.F90
    ils_gaussian.cc
    ils_instrument.cc
    ils_table.cc
    initial_guess_value.cc
    instrument_doppler.cc
    jennrich_sampson_nlls_problem.cc
    l2_fp_configuration_lua.cc
    l_rad_driver.cc
    l_rad_driver_f.F90
    l_rad_rt.cc
    level_1b_acos.cc
    level_1b_average.cc
    level_1b_cache.cc
    level_1b_fts.cc
    level_1b_fts_f.F90
    level_1b_heritage.cc
    level_1b_oco.cc
    level_1b_scale_radiance.cc
    level_1b_uq.cc
    absco.cc
    nlls_max_a_posteriori.cc
    nlls_max_likelihood.cc
    nlls_problem_scaled.cc
    lidort_driver.cc
    lidort_interface_masters.F90
    lidort_interface_masters_io.F90
    lidort_interface_types.F90
    lidort_interface_types_io.F90
    lidort_rt.cc
    log_timing.cc
    lsi_rt.cc
    max_a_posteriori_oco.cc
    max_likelihood_oco.cc
    merra_aerosol.cc
    meyer_ml_problem.cc
    meyer_nlls_problem.cc
    model_measure_bard.cc
    model_measure_meyer.cc
    model_measure_oco.cc
    # Disabled due to incompatibility with GSL >= 2.0 due to change in interface it uses
    #nlls_solver_gsl.cc
    #nlls_solver_gsl_lmder.cc
    #nlls_solver_gsl_lmsder.cc
    nonuniform_spectrum_sampling.cc
    oco_forward_model.cc
    oco_noise_model.cc
    oco_sim_apriori.cc
    output_hdf.cc
    output_hdf_iteration.cc
    powell_nlls_problem.cc
    powell_singular_nlls_problem.cc
    precomputed_noise_model.cc
    pressure_sigma.cc
    radiance_scaling.cc
    radiance_scaling_linear_fit.cc
    radiance_scaling_sv_fit.cc
    radiant2.8_direct.F90
    radiant_driver.cc
    rayleigh.cc
    rayleigh_f.F90
    reference_vmr_apriori.cc
    refractive_index.cc
    relative_humidity.cc
    rosenbrock2_nlls_problem.cc
    solar_absorption_and_continuum.cc
    solar_absorption_gfit_file.cc
    solar_absorption_gfit_file_f.F90
    solar_absorption_table.cc
    solar_continuum_table.cc
    solar_doppler_shift_l1b.cc
    solar_doppler_shift_polynomial.cc
    solver_iteration_log.cc
    spectral_window_range.cc
    spectrum_sampling_fixed_spacing.cc
    stokes_coefficient_constant.cc
    stokes_coefficient_fraction.cc
    tccon_apriori.cc
    temperature_met.cc
    temperature_level_offset.cc
    twostream_driver.cc
    twostream_interface.F90
    twostream_rt.cc
    uniform_spectrum_sampling.cc
    uplooking_raytracing.cc
    uq_noise_model.cc
    zero_offset_waveform.cc
)

set(TEST_SOURCES
    absco_hdf_test.cc
    absorber_absco_test.cc
    absorber_vmr_met_test.cc
    absorber_vmr_level_scaled_test.cc
    absorber_vmr_level_test.cc
    aerosol_optical_test.cc
    aerosol_property_hdf_test.cc
    aerosol_property_rh_hdf_test.cc
    aerosol_shape_gaussian_test.cc
    altitude_hydrostatic_test.cc
    atmosphere_fixture.cc
    atmosphere_oco_test.cc
    bad_sample_noise_model_test.cc
    chapman_boa_rt_test.cc
    chapman_boa_test.cc
    chisq_convergence_test.cc
    composite_initial_guess_full_guess_test.cc
    composite_perturbation_test.cc
    configuration_fixture.cc
    connor_convergence_test.cc
    connor_solver_test.cc
    cost_minimizer_gsl_test.cc
    dispersion_fit_test.cc
    dispersion_polynomial_test.cc
    empirical_orthogonal_function_test.cc
    error_analysis_test.cc
    # Disabled due to incompatibility with GSL >= 2.0 due to change in interface it uses
    #fdf_nlls_solver_test.cc
    fluorescence_effect_test.cc
    forward_model_cost_function_test.cc
    fp_logger_test.cc
    full_output_test.cc
    gas_vmr_apriori_test.cc
    gosat_noise_model_test.cc
    ground_brdf_test.cc
    ground_coxmunk_plus_lambertian_test.cc
    ground_coxmunk_test.cc
    ground_lambertian_test.cc
    hdf_constant_test.cc
    ils_convolution_test.cc
    ils_fts_test.cc
    ils_gaussian_test.cc
    ils_instrument_test.cc
    ils_table_test.cc
    initial_guess_value_test.cc
    instrument_doppler_test.cc
    l_rad_driver_test.cc
    l_rad_rt_test.cc
    level_1b_acos_test.cc
    level_1b_average_test.cc
    level_1b_cache_test.cc
    level_1b_fts_test.cc
    level_1b_heritage_test.cc
    level_1b_oco_test.cc
    level_1b_scale_radiance_test.cc
    lidort_driver_test.cc
    lidort_fixture.cc
    lidort_interface_masters_test.cc
    lidort_interface_types_test.cc
    lidort_rt_test.cc
    lsi_rt_test.cc
    merra_aerosol_test.cc
    nlls_max_a_posteriori_test.cc
    nlls_max_likelihood_test.cc
    # Disabled due to incompatibility with GSL >= 2.0 due to change in interface it uses
    #nlls_solver_gsl_test.cc
    nonuniform_lsi_rt_test.cc
    nonuniform_spectrum_sampling_test.cc
    oco_forward_model_test.cc
    oco_noise_model_test.cc
    oco_sim_apriori_test.cc
    output_hdf_iteration_test.cc
    output_hdf_test.cc
    precomputed_noise_model_test.cc
    pressure_sigma_test.cc
    radiance_scaling_linear_fit_test.cc
    radiance_scaling_sv_fit_test.cc
    rayleigh_only_test.cc
    rayleigh_test.cc
    reference_vmr_apriori_test.cc
    refractive_index_test.cc
    relative_humidity_test.cc
    solar_absorption_and_continuum_test.cc
    solar_absorption_gfit_file_test.cc
    solar_absorption_table_test.cc
    solar_continuum_table_test.cc
    solar_doppler_shift_l1b_test.cc
    solar_doppler_shift_polynomial_test.cc
    solver_finished_fixture.cc
    spectral_window_range_test.cc
    spectrum_sampling_fixed_spacing_test.cc
    stokes_coefficient_constant_test.cc
    stokes_coefficient_fraction_test.cc
    tccon_apriori_test.cc
    temperature_met_test.cc
    temperature_level_offset_test.cc
    twostream_driver_test.cc
    twostream_interface_test.cc
    twostream_rt_test.cc
    uniform_spectrum_sampling_test.cc
    zero_offset_waveform_test.cc
)

# Full path already included
file(GLOB_RECURSE SWIG_SOURCES *.i)
# Remove ununused SWIG files
foreach(file ${SWIG_SOURCES})
    if(${file} MATCHES "nlls_solver_gsl")
        list(REMOVE_ITEM SWIG_SOURCES ${file})
    endif()
endforeach()
list(APPEND SWIG_INTERFACE_FILES ${SWIG_SOURCES})

# Add current source directory to source file names
foreach(source_name ${DIR_SOURCES})
    set(FP_SOURCE_FILES ${FP_SOURCE_FILES} ${CMAKE_CURRENT_SOURCE_DIR}/${source_name})
endforeach(source_name)

foreach(source_name ${TEST_SOURCES})
    set(FP_TEST_FILES ${FP_TEST_FILES} ${CMAKE_CURRENT_SOURCE_DIR}/${source_name})
endforeach(source_name)

# Expose the list of source files to the parent cmake file
set(FP_SOURCE_FILES ${FP_SOURCE_FILES} PARENT_SCOPE)
set(FP_TEST_FILES ${FP_TEST_FILES} PARENT_SCOPE)
set(SWIG_INTERFACE_FILES ${SWIG_INTERFACE_FILES} PARENT_SCOPE)

