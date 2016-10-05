# Dump data to a xls spreadsheet that we can open in openoffice or excel
import xlwt
from full_physics import *
import numpy as np
import os

bdir = os.path.dirname(__file__) + "/"
sdir = bdir + "simulator_result/"
sid_name = "2010090912004075"
ecmwf_name = "../input/oco2_sim_met.h5"
l1b_name = "../input/oco2_sim_l1b.h5"
scene_file = "../input/oco2_sim_scene.h5"
r = L2Run(bdir + "config/config_orbit_sim_match.lua", sid_name,ecmwf_name, 
          l1b_name, scene_file = scene_file)

hres_ref = np.genfromtxt(sdir + "hires_10774_1.txt", skiprows = 1)
sd = SpectralDomain(hres_ref[:,0], Unit("nanometer"))
sd = SpectralDomain(sd.wavelength(Unit("micron")), Unit("micron"))
refl = hres_ref[:,2]
rcalc = r.radiative_transfer.reflectance(sd, 0, True).value
stkcalc = r.radiative_transfer.stokes(sd, 0)
maxindex = np.argmax(abs(refl-rcalc))
wnmax = sd.wavenumber[maxindex]
lrad_rt = r.radiative_transfer.high_stream_radiative_transfer.rt
lidort_rt = lrad_rt.radiative_transfer
atm = lidort_rt.atmosphere

ab = atm.absorber
wb = xlwt.Workbook()
ws_t = wb.add_sheet("Calculated Tau")
ws_t.write(0,0, "Total Tau")
ws_t.write(0,1, sum(ab.optical_depth_each_layer(wnmax,0).value[:,ab.gas_index("O2")]))
ws = wb.add_sheet("Sublayer data")
ws_c = wb.add_sheet("Constants")
row = 0
ws_c.write(row,0,"Wnmax")
ws_c.write(row,1,wnmax)
row += 1
ws_c.write(row,0,"Spectral Index")
ws_c.write(row,1,0)
row += 1
ws_c.write(row,0,"Gas")
ws_c.write(row,1,"O2")
row += 1
const = DefaultConstant()
ws_c.write(row,0,"Molar Weight Water")
ws_c.write(row,1,const.molar_weight_water.value)
row += 1
ws_c.write(row,0,"Molar Weight Dry Air")
ws_c.write(row,1,const.molar_weight_dry_air.value)
row += 1
ws_c.write(row,0,"Avogadro Constant")
ws_c.write(row,1,const.avogadro_constant.value)
row += 1


col = 0
ws.write(0,col,"Pressure (Pa)")
ws.write(1,col,"Generated by creating 10 sublayers from each pressure sigma level")
p = ab.pressure_sublayer.value.value
for i in range(p.shape[0]):
    ws.write(i+2,col,p[i])
col += 1
ws.write(0,col,"Temperature (K)")
ws.write(1,col,"Read from ECMWF file and interpolate to pressure levels using log/log interpolation")
t = ab.temperature_sublayer.value.value
for i in range(t.shape[0]):
    ws.write(i+2,col,t[i])

col += 1
ws.write(0,col,"H2O VMR")
ws.write(1,col,"Read specific humidity from ECMWF file and interpolate to pressure levels using log/log interpolation. Then convert to H2O VMR by s / (1-s) * molar_weight_dry_air / molar_weight_water")
h = ab.h2o_vmr_sublayer.value.value
for i in range(h.shape[0]):
    ws.write(i+2,col,h[i])

col += 1
ws.write(0,col,"Gravity (m/s^2)")
ws.write(1,col,"Calculated by hydrostatic equations. Note that the code for this is suspect, it iterates but every iteration gives the same value. Code can be found in altitude_hyrdostatic.")
g = ab.gravity_sublayer(0).value.value
for i in range(g.shape[0]):
    ws.write(i+2,col,g[i])

col += 1
ws.write(0,col,"O2 VMR")
ws.write(1,col,"Hard code value set in lua configuration file")
o2vmr = ab.vmr_sublayer("O2").value.value
for i in range(o2vmr.shape[0]):
    ws.write(i+2,col,o2vmr[i])

wb.save("absorber_data.xls")


