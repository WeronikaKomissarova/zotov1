import binascii
import numpy as np
import matplotlib.pyplot as plt
N=1024
st = input('String: ')
def encode(s):
    return (list(map(lambda x: "{0:b}".format(ord(x)).zfill(7),s)))

def enc(s):
    return bin(int.from_bytes(s.encode(), 'big'))[2:]


mod_psk = np.array(list(''.join(encode(st))),dtype=int)
M4=np.array([])
M=mod_psk.size
for i in mod_psk:
    if (str(i)=='1'):
        a=np.array(np.sin(2*np.pi*np.linspace(0,1,int(1000/M))))
        M4=np.append(M4,a)
    if (str(i)=='0'):
        M4=np.append(M4,np.cos(np.pi/2 + 2*np.pi*np.linspace(0,1,int(1000/M))))


plt.plot(M4)
plt.plot(np.repeat(mod_psk,repeats=int(1000/M)))
plt.show()