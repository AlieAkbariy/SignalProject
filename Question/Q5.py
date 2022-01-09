import matplotlib.pyplot as plt
import numpy as np


def a(k):
    a_k = 0.5
    if k > 0:
        a_k = np.sin((k * np.pi) / 2) / (k * np.pi)
    return a_k


if __name__ == '__main__':
    x_t = 0
    t = np.linspace(-10, 10, 1000)

    for k in range(11):
        a_k = a(k)
        x_t += a_k * np.cos(k * t * (np.pi / 4))
        plt.figure(figsize=(10, 10))
        plt.plot(t, x_t)
        plt.show()
