import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = np.array([10, 15, 25, 35, 50, 70, 100, 150, 210, 280, 350])
wind_energy = np.array([30, 35, 45, 60, 85, 120, 160, 210, 260, 320, 390])
hydro_energy = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300])

fig, ax = plt.subplots(figsize=(14, 8))

# Manually shuffled colors
ax.stackplot(years, solar_energy, wind_energy, hydro_energy,
             labels=['Solar', 'Wind', 'Hydro'],
             colors=['#4682B4', '#3CB371', '#FF6347'], alpha=0.8)

ax.set_title("Renewable Energy Production by Source (2010-2020)",
             fontsize=18, fontweight='medium', pad=15)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Energy Production (GWh)', fontsize=13)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 1000)

ax.set_xticks(years)
plt.xticks(rotation=30)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), title="Energy Source", fontsize=11)

ax.grid(True, linestyle='-', linewidth=0.5, alpha=0.3)

plt.tight_layout()

plt.show()