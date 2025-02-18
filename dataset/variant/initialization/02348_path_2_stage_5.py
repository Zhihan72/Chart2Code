import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import uniform_filter1d

years = np.arange(2000, 2024)
north_america_speeds = [0.7, 0.5, 1, 3, 2, 4, 5, 7, 6, 8, 10, 12, 15, 18, 20, 25, 30, 32, 35, 40, 43, 45, 48, 1.5]
europe_speeds = [0.6, 0.4, 0.8, 3, 1.5, 2.2, 4, 5, 6.5, 7.5, 9, 13, 10, 15, 18, 22, 25, 28, 31, 35, 38, 40, 42, 1.2]
asia_speeds = [0.5, 0.3, 0.6, 9, 1.2, 1.8, 3, 4, 6, 5, 9, 11, 13, 17, 21, 24, 27, 30, 34, 37, 39, 42, 45, 0.9]
africa_speeds = [0.2, 0.1, 0.3, 1, 0.7, 1.2, 1.5, 4, 3, 2, 5, 7, 9, 11, 13, 15, 18, 21, 24, 28, 30, 32, 35, 0.5]
south_america_speeds = [0.3, 0.2, 0.4, 1.2, 0.9, 1.5, 2, 5, 4, 3, 7, 9, 11, 14, 17, 23, 20, 27, 29, 32, 35, 38, 41, 0.6]

fig, ax = plt.subplots(figsize=(14, 10))

colors = ['#ff7f0e', '#9467bd', '#d62728', '#8c564b', '#1f77b4', '#2ca02c']

# Randomly altering the labels
ax.plot(years, north_america_speeds, marker='o', color=colors[4], linewidth=2, label='N.A.')
ax.plot(years, europe_speeds, marker='s', color=colors[0], linewidth=2, label='Europe')
ax.plot(years, asia_speeds, marker='^', color=colors[5], linewidth=2, label='Asian Area')
ax.plot(years, africa_speeds, marker='D', color=colors[2], linewidth=2, label='Africa Region')
ax.plot(years, south_america_speeds, marker='v', color=colors[3], linewidth=2, label='S.America')

na_moving_avg = uniform_filter1d(north_america_speeds, size=3)
ax.plot(years, na_moving_avg, linestyle='--', color=colors[1], linewidth=2, label='N.A. Trend')

ax.annotate('Pandemic Impact', xy=(2020, 35), xytext=(2012, 43),
            arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=10, fontstyle='italic')

# Randomly altering the title and axis labels
ax.set_title('Internet Speed Trends: 2000-2023', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Timeline', fontsize=12)
ax.set_ylabel('Speed in Mbps', fontsize=12)

ax.legend()
plt.tight_layout()
plt.show()