import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2023)

traditional_energy = np.array([120, 114, 119, 110, 115, 107, 102, 99, 95, 92, 91, 88, 87, 82, 81, 75, 73, 72, 71, 68, 66, 64, 61])
solar_energy = np.array([0, 0, 0, 1, 0, 0, 0, 3, 5, 7, 8, 10, 16, 14, 22, 24, 29, 33, 38, 52, 54, 58, 66])
wind_energy = np.array([0, 1, 0, 0, 0, 1, 0, 1, 4, 6, 6, 9, 13, 19, 25, 31, 40, 45, 56, 62, 67, 68, 76])

plt.figure(figsize=(14, 8))

# Applying the same color 'blue' to all data groups
plt.plot(years, traditional_energy, color='blue', linestyle='-', linewidth=2)
plt.plot(years, solar_energy, color='blue', linestyle='--', linewidth=2)
plt.plot(years, wind_energy, color='blue', linestyle='-.', linewidth=2)

plt.scatter(years, traditional_energy, color='blue', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, solar_energy, color='blue', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, wind_energy, color='blue', s=50, edgecolors='black', alpha=0.7)

plt.xticks(np.arange(2000, 2023, 2), fontsize=10, rotation=45)
plt.yticks(fontsize=10)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

plt.show()