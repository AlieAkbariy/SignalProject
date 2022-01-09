import matplotlib.pyplot as plt
import numpy as np

B = 6


def y(t):
    y_t = 0
    if 0 < t < B:
        y_t = 1 - np.exp(-t)
    elif t > B:
        y_t = np.exp(B - t) - np.exp(-t)
    return y_t


if __name__ == '__main__':
    t = np.linspace(-10, 10, 1000)
    y_list = list()
    for i in t:
        temp = y(i)
        y_list.append(temp)

    plt.figure(figsize=(10, 10), dpi=100)
    y_t = np.array(y_list)
    plt.title('y(t)')
    plt.plot(t, y_t)
    plt.show()
