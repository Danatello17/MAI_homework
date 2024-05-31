import wget
import matplotlib.pyplot as plt
import os
import scipy.constants as constants
import scipy.special as special
import numpy as np
import csv
import shutil

VARIANT = 8


class Calculate_EDA:
    def __init__(self, diameter, frequency):
        self.radius = diameter / 2
        self.wave_length = 0
        self.k = 0
        self.update(frequency)

    def update(self, frequency):
        self.wave_length = np.longdouble(constants.speed_of_light / frequency)
        self.k = np.longdouble(2 * constants.pi / self.wave_length)

    def a_n(self, n):
        numerator = np.longdouble(special.spherical_jn(n, self.k * self.radius))
        divider = self.h_n(n, self.k * self.radius)
        return np.divide(numerator, divider)

    def b_n(self, n):
        numerator = self.k * self.radius * np.longdouble(special.spherical_jn(n - 1, self.k * self.radius)) - n * np.longdouble(special.spherical_jn(n, self.k * self.radius))
        divider = self.k * self.radius * self.h_n(n - 1, self.k * self.radius) - n * self.h_n(n, self.k * self.radius)
        return np.divide(numerator, divider)

    def h_n(self, n, arg):
        return np.clongdouble(special.spherical_jn(n, arg) + 1j * special.spherical_yn(n, arg))

    def result(self):
        coef = self.wave_length**2 / constants.pi
        series_sum = 0
        for n in range(1, 51):
            series_sum += (-1) ** n * (n + 0.5) * (self.b_n(n) - self.a_n(n))
        result = coef * np.abs(series_sum)**2
        return result


def exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True


def init_params():
    if not(exists('task_rcs_01.txt')):
        wget.download('https://jenyay.net/uploads/Student/Modelling/task_rcs_01.txt')
        print()

    D = 0
    fmin = 0
    fmax = 0

    with open("task_rcs_01.txt", "r") as file:
        file_data = file.read()
        lines = file_data.splitlines()
        line = lines[VARIANT - 1]
        file.close()
    line = line.replace(";", '')
    line = line.replace("D", '')
    line = line.replace("fmax", '')
    line = line.replace("fmin", '')
    line = line.replace("=", '')
    f = line.split(' ')
    D = float(f[1])
    fmin = float(f[2])
    fmax = float(f[3])


    return(D, fmin, fmax)


def main():
    D, fmin, fmax = init_params()
    freq = np.linspace(fmin, fmax, 100)
    eda = np.zeros_like(freq)
    wave_length = np.zeros_like(freq)
    calc = Calculate_EDA(D, 1)
    for i, frequ in enumerate(freq):
        calc.update(frequ)
        eda[i] = calc.result()
        wave_length[i] = calc.wave_length

    fig, ax = plt.subplots()
    ax.plot(freq, eda)
    plt.ylabel("ЭПР, м^2")
    plt.xlabel("Частота, Гц")
    plt.show()

    with open('result4.csv', 'w', newline='') as csvfile:
        c = csv.writer(csvfile, delimiter=',',
                       quotechar='|', quoting=csv.QUOTE_MINIMAL)
        c.writerow(['freq', 'length', 'eda'])
        for i in range(len(freq)):
            c.writerow([freq[i], wave_length[i], eda[i]])
    source_path = "result4.csv"
    destination_path = "result"
    if not(os.path.exists("result/result4.csv")):
        shutil.move(source_path, destination_path)

main()
