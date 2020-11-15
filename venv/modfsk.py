import binascii
import numpy as np
import matplotlib.pyplot as plt
N=1024
st = input('String: ')
def encode(s):
    return (list(map(lambda x: "{0:b}".format(ord(x)).zfill(7),s)))

def enc(s):
    return bin(int.from_bytes(s.encode(), 'big'))[2:]

#print(list(enc(st)))
#print(list(''.join(encode(st))))
M4=np.array([])
mod_rnd = np.array(list(''.join(encode(st))),dtype=int)
print(mod_rnd)
M=mod_rnd.size
for i in mod_rnd:
    if (str(i)=='1'):
        a=np.array(np.sin(4*np.pi*np.linspace(0,M,int(1000/M))))
        M4=np.append(M4,a)
    if (str(i)=='0'):
        M4=np.append(M4,np.sin(8*np.pi*np.linspace(0,M,int(1000/M))))


plt.plot(np.repeat(mod_rnd,repeats=int(1000/M)))
plt.plot(M4)
plt.show()