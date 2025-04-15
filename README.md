# Digital Signal Processing

This repository contains Python implementations of fundamental concepts in Digital Signal Processing (DSP). The experiments involve signal generation, sampling, quantization, discrete-time operations, convolution, correlation, and more. Libraries like NumPy and Matplotlib are used for visualization and computation.

## Table of Contents

- [1. Creating an Analog Signal](#1-creating-an-analog-signal)
- [2. Sampling](#2-sampling)
- [3. Quantization](#3-quantization)
- [4. Elementary Discrete-Time Signals](#4-elementary-discrete-time-signals)
- [5. Elementary Operations on Discrete-Time Signals](#5-elementary-operations-on-discrete-time-signals)
- [6. Shifting](#6-shifting)
- [7. Scaling](#7-scaling)
- [8. Reversal](#8-reversal)
- [9. Convolution](#9-convolution)
- [10. Correlation](#10-correlation)
- [11. Fourier Series](#11-fourier-series)

## 1. Creating an Analog Signal

A simple sinusoidal signal is generated using the equation:

```python
t_continuous = np.linspace(tmin, tmax, 1000)
y_continuous = np.sin(2 * np.pi * frequency * t_continuous)
```

![Analog Signal](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/01.jpg)

## 2. Sampling

Sampling converts a continuous-time signal into a discrete-time signal by taking values at specific intervals:

```python
t_discrete = np.arange(tmin, tmax, 1/sampling_frequency)
y_discrete = np.sin(2 * np.pi * frequency * t_discrete)
```

![Sampling](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/02.jpg)

## 3. Quantization

Quantization involves mapping sampled values to a finite set of discrete levels. It reduces the precision of the signal but is essential for digital representation.

```python
min_val, max_val = -1, 1
quantization_step = (max_val - min_val) / (level - 1)
y_quantized = np.round(y_discrete / quantization_step) * quantization_step
```

![Quantization](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/03.jpg)

## 4. Elementary Discrete-Time Signals

These basic signals form the foundation for DSP operations:
- **Unit Sample Signal (Impulse Function, δ(n))**: A signal that is 1 at \( n=0 \) and 0 elsewhere.
- **Unit Step Signal (u(n))**: A signal that is 1 for \( n \geq 0 \) and 0 otherwise.
- **Unit Ramp Signal (ur(n))**: A signal that increases linearly with \( n \).

```python
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
```

![Elementary Discrete-Time Signals](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/04.jpg)

## 5. Elementary Operations on Discrete-Time Signals

Operations performed on two discrete-time signals include:
- **Addition:** Element-wise sum of two signals.
- **Subtraction:** Element-wise difference of two signals.
- **Multiplication:** Pointwise multiplication of signals.
- **Division:** Pointwise division of signals.
- **Scalar Multiplication:** Scaling a signal by a constant factor.

```python
add = y1 + y2
sub = y1 - y2
div = y1 / y2
mul = y1 * y2
scalar_mul = y1 * 2
```

![Elementary Operations on Discrete-Time Signals](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/05.jpg)

## 6. Shifting

- **Right Shifting (Delay):** \( y[n] = x[n - k] \)
- **Left Shifting (Advance):** \( y[n] = x[n + k] \)

```python
# Calculate shifted indices and populate y(n)
for n in range(left - k, right - k + 1):
    if n + k in x:
        y[n] = x[n + k]
```
![Left Shifting](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/06_l.jpg)
![Right Shifting](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/06_r.jpg)

## 7. Scaling

- **Up Scaling (Expansion):** Increases time intervals, making the signal appear compressed.
- **Down Scaling (Compression):** Decreases time intervals, making the signal appear stretched.

```python
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
```

![Up Scaling](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/07_u.jpg)
![Down Scaling](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/07_d.jpg)

## 8. Reversal

Time reversal flips the signal around ( n=0 ):
y[n] = x[-n]

```python
for i in range(-right, -left+1):
    y[i] = x[-i]
```

![Reversal](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/08.jpg)

## 9. Convolution

Convolution helps determine how two signals interact. Three approaches are implemented:
1. **Manual Convolution:** Using the convolution summation formula. 
2. **Using `np.convolve()` Function:** Built-in NumPy function, [convolve()](https://numpy.org/doc/2.1/reference/generated/numpy.convolve.html) for efficient computation. 
![Convolution](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/conv.jpg)

3. **Noise Removal using Convolution:** Using convolution with a smoothing kernel to filter noise. 
![Noise Remover](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/noiseremover.jpg)
<br>

## 10. Correlation

Correlation measures similarity between signals:
1. **Manual Correlation:** Computed using the mathematical formula.
![Correlation](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/corr.jpg)
2. **Autocorrelation:** Determines periodicity in signals using:
   Implemented both manually and using [np.correlate()](https://numpy.org/doc/2.1/reference/generated/numpy.correlate.html).
   ![Auto Correlation](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/auto.jpg)

> [!IMPORTANT]
> Your sine wave is sampled over a limited number of points. Unlike an infinitely long sine wave, a finite-length signal gradually loses energy as you shift it further. This causes the autocorrelation amplitude to decrease over time.


3. **Harmonic Signal Generation:** A composite signal made by summing sinusoidal signals of different frequencies:
This harmonic signal represents a sum of sine waves with increasing frequencies, useful for analyzing periodicity.
![Harmonic Signal](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/harmonic.jpg)

---

## 11. Fourier Series

It contains experiments and implementations related to **Fourier Series**. The experiments demonstrate how periodic signals can be decomposed into sine/cosine components (Fourier Series) and reconstructed from their frequency-domain representations.

---

1. **Harmonic Signal (Sum of Sine Waves)**
To demonstrate that a periodic signal can be represented as a sum of sine signals (Fourier Series).

**Procedure**
1. Generated multiple sine waves with different frequencies (harmonics).
2. Summed them to produce a periodic signal.
3. Observed that the resulting signal is periodic.

**Results**
The following image shows the individual sine waves and their summation, which forms a periodic signal:

![Harmonic Signal Summation](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/f1.jpg) 

```python
t = np.arange(tmin, tmax, 1/sampling_frequency)
y = np.sin(2 * np.pi * frequency * t)
Y = 0

for i in range(50):
    Y += np.sin(2 * np.pi * (frequency + 2*i) * t)

```

---

2. **Fourier Coefficients of a Square Wave**
To analyze the Fourier coefficients C<sub>k</sub> of a square wave, plot its **frequency-domain representation**, **Power Spectrum** and **Reconstruct the signal** from its Fourier coefficients.

**Procedure**
1. Computed the Fourier coefficients C<sub>k</sub> of a square wave.
Here, C<sub>k</sub> = $$\frac{A.a.sin(π.k.F)}{T.π.K.F}$$
2. Plotted the **magnitude spectrum** (frequency domain, C<sub>k</sub>).
3. Plotted the **power spectrum** (squared magnitude of |C<sub>k</sub>|<sup>2</sup>).
4. Reconstructed the square wave using the Fourier coefficients.
The square wave was successfully reconstructed using Fourier coefficients, demonstrating the **synthesis** capability of Fourier Series.
x(t) = Σ Cₖ · e^(j·2π·k·f₀·t)

```python
# Fourier Coefficients
Ck = np.zeros_like(k, dtype=np.float64)
Ck[k != 0] = (A * a * np.sin(np.pi * k[k != 0] * Fa)) / (Tp * np.pi * k[k != 0] * Fa)
Ck[k == 0] = A * a / Tp

# Power Spectrum
Pk = np.abs(Ck) ** 2

# Time and Reconstructed Signal
# t = np.linspace(0, Tp, 1000)
T_show = 4 * Tp  # e.g., 4 full periods
t = np.linspace(0, T_show, 4000)

x_t = np.zeros_like(t, dtype=np.complex128)
for i, ki in enumerate(k):
    x_t += Ck[i] * np.exp(1j * 2 * np.pi * ki * Fa * t)
x_t = np.real(x_t)

```

![Fourier](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/f2.jpg) 




