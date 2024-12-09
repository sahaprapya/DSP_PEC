import matplotlib.pyplot as plt
import numpy as np

# Generate time values

duration = 2          # Duration in seconds
sampling_rate = 1000  # Sampling rate in Hz

t = np.linspace(-duration, duration, int(2 * sampling_rate * duration), endpoint=False)

# Generate unit ramp signal
r_t = np.maximum(0, t)  # Unit ramp: 0 if t < 0, t if t >= 0

# Plot the unit ramp signal
plt.plot(t, r_t, label="Unit Ramp Signal")
plt.title("Unit Ramp Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.8)
plt.axvline(0, color='black',linewidth=0.8)
plt.legend()
plt.show()
