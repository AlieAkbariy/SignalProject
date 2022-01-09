import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------
# x(t) = sin(πt)/πt

plt.figure(figsize=(10, 10), dpi=100)
t = np.linspace(-10, 10, 1000)  # build point for t
x = []
for i in t:  # build x(t)
    temp = (np.sin(np.pi * i)) / (np.pi * i)
    x.append(temp)

x_t = np.array(x)
plt.subplot(3, 1, 1)
plt.title('x(t)')
plt.plot(t, x_t)

# ------------------------------------------------------------------------------
# x(t) = sin(πt + 2)/(πt+2)

x = []
for i in t:  # build x(t + 2)
    temp = (np.sin(np.pi * i + 2)) / (np.pi * i + 2)
    x.append(temp)

x_t = np.array(x)
plt.subplot(3, 1, 2)
plt.title('x(t+2)')
plt.plot(t, x_t)

# ------------------------------------------------------------------------------
# x(t) = sin(5πt + 2)/(5πt+2)

x = []
for i in t:  # build x(5t+2)
    temp = (np.sin(5 * np.pi * i + 2)) / (5 * np.pi * i + 2)
    x.append(temp)

x_t = np.array(x)

plt.subplot(3, 1, 3)
plt.title('x(5t+2)')
plt.plot(t, x_t)

plt.show()
