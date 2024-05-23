import matplotlib.pyplot as plt
import numpy as np


def wi(x):
    return 1+(x-1)/4


def func(x1, x2):
    term1 = np.sin(np.pi * wi(x1)) ** 2
    + (wi(x1) - 1) ** 2 * (1 + 10 * np.sin(np.pi * wi(x1) + 1) ** 2)
    term2 = (wi(x2) - 1) ** 2 * (1 + np.sin(2 * np.pi * wi(x2)) ** 2)
    return term1 + term2


def main():
    fig = plt.figure(figsize=(8, 8))
    x1 = np.linspace(-5, 5, 100)
    x2 = np.linspace(-5, 5, 100)
    ax1 = fig.add_subplot(221, projection='3d')
    x, y = np.meshgrid(x1, x2)
    z = func(x, y)
    ax1.plot_surface(x, y, z, cmap='Spectral')
    ax1.set_xlabel('x1')
    ax1.set_ylabel('x2')
    ax1.set_zlabel('y=f(x1, x2)')
    ax2 = fig.add_subplot(222, projection='3d')
    ax2.plot_surface(x, y, z, cmap='Spectral')
    ax2.view_init(elev=90, azim=0)
    ax2.set_xlabel('x1')
    ax2.set_ylabel('x2')
    ax2.set_zlabel('y=f(x1, x2)')
    ax2.axes.zaxis.set_ticklabels([])
    ax3 = fig.add_subplot(223)
    x = np.linspace(-5, 5, 100)
    y = func(x, 1)
    ax3.plot(x, y, color='wheat')
    ax3.set_xlabel('x1')
    ax3.set_ylabel('y=f(x1, 1)')
    ax4 = fig.add_subplot(224)
    x = np.linspace(-5, 5, 100)
    y = func(1, x)
    ax4.plot(x, y, color='peru')
    ax4.set_xlabel('x2')
    ax4.set_ylabel('y=f(1, x2)', labelpad=-265)
    func_1_1 = func(1, 1)
    plt.text(-6, -19,
             f'Координаты тестовой точки: (1; 1)\nf(1, 1) = {func_1_1}')
    plt.show()


main()
