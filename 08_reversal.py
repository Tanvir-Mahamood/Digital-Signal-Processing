import numpy as np
import matplotlib.pyplot as plt

x = {n: np.sin(0.1 * n) + np.random.uniform(-0.1, 0.1) for n in range(-25, 25)}
y = {}
left = min(x.keys())
right = max(x.keys())

for i in range(-right, -left+1):
    y[i] = x[-i]

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].stem(list(x.keys()), list(x.values()), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[0].set_title('Input Signal, x(n)')
axs[0].grid(True)

axs[1].stem(list(y.keys()), list(y.values()), basefmt=" ", linefmt="green", markerfmt="go")
axs[1].set_title("Reversal")
axs[1].grid(True)

plt.tight_layout()
plt.show()
