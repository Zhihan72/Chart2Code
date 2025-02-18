import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# Given growth data sets.
growth_data = [
    [22, 24, 23, 25, 27, 30, 28, 25, 27, 26, 29, 31, 28, 32, 29, 30, 31, 33, 30, 31, 35, 29, 34, 37, 36, 35, 33, 32, 36, 37, 38, 39],
    [18, 19, 22, 20, 21, 25, 24, 22, 23, 24, 20, 26, 27, 29, 22, 28, 30, 26, 28, 25, 27, 29, 31, 30, 32, 29, 31, 28, 30, 33, 29, 27],
    [10, 12, 11, 15, 18, 17, 16, 20, 22, 25, 27, 28, 26, 23, 22, 24, 26, 25, 23, 21, 25, 28, 29, 30, 31, 29, 32, 30, 31, 28, 26, 27],
    [9, 11, 13, 14, 16, 20, 17, 18, 20, 21, 24, 26, 27, 28, 29, 30, 28, 27, 26, 29, 32, 31, 33, 30, 29, 31, 32, 33, 30, 28, 29, 27],
    [8, 10, 12, 15, 18, 16, 13, 17, 19, 22, 20, 21, 23, 25, 24, 26, 28, 30, 27, 25, 29, 31, 34, 32, 28, 30, 29, 33, 31, 35, 33, 32],
    [7, 11, 14, 16, 19, 21, 23, 18, 20, 24, 27, 25, 22, 28, 29, 30, 32, 34, 33, 35, 37, 36, 31, 33, 38, 39, 34, 31, 30, 29, 32, 35],
    [25, 26, 24, 28, 29, 30, 27, 31, 34, 32, 30, 33, 36, 37, 35, 34, 38, 40, 39, 37, 35, 36, 31, 33, 32, 37, 39, 38, 36, 34, 32, 33],
    [27, 29, 30, 28, 31, 32, 33, 35, 37, 36, 35, 38, 39, 37, 36, 35, 34, 33, 32, 31, 30, 29, 34, 32, 35, 37, 38, 39, 36, 35, 33, 31],
]

# Create a figure and axis.
fig, ax = plt.subplots(figsize=(14, 10))

# Colors for each density plot.
colors = ['skyblue', 'palegreen', 'lightseagreen', 'lightcoral', 'plum', 
          'lavender', 'lightyellow', 'peachpuff']

# Create density plots for each data set.
for i, data in enumerate(growth_data):
    density = gaussian_kde(data)
    x_vals = np.linspace(min(data), max(data), 200)
    density.covariance_factor = lambda: .25
    density._compute_covariance()
    
    ax.fill_betweenx(x_vals, density(x_vals), alpha=0.5, color=colors[i], linewidth=1.5)

# Set axis labels.
ax.set_xlabel('Density')
ax.set_ylabel('Data Value Range')

# Grid styling.
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

# Show plot.
plt.show()