import math
import numpy as np
import pylab

N=1000
k=int(input('K: '))
dn=int(N/k)

def sigma(x):
    if x<0:return 0
    else:return 1

def f(x):
    return ((1/(400*math.sqrt(2*math.pi)))*(math.exp(-((x-500)**2)/(2*400*400))))*10**7

Mas1=np.arange(0,N,1)
gauss_func=np.array([f(x) for x in Mas1])


def step(x):
    s=gauss_func[0]*sigma(x)
    for j in range(1,k):
        s+=(gauss_func[j*dn]-gauss_func[(j-1)*dn])*(sigma(x-j*dn))
    return s

steps=np.array([step(x) for x in Mas1])

pylab.plot(Mas1,gauss_func)
pylab.plot(Mas1,steps)
pylab.show()
