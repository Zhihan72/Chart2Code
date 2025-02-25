import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)

city_A_temps = [16.2, 16.5, 17.0, 17.3, 17.7, 18.1, 18.4, 18.7, 19.1, 19.5, 19.8, 20.2, 20.5]
city_B_temps = [14.0, 14.4, 14.7, 15.1, 15.4, 15.8, 16.1, 16.4, 16.8, 17.1, 17.5, 17.8, 18.2]
city_C_temps = [10.5, 10.8, 11.2, 11.5, 11.9, 12.2, 12.6, 12.9, 13.3, 13.6, 14.0, 14.3, 14.7]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, city_A_temps, marker='o', linestyle='-', color='#1f77b4', linewidth=2)
ax.plot(years, city_B_temps, marker='s', linestyle='--', color='#ff7f0e', linewidth=2)
ax.plot(years, city_C_temps, marker='^', linestyle='-.', color='#2ca02c', linewidth=2)

ax.set_xticks(years)

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()