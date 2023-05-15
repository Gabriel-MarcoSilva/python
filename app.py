import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

for N in range(1, 6):
    Fs = 8192  # Freq de amostragem
    t = np.linspace(0, 1 - 1 / Fs, Fs)
    f = 2
    amp = 1

    ax = fig.add_subplot(3, 2, N)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.2, 1.2)
    tt = f'Ordem {N}'
    ax.set_title(tt)

    res = amp / 2
    for k in range(1, N+1):
        res = res - (amp / (k * np.pi)) * np.sin(2 * np.pi * k * f * t)
        ax.plot(t, res)
        plt.pause(0.1)

N = 10  # Ordem da série
Fs = 8192  # Freq de amostragem
t = np.linspace(0, 1 - 1 / Fs, Fs)
f = 2
amp = 1

ax = fig.add_subplot(3, 2, 6)
ax.set_xlim(0, 1)
ax.set_ylim(-0.2, 1.2)
tt = f'Ordem {N}'
ax.set_title(tt)

res = amp / 2
for k in range(1, N+1):
    res = res - (amp / (k * np.pi)) * np.sin(2 * np.pi * k * f * t)
    ax.plot(t, res)
    plt.pause(0.1)

plt.show()
