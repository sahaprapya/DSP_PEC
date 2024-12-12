import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Define parameters
fs = 1000  # Sampling frequency in Hz
num_taps = 51  # Filter order + 1
filter_type = 'lowpass'  # Options: 'lowpass', 'highpass', 'bandpass', 'bandstop'
cutoff_freqs = [200]  # Cutoff frequency in Hz (use two values for bandpass/bandstop)

# Nyquist frequency
nyquist = fs / 2

# Normalize cutoff frequencies
normalized_cutoff = [f / nyquist for f in cutoff_freqs]

# Design the FIR filter
fir_coefficients = firwin(num_taps, normalized_cutoff, pass_zero=filter_type, window='hamming')

# Compute the frequency response
w, h = freqz(fir_coefficients, worN=8000, fs=fs)

# Plot the frequency response
plt.figure(figsize=(8, 4))
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.title(f"{filter_type.capitalize()} FIR Filter Response")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.grid()
plt.show()

# Display the filter coefficients
print("Filter coefficients:")
print(fir_coefficients)
