import numpy as np
import matplotlib.pyplot as plt
import math

x = {n: np.sin(0.1 * n) + np.random.uniform(-0.1, 0.1) for n in range(-25, 25)}
y = {}
left = min(x.keys())
right = max(x.keys())

def interpolation(n1, n2):
    n1 = max(n1, left)
    n2 = max(n2, left)
    n1 = min(n1, right)
    n2 = min(n2, right)

    val1 = x[n1]
    val2 = x[n2]

    return (val1 + val2) / 2
    
a = float(input("How much Scaling? "))

l = int(left // a)
r = int(right // a)

for n in range(l, r+1):
    key = a * n
    if key == int(key):
        key_int = int(key)
        if key_int in x:
            y[n] = x[key_int]
        else:
            y[n] = 0  # or some other default value
    else:
        y[n] = interpolation(math.floor(key), math.ceil(key))

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].stem(list(x.keys()), list(x.values()), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[0].set_title('Input Signal, x(n)')
axs[0].grid(True)

axs[1].stem(list(y.keys()), list(y.values()), basefmt=" ", linefmt="green", markerfmt="go")
axs[1].set_title('Down Scaled' if a > 1 else 'Up Scaled')
axs[1].grid(True)

plt.tight_layout()
plt.show()