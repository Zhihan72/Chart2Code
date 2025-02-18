import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)
solar_growth = [2, 5, 1, 7, 10, 14, 25, 8, 30, 35, 40, 3, 56, 48, 52, 19, 60, 45, 70, 65, 80]
wind_growth = [5, 3, 8, 11, 15, 20, 30, 25, 36, 42, 49, 2, 61, 68, 75, 90, 82, 55, 97, 104, 110]
hydro_growth = [6, 7, 10, 8, 12, 5, 22, 15, 18, 30, 40, 26, 50, 45, 55, 35, 60, 70, 65, 75, 80]

plt.figure(figsize=(14, 8))

plt.plot(years, solar_growth, color='#00FF00', marker='o', linewidth=2, linestyle='-')
plt.plot(years, wind_growth, color='#FFA500', marker='^', linewidth=2, linestyle='--')
plt.plot(years, hydro_growth, color='#1E90FF', marker='s', linewidth=2, linestyle='-.')

plt.title('Renewable Sources Expansion (2010-2030)', fontsize=16, fontweight='bold')
plt.xlabel('Timeline', fontsize=14)
plt.ylabel('Yearly Increase (%)', fontsize=14)

plt.annotate('Big Jump\nin Solar', xy=(2015, 10), xytext=(2012, 15),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Gradual Rise\nin Wind Power', xy=(2020, 36), xytext=(2016, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Stable Growth\nin Hydro', xy=(2025, 65), xytext=(2020, 80),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(0, 121, 10))

plt.tight_layout()
plt.show()