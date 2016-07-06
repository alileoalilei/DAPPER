from params import ndim
import aotensor
import numpy as np
from scipy.sparse import dok_matrix
from scipy.sparse import csr_matrix
import time

aotensor=aotensor.init_aotensor()


def sparse_mul3(arr) :
	""" Calculate for each i the sums on j,k of the product
	tensor(i,j,k)* arr(j) * arr(k) """
	res=np.zeros(ndim+1)
	for i in range(1,ndim+1) :
		X=aotensor[i]
		for m in range(0,len(X)) :
			(j,k,v)=X[m]
			res[i]=res[i]+v*arr[j]*arr[k]
	return res
	
def tendencies(y) :
	""" Calculate the tendencies thanks to the product of the tensor and the vector y"""
	return sparse_mul3(y)

buf_f0=np.zeros(ndim,dtype=float)
buf_f1=np.zeros(ndim,dtype=float)
buf_y1=np.zeros(ndim,dtype=float)

def step(y,t,dt) :
	""" Heun method integration"""
	buf_f0=tendencies(y)
	buf_y1= y + dt * buf_f0
	buf_f1=tendencies(buf_y1)
	
	return (y + 0.5 * (buf_f0 + buf_f1) * dt,t+dt)

if __name__ == "__main__":
	import ic
	X=ic.X0
	#for i in range(0,80):
	X=sparse_mul3(X)
	print (sparse_mul3(X))

