import matplotlib.pyplot as plt
import numpy as np

countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E', 'Country F', 'Country G']
years = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

co2_reductions = np.array([
    [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0],
    [0.3, 0.32, 0.34, 0.37, 0.4, 0.42, 0.45, 0.48, 0.5, 0.52, 0.55],
    [0.2, 0.23, 0.25, 0.28, 0.3, 0.33, 0.35, 0.38, 0.4, 0.43, 0.45],
    [0.4, 0.42, 0.45, 0.47, 0.5, 0.53, 0.55, 0.58, 0.6, 0.63, 0.65],
    [0.1, 0.13, 0.15, 0.17, 0.2, 0.22, 0.25, 0.27, 0.3, 0.33, 0.35],
    [0.25, 0.28, 0.3, 0.33, 0.35, 0.37, 0.4, 0.42, 0.45, 0.48, 0.5],
    [0.6, 0.62, 0.65, 0.67, 0.7, 0.73, 0.75, 0.78, 0.8, 0.82, 0.85]
])

colors = ['#FF5733', '#FFC300', '#DAF7A6', '#581845', '#900C3F', '#3498DB', '#2ECC71']
markers = ['o', 's', 'D', '^', 'v', '>', '<']  # a variety of marker shapes
line_styles = ['-', '--', '-.', ':', '-', '--', '-.']  # different line styles

plt.figure(figsize=(14, 8))

for i, color in enumerate(colors):
    plt.plot(years, co2_reductions[i], marker=markers[i], color=color, linestyle=line_styles[i], label=countries[i])

plt.xticks(years)
plt.grid(axis='both', linestyle='-.', alpha=0.5)  # altered grid style

plt.legend(loc='upper left', frameon=True, shadow=True, borderpad=1.5)  # adding legend with a styled border

plt.tight_layout()

plt.show()