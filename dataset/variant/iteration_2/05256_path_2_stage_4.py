import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Mei', 'Abr', 'Mar', 'Ene', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic', 'Feb'])  
springfield_temps = np.array([1, 3, 8, 12, 16, 20, 23, 22, 18, 13, 8, 3])
riverton_temps = np.array([0, 2, 6, 10, 15, 19, 22, 21, 16, 10, 5, 1])
laketown_temps = np.array([-2, 0, 5, 9, 14, 18, 21, 20, 15, 9, 4, -1])
greenhill_temps = np.array([2, 4, 9, 13, 17, 21, 24, 23, 19, 14, 9, 4])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, springfield_temps, marker='s', linestyle='-', color='b', label='Sprinkfield-researched', linewidth=2.5)
ax.plot(months, riverton_temps, marker='^', linestyle='--', color='g', label='Rivertown-detailed', linewidth=2.5)
ax.plot(months, laketown_temps, marker='d', linestyle=':', color='r', label='Laketune-assessed', linewidth=2.5)
ax.plot(months, greenhill_temps, marker='o', linestyle='-.', color='magenta', label='Greenslope-evaluated', linewidth=2.5)

ax.set_title('Annual Temperature Changes', fontsize=18, fontweight='bold')
ax.set_xlabel('Mes', fontsize=14)
ax.set_ylabel('Temperatura (°C)', fontsize=14)

ax.legend(title='Analyzed Places', fontsize=12, loc='lower left')

ax.grid(True, linestyle=':', which='both', color='lightgrey', alpha=0.5)

for spine in ax.spines.values():
    spine.set_visible(False)

for i in range(len(months)):
    ax.annotate(f"{springfield_temps[i]}°C", (months[i], springfield_temps[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8, color='b')
    ax.annotate(f"{riverton_temps[i]}°C", (months[i], riverton_temps[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8, color='g')
    ax.annotate(f"{laketown_temps[i]}°C", (months[i], laketown_temps[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8, color='r')
    ax.annotate(f"{greenhill_temps[i]}°C", (months[i], greenhill_temps[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8, color='magenta')

plt.tight_layout()

plt.show()