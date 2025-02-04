import numpy as np
import matplotlib.pyplot as plt

# Analog Signal with Noise
idx_x = np.linspace(-np.pi, 2 * np.pi, 60)
x = np.sin(idx_x) + np.random.uniform(-0.2, 0.2, 60)

h = np.ones(5) / 5 
y = np.convolve(x, h, mode='same')  

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].stem(list(idx_x), list(x), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[0].set_title('Input Signal, x(n)')
axs[0].grid(True)

axs[1].stem(list(idx_x), list(y), basefmt=" ", linefmt="green", markerfmt="go")
axs[1].set_title("Convoluted Noiseless Signal")
axs[1].grid(True)

plt.tight_layout()
plt.show()



