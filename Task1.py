import matplotlib.pyplot as plt
import numpy as np


def func(x):
    """
    f(x)=−|sin(x)cos(A)exp(|1−√(x^2+ A^2)/π|)
    """
    A = 9.66459
    f = -abs(np.sin(x) * np.cos(x)
             * np.exp(abs(1 - np.sqrt(x**2 + A**2) / np.pi)))

    return f


if __name__ == "__main__":
    xmin = -10.0
    xmax = 10.0
    count = 500

    xdata = np.linspace(xmin, xmax, count)
    ydata1 = [func(x) for x in xdata]

    plt.plot(xdata, ydata1, "-k", label="f(x)")
    plt.legend()

    plt.grid()
    plt.show()
