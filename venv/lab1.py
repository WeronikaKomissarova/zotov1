import numpy as np
import matplotlib.pyplot as plt
N = 200
# Random array of ones and zeros
np.random.seed(1)
mod_rnd = np.random.randint(0, 2, 20)
# Repeat number of ones and zeros
mod_fsk = np.repeat(mod_rnd, repeats=N)

# FSK signal
M = mod_fsk.size
mod_frq = np.zeros(M)

# Set freq 'bits' (0, 1)
mod_frq[mod_fsk == 0] = 10
mod_frq[mod_fsk == 1] = 50

sig_fsk = np.sin(mod_frq *  2.0 * np.pi * np.linspace(0, 1, M))

# PLot results
plt.figure(figsize=(16, 5), dpi=120)
plt.subplot(2, 1, 1)
plt.title('Digital signal', fontsize=14)
plt.plot(mod_fsk, color='C0', linewidth=2.0)
plt.xlim([0, M-1])
plt.grid(True)

plt.subplot(2, 1, 2)
plt.title('FSK-signal', fontsize=14)
plt.plot(mod_fsk, '--', color='C0', linewidth=2.0)
plt.plot(sig_fsk, '-', color='C1', linewidth=2.0)
plt.xlim([0, M-1])
plt.grid(True)
plt.tight_layout()
plt.show()