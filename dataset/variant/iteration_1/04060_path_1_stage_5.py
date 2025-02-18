import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2024)
solar_growth = [5, 8, 9, 9, 10, 12, 13, 17, 19, 21, 23, 24, 25, 27]
wind_growth = [3, 6, 7, 6, 8, 9, 12, 12, 15, 17, 18, 17, 21, 22]
hydro_growth = [4, 5, 4, 3, 6, 5, 6, 8, 6, 9, 8, 7, 8, 10]
geo_growth = [2, 4, 3, 4, 4, 4, 6, 7, 5, 7, 6, 9, 7, 8]
bio_growth = [2, 1, 3, 2, 4, 4, 3, 5, 6, 4, 6, 7, 5, 6]

colors = ['#32CD32', '#FF8C00', '#87CEEB', '#8B4513', '#FFD700']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

ax1.pie(
    [30, 25, 20, 15, 10],
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
ax2.set_xticks(years)
ax2.set_xlim(2010, 2023)
ax2.set_ylim(0, 30)

plt.tight_layout()
plt.show()