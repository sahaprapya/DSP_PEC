import numpy as np
import matplotlib.pyplot as plt

# Define the input sequence
x = [1, 2, 3, 4]  # Example sequence

# Length of the sequence
N = len(x)

# Compute autocorrelation manually
autocorr = []
for k in range(-N + 1, N):  # Lag values from -(N-1) to (N-1)
    sum_corr = 0
    for n in range(N):
        if 0 <= n + k < N:  # Check bounds for valid indices
            sum_corr += x[n] * x[n + k]
    autocorr.append(sum_corr)

# Define the lags
lags = np.arange(-N + 1, N)

# Print the autocorrelation values
print("Autocorrelation values:")
for lag, value in zip(lags, autocorr):
    print(f"Lag {lag}: {value}")


# Plot the autocorrelation
plt.stem(lags, autocorr)
plt.title('Autocorrelation')
plt.xlabel('Lag (k)')
plt.ylabel('Autocorrelation Value')
plt.grid(True)
plt.show()


