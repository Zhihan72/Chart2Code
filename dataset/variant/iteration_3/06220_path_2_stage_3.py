import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar = [1.2, 1.6, 2.0, 2.8, 3.5, 4.2, 5.1, 6.3, 7.4, 8.6, 9.8]
wind = [2.5, 3.0, 3.8, 4.5, 5.1, 5.8, 6.3, 7.0, 7.8, 9.0, 10.2]
hydro = [8.1, 8.2, 8.4, 8.5, 8.7, 8.9, 9.0, 9.2, 9.3, 9.5, 9.7]
geothermal = [0.4, 0.6, 0.8, 0.9, 1.0, 1.1, 1.3, 1.5, 1.6, 1.8, 2.0]
biomass = [0.3, 0.5, 0.7, 0.8, 1.0, 1.2, 1.4, 1.6, 1.9, 2.1, 2.3]

# New colors for each energy source
colors = ['#ff5733', '#33ff57', '#3357ff', '#ffa833', '#8333ff']

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar, color=colors[0], marker='o', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, wind, color=colors[1], marker='s', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, hydro, color=colors[2], marker='^', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, geothermal, color=colors[3], marker='d', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, biomass, color=colors[4], marker='*', linestyle='-', linewidth=2, markersize=8)

ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Energy Generation (GW)", fontsize=14)
ax.set_xticks(years)

plt.tight_layout()
plt.show()