---
title: Discrete Fourier Transform
---

## Definition

For a 1D discrete signal with $N$ samples, the DFT is:

$$\hat{g}_k = \sum_{n=0}^{N-1} g_n \cdot e^{-i2\pi kn/N}, \quad k = 0, 1, ..., N-1$$

The inverse DFT:
$$g_n = \frac{1}{N} \sum_{k=0}^{N-1} \hat{g}_k \cdot e^{i2\pi kn/N}, \quad n = 0, 1, ..., N-1$$

For 2D images ($M \times N$):
$$\hat{g}[k,l] = \sum_{m=0}^{M-1} \sum_{n=0}^{N-1} g[m,n] \cdot e^{-i2\pi\left(\frac{km}{M} + \frac{ln}{N}\right)}$$

---

## Standard DFT Pseudocode

### 1D DFT

```
Algorithm DFT_1D(signal)
Input:
    - signal: array of N real/complex numbers [g_0, g_1, ..., g_{N-1}]

Output:
    - spectrum: array of N complex numbers [ĝ_0, ĝ_1, ..., ĝ_{N-1}]

1. N ← LENGTH(signal)
2. spectrum ← ARRAY of size N (complex)

3. FOR k = 0 TO N-1 DO:
4.     sum ← 0 (complex)
5.     FOR n = 0 TO N-1 DO:
6.         angle ← -2π × k × n / N
7.         twiddle ← COS(angle) + i × SIN(angle)    // e^{-i2πkn/N}
8.         sum ← sum + signal[n] × twiddle
9.     END FOR
10.    spectrum[k] ← sum
11. END FOR

12. RETURN spectrum
```

### 2D DFT (for images)

```
Algorithm DFT_2D(image)
Input:
    - image: M × N matrix

Output:
    - spectrum: M × N complex matrix

1. M, N ← image.shape
2. spectrum ← M × N complex matrix

3. // Apply 1D DFT to each row
4. FOR m = 0 TO M-1 DO:
5.     row_spectrum[m, :] ← DFT_1D(image[m, :])
6. END FOR

7. // Apply 1D DFT to each column
8. FOR n = 0 TO N-1 DO:
9.     spectrum[:, n] ← DFT_1D(row_spectrum[:, n])
10. END FOR

11. RETURN spectrum
```

---

## Inverse DFT Pseudocode

### 1D Inverse DFT

```
Algorithm IDFT_1D(spectrum)
Input:
    - spectrum: array of N complex numbers

Output:
    - signal: array of N real/complex numbers

1. N ← LENGTH(spectrum)
2. signal ← ARRAY of size N (complex)

3. FOR n = 0 TO N-1 DO:
4.     sum ← 0 (complex)
5.     FOR k = 0 TO N-1 DO:
6.         angle ← 2π × k × n / N
7.         twiddle ← COS(angle) + i × SIN(angle)    // e^{i2πkn/N}
8.         sum ← sum + spectrum[k] × twiddle
9.     END FOR
10.    signal[n] ← sum / N
11. END FOR

12. RETURN signal
```

---

## Complexity Analysis

| Algorithm | Time Complexity                               |
| --------- | --------------------------------------------- |
| Naive DFT | $O(N^2)$ for 1D, $O(MN(M+N))$ for 2D          |
| FFT       | $O(N \log N)$ for 1D, $O(MN \log(MN))$ for 2D |

---

## Fast Fourier Transform (FFT) - Divide and Conquer

The FFT exploits the periodicity and symmetry of the twiddle factors:

```
Algorithm FFT_1D(signal)
Input:
    - signal: array of N = 2^m samples

Output:
    - spectrum: array of N complex numbers

1. N ← LENGTH(signal)

2. IF N == 1 THEN:
3.     RETURN signal

4. // Divide
5. even ← FFT_1D(signal[0, 2, 4, ...])      // Even indices
6. odd  ← FFT_1D(signal[1, 3, 5, ...])      // Odd indices

7. // Combine (Butterfly operation)
8. spectrum ← ARRAY of size N
9. FOR k = 0 TO N/2 - 1 DO:
10.    twiddle ← EXP(-2πi × k / N)
11.    spectrum[k]       ← even[k] + twiddle × odd[k]
12.    spectrum[k + N/2] ← even[k] - twiddle × odd[k]
13. END FOR

14. RETURN spectrum
```

---

## Key Properties

| Property           | Time Domain              | Frequency Domain                     |
| ------------------ | ------------------------ | ------------------------------------ | --- | ----------------- | ---------- | --- |
| Linearity          | $\alpha g_1 + \beta g_2$ | $\alpha \hat{g}_1 + \beta \hat{g}_2$ |
| Shifting           | $g[n - n_0]$             | $e^{-i2\pi kn_0/N} \cdot \hat{g}[k]$ |
| Convolution        | $g_1 * g_2$              | $\hat{g}_1 \cdot \hat{g}_2$          |
| Parseval's Theorem | $\sum                    | g[n]                                 | ^2$ | $\frac{1}{N} \sum | \hat{g}[k] | ^2$ |

---

## Frequency Ordering

For $N$ samples, DFT frequencies are:

- Without shift: $[0, \frac{1}{N}, \frac{2}{N}, ..., \frac{N/2}{N}, -\frac{N/2-1}{N}, ..., -\frac{1}{N}]$
- After fftshift: $[-\frac{N/2}{N}, ..., -\frac{1}{N}, 0, \frac{1}{N}, ..., \frac{N/2-1}{N}]$

---

## Practical Implementation (Python/NumPy style)

```python
import numpy as np

# Forward transform
F = np.fft.fft2(image)
F_shifted = np.fft.fftshift(F)  # Center zero frequency

# Magnitude spectrum (for visualization)
magnitude = np.log(np.abs(F_shifted) + 1)

# Inverse transform
image_reconstructed = np.real(np.fft.ifft2(np.fft.ifftshift(F_shifted)))
```
