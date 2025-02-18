import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
asia_temp = [-0.2, 0.1, 0.3, 0.5, 0.4, 0.6, 0.7, 0.8, 0.9, 1.2, 1.3]
europe_temp = [-0.1, 0.0, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.0, 1.1, 1.2]
north_america_temp = [-0.3, -0.2, 0.1, 0.3, 0.2, 0.5, 0.6, 0.8, 0.9, 1.0, 1.1]
south_america_temp = [0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.3, 1.4]

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(years, asia_temp, marker='x', linestyle=':', linewidth=1.5)
ax.plot(years, europe_temp, marker='+', linestyle='-', linewidth=1.5)
ax.plot(years, north_america_temp, marker='2', linestyle='--', linewidth=1.5)
ax.plot(years, south_america_temp, marker='3', linestyle='-', linewidth=1.5)

ax.grid(visible=False, which='both')

plt.tight_layout()
plt.show()