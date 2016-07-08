from mods.MAOOAM.params2 import ndim
import mods.MAOOAM.aotensor as aotensor
import numpy as np
from scipy.sparse import dok_matrix
from scipy.sparse import csr_matrix
import time

aotensor=aotensor.init_aotensor()


def sparse_mul3(arr) :
	""" Calculate for each i the sums on j,k of the product
	tensor(i,j,k)* arr(j) * arr(k) """
	if np.ndim(arr) is 1:
		arr = arr.reshape((1,len(arr)))
	res=np.zeros(ndim+1)
	for (i,j,k,v) in aotensor :
		res[i]=res[i]+v*arr[0][j]*arr[0][k]
	if res.shape[0] is 1:
		res = res.squeeze()
	return res
	
def tendencies(y) :
	""" Calculate the tendencies thanks to the product of the tensor and the vector y"""
	return sparse_mul3(y)

buf_f0=np.zeros(ndim+1,dtype=float)
buf_f1=np.zeros(ndim+1,dtype=float)
buf_y1=np.zeros(ndim+1,dtype=float)

def step(y,t,dt) :
	""" Heun method integration"""
	buf_f0=tendencies(y)
	buf_y1= y + dt * buf_f0
	buf_f1=tendencies(buf_y1)
	print (y + 0.5 * (buf_f0 + buf_f1) * dt)
	return y + 0.5 * (buf_f0 + buf_f1) * dt

if __name__ == "__main__":
	import ic
	X=ic.X0
	#for i in range(0,80):
	X=sparse_mul3(X)
	print (sparse_mul3(X))

