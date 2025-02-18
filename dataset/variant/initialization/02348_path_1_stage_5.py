import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import uniform_filter1d

years = np.arange(2000, 2024)
north_america_speeds = [1, 0.5, 0.7, 1.5, 2, 3, 5, 4, 6, 7, 8, 10, 12, 15, 20, 18, 25, 30, 35, 32, 40, 43, 48, 45]
europe_speeds = [0.8, 0.4, 0.6, 1.2, 1.5, 3, 2.2, 4, 6.5, 5, 7.5, 9, 10, 13, 18, 15, 22, 28, 31, 25, 35, 38, 42, 40]
asia_speeds = [0.6, 0.3, 0.5, 0.9, 1.2, 2.5, 1.8, 3, 4, 5, 6, 9, 11, 17, 13, 21, 24, 27, 30, 34, 39, 37, 45, 42]
africa_speeds = [0.3, 0.1, 0.2, 0.5, 0.7, 1.2, 1, 1.5, 2, 4, 3, 5, 7, 11, 9, 13, 15, 21, 18, 24, 28, 30, 35, 32]
south_america_speeds = [0.4, 0.2, 0.3, 0.6, 1.2, 0.9, 1.5, 2, 4, 3, 5, 7, 9, 14, 11, 17, 20, 23, 27, 32, 35, 29, 41, 38]
mobile_speeds = [0.1, 0.15, 0.2, 0.45, 0.3, 0.6, 0.9, 1.2, 1.6, 2, 3, 6, 4.5, 10, 7, 12, 18, 14, 21, 28, 31, 25, 37, 34]

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))

single_color = '#1f77b4'

axs[0].plot(years, north_america_speeds, marker='o', color=single_color, linewidth=2)
axs[0].plot(years, europe_speeds, marker='s', color=single_color, linewidth=2)
axs[0].plot(years, asia_speeds, marker='^', color=single_color, linewidth=2)
axs[0].plot(years, africa_speeds, marker='D', color=single_color, linewidth=2)
axs[0].plot(years, south_america_speeds, marker='v', color=single_color, linewidth=2)

na_moving_avg = uniform_filter1d(north_america_speeds, size=3)
axs[0].plot(years, na_moving_avg, linestyle='--', color=single_color, linewidth=2)

axs[1].plot(years, mobile_speeds, marker='x', color=single_color, linewidth=2)

plt.tight_layout()
plt.show()