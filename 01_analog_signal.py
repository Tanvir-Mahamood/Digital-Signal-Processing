import numpy as np
import matplotlib.pyplot as plt

tmin=-1
tmax=1
frequency = 2

# continus time signal
t_continus = np.linspace(tmin,tmax,1000)
y_continus = np.sin(2 * np.pi * frequency * t_continus)

plt.plot(t_continus, y_continus)
plt.title("Analog Signal")
plt.grid(True)
plt.show()
