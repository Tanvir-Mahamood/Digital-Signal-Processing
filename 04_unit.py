import numpy as np
import matplotlib.pyplot as plt


n = np.arange(-10, 11, 1)

#unit Sample Sequence
unit_sample = np.zeros(len(n))
for i in range(len(n)):
    if n[i] == 0:
        unit_sample[i] = 1

#Unit Step Sequence
unit_step = np.zeros(len(n))
for i in range(len(n)):
    if n[i] >= 0:
        unit_step[i] = 1


#Unit ramp Sequence
unit_ramp = np.zeros(len(n))
for i in range(len(n)):
    if n[i] >= 0:
        unit_ramp[i] = n[i]


#Plotting the signals.
fig, axs = plt.subplots(3,2,figsize=(8,8))
axs[0][0].stem(n, unit_sample)
axs[0][0].set_title('Unit Sample Sequence.')

axs[1][0].stem(n, unit_step)
axs[1][0].set_title('Unit Step Sequence.')

axs[2][0].stem(n,unit_ramp)
axs[2][0].set_title('Unit Ramp Sequence.')


plt.tight_layout()
plt.show()