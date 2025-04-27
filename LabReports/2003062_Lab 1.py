import numpy as np
import matplotlib.pyplot as plt

tmin=-1
tmax=1
frequency = 1 
sampling_frequency = 30 # above Nyquist rate (2*frequency)
level = 11

# Continus Sinusoidal Signal
t_continus = np.linspace(tmin, tmax, 1000)
y_continus = np.sin(2 * np.pi * frequency * t_continus)

# Sample the signal: discrete time signal
t_discrete = np.arange(tmin, tmax, 1/sampling_frequency)
y_discrete = np.sin(2 * np.pi * frequency * t_discrete)

# quantization
min_val, max_val = -1, 1
quantization_step = (max_val - min_val) / (level - 1)
# y_quantized = np.round(y_discrete / quantization_step) * quantization_step
y_quantized = np.round((y_discrete - min_val) / quantization_step) * quantization_step + min_val

fig, axs = plt.subplots(3,1,figsize=(10,10))
axs[0].plot(t_continus, y_continus)
axs[0].set_title('Sinusoidal Signal')
axs[0].grid(True)

axs[1].stem(t_discrete, y_discrete)
axs[1].set_title('Sampled Signal')
axs[1].grid(True)

axs[2].stem(t_discrete, y_quantized)
axs[2].set_title('Sinusoidal Signal')

for label_value in np.arange(min_val, max_val + quantization_step, quantization_step):
    axs[2].axhline(y=label_value, color='g', linestyle='--')

plt.tight_layout()
plt.show()
