import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
x1 = np.array([1, 2, 3])
h1 = np.array([4, 5, 6])

idx_x1 = np.arange(0,len(x1))
idx_h1 = np.arange(0,len(h1))

def perform_convolution(x, h):
    n1 = len(x1)
    n2 = len(h1)
    y_length = n1 + n2 - 1
    y1 = np.zeros(y_length)

    for i in range(y_length):
        for j in range(n1):
            if 0 <= i - j < n2:
                y1[i] += x1[j] * h1[i - j]
    return y1

y1 = perform_convolution(x1, h1)
idx_y1 = np.arange(0,len(y1))
print("Convolution Result:", y1)

# -------------------------------------------------------------------

x2 = np.array([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
idx_x2 = np.arange(0,len(x2))
h2 = np.array([0.2,0.2,0.2,0.2,0.2])

y2 = np.convolve(x2, h2)
idx_y2 = np.arange(0, len(y2))

# -------------------------------------------------------------------

# Analog Signal with Noise
idx_x3 = np.linspace(-np.pi, 2 * np.pi, 60)
x3 = np.sin(idx_x3) + np.random.uniform(-0.2, 0.2, 60)

h3 = np.ones(5) / 5 
y3 = np.convolve(x3, h3, mode='same') 

# -------------------------------------------------------------------

x4 = x1
y4 = h1

idx_x4 = np.arange(0,len(x4))
idx_y4 = np.arange(0,len(y4))

plt_x = []
plt_y = []

for lag in range(-len(y4) + 1, len(x4)):  
    r = 0
    for i in range(len(x4)):
        if 0 <= i - lag < len(y4):  
            r += x4[i] * y4[i - lag]  
    plt_x.append(lag)
    plt_y.append(r)

# ---------------------------------------------------------------

fig, axs = plt.subplots(4, 3, figsize=(10,10))
axs[0][0].stem(list(idx_x1), list(x1), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[0][0].set_title('x1(n)')
axs[0][0].grid(True)

axs[0][1].stem(list(idx_h1), list(h1), basefmt=" ", linefmt="green", markerfmt="go")
axs[0][1].set_title('h1(n)')
axs[0][1].grid(True)

axs[0][2].stem(list(idx_y1), list(y1), basefmt=" ", linefmt="green", markerfmt="go")
axs[0][2].set_title('y1(n) = conv(x,h)')
axs[0][2].grid(True)


axs[1][0].stem(list(idx_x2), list(x2), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[1][0].set_title('x2(n)')
axs[1][0].grid(True)

axs[1][1].stem(list(idx_y2), list(y2), basefmt=" ", linefmt="green", markerfmt="go")
axs[1][1].set_title('y2=conv(x,h)')
axs[1][1].grid(True)

axs[2][0].stem(list(idx_x3), list(x3), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[2][0].set_title('x2(n)')
axs[2][0].grid(True)

axs[2][1].stem(list(idx_x3), list(y3), basefmt=" ", linefmt="green", markerfmt="go")
axs[2][1].set_title('y2=conv(x,h)')
axs[2][1].grid(True)


axs[3][0].stem(list(idx_x4), list(x4), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[3][0].set_title('x1(n)')
axs[3][0].grid(True)

axs[3][1].stem(list(idx_y4), list(y4), basefmt=" ", linefmt="green", markerfmt="go")
axs[3][1].set_title('x2(n)')
axs[3][1].grid(True)

axs[3][2].stem(list(plt_x), list(plt_y), basefmt=" ", linefmt="green", markerfmt="go")
axs[3][2].set_title('Correlation with diff time delay')
axs[3][2].grid(True)

plt.tight_layout()
plt.show()