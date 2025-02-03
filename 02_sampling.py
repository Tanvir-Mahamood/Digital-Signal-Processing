import numpy as np
import matplotlib.pyplot as plt

tmin=-1
tmax=1
frequency = 1
sampling_frequency = 30

# continus time signal
t_continus = np.linspace(tmin, tmax, 1000)
y_continus = np.sin(2 * np.pi * frequency * t_continus)

# discrete time signal
t_discrete = np.arange(tmin, tmax, 1/sampling_frequency)
y_discrete = np.sin(2 * np.pi * frequency * t_discrete)

# plt.plot(t_continus, y_continus)
plt.stem(t_discrete, y_discrete)
plt.title("Sampling")
plt.grid(True)
plt.show()
