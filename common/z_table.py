# Import all libraries for this portion of the blog post
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def print_normal_distribution():
    # print standard normal distribution

    x = np.linspace(-4, 4, num=100)
    constant = 1.0 / np.sqrt(2*np.pi)
    pdf_normal_distribution = constant * np.exp((-x**2) / 2.0)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, pdf_normal_distribution)
    ax.set_ylim(0)
    ax.set_title('Normal Distribution', size=20)
    ax.set_ylabel('Probability Density', size=20)
    plt.show()


def normal_p_density(x):
    c = 1.0 / np.sqrt(2*np.pi)
    return c * np.exp((-x**2) / 2.0)


def calculate_p_from_z(z):
    p1, _ = quad(normal_p_density, np.NINF, -z)
    p2, _ = quad(normal_p_density, z, np.Inf)
    return p1 + p2


if __name__ == "__main__":
    print_normal_distribution()

    # calculate cumulative distribution
    print(calculate_p_from_z(3))

