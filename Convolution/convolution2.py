import numpy as np
import matplotlib.pyplot as plt

# Input signals
x = np.array([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
idx_x = np.arange(0,len(x))
h = np.array([0.2,0.2,0.2,0.2,0.2])

y = np.convolve(x, h)
idx_y = np.arange(0, len(y))
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].stem(list(idx_x), list(x), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[0].set_title('Input Signal, x(n)')
axs[0].grid(True)

axs[1].stem(list(idx_y), list(y), basefmt=" ", linefmt="green", markerfmt="go")
axs[1].set_title("Convoluted Signal")
axs[1].grid(True)

plt.tight_layout()
plt.show()