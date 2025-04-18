import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)

spring_temps = [12, 13, 12, 13, 14, 14, 15, 15, 16, 17, 17, 18, 18, 19, 20, 20, 21, 21, 22, 23, 23, 24, 24, 25, 25, 26, 27, 27, 28, 29, 29]
summer_temps = [24, 25, 24, 25, 26, 26, 27, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 36, 37, 37, 38, 38, 39, 40, 40, 41, 41, 42, 43, 43]
autumn_temps = [15, 16, 15, 16, 17, 17, 18, 19, 20, 21, 21, 22, 22, 23, 24, 24, 25, 25, 26, 27, 27, 28, 28, 29, 30, 30, 31, 31, 32, 33, 33]

fig, ax = plt.subplots(figsize=(12, 6))
fig.suptitle('Avg Temps in Verdad Valley\n1990-2020', fontsize=16, fontweight='bold', y=0.94)

# Shuffled color assignment
ax.stackplot(years, spring_temps, summer_temps, autumn_temps,
             labels=['Spr', 'Sum', 'Aut'],
             colors=['#4daf4a', '#e41a1c', '#377eb8'], alpha=0.8)  # Colors shuffled
ax.set_title('Seasonal Temp Trends', fontsize=14, pad=8)
ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Temp (°C)', fontsize=12)
ax.legend(loc='upper right', title='', fontsize=9)
ax.grid(True, linestyle='-', color='gray', linewidth=0.5)
ax.set_xticks(years[::3])
ax.set_xticklabels(years[::3], rotation=30, fontsize=10)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()