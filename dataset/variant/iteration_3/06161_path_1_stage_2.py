import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
asia_bandwidth = np.array([2, 5, 10, 15, 20, 35, 50, 70, 100, 150, 200, 270, 350, 450, 600, 750, 900, 1100, 1400, 1700, 2000])
europe_bandwidth = np.array([1, 3, 8, 12, 18, 28, 40, 55, 80, 110, 140, 190, 250, 320, 400, 480, 560, 660, 790, 850, 900])
north_america_bandwidth = np.array([1.5, 4, 7, 11, 17, 26, 37, 50, 68, 95, 125, 160, 200, 270, 340, 440, 520, 600, 720, 800, 880])
africa_bandwidth = np.array([0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30, 45, 70, 100, 150, 220, 300, 400, 550, 700, 900, 1200])

plt.figure(figsize=(14, 8))

plt.plot(years, asia_bandwidth, color='red', linewidth=2, marker='o', markersize=5)
plt.plot(years, europe_bandwidth, color='blue', linewidth=2, marker='s', markersize=5)
plt.plot(years, north_america_bandwidth, color='green', linewidth=2, marker='^', markersize=5)
plt.plot(years, africa_bandwidth, color='purple', linewidth=2, marker='d', markersize=5)

plt.title('Internet Usage Surge (2000 - 2020)', fontsize=16, fontweight='bold')
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Data Transfer (Gbps)', fontsize=12)

plt.xticks(np.arange(2000, 2021, 2), rotation=45)
plt.yticks(np.arange(0, 2201, 200))

plt.tight_layout()
plt.show()