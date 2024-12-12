import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz

# Step 1: Get user input for filter type and parameters
print("IIR Filter Design")
print("1. Butterworth")
filter_type = int(input("Select filter type (1 for Butterworth): "))

if filter_type != 1:
    print("Currently only Butterworth filter is available. Exiting.")
    exit()

print("Filter Configuration")
print("1. Lowpass")
config_type = int(input("Select filter configuration (1 for Lowpass): "))

if config_type != 1:
    print("Currently only Lowpass filter is available. Exiting.")
    exit()

# Step 2: Get additional parameters
fs = float(input("Enter the sampling frequency (Hz): "))
f = float(input("Enter the cutoff frequency (Hz): "))
order = int(input("Enter the filter order: "))

# Normalize the cutoff frequency
wn = f / (fs / 2)  # Normalized cutoff frequency

# Step 3: Design the Butterworth filter
b, a = butter(order, wn, btype='low')

# Step 4: Calculate the frequency response
w, h = freqz(b, a, worN=8000)

# Step 5: Plot the frequency response
plt.figure(figsize=(10, 6))
plt.plot(0.5 * fs * w / np.pi, 20 * np.log10(abs(h)), 'b')
plt.title('Butterworth Lowpass Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.grid()
plt.show()

# Step 6: Display the filter coefficients
print("Filter coefficients:")
print("Numerator (b):", b)
print("Denominator (a):", a)
