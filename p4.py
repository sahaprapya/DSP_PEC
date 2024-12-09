import numpy as np
import matplotlib.pyplot as plt

# Generate time values
duration = 5         # Duration in seconds
sampling_rate = 1000  # Sampling rate in Hz

# Generate time vector
t = np.linspace(-duration, duration, int(2 * sampling_rate * duration), endpoint=False)

# Parameters for the exponential signal
A = 1  # Amplitude
alpha = 0.5  # Growth rate (change this for different growth/decay behavior)

# Generate exponential signal
x_t = A * np.exp(alpha * t)  # Exponential signal formula: A * e^(alpha * t)

# Plot the exponential signal
plt.plot(t, x_t, label="Exponential Signal")
plt.title("Exponential Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
