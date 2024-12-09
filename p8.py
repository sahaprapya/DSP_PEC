import numpy as np
import matplotlib.pyplot as plt

# Define the input signal
x = [1, 2, 3, 4]  # Example sequence

# Number of points in the signal
N = len(x)

# Initialize an empty list to store the DFT results
X = []

# Compute the DFT manually
for k in range(N):  # For each frequency index k
    sum_real = 0
    sum_imag = 0
    for n in range(N):  # For each time index n
        angle = -2 * np.pi * k * n / N
        sum_real += x[n] * np.cos(angle)  # Real part
        sum_imag += x[n] * np.sin(angle)  # Imaginary part
    X.append(complex(sum_real, sum_imag))  # Combine real and imaginary parts

# Compute the magnitudes of the DFT components
magnitudes = [abs(val) for val in X]

# Plot the DFT magnitudes
plt.stem(range(N), magnitudes)
plt.title('Magnitude of DFT')
plt.xlabel('Frequency Index (k)')
plt.ylabel('Magnitude |X(k)|')
plt.grid(True)
plt.show()
