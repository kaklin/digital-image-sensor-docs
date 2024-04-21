import matplotlib.pyplot as plt
import csv


def plot_sunlight():
    wavelength = []
    spectral_irradiance = []

    with open('ASTM_G-173-03_AM1.5G.csv', 'r') as f:
        reader = csv.reader(f)

        # skip header
        next(reader)

        for row in reader:
            wavelength.append(float(row[0]))
            spectral_irradiance.append(float(row[1]))
            # print(float(row[0]), float(row[1]))

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(wavelength, spectral_irradiance)

    ax.set_xlabel('Wavelength [$nm$]')
    ax.set_ylabel('Spectral Irradiance [$Wm^{-2}nm^{-1}$]')
    ax.set_ylim([0, None])

    plt.tight_layout(pad=0.4)
    plt.show()
