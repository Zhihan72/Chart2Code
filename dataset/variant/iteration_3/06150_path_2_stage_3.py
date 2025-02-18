import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2024)
bandwidth = [5, 8, 12, 18, 28, 40, 55, 70, 85, 100, 120, 150, 170, 200]
latency = [200, 190, 170, 150, 125, 100, 85, 70, 60, 50, 45, 40, 35, 30]

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, bandwidth, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, latency, color='green', marker='s', linestyle='--', linewidth=2, markersize=8)

ax.set_xticks(years)
ax.set_xlim(2009, 2023)
ax.set_ylim(0, 220)

plt.tight_layout()
plt.show()