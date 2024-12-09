import numpy as np
import matplotlib.pyplot as plt

# Coefficients for the numerator (1 + z^-1) and denominator (1 - 0.5 * z^-1)
num_coeffs = [1, 1]  # 1 + z^-1
den_coeffs = [1, -0.5]  # 1 - 0.5 * z^-1

# Number of samples (N)
N = 50  # This determines the resolution of the inverse Z-transform

# Create the frequency points on the unit circle (angle from 0 to 2pi)
z = np.exp(1j * np.linspace(0, 2 * np.pi, N))

# Compute the Z-transform on the unit circle
X_z = np.polyval(num_coeffs, z) / np.polyval(den_coeffs, z)

# Compute the inverse Z-transform (IDFT)
x_n = np.fft.ifft(X_z).real

# Plot the time-domain signal (inverse Z-transform result)
plt.plot(np.arange(N), x_n)
plt.title('Inverse Z-Transform (Time Domain Signal)')
plt.xlabel('n (Discrete Time)')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()
