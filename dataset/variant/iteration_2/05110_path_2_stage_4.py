import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2060, 10)

solar_capacity = [500, 1000, 2000, 100, 33, 18]
wind_capacity = [300, 1500, 10, 85, 700, 20]
hydro_capacity = [880, 800, 960, 840, 750, 920]
biomass_capacity = [120, 200, 160, 25, 80, 50]

milestones = [
    "Dev Phase",
    "Viability",
    "Adoption",
    "Scaling",
    "Breakthroughs",
    "Growth"
]

fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(years, solar_capacity, marker='x', linestyle='-', color='green', linewidth=2, label='Solar')
ax.plot(years, wind_capacity, marker='d', linestyle='-', color='orange', linewidth=2, label='Wind')
ax.plot(years, hydro_capacity, marker='v', linestyle='-', color='blue', linewidth=2, label='Hydro')
ax.plot(years, biomass_capacity, marker='p', linestyle='-', color='red', linewidth=2, label='Biomass')

ax.set_title('Renewable Energy Capacity (2000-2050)', fontsize=14, fontweight='normal')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Capacity (GW)', fontsize=12)
ax.grid(False)
ax.legend(title='Energy Sources', loc='lower right', fontsize=10)

for i, milestone in enumerate(milestones):
    ax.annotate(
        milestone, 
        xy=(years[i], solar_capacity[i]), 
        xytext=(years[i], solar_capacity[i] + 250), 
        textcoords='data', 
        arrowprops=dict(facecolor='gray', arrowstyle='->'), 
        fontsize=9, 
        ha='right'
    )

ax.set_xlim(2000, 2050)
ax.set_ylim(0, 2200)
plt.tight_layout()
plt.show()