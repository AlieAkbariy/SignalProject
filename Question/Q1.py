import cmath

import matplotlib.pyplot as plt
import numpy as np

OMEGA = (2 * np.pi) / 21


def calculate_coefficient():
    coefficient_list = list()
    for k in range(22):
        temp = 0
        for n in range(22):
            t = -1j * k * n * OMEGA
            temp += (np.power(0.75, n) * cmath.exp(t))

        temp = temp / 21
        coefficient_list.append(temp)
    return coefficient_list


def calculate_fourier_series(coefficient_list):
    fourier_series = list()
    for n in range(22):
        temp = 0
        for k in range(22):
            t = 1j * k * n * OMEGA
            temp += coefficient_list[k] * cmath.exp(t)
        fourier_series.append(temp)
    return fourier_series


def calculate_phase_value(fourier_series):
    value_list = list()
    phase_list = list()
    for i in fourier_series:
        value_list.append(abs(i))
        phase_list.append(cmath.phase(i))
    return value_list, phase_list


if __name__ == '__main__':
    n = np.array(range(22))
    coefficient_list = calculate_coefficient()
    fourier_series = calculate_fourier_series(coefficient_list)
    value_list, phase_list = calculate_phase_value(fourier_series)
    value = np.array(value_list)
    phase = np.array(phase_list)

    plt.figure(figsize=(10, 10), dpi=100)
    plt.subplot(2, 1, 1)
    plt.title("Value")
    plt.stem(n, value)

    plt.subplot(2, 1, 2)
    plt.title("Phase")
    plt.stem(n, phase)
    plt.show()
