import numpy as np

# Input signals
x = np.array([1, 2, 3])
h = np.array([4, 5, 6])

def perform_convolution(x, h):
    n1 = len(x)
    n2 = len(h)
    y_length = n1 + n2 - 1
    y = np.zeros(y_length)

    for i in range(y_length):
        for j in range(n1):
            if 0 <= i - j < n2:
                y[i] += x[j] * h[i - j]
    return y

y = perform_convolution(x, h)
print("Convolution Result:", y)
