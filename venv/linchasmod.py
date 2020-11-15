import numpy as np
import matplotlib.pyplot as plt
import pylab

amp=float(input("Amplitude: "))

beta=float(input('beta:'))



def sign_chirp(amp=1.0, beta=0.25, N=1024, tau=256):
    res=[]
    t=np.linspace(0,8,N)
    y=np.array([np.sin(2*np.pi*(i+((beta/2)*i*i))) for i in t])
    return t,y


pylab.grid(True)
pylab.plot(sign_chirp(amp,beta)[1])
pylab.show()




