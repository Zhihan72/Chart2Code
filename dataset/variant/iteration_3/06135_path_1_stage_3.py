import matplotlib.pyplot as plt
import numpy as np

sunlight = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
succulent_growth = np.array([5, 10, 8, 14, 3, 16, 17.5, 12, 18, 2])
fern_growth = np.array([4, 3, 7, 1, 2, 6.5, 5.5, 8.5, 8, 7.5])
pothos_growth = np.array([23, 4, 11, 16, 20, 27, 7, 1, 2, 25])
cactus_growth = np.array([12, 8, 11.5, 6, 7, 4, 8, 12.5, 2, 10])

sizes = np.array([50, 90, 110, 70, 130, 230, 150, 170, 190, 210])

plt.figure(figsize=(14, 8))

plt.scatter(sunlight, succulent_growth, s=sizes, c='green', alpha=0.6, edgecolor='k')
plt.scatter(sunlight, fern_growth, s=sizes, c='orange', alpha=0.6, edgecolor='k')
plt.scatter(sunlight, pothos_growth, s=sizes, c='blue', alpha=0.6, edgecolor='k')
plt.scatter(sunlight, cactus_growth, s=sizes, c='red', alpha=0.6, edgecolor='k')

plt.title('Sunlight vs. Growth', fontsize=16, fontweight='bold')
plt.xlabel('Sunlight (hrs/day)', fontsize=12)
plt.ylabel('Growth (cm)', fontsize=12)

plt.tight_layout()

plt.show()