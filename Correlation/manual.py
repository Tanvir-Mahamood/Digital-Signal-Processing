import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

plt_x = []
plt_y = []

for lag in range(-len(y) + 1, len(x)):  
    r = 0
    for i in range(len(x)):
        if 0 <= i - lag < len(y):  
            r += x[i] * y[i - lag]  
    plt_x.append(lag)
    plt_y.append(r)

plt.stem(plt_x, plt_y)
plt.title("Lag vs Correlated Value")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)
plt.show()


"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3])
y = np.array([4,5,6])
r = 0
plt_x = []
plt_y = []

n = max(len(x), len(y))

for lag in range(-10, 10):
    r = 0
    for i in range(n):
        xx = x[i] if i < len(x) else 0
        yy = y[i-lag] if i-lag>=0 and i-lag<len(y) else 0
        r = xx * yy
    plt_x.append(lag)
    plt_y.append(r)


plt.stem(plt_x, plt_y)
plt.title("Lag vs Correlated value")
plt.grid(True)
plt.show()
"""