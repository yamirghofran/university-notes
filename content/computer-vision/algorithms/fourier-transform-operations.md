# Fourier Transform Operations

## Overview

The Fourier Transform decomposes an image into its frequency components. In the frequency domain:

- **Center (low frequencies)**: Overall structure, smooth variations, brightness
- **Outer rings (high frequencies)**: Edges, fine details, noise

---

## 1. Downsampling in Fourier Space

### Concept

Reduce image size by cropping the central portion of the Fourier spectrum. This preserves low frequencies (overall structure) while removing high frequencies (fine details).

### Why it works

- High frequencies = fine details, sharp edges
- Low frequencies = overall structure, smooth variations
- By keeping only central frequencies, we avoid aliasing

### Method

Crop central portion of Fourier spectrum:
$$\hat{I}_{new}(u,v) = \begin{cases} \hat{I}(u,v) & \text{if } |u|, |v| \leq L'/2 \\ 0 & \text{otherwise} \end{cases}$$

Where $L'$ is the new (smaller) dimension.

### Pseudocode

```
Algorithm FourierDownsample(image, new_size)
Input:
    - image: input image (M × N)
    - new_size: (new_h, new_w) target dimensions

Output:
    - downsampled image

1. F ← FFT_SHIFT(FFT2(image))           // Forward FFT and center
2. h, w ← image.shape
3. new_h, new_w ← new_size
4.
5. // Calculate crop region (center)
6. start_h ← (h - new_h) // 2
7. start_w ← (w - new_w) // 2
8.
9. // Crop spectrum
10. F_cropped ← F[start_h : start_h+new_h, start_w : start_w+new_w]
11.
12. // Inverse FFT
13. result ← REAL(IFFT2(IFFT_SHIFT(F_cropped)))
14. RETURN result
```

### Advantages

1. **Built-in anti-aliasing**: By removing high frequencies, no aliasing occurs
2. **No ringing**: Smooth cutoff prevents artifacts
3. **Theoretically optimal**: Preserves maximum information for given size

---

## 2. Shifting in Fourier Space

### Concept

Shifting an image in spatial domain is equivalent to multiplying the Fourier transform by a phase factor.

### Formula

$$I(x - x_0, y - y_0) \leftrightarrow \hat{I}(u,v) \cdot e^{-i2\pi(ux_0/N + vy_0/M)}$$

### Pseudocode

```
Algorithm FourierShift(image, shift_x, shift_y)
Input:
    - image: input image
    - shift_x, shift_y: shift amounts in pixels

Output:
    - shifted image

1. M, N ← image.shape
2. F ← FFT2(image)                      // Forward FFT

3. // Create frequency grids
4. u ← FFT_FREQ(N)                      // Horizontal frequencies
5. v ← FFT_FREQ(M)                      // Vertical frequencies
6. U, V ← MESHGRID(u, v)

7. // Compute phase shift
8. phase ← EXP(-2j × π × (U × shift_x + V × shift_y))

9. // Apply phase shift
10. F_shifted ← F × phase

11. // Inverse FFT
12. result ← REAL(IFFT2(F_shifted))
13. RETURN result
```

### Advantages

- Subpixel shifts without interpolation
- Efficient if already in Fourier domain
- No interpolation artifacts

---

## 3. Low-Pass Filtering in Fourier Space

### Concept

Keep low frequencies (smooth variations) and remove high frequencies (noise, edges).

### Types of Low-Pass Filters

#### Ideal Low-Pass (not recommended - causes ringing)

$$H(u,v) = \begin{cases} 1 & \text{if } \sqrt{u^2 + v^2} \leq D \\ 0 & \text{otherwise} \end{cases}$$

#### Gaussian Low-Pass (recommended - smooth)

$$H(u,v) = e^{-\frac{u^2 + v^2}{2\sigma^2}}$$

#### Butterworth Low-Pass

$$H(u,v) = \frac{1}{1 + \left(\frac{D(u,v)}{D_0}\right)^{2n}}$$

### Pseudocode

```
Algorithm GaussianLowPass(image, sigma)
Input:
    - image: input image (M × N)
    - sigma: standard deviation (controls cutoff frequency)

Output:
    - filtered image

1. M, N ← image.shape

2. // Create frequency grid (centered)
3. u ← ARANGE(-M//2, M//2)
4. v ← ARANGE(-N//2, N//2)
5. U, V ← MESHGRID(v, u)

6. // Compute Gaussian mask
7. D2 ← U² + V²
8. H ← EXP(-D2 / (2 × sigma²))

9. // Apply filter in frequency domain
10. F ← FFT_SHIFT(FFT2(image))
11. G ← H × F                              // Element-wise multiplication

12. // Inverse transform
13. result ← REAL(IFFT2(IFFT_SHIFT(G)))
14. RETURN result
```

### Choosing Filter Size

- To remove features of size $S$: cutoff frequency $f = 1/S$
- Larger $\sigma$ = more aggressive smoothing

---

## Key Properties Summary

| Operation    | Spatial Domain   | Frequency Domain |
| ------------ | ---------------- | ---------------- |
| Downsampling | Blur + subsample | Crop center      |
| Upsampling   | Interpolation    | Zero-pad         |
| Shifting     | Re-sample        | Phase multiply   |
| Low-pass     | Gaussian blur    | Gaussian mask    |

---

## Important Notes

1. **Always use fftshift** to center zero frequency for visualization and easier mask creation
2. **Log transform** for visualization: $\log(|F| + 1)$
3. **Soft edges** are important: Binary masks cause artifacts (Gibbs phenomenon)
4. **Convolution theorem**: Convolution in spatial = multiplication in frequency
