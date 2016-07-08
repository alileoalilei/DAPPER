import numpy as np

X0=np.zeros(57)

X0[0]=1. #one dimension more to have ndim+1 to support the multiplication with the tensor (j and k are in [|0,ndim|]

#psi variables
X0[1]=0.0 # typ=A, NX0=0, Ny= 1.0
X0[2]=0.0 # typ=K, NX0=1.0, Ny= 1.0
X0[3]=0.0 # typ=L, NX0=1.0, Ny= 1.0
X0[4]=0.0 # typ=A, NX0=0, Ny= 2.0
X0[5]=0.0 # typ=K, NX0=1.0, Ny= 2.0
X0[6]=0.0 # typ=L, NX0=1.0, Ny= 2.0
X0[7]=0.0 # typ=A, NX0=0, Ny= 3.0
X0[8]=0.0 # typ=K, NX0=1.0, Ny= 3.0
X0[9]=0.0 # typ=L, NX0=1.0, Ny= 3.0
X0[10]=0.0 # typ=A, NX0=0, Ny= 4.0
X0[11]=0.0 # typ=K, NX0=1.0, Ny= 4.0
X0[12]=0.0 # typ=L, NX0=1.0, Ny= 4.0
X0[13]=0.0 # typ=K, NX0=2.0, Ny= 1.0
X0[14]=0.0 # typ=L, NX0=2.0, Ny= 1.0
X0[15]=0.0 # typ=K, NX0=2.0, Ny= 2.0
X0[16]=0.0 # typ=L, NX0=2.0, Ny= 2.0
X0[17]=0.0 # typ=K, NX0=2.0, Ny= 3.0
X0[18]=0.0 # typ=L, NX0=2.0, Ny= 3.0
X0[19]=0.0 # typ=K, NX0=2.0, Ny= 4.0
X0[20]=0.0 # typ=L, NX0=2.0, Ny= 4.0

#theta variables
X0[21]=0.0 # typ=A, NX0=0, Ny= 1.0
X0[22]=0.0 # typ=K, NX0=1.0, Ny= 1.0
X0[23]=0.0 # typ=L, NX0=1.0, Ny= 1.0
X0[24]=0.0 # typ=A, NX0=0, Ny= 2.0
X0[25]=0.0 # typ=K, NX0=1.0, Ny= 2.0
X0[26]=0.0 # typ=L, NX0=1.0, Ny= 2.0
X0[27]=0.0 # typ=A, NX0=0, Ny= 3.0
X0[28]=0.0 # typ=K, NX0=1.0, Ny= 3.0
X0[29]=0.0 # typ=L, NX0=1.0, Ny= 3.0
X0[30]=0.0 # typ=A, NX0=0, Ny= 4.0
X0[31]=0.0 # typ=K, NX0=1.0, Ny= 4.0
X0[32]=0.0 # typ=L, NX0=1.0, Ny= 4.0
X0[33]=0.0 # typ=K, NX0=2.0, Ny= 1.0
X0[34]=0.0 # typ=L, NX0=2.0, Ny= 1.0
X0[35]=0.0 # typ=K, NX0=2.0, Ny= 2.0
X0[36]=0.0 # typ=L, NX0=2.0, Ny= 2.0
X0[37]=0.0 # typ=K, NX0=2.0, Ny= 3.0
X0[38]=0.0 # typ=L, NX0=2.0, Ny= 3.0
X0[39]=0.0 # typ=K, NX0=2.0, Ny= 4.0
X0[40]=0.0 # typ=L, NX0=2.0, Ny= 4.0

#A variables
X0[41]=0.0 # NX0=0.5, Ny= 1.0
X0[42]=0.0 # NX0=0.5, Ny= 2.0
X0[43]=0.0 # NX0=0.5, Ny= 3.0
X0[44]=0.0 # NX0=0.5, Ny= 4.0
X0[45]=0.0 # NX0=1.0, Ny= 1.0
X0[46]=0.0 # NX0=1.0, Ny= 2.0
X0[47]=0.0 # NX0=1.0, Ny= 3.0
X0[48]=0.0 # NX0=1.0, Ny= 4.0

#T variables
X0[49]=0.0 # NX0=0.5, Ny= 1.0
X0[50]=0.0 # NX0=0.5, Ny= 2.0
X0[51]=0.0 # NX0=0.5, Ny= 3.0
X0[52]=0.0 # NX0=0.5, Ny= 4.0
X0[53]=0.0 # NX0=1.0, Ny= 1.0
X0[54]=0.0 # NX0=1.0, Ny= 2.0
X0[55]=0.0 # NX0=1.0, Ny= 3.0
X0[56]=0.0 # NX0=1.0, Ny= 4.0
