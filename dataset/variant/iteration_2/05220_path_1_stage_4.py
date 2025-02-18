import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Manually shuffled energy data to preserve structure while altering content
solar_energy = np.array([25, 35, 15, 210, 280, 100, 50, 70, 150, 10, 350])
wind_energy = np.array([60, 120, 210, 30, 320, 160, 45, 260, 35, 85, 390])
hydro_energy = np.array([250, 200, 290, 270, 230, 280, 220, 240, 260, 210, 300])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, solar_energy, wind_energy, hydro_energy,
             labels=['Sunshine', 'Gust', 'Water Flow'],
             colors=['#4682B4', '#3CB371', '#FF6347'], alpha=0.8)

ax.set_title("Power Generation Modes (2010-2020)",
             fontsize=18, fontweight='medium', pad=15)
ax.set_xlabel('Timeline', fontsize=13)
ax.set_ylabel('Output (GWh)', fontsize=13)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 1000)

ax.set_xticks(years)
plt.xticks(rotation=30)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), title="Type of Source", fontsize=11)

ax.grid(True, linestyle='-', linewidth=0.5, alpha=0.3)

plt.tight_layout()

plt.show()