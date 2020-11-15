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

np.random.seed(6)
mod_rnd = np.array(list(''.join(encode(st))),dtype=int)
print(mod_rnd)
# Repeat number of ones and zeros
mod_ask = np.repeat(mod_rnd, repeats=10)


M=mod_ask.size
t=np.linspace(0,M/10,M)
sig_ask= mod_ask * np.sin(2.0*np.pi*np.linspace(0,M/10,M))

plt.plot(t,mod_ask)
plt.plot(t,sig_ask)
plt.grid(True)
plt.show()
