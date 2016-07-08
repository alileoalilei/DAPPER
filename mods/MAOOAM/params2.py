#parameters module
import numpy as np


#-----------------------------------------------------------
# Integral parameters
#-----------------------------------------------------------

t_trans = 4000  #  transient period (e.g. 1.e7)
t_run = 4000  #  length of trajectory on the attractor (e.g. 5.e8)
dt = 1      #  the time step
writeout = True   #  write out all variables every tw time units
tw = 10   #  the time step of writing

#-----------------------------------------------------------
# Number of blocks
#-----------------------------------------------------------

#generate the mode blocks for either ocean or atmosphere
#up to given wavenumbers
#nxmax and nymax are the maximum

def get_modes(nxmax,nymax) :
	res=np.zeros((nxmax*nymax,2))
	i=0
	for Nx in range (1,nxmax+1) :
		for Ny in range (1,nymax+1) :
			res[i]=[Nx,Ny]
			i+=1
	return res

def init_params(nboc,nbatm):
	natmres=0
	for i in range (0,nbatm):
		if (ams[i,0]==1) :
			natmres=natmres+3
		else:
			natmres=natmres+2
	s=np.shape(oms)
	nocres=s[0]
	
	return (natmres,nocres,2*(natmres+nocres))

#select (.,.) the maximum value admitted for Nx and Ny
#don't forget to delete ic.py, it will regenerates

oms =get_modes(2,4)# ocean mode selection
ams =get_modes(2,4)# atmosphere mode selection
nboc,nbatm = 2*4,2*4	  # number of blocks
(natm,noc,ndim)=init_params(nboc,nbatm)

#noc,natm=8,10     # number of basis functions
#ndim=36		  # number of variables




#-----------------------------------------------------------
#  Scale parameters for the ocean and the atmosphere
#-----------------------------------------------------------
scale = 5.e6      #  the characteristic space scale, L*pi
f0    = 1.032e-4  #  Coriolis parameter at 45 degrees latitude	
n     = 1.5e0     #  aspect ratio (n = 2Ly/Lx ; Lx = 2*pi*L/n; Ly = pi*L)
rra   = 6370.e3   #  earth radius	
phi0_npi = 0.25e0 #  latitude exprimed in fraction of pi

#Parameters for the ocean
gp    = 3.1e-2    #  reduced gravity
r     = 1.e-7     #  frictional coefficient at the bottom of the ocean	
h     = 136.5      #  depth of the water layer of the ocean
d     = 1e-8     # 1.1 10-7 the coupling parameter (should be divided by f0 in order to be adimensional)

#Parameters for the atmosphere
k     = 0.0145    #  atmosphere bottom friction coefficient
kp    = 0.0290    #  atmosphere internal friction coefficient
sig0  = 0.1e0     #  static stability of the atmosphere

#Temperature-related parameters for the ocean
Go    = 5.46e8      #  Specific heat capacity of the ocean (50m layer)
Co    = 200.e0    #310.0 GMD  Constant short-wave radiation of the ocean
To0   = 301.46e0    #  Stationary solution for the 0-th order ocean temperature

#Temperature-related parameters for the atmosphere
Ga    = 1.e7      #  Specific heat capacity of the atmosphere
Ca    = 103.3333e0    #  Constant short-wave radiation of the atmosphere
epsa  = 0.7e0    #  Emissivity coefficient for the grey-body atmosphere
Ta0   = 289.30    #  Stationary solution for the 0-th order atmospheric temperature

#Other temperature-related parameters/constants
sc    = 1.      #  Ratio of surface to atmosphere temperature
lambdaa = 20   #  15.06 GMD Sensible + turbulent heat exchange between ocean and atmosphere
rr    = 287.e0    #  Gas constant of dry air
sb    = 5.6e-8    #  Stefan-Boltzmann constant

#-----------------------------------------------------------
# Some general parameters (Domain, beta, gamma, coupling
#-----------------------------------------------------------

pi=np.arccos(-1.e0)
L=scale/pi
phi0=phi0_npi*pi
LR=np.sqrt(gp*h)/f0
G=-L**2/LR**2
betp=L/rra*np.cos(phi0)/np.sin(phi0)
rp=r/f0
dp=d/f0
kd=k*2
kdp=kp

#-----------------------------------------------------------
# Derived Quantities
#-----------------------------------------------------------

Cpo=Co/(Go*f0) * rr/(f0**2*L**2)
Lpo=lambdaa/(Go*f0)
Cpa=Ca/(Ga*f0) * rr/(f0**2*L**2)/2 # Cpa acts on psi1-psi3, not on theta
Lpa=lambdaa/(Ga*f0)
sbpo=4*sb*To0**3/(Go*f0) # long wave radiation lost by ocean to atmosphere space
sbpa=8*epsa*sb*Ta0**3/(Go*f0) # long wave radiation from atmosphere absorbed by ocean
LSBpo=2*epsa*sb*To0**3/(Ga*f0) # long wave radiation from ocean absorbed by atmosphere
LSBpa=8*epsa*sb*Ta0**3/(Ga*f0) # long wave radiation lost by atmosphere to space & ocean


