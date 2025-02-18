import numpy as np
import matplotlib.pyplot as plt

tmin=-1
tmax=1
frequency = 1
sampling_frequency = 70

t = np.arange(tmin, tmax, 1/sampling_frequency)
y = np.sin(2 * np.pi * frequency * t)
Y = 0

for i in range(50):
    Y += np.sin(2 * np.pi * (frequency + 2*i) * t)

# plt.plot(t_continus, y_continus)
plt.stem(t, Y)
plt.title("Harmonic")
plt.grid(True)
plt.show()