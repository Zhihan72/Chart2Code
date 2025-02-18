import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy_change = np.array([6, 8, 5, -5, 20, 11, -7, 15, -10, 75, -26])
wind_energy_change = np.array([12, -15, 20, -10, 25, 52, 40, -33, -65, 100, 10])
hydropower_energy_change = np.array([-42, 41, -35, 36, 32, -38, 40, -39, 44, 30, -37])

fig, ax = plt.subplots(figsize=(12, 8))

combined_color = 'cornflowerblue'

ax.barh(years, solar_energy_change, color=combined_color, edgecolor='black', align='center', label='Solar Energy')
ax.barh(years, wind_energy_change, color=combined_color, edgecolor='black', align='center', left=solar_energy_change, label='Wind Energy')
ax.barh(years, hydropower_energy_change, color=combined_color, edgecolor='black', align='center', 
        left=solar_energy_change + wind_energy_change, label='Hydropower Energy')

ax.axvline(0, color='black', linewidth=0.8)

ax.set_yticks(years)
ax.set_xticks(np.arange(-150, 151, 25))
ax.legend()

plt.tight_layout()
plt.show()