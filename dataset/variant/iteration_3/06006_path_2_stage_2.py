import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)
solar_growth = [1, 2, 3, 5, 7, 10, 14, 19, 25, 30, 35, 40, 45, 48, 52, 56, 60, 65, 70, 75, 80]
wind_growth = [2, 3, 5, 8, 11, 15, 20, 25, 30, 36, 42, 49, 55, 61, 68, 75, 82, 90, 97, 104, 110]

plt.figure(figsize=(14, 8))

plt.plot(years, solar_growth, color='#FFA500', marker='o', linewidth=2, linestyle='-')
plt.plot(years, wind_growth, color='#1E90FF', marker='^', linewidth=2, linestyle='--')

plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(0, 121, 10))

plt.tight_layout()
plt.show()