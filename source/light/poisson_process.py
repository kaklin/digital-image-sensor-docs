import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson
from scipy.special import factorial, gammainc


def plot_events():
    fig, ax = plt.subplots(figsize=(8.5, 1.8), gridspec_kw={'bottom': 0.32})
    l = 10
    events = 50

    time_stamps = [0]
    for i in range(events-1):
        time_stamps[-1]
        time_stamps.append(time_stamps[-1] + np.random.exponential(1/l))

    ax.vlines(time_stamps, ymin=0, ymax=1)
    ax.scatter(time_stamps, [1]*events)

    ax.set_xlabel('Time [$s$]')
    ax.set_ylim([0, 1.8])
    ax.set_xlim([0, 5])
    ax.set_yticks([])

    plt.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.1)
    plt.show()


def plot_poisson():
    x = np.arange(0,35,1)
    lambdas = np.array([1, 4, 10, 20])
    fig, ax = plt.subplots(figsize=(8.5, 4.8))

    for l in lambdas:
        ax.scatter(x, poisson.pmf(x, l), label=f'$\lambda={l}$')

    ax.grid()
    ax.legend()
    ax.set_xlabel('$k$')
    ax.set_ylabel('Probability')

    # plt.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.1)
    plt.tight_layout(pad=0.4)
    plt.show()


def plot_exponential():
    x = np.arange(0,2,0.02)
    lambdas = np.array([1, 4, 10, 20])
    fig, ax = plt.subplots(ncols=2, figsize=(8.5, 4.8))

    for l in lambdas:
        ax[0].plot(x, l*np.exp(-l * x), label=f'$\lambda={l}$')

    ax[0].grid()
    ax[0].legend()
    ax[0].set_xlabel('Inter-event time $t$')
    ax[0].set_ylabel('Probability Density')

    x = np.logspace(-3,1)
    for l in lambdas:
        ax[1].loglog(x, l*np.exp(-l * x), label=f'$\lambda={l}$')

    ax[1].grid(which='both', alpha=0.5)
    ax[1].legend()
    ax[1].set_ylim([1e-2, 1e2])
    ax[1].set_xlabel('Inter-event time $t$')

    # plt.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.1)
    plt.tight_layout(pad=0.4)
    plt.show()


def plot_truncated_poisson():
    lambdas = [1,4,10,20]
    limit = 7
    x = np.arange(0,limit+1,1)
    fig, ax = plt.subplots(figsize=(8.5, 4.8))

    for l in lambdas:
        pmf = np.exp(-l)*(l**x)/factorial(x)

        pmf[-1] = gammainc(limit, l)

        ax.scatter(x, pmf, label=f'$\lambda={l}$')

    ax.grid()
    ax.legend()
    ax.set_xlim([None, 15])
    ax.set_xlabel('$k$')
    ax.set_ylabel('Probability')

    # plt.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.1)
    plt.tight_layout(pad=0.4)
    plt.show()
