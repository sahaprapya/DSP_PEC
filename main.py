import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 5
amplitude = 1
phase = 0
duration = 2
sampling_rate = 1000

# Generate time vector
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate Sine and Cosine signals
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t + phase)
cosine_wave = amplitude * np.cos(2 * np.pi * frequency * t + phase)

# Plot the signals
plt.figure(figsize=(10, 6))

# Sine wave
plt.subplot(2, 1, 1)
plt.plot(t, sine_wave, label='Sine Wave', color='red')
plt.title('Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Cosine wave
plt.subplot(2, 1, 2)
plt.plot(t, cosine_wave, label='Cosine Wave', color='orange')
plt.title('Cosine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
