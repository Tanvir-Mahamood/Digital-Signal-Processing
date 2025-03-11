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
3. **Harmonic Signal Generation:** A composite signal made by summing sinusoidal signals of different frequencies:
This harmonic signal represents a sum of sine waves with increasing frequencies, useful for analyzing periodicity.
![Harmonic Signal](https://github.com/Tanvir-Mahamood/Digital-Signal-Processing/blob/main/Screenshots/harmonic.jpg)

---

## How to Run

1. Install the required libraries:
   ```bash
   pip install numpy matplotlib
   pip install numpy
   ```
2. Run each script in a Python environment:
   ```bash
   python script_name.py
   ```
3. Output plots will be displayed for visualization.

---

## Acknowledgments

This repository serves as a reference for understanding fundamental DSP operations using Python. The concepts implemented are widely used in signal processing, communications, and control systems.

Happy Coding! 🚀

