import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Manually shuffled values
asia_bandwidth = np.array([2, 10, 5, 15, 35, 20, 50, 100, 70, 150, 270, 200, 350, 450, 600, 900, 750, 1100, 1400, 1700, 2000])
europe_bandwidth = np.array([1, 8, 3, 18, 28, 12, 40, 80, 55, 110, 190, 140, 250, 400, 320, 480, 560, 790, 660, 850, 900])
north_america_bandwidth = np.array([1.5, 7, 4, 17, 26, 11, 37, 68, 50, 95, 160, 125, 200, 440, 270, 340, 520, 600, 720, 800, 880])
africa_bandwidth = np.array([0.5, 2, 1, 5, 3, 7, 10, 20, 15, 45, 30, 70, 100, 220, 150, 300, 550, 400, 700, 900, 1200])

plt.figure(figsize=(14, 8))

plt.plot(years, asia_bandwidth, color='green', linewidth=1, marker='X', markersize=6)
plt.plot(years, europe_bandwidth, color='orange', linewidth=3, marker='P', markersize=8)
plt.plot(years, north_america_bandwidth, color='brown', linewidth=2, marker='v', markersize=5)
plt.plot(years, africa_bandwidth, color='blue', linewidth=2, linestyle='-.', marker='*', markersize=7)

plt.grid(True, linestyle=':', linewidth=1, alpha=0.5)
plt.xticks(np.arange(2000, 2021, 4), rotation=30)
plt.yticks(np.arange(0, 2201, 300))

plt.tight_layout()

plt.show()