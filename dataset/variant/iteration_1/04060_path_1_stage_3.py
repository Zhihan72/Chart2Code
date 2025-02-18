import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass']
usage_percentages = [30, 25, 20, 15, 10]
years = np.arange(2010, 2024)
solar_growth = [5, 7, 9, 10, 11, 13, 15, 16, 18, 20, 22, 23, 25, 26]
wind_growth = [4, 5, 6, 7, 9, 10, 11, 13, 14, 16, 17, 18, 20, 21]
hydro_growth = [3, 3, 3, 4, 5, 6, 7, 7, 7, 8, 8, 8, 9, 9]
geo_growth = [2, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 8]
bio_growth = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7]

colors = ['#32CD32', '#FF8C00', '#87CEEB', '#8B4513', '#FFD700']

# Changing from a 1 row, 2 column structure to a 2 row, 1 column structure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

ax1.pie(
    usage_percentages,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140
)
ax1.axis('equal')

ax2.plot(years, solar_growth, marker='o', linestyle='-', linewidth=2, color='#32CD32')
ax2.plot(years, wind_growth, marker='s', linestyle='--', linewidth=2, color='#FF8C00')
ax2.plot(years, hydro_growth, marker='^', linestyle='-.', linewidth=2, color='#87CEEB')
ax2.plot(years, geo_growth, marker='d', linestyle=':', linewidth=2, color='#8B4513')
ax2.plot(years, bio_growth, marker='x', linestyle='-', linewidth=2, color='#FFD700')
ax2.set_xlabel("Year", fontsize=14)
ax2.set_ylabel("Growth Rate (%)", fontsize=14)
ax2.set_xticks(years)
ax2.set_xlim(2010, 2023)
ax2.set_ylim(0, 30)

plt.tight_layout()
plt.show()