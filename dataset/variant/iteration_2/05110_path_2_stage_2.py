import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2060, 10)

# Manually shuffled data to simulate randomness while maintaining dimensional structure
solar_capacity = [500, 1000, 2000, 100, 33, 18]
wind_capacity = [300, 1500, 10, 85, 700, 20]
hydro_capacity = [880, 800, 960, 840, 750, 920]
biomass_capacity = [120, 200, 160, 25, 80, 50]

milestones = [
    "Early Development Phase",
    "Commercial Viability Achieved",
    "Mainstream Adoption",
    "Rapid Scaling",
    "Technological Breakthroughs",
    "Future Growth"
]

fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(years, solar_capacity, marker='o', linestyle='-', color='purple', linewidth=2, label='Solar Power')
ax.plot(years, wind_capacity, marker='s', linestyle='--', color='cyan', linewidth=2, label='Wind Power')
ax.plot(years, hydro_capacity, marker='^', linestyle='-.', color='magenta', linewidth=2, label='Hydropower')
ax.plot(years, biomass_capacity, marker='d', linestyle=':', color='lime', linewidth=2, label='Biomass Power')

ax.set_title('The Evolution and Forecast of Renewable Energy Capacity (2000-2050)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Installed Capacity (GW)', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(title='Energy Source', loc='upper left', fontsize=12)

for i, milestone in enumerate(milestones):
    ax.annotate(
        milestone, 
        xy=(years[i], solar_capacity[i]), 
        xytext=(years[i], solar_capacity[i] + 250), 
        textcoords='data', 
        arrowprops=dict(facecolor='black', arrowstyle='->'), 
        fontsize=10, 
        ha='center'
    )

ax.set_xlim(2000, 2050)
ax.set_ylim(0, 2200)
plt.tight_layout()
plt.show()