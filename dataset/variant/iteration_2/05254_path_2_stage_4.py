import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar = np.array([2, 3, 4, 6, 8, 12, 15, 18, 22, 26, 30])
wind = np.array([5, 7, 10, 13, 16, 20, 25, 29, 35, 40, 45])
hydro = np.array([30, 31, 32, 33, 34, 34, 35, 36, 37, 37, 38])

# Compute the total energy without biomass and geothermal
total_energy = solar + wind + hydro
data = np.vstack([solar, wind, hydro])

fig, ax1 = plt.subplots(figsize=(14, 8))
ax1.stackplot(years, data, colors=['#FF6347', '#4682B4', '#9ACD32'], alpha=0.8)

ax1.plot(years, total_energy, color='black', marker='o', linestyle='--', linewidth=2)

ax1.set_title('Renewable Energy Growth\n(2010-2020)', fontsize=16, fontweight='bold', ha='center')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Prod. (TWh)', fontsize=14)

max_year = years[np.argmax(total_energy)]
max_value = np.max(total_energy)
ax1.annotate(f'Max: {max_value} TWh in {max_year}', xy=(max_year, max_value),
             xytext=(max_year-3, max_value-10),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center', color='black')

plt.tight_layout()
plt.show()