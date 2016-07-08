# Reproduce results from
# table1 of sakov et al "iEnKF" (2012)

from common import *

import numpy as np
import mods.MAOOAM.params2
import mods.MAOOAM.aotensor
import mods.MAOOAM.integrator
import mods.MAOOAM.ic_def as ic_def

ic_def.load_IC()
import mods.MAOOAM.ic as ic
mu0= ic.X0

print (" Model initialized")


m = mods.MAOOAM.params2.ndim +1
p = m


T = 4**4
t = Chronology(0.1,dkObs=225,T=T,BurnIn=4)
#t = Chronology(0.1,dkObs=0.1,T=T,BurnIn=4)

m = mods.MAOOAM.params2.ndim +1
f = {
    'm': m,
    'model': lambda x,t,dt: mods.MAOOAM.integrator.step(x,t,dt),
    'noise': 0
    }

C0=0.01*eye(m)
C0[0,0]= 0 # because the first component of the state vector is 1

X0 = GaussRV(C=CovMat(C0),mu=mu0)
#X0 = GaussRV(C=0.01,mu=mu0)

R = C0.copy()
R[0,0]= 0.01
hnoise = GaussRV(C=CovMat(R),mu=0)

h = {
    'm': p,
    'model': lambda x,t: x,
    'noise': hnoise,
    }

other = {'name': os.path.basename(__file__)}

params = OSSE(f,h,t,X0,**other)
