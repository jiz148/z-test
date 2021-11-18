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
    ax.set_title('Standardized Normal Distribution', size=20)
    ax.set_ylabel('Probability Density', size=20)
    plt.show()


def normal_p_density(x):
    c = 1.0 / np.sqrt(2*np.pi)
    return c * np.exp((-x**2) / 2.0)


def calculate_p_from_z(z):
    """
    two tails
    """
    p1, _ = quad(normal_p_density, np.NINF, -z)
    p2, _ = quad(normal_p_density, z, np.Inf)
    return p1 + p2


def get_z_table():
    std_normal_table = pd.DataFrame(data=[],
                                    index=np.round(np.arange(0, 3.5, .1), 2),
                                    columns=np.round(np.arange(0.00, .1, 0.01), 2)
                                    )
    for i in std_normal_table.index:
        for c in std_normal_table.columns:
            z = np.round(i + c, 2)
            value, _ = quad(normal_p_density, np.NINF, z)
            std_normal_table.loc[i, c] = value

    std_normal_table.index = std_normal_table.index.astype(str)
    std_normal_table.columns = [str(column).ljust(4, '0') for column in std_normal_table.columns]
    return std_normal_table


if __name__ == "__main__":
    # print z distribution
    # print_normal_distribution()

    # calculate cumulative distribution
    # print(calculate_p_from_z(3), '\n')

    # print z-table for approximating  p-value by hand
    print(get_z_table().to_markdown())
