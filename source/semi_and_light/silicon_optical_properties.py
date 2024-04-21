import matplotlib.pyplot as plt
import csv
import numpy as np


def plot_silicon_absorption():
    wavelength = []
    absorption_coefficient = []

    with open('silicon_optical_properties.csv', 'r') as f:
        reader = csv.reader(f)

        # skip header
        next(reader)

        for row in reader:
            wavelength.append(float(row[0]))
            absorption_coefficient.append(float(row[1]))

    fig, ax = plt.subplots(ncols=2, figsize=(8.5, 4.8))
    ax[0].semilogy(wavelength, absorption_coefficient)
    ax[0].set_xlabel('Wavelength [$nm$]')
    ax[0].set_ylabel('Absorption Coefficient $ \\alpha $ [$cm^{-1}$]')
    ax[0].grid(which='both', alpha=0.5)

    ax[1].semilogy(wavelength, 100/np.array(absorption_coefficient))
    ax[1].grid(which='both', alpha=0.5)
    ax[1].set_xlabel('Wavelength [$nm$]')
    ax[1].set_ylabel('Absorption Depth [$m$]')

    ax[1].yaxis.tick_right()
    ax[1].yaxis.set_label_position('right')

    plt.tight_layout(pad=0.4)
    plt.show()


def plot_refractive_index():
    wavelength = []
    n = []
    k = []

    with open('silicon_optical_properties.csv', 'r') as f:
        reader = csv.reader(f)

        # skip header
        next(reader)

        for row in reader:
            wavelength.append(float(row[0]))
            n.append(float(row[2]))
            k.append(float(row[3]))

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(wavelength, n, label='n - real part')
    ax.plot(wavelength, k, label='$ \\kappa$ - imaginary part')
    ax.set_xlabel('Wavelength [$nm$]')
    ax.set_ylabel('Complex Refractive Index')
    ax.grid(which='both', alpha=0.5)
    ax.set_ylim([0, None])
    ax.legend()

    plt.tight_layout(pad=0.4)
    plt.show()


def plot_reflectivity():
    wavelength = []
    n = []

    with open('silicon_optical_properties.csv', 'r') as f:
        reader = csv.reader(f)

        # skip header
        next(reader)

        for row in reader:
            wavelength.append(float(row[0]))
            n.append(float(row[2]))

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    n = np.array(n)
    reflectivity = np.abs((1-n)/(1+n))**2
    ax.plot(wavelength, reflectivity)
    ax.set_xlabel('Wavelength [$nm$]')
    ax.set_ylabel('Reflectivity')
    ax.grid(which='both', alpha=0.5)
    ax.set_ylim([0, None])

    plt.tight_layout(pad=0.4)
    plt.show()