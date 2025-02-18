import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

batteries = [0.5, 2, 1, 5, 3, 12, 18, 20, 28, 35, 50]
pumped_storage = [6, 7, 5, 10, 12, 14, 13, 17, 19, 21, 22]
compressed_air = [0.3, 0.2, 0.6, 0.8, 1.3, 1.4, 1.8, 2.6, 2.8, 3.3, 4.2]
flywheels = [0.12, 0.11, 0.17, 0.15, 0.24, 0.28, 0.34, 0.33, 0.45, 0.47, 0.52]

storage_data = np.array([batteries, pumped_storage, compressed_air, flywheels])

# Alter the colors to change the appearance of different fill areas
colors = ['#FFD700', '#8A2BE2', '#00FF7F', '#FF6347']

fig, ax = plt.subplots(figsize=(12, 8))
# Use different alpha for slight variation in transparency
ax.stackplot(years, storage_data, colors=colors, alpha=0.9)

ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 90)
ax.set_xticks(years)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)} GWh'))

# Change grid lines from '--' to ':' and adjust alpha for contrast
ax.grid(axis='y', linestyle=':', alpha=0.5)

# Randomly change legend position
ax.legend(['Batteries', 'Pumped Storage', 'Compressed Air', 'Flywheels'], loc='upper left')

# Randomly alter the line width of chart border 
for spine in ax.spines.values():
    spine.set_linewidth(1.5)

plt.tight_layout()

plt.show()