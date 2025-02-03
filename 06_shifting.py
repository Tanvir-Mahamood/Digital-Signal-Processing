import numpy as np
import matplotlib.pyplot as plt

# Generate a larger input signal (50 elements)
x = {n: np.sin(0.1 * n) + np.random.uniform(-0.1, 0.1) for n in range(-50, 50)}

# Initialize shifted output dictionary
y = {}

left = min(x.keys())
right = max(x.keys())

k = int(input("How much shifting? "))

# Calculate shifted indices and populate y(n)
for n in range(left - k, right - k + 1):
    if n + k in x:
        y[n] = x[n + k]

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].stem(list(x.keys()), list(x.values()), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[0].set_title('Input Signal, x(n)')
axs[0].grid(True)

axs[1].stem(list(y.keys()), list(y.values()), basefmt=" ", linefmt="green", markerfmt="go")
axs[1].set_title('Left Shifted Signal' if k >= 0 else 'Right Shifted Signal')
axs[1].grid(True)

plt.tight_layout()
plt.show()
