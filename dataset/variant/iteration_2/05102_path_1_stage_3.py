import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
hydropower = np.array([115, 127, 133, 130, 142, 150, 145, 155, 158, 160, 162])
solar = np.array([7, 9, 11, 20, 28, 34, 43, 62, 78, 95, 125])
wind = np.array([12, 17, 24, 28, 40, 49, 57, 77, 89, 105, 136])
fossil_fuels = np.array([305, 285, 275, 265, 255, 245, 230, 215, 205, 185, 168])
nuclear = 700 - (hydropower + solar + wind + fossil_fuels)

fig, ax1 = plt.subplots(figsize=(14, 8))

new_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
ax1.stackplot(years, hydropower, solar, wind, fossil_fuels, labels=['Hydro', 'Sun', 'Air', 'Carbon'], colors=new_colors, alpha=0.85)

ax1.set_xlabel('Timeline', fontsize=12)
ax1.set_ylabel('Output (TWh)', fontsize=12, color='k')
ax1.set_title('Power Generation Changes in Renewable Area\n(2010-2020)', fontsize=16, weight='bold')
ax1.grid(alpha=0.3)
ax1.legend(loc='upper left', title='Power Supplies', fontsize=10)

ax2 = ax1.twinx()
ax2.plot(years, nuclear, color='purple', marker='o', linestyle='--', linewidth=2.5, label='Atomic Power')
ax2.set_ylabel('Atomic Power (TWh)', fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')
ax2.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()