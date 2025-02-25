import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2060, 10)

solar_capacity = [33, 18, 500, 1000, 2000, 100]
wind_capacity = [85, 20, 700, 10, 1500, 300]
hydro_capacity = [880, 800, 750, 840, 960, 920]
biomass_capacity = [120, 160, 200, 25, 80, 50]

fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(years, solar_capacity, marker='o', linestyle='-', color='blue', linewidth=2)
ax.plot(years, wind_capacity, marker='s', linestyle='--', color='green', linewidth=2)
ax.plot(years, hydro_capacity, marker='^', linestyle='-.', color='brown', linewidth=2)
ax.plot(years, biomass_capacity, marker='d', linestyle=':', color='orange', linewidth=2)

# Randomly altering textual elements
ax.set_title('Forecast 2060: Renewables Capacity Upsurge', fontsize=16, fontweight='bold')
ax.set_xlabel('Timeline (Years)', fontsize=14)
ax.set_ylabel('Capacity (GW) Deployment', fontsize=14)
ax.set_xlim(2000, 2050)
ax.set_ylim(0, 2200)

plt.show()