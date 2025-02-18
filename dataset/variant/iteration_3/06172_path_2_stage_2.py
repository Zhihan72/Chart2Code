import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2023)

traditional_energy = np.array([120, 118, 115, 113, 110, 107, 104, 100, 97, 94, 91, 88, 85, 83, 80, 78, 76, 74, 72, 70, 67, 65, 60])
solar_energy = np.array([0, 0, 0, 0, 0, 0, 0, 2, 4, 6, 8, 10, 12, 16, 20, 25, 30, 35, 40, 50, 55, 60, 65])
wind_energy = np.array([0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 10, 13, 18, 23, 30, 38, 47, 55, 60, 65, 70, 75])

plt.figure(figsize=(14, 8))

plt.plot(years, traditional_energy, color='brown', linestyle='-', linewidth=2)
plt.plot(years, solar_energy, color='orange', linestyle='--', linewidth=2)
plt.plot(years, wind_energy, color='cyan', linestyle='-.', linewidth=2)

plt.scatter(years, traditional_energy, color='brown', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, solar_energy, color='orange', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, wind_energy, color='cyan', s=50, edgecolors='black', alpha=0.7)

plt.xticks(np.arange(2000, 2023, 2), fontsize=10, rotation=45)
plt.yticks(fontsize=10)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

plt.show()