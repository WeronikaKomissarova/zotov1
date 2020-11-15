import numpy as np
import matplotlib.pyplot as plt


amp=float(input("Amplitude: "))
km=float(input("Коэффициент модуляции: "))
fc=float(input('Current frequency:'))
fs=float(input('Signal frequency: '))


def signal_am(amp=1.0, km=0.25, fc=10.0, fs=2.0, N=1024): #fc несущая fs сигнала
    x = 2.0 * np.pi * np.linspace(0, 1, N)
    s=amp * (1+ km * np.sin(fs * x))
    return s, amp * (1 + km * np.sin(fs * x)) * np.sin(fc * x)


plt.plot(signal_am(amp,km,fc,fs)[1])
plt.plot(signal_am(amp,km,fc,fs)[0])
plt.show()