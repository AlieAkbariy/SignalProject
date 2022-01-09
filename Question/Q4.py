import matplotlib.pyplot as plt
import numpy as np

# Calculate H(JW) for Question number 4 part 1
W = np.linspace(-10, 10, 1000)
h_jw = 4 / (4 + W ** 2)

# Calculate X_total(t) = X_s(t) + X_n(t) for Question number 4 part 2
T = np.linspace(-10, 10, 1000)
x_s = np.cos(0.1 * T)
x_n = 0.03 * np.cos(10 * T)
x_total = x_s + x_n

# Calculate y_t for Question number 4 part 3
y_t = (4 * np.cos(0.1 * T)) / 4.01

plt.figure(figsize=(10, 15), dpi=100)
plt.subplot(4, 1, 1)
plt.title('H(JW)')
plt.plot(W, h_jw)

plt.subplot(4, 1, 2)
plt.title('X_Total(t)')
plt.plot(T, x_total)

plt.subplot(4, 1, 3)
plt.title('Y(t)')
plt.plot(T, y_t)

plt.subplot(4, 1, 4)
plt.title('X_Total(t)')
plt.plot(T, x_total, color='r', label='X_total(t)')
plt.plot(T, y_t, color='g', label='Y(t)')
plt.legend()
plt.show()
