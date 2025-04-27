import numpy as np
import matplotlib.pyplot as plt
import math

n = np.arange(-10, 11, 1)
unit_sample = np.zeros(len(n))
unit_step = np.zeros(len(n))
unit_ramp = np.zeros(len(n))

def unit_sample_signal():
    for i in range(len(n)):
        if n[i] == 0:
            unit_sample[i] = 1

def unit_step_signal():
    for i in range(len(n)):
        if n[i] >= 0:
            unit_step[i] = 1

def unit_ramp_signal():
    for i in range(len(n)):
        if n[i] >= 0:
            unit_ramp[i] = n[i]

def shifting_signal(x1, k):
    y_shifted = {}

    left = min(x1.keys())
    right = max(x1.keys())

    
    for n in range(left - k, right - k + 1): # Shifting
        if n + k in x1:
            y_shifted[n] = x1[n + k]

    return y_shifted

def scalling_signal(x1, a):
    y_scalled = {}

    left = min(x1.keys())
    right = max(x1.keys())

    def interpolation(n1, n2):
        n1 = max(n1, left)
        n2 = max(n2, left)
        n1 = min(n1, right)
        n2 = min(n2, right)

        val1 = x1[n1]
        val2 = x1[n2]

        return (val1 + val2) / 2
        

    l = int(left // a)
    r = int(right // a)

    for n in range(l, r+1):
        key = a * n
        if key == int(key):
            key_int = int(key)
            if key_int in x1:
                y_scalled[n] = x1[key_int]
            else:
                y_scalled[n] = 0  # or some other default value
        else:
            y_scalled[n] = interpolation(math.floor(key), math.ceil(key))

    return y_scalled
    
def reversal_signal(xxx):
    y_reversaled = {}
    left = min(xxx.keys())
    right = max(xxx.keys())

    for i in range(-right, -left+1):
        y_reversaled[i] = xxx[-i]

    return y_reversaled


# Task 1
unit_sample_signal()
unit_step_signal()
unit_ramp_signal()

# Task 2
n_range = range(-50, 50)
x1 = {n: np.sin(0.1 * n) + np.random.uniform(-0.1, 0.1) for n in n_range}
x2 = {n: np.sin(0.15 * n + 2) + np.random.uniform(-0.15, 0.15) for n in n_range}

n_vals = np.array(list(n_range))
x1_vals = np.array([x1[n] for n in n_range])
x2_vals = np.array([x2[n] for n in n_range])

# ------------------------------------------------------------------
sum_sig = x1_vals + x2_vals
prod_sig = x1_vals * x2_vals
# ------------------------------------------------------------------
y_shifted = {}
k = -20
y_shifted = shifting_signal(x1, k)
# -------------------------------------------------------------------
y_scalled = {}
a = 3
y_scalled = scalling_signal(x1, a)
# -------------------------------------------------------------------
y_reversaled = {}
y_reversaled = reversal_signal(x1)
# -------------------------------------------------------------------
y_combined = {} # sin(-2n+3)
y_combined = shifting_signal(x1, 3)
y_combined = scalling_signal(y_combined, 2)
y_combined = reversal_signal(y_combined)

fig, axs = plt.subplots(4, 3, figsize=(15, 7))

axs[0][0].stem(n, unit_sample)
axs[0][0].set_title('Unit Sample Sequence.')

axs[0][1].stem(n, unit_step)
axs[0][1].set_title('Unit Step Sequence.')

axs[0][2].stem(n,unit_ramp)
axs[0][2].set_title('Unit Ramp Sequence.')

axs[1][0].stem(list(x1.keys()), list(x1.values()), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[1][0].set_title('Input Signal, x1(n)')
axs[1][0].grid(True)

axs[1][1].stem(list(x2.keys()), list(x2.values()), basefmt=" ", linefmt="blue", markerfmt="bo")
axs[1][1].set_title('Input Signal, x2(n)')
axs[1][1].grid(True)

axs[1][2].stem(n_vals, sum_sig, markerfmt='ro', basefmt=" ")
axs[1][2].set_title('Addition')

axs[2][0].stem(n_vals, prod_sig, markerfmt='ro', basefmt=" ")
axs[2][0].set_title('Multiplication')

axs[2][1].stem(list(y_shifted.keys()), list(y_shifted.values()), basefmt=" ", linefmt="green", markerfmt="go")
axs[2][1].set_title('Left Shifted Signal' if k >= 0 else 'Right Shifted Signal')
axs[2][1].grid(True)

axs[2][2].stem(list(y_scalled.keys()), list(y_scalled.values()), basefmt=" ", linefmt="green", markerfmt="go")
axs[2][2].set_title('Down Scaled' if a > 1 else 'Up Scaled')
axs[2][2].grid(True)

axs[3][0].stem(list(y_reversaled.keys()), list(y_reversaled.values()), basefmt=" ", linefmt="green", markerfmt="go")
axs[3][0].set_title('Reversal')
axs[3][0].grid(True)

axs[3][1].stem(list(y_combined.keys()), list(y_combined.values()), basefmt=" ", linefmt="green", markerfmt="go")
axs[3][1].set_title('Combined')
axs[3][1].grid(True)

plt.tight_layout()
plt.show()
