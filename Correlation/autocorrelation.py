import numpy as np
import matplotlib.pyplot as plt

idx_x = np.linspace(-2*np.pi, 2*np.pi, 70)
x = np.sin(idx_x)

plt_x = []
plt_y = []

"""
for lag in range(-len(x) + 1, len(x)):
    r = 0
    for i in range(len(x)):
        if 0 <= i - lag < len(x):  
            r += x[i] * x[i - lag]  
    plt_x.append(lag)
    plt_y.append(r)

plt.stem(plt_x, plt_y)
plt.title("Autocorrelation of x[n]")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)
plt.show()

"""


autocorr = np.correlate(x, x, mode="full")
lags = np.arange(-len(x) + 1, len(x))

plt.stem(lags, autocorr)
plt.title("Autocorrelation of x[n]")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)
plt.show()

