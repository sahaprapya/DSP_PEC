import numpy as np
import matplotlib.pyplot as plt

# Define the two input sequences
x = [1, 2, 3, 4]  # First sequence
y = [4, 3, 2, 1]  # Second sequence

# Length of the sequences
N = len(x)
M = len(y)

# Pad the shorter sequence with zeros to make both sequences equal in length (optional)
if N != M:
    if N < M:
        x = np.pad(x, (0, M - N))
    else:
        y = np.pad(y, (0, N - M))

# Compute cross-correlation manually
cross_corr = []
for k in range(-N + 1, N):  # Lag values from -(N-1) to (N-1)
    sum_corr = 0
    for n in range(N):
        if 0 <= n + k < N:  # Check bounds for valid indices
            sum_corr += x[n] * y[n + k]
    cross_corr.append(sum_corr)

# Define the lags
lags = np.arange(-N + 1, N)

# Print the cross-correlation values
print("Cross-Correlation values:")
for lag, value in zip(lags, cross_corr):
    print(f"Lag {lag}: {value}")

# Plot the cross-correlation
plt.stem(lags, cross_corr)
plt.title('Cross-Correlation')
plt.xlabel('Lag (k)')
plt.ylabel('Cross-Correlation Value')
plt.grid(True)
plt.show()


