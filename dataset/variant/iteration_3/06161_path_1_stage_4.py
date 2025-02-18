import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
# Randomly adjusted bandwidth values for demonstration
asia_bandwidth = np.array([5, 10, 15, 20, 2, 35, 50, 100, 70, 200, 150, 270, 450, 350, 600, 750, 900, 1400, 1700, 1100, 2000])
europe_bandwidth = np.array([3, 1, 8, 18, 12, 28, 55, 40, 140, 110, 80, 190, 320, 250, 400, 480, 560, 790, 850, 660, 900])
north_america_bandwidth = np.array([4, 1.5, 11, 17, 7, 26, 50, 37, 125, 68, 95, 160, 270, 200, 340, 600, 440, 720, 800, 520, 880])
africa_bandwidth = np.array([1, 0.5, 2, 5, 3, 7, 15, 10, 45, 20, 30, 70, 150, 100, 220, 300, 550, 700, 900, 1200, 400])

plt.figure(figsize=(14, 8))

plt.plot(years, asia_bandwidth, color='blue', linewidth=2, marker='o', markersize=5)
plt.plot(years, europe_bandwidth, color='blue', linewidth=2, marker='s', markersize=5)
plt.plot(years, north_america_bandwidth, color='blue', linewidth=2, marker='^', markersize=5)
plt.plot(years, africa_bandwidth, color='blue', linewidth=2, marker='d', markersize=5)

plt.title('Internet Usage Surge (2000 - 2020)', fontsize=16, fontweight='bold')
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Data Transfer (Gbps)', fontsize=12)

plt.xticks(np.arange(2000, 2021, 2), rotation=45)
plt.yticks(np.arange(0, 2201, 200))

plt.tight_layout()
plt.show()