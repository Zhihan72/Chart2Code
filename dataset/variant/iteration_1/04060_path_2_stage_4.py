import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Hydropower', 'Biomass', 'Geothermal', 'Solar', 'Wind']
usage_percentages = [20, 10, 15, 30, 25]

years = np.arange(2010, 2024)
solar_growth = [5, 7, 9, 10, 11, 13, 15, 16, 18, 20, 22, 23, 25, 26]
wind_growth = [4, 5, 6, 7, 9, 10, 11, 13, 14, 16, 17, 18, 20, 21]
hydro_growth = [3, 3, 3, 4, 5, 6, 7, 7, 7, 8, 8, 8, 9, 9]
geo_growth = [2, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 8]
bio_growth = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7]

consistent_color = '#32CD32'

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

ax1.pie(
    usage_percentages,
    labels=energy_sources,
    colors=[consistent_color] * len(energy_sources),
    autopct='%1.1f%%',
    startangle=140
)
ax1.axis('equal')

ax2.plot(years, solar_growth, marker='o', linestyle='-', linewidth=2, color=consistent_color)
ax2.plot(years, wind_growth, marker='s', linestyle='--', linewidth=2, color=consistent_color)
ax2.plot(years, hydro_growth, marker='^', linestyle='-.', linewidth=2, color=consistent_color)
ax2.plot(years, geo_growth, marker='d', linestyle=':', linewidth=2, color=consistent_color)
ax2.plot(years, bio_growth, marker='x', linestyle='-', linewidth=2, color=consistent_color)

ax2.set_xlabel("Growth Rate (%)", fontsize=14)
ax2.set_ylabel("Year", fontsize=14)
ax2.set_xticks(years)
ax2.set_xlim(2010, 2023)
ax2.set_ylim(0, 30)

plt.tight_layout()
plt.show()