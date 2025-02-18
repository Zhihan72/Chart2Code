import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = [3.5, 1.6, 5.1, 6.3, 9.8, 1.2, 2.0, 4.2, 7.4, 8.6, 2.8]
wind = [5.1, 10.2, 3.0, 7.0, 4.5, 6.3, 7.8, 2.5, 3.8, 9.0, 5.8]
hydro = [9.3, 8.2, 9.7, 8.1, 8.5, 8.9, 9.0, 8.7, 9.2, 8.4, 9.5]
geothermal = [1.0, 0.4, 0.8, 1.3, 1.5, 2.0, 1.6, 1.1, 1.8, 0.9, 0.6]

single_color = '#ff7f0e'
fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar, color=single_color, marker='o', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, wind, color=single_color, marker='s', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, hydro, color=single_color, marker='^', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, geothermal, color=single_color, marker='d', linestyle='-', linewidth=2, markersize=8)

# Removed title, axis labels, and annotation
ax.set_xticks(years)

plt.tight_layout()
plt.show()