import numpy as np
import matplotlib.pyplot as plt

# Define the signal x[n]
n = np.arange(0, 20)  # Discrete time indices
x_n = np.sin(0.2 * np.pi * n)  # Example signal: sin wave

# Compute the Z-transform
z = np.linspace(0.1, 2, 1000)  # Values for z (magnitude)
X_z = np.array([np.sum(x_n * z_val**(-n)) for z_val in z])  # Z-transform for each z

# Plot the real and imaginary parts of the Z-transform
plt.plot(z, np.real(X_z), label='Real Part')
plt.plot(z, np.imag(X_z), label='Imaginary Part')
plt.title('Z-Transform')
plt.xlabel('Magnitude of z')
plt.ylabel('Z-Transform')
plt.legend()
plt.grid(True)
plt.show()
