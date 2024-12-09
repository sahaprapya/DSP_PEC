import numpy as np
import matplotlib.pyplot as plt

# Parameters
duration = 2          # Duration in seconds
sampling_rate = 1000  # Sampling rate in Hz

# Generate time vector
t = np.linspace(-duration, duration, int(2 * sampling_rate * duration), endpoint=False)

# Generate Unit Step signal
unit_step = np.where(t >= 0, 1, 0)

# Plot the Unit Step signal
plt.figure(figsize=(8, 4))
plt.plot(t, unit_step, label='Unit Step Signal', color='blue')
plt.title('Unit Step Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.show()
