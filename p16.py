import numpy as np
import matplotlib.pyplot as plt

# Signal in time domain
t = np.linspace(0, 1, 500)
original_signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# Fourier Transform
freq_signal = np.fft.fft(original_signal)
# Reconstruct the signal using Inverse Fourier Transform
reconstructed_signal = np.fft.ifft(freq_signal)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, original_signal, label='Original Signal')
plt.plot(t, reconstructed_signal.real, '--', label='Reconstructed Signal')
plt.legend()
plt.show()
