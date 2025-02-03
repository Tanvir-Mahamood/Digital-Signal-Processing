import numpy as np
import matplotlib.pyplot as plt

tmin=-1
tmax=1
frequency = 1
sampling_frequency = 30
level = 11


t1 = np.arange(tmin, tmax, 1/sampling_frequency)
y_discrete = np.sin(2 * np.pi * frequency * t1)
quantization_step = (tmin - tmax) / (level - 1)
y1 = np.round(y_discrete / quantization_step) * quantization_step


y_discrete = np.sin(2 * np.pi * frequency * 2 * t1)
quantization_step = (tmin - tmax) / (level - 1)
y2 = np.round(y_discrete / quantization_step) * quantization_step

add = y1 + y2
sub = y1 - y2
div = y1 / y2
mul = y1 * y2

scalar_mul = y1 * 2



#Plotting the signals.
fig, axs = plt.subplots(4,2,figsize=(8,8))
axs[0][0].stem(t1, y1)
axs[0][0].set_title('Signal-1')

axs[0][1].stem(t1, y2)
axs[0][1].set_title('Signal-2')

axs[1][0].stem(t1, add)
axs[1][0].set_title('Addition')

axs[1][1].stem(t1, sub)
axs[1][1].set_title('Subtraction')

axs[2][0].stem(t1, div)
axs[2][0].set_title('Division')

axs[2][1].stem(t1, mul)
axs[2][1].set_title('Multiplication')

axs[3][0].stem(t1, scalar_mul)
axs[3][0].set_title('Scaler Multiplication')



plt.tight_layout()
plt.show()