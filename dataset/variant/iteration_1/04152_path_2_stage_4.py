import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

march_extent = [15.64, 15.61, 15.48, 15.36, 15.25, 14.94, 14.80, 14.71, 14.65, 14.55, 14.35, 14.26, 14.16, 14.10, 14.04, 13.91, 13.83, 13.80, 13.66, 13.54, 13.41]
june_extent = [11.34, 11.29, 11.23, 11.08, 10.94, 10.74, 10.51, 10.33, 10.14, 10.05, 9.91, 9.75, 9.59, 9.41, 9.28, 9.13, 9.00, 8.89, 8.75, 8.65, 8.53]
# september_extent = [6.41, 6.37, 6.30, 6.14, 5.97, 5.75, 5.55, 5.36, 5.20, 5.10, 4.92, 4.76, 4.63, 4.50, 4.38, 4.24, 4.12, 4.00, 3.88, 3.76, 3.67]
december_extent = [13.54, 13.52, 13.49, 13.42, 13.30, 13.11, 12.93, 12.82, 12.63, 12.48, 12.30, 12.13, 11.96, 11.81, 11.67, 11.52, 11.38, 11.27, 11.15, 11.03, 10.91]

fig, ax = plt.subplots(figsize=(14, 8))

new_colors = ['#ff5733', '#33ff57', '#ff33a1']
extents = [march_extent, june_extent, december_extent]
markers = ['x', '*', 's'] 
linestyles = ['-', '--', ':'] 

for extent, color, marker, linestyle in zip(extents, new_colors, markers, linestyles):
    ax.plot(years, extent, color=color, marker=marker, linestyle=linestyle, linewidth=1.5)

ax.grid(True, linestyle=':', which='major', color='grey', alpha=0.7)

plt.tight_layout()

plt.show()