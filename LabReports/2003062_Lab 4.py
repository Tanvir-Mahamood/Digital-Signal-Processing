import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------
tmin=-1
tmax=1
frequency = 1
sampling_frequency = 80

t = np.arange(tmin, tmax, 1/sampling_frequency)
y = np.sin(2 * np.pi * frequency * t)
Y = 0

for i in range(50):
    Y += np.sin(2 * np.pi * (frequency + 2*i) * t)

# -----------------------------------------------------------
A = 1.0
a = 1.0
Tp = 2.0
Fa = 1 / Tp
k = np.arange(-100, 101)

# Fourier Coefficients
Ck = np.zeros_like(k, dtype=np.float64)
Ck[k != 0] = (A * a * np.sin(np.pi * k[k != 0] * Fa)) / (Tp * np.pi * k[k != 0] * Fa)
Ck[k == 0] = A * a / Tp

# Power Spectrum
Pk = np.abs(Ck) ** 2

# Time and Reconstructed Signal
# t = np.linspace(0, Tp, 1000)
T_show = 4 * Tp  # e.g., 4 full periods
t_ = np.linspace(0, T_show, 4000)

x_t = np.zeros_like(t_, dtype=np.complex128)
for i, ki in enumerate(k):
    x_t += Ck[i] * np.exp(1j * 2 * np.pi * ki * Fa * t_)
x_t = np.real(x_t)

# Create subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 10))  # 3 rows, 1 column

axs[0].stem(t, Y)
axs[0].set_title("Harmoic")
axs[0].set_xlabel('t')
axs[0].set_ylabel('y')
axs[0].grid(True)


# Plot Fourier Coefficients
axs[1].stem(k, Ck, basefmt=" ", markerfmt='ro', linefmt='b-')
axs[1].set_title('Fourier Coefficients $C_k$')
axs[1].set_xlabel('k')
axs[1].set_ylabel('$C_k$')
axs[1].grid(True)

# Plot Power Spectrum
axs[2].stem(k, Pk, basefmt=" ", markerfmt='go', linefmt='g-')
axs[2].set_title('Power Spectrum $|C_k|^2$')
axs[2].set_xlabel('k')
axs[2].set_ylabel('Power')
axs[2].grid(True)

# Plot Reconstructed Signal
axs[3].plot(t_, x_t, 'm')
axs[3].set_title('Reconstructed Signal $x(t)$ from Fourier Coefficients')
axs[3].set_xlabel('Time (t)')
axs[3].set_ylabel('x(t)')
axs[3].grid(True)

# Adjust layout
plt.tight_layout()
plt.show()
