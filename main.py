import numpy as np
#from algo import PenaltyFunc

def PenaltyFunc(rk, be):
	count = 0
	eps = 0.0001
	#file = open(r"C:\Users\ASUSa\Desktop\Results.txt")
	x = np.array[	[ -1, -1, -1, -1 ] ]
	while (rk * Alfa(x) >= eps and count < 500):
		count += 1
		x = PosDirMethod(x, rk)
		rk *= be
		#file.write(x,count)
	
	#file.close()
	print( x)

def PosDirMethod(x, rk):
	pass
def Alfa(x):
	pass

Cik = np.array([
	[5000,	7000,	20000,	12000],
	[9000,	4000,	8000,	10000],
	[6000,	8000,	4000,	8000]
	])

Lik = np.array([
	[500,	1200,	1000,	2000],
	[1750,	1800,	1500,	3300],
	[2000,	2450,	2000,	4000]
	])

Bk = np.array([30,	20,	40])
Rk = np.array([3000,	2000,	7000])

Gi = np.array([20000,	10000,	15000,	32000])
Di = np.array([40000,	30000,	25000,	40000])
Cip = np.array([5000,	 7000,	12000,	10000])
Si = np.array([ 8000,	15000,	14000,	12000])
Lip = np.array([2000,	 1500,	 2500,	 1500])

r = 0.01


m = 3
n = 4
p = b = 0

x = PenaltyFunc(r, b)
resultValue = f(x)
Cik = np.empty((3,4))

print(x)

