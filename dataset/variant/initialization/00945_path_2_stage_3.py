import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])

solar_contribution = np.array([90, 70, 130, 50, 110])
wind_contribution = np.array([85, 105, 40, 60, 95])
hydro_contribution = np.array([55, 60, 50, 65, 45])
biomass_contribution = np.array([35, 30, 45, 25, 40])

# Shuffled colors for the data groups
colors = ['#00A86B', '#8B4513', '#FDB813', '#1F78B4']

fig, ax = plt.subplots(figsize=(12, 7))

ax.bar(years, solar_contribution, color=colors[0], edgecolor='none', alpha=0.9)
ax.bar(years, wind_contribution, bottom=solar_contribution, color=colors[1], edgecolor='none', alpha=0.9)
ax.bar(years, hydro_contribution, bottom=solar_contribution + wind_contribution, color=colors[2], edgecolor='none', alpha=0.9)
ax.bar(years, biomass_contribution, bottom=solar_contribution + wind_contribution + hydro_contribution, color=colors[3], edgecolor='none', alpha=0.9)

ax.set_title("Economic Contribution of Renewable Energy\nin GreenVille (2018-2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Economic Contribution (Million USD)", fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()