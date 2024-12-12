import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 32000
N = 1000
t = np.arange(N) / fs

# Frequencies in Hz
f1 = 4000    # 4 kHz
f2 = 8000    # 8 kHz
f3 = 16000   # 16 kHz

# Amplitudes corresponding to 10 dB, 20 dB, 40 dB
A1 = 10 ** (10 / 20)
A2 = 10 ** (20 / 20)
A3 = 10 ** (40 / 20)

# Generate the composite signal
signal = A1 * np.sin(2 * np.pi * f1 * t) + A2 * np.sin(2 * np.pi * f2 * t) + A3 * np.sin(2 * np.pi * f3 * t)

# PART (a): Plot the generated composite signal
plt.figure(figsize=(10, 4))
plt.plot(t[:200], signal[:200])  # Plotting first 200 samples for clarity
plt.title("Generated Composite Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# Sampling the signal at the Nyquist rate
nyquist_rate = 2 * f3
sample_interval = int(fs / nyquist_rate)
sampled_signal = signal[::sample_interval]
sampled_time = t[::sample_interval]

# PART (b1): Plot the sampled signal
plt.figure(figsize=(10, 4))
plt.stem(sampled_time[:50], sampled_signal[:50])
plt.title("Sampled Signal (Following Nyquist Rate)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# PART (b2): Reconstructed signal
reconstructed_signal = np.zeros_like(signal)
reconstructed_signal[::sample_interval] = sampled_signal

plt.figure(figsize=(10, 4))
plt.plot(t[:200], reconstructed_signal[:200], label="Reconstructed Signal")
plt.plot(t[:200], signal[:200], '--', label="Original Signal", alpha=0.6)
plt.title("Reconstructed Signal vs Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

# PART (c): Perform 8-point DFT on the sampled signal
dft_length = 8
dft_result = np.fft.fft(sampled_signal[:dft_length], dft_length)
amplitude_spectrum = np.abs(dft_result)
phase_spectrum = np.angle(dft_result)

# Plot amplitude spectrum
plt.figure(figsize=(10, 4))
plt.stem(range(dft_length), amplitude_spectrum)
plt.title("Amplitude Spectrum (8-point DFT)")
plt.xlabel("Frequency Bin")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# Plot phase spectrum
plt.figure(figsize=(10, 4))
plt.stem(range(dft_length), phase_spectrum)
plt.title("Phase Spectrum (8-point DFT)")
plt.xlabel("Frequency Bin")
plt.ylabel("Phase (radians)")
plt.grid()
plt.show()
