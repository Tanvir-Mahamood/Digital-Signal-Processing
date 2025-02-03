import numpy as np
import matplotlib.pyplot as plt

tmin=-1
tmax=1
frequency = 1
sampling_frequency = 30
level = 11

# continus time signal
t_continus = np.linspace(tmin, tmax, 1000)
y_continus = np.sin(2 * np.pi * frequency * t_continus)

# discrete time signal
t_discrete = np.arange(tmin, tmax, 1/sampling_frequency)
y_discrete = np.sin(2 * np.pi * frequency * t_discrete)

# quantization
min_val, max_val = -1, 1
quantization_step = (max_val - min_val) / (level - 1)
y_quantized = np.round(y_discrete / quantization_step) * quantization_step

# plt.plot(t_continus, y_continus)
# plt.stem(t_discrete, y_discrete)
plt.stem(t_discrete, y_quantized)
for label_value in np.arange(min_val, max_val + quantization_step, quantization_step):
    plt.axhline(y=label_value, color='g', linestyle='--')
plt.title("Quantization")
plt.grid(True)
plt.show()
