import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
usa_missions = np.array([37, 30, 15, 27, 33, 22, 21, 16, 35, 18, 32])
russia_missions = np.array([25, 30, 22, 23, 20, 24, 24, 22, 28, 27, 25])
china_missions = np.array([5, 10, 20, 8, 12, 28, 18, 6, 15, 23, 25])

total_missions = usa_missions + russia_missions + china_missions

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, usa_missions, marker='o', linestyle='-', color='orange', linewidth=2, markersize=8)
ax1.plot(years, russia_missions, marker='d', linestyle='--', color='magenta', linewidth=2, markersize=8)
ax1.plot(years, china_missions, marker='s', linestyle='-.', color='cyan', linewidth=2, markersize=8)

ax2 = ax1.twinx()
ax2.plot(years, total_missions, color='gray', linestyle='-', marker='v', linewidth=3, markersize=10, alpha=0.6)

ax1.set_xticks(years)

plt.tight_layout()

plt.show()