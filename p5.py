import numpy as np
import matplotlib.pyplot as plt

# Define two example sequences (signals)
x = np.array([1, 2, 9, 4])  # Example sequence x[n]
h = np.array([0.5, 1, 0.5])  # Example sequence h[n]

# Compute the convolution using numpy's convolve function
y = np.convolve(x, h, mode='full')  # 'full' returns the complete convolution result

# Plot the original sequences and their convolution result
plt.figure(figsize=(12, 8))

# Plot x[n]
plt.subplot(3, 1, 1)
plt.plot(np.arange(len(x)), x, label='x[n]', color='blue', marker='o')
plt.title('Sequence x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.legend()

# Plot h[n]
plt.subplot(3, 1, 2)
plt.plot(np.arange(len(h)), h, label='h[n]', color='green', marker='o')
plt.title('Sequence h[n]')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.grid(True)
plt.legend()

# Plot y[n] (Convolution result)
plt.subplot(3, 1, 3)
plt.plot(np.arange(len(y)), y, label='y[n]', color='red', marker='o')
plt.title('Convolution Result y[n]')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid(True)
plt.legend()

# Show all plots
plt.tight_layout()
plt.show()
