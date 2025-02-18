import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar = [5, 6, 8, 10, 13, 16, 20, 25, 30, 35, 40]
wind = [10, 12, 15, 18, 22, 27, 33, 39, 46, 53, 60]
hydro = [20, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
geo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
bio = [3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16]
ocean = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6]

total = (np.array(solar) + np.array(wind) + np.array(hydro) +
         np.array(geo) + np.array(bio) + np.array(ocean))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

ax1.bar(years, solar, label='Solar', color='#FFC300')
ax1.bar(years, wind, bottom=solar, label='Wind', color='#2E86C1')
ax1.bar(years, hydro, bottom=np.array(solar) + np.array(wind), label='Hydro', color='#28B463')
ax1.bar(years, geo, bottom=np.array(solar) + np.array(wind) + np.array(hydro), label='Geo', color='#CB4335')
ax1.bar(years, bio, bottom=np.array(solar) + np.array(wind) + np.array(hydro) + np.array(geo), label='Bio', color='#8E44AD')
ax1.bar(years, ocean, bottom=np.array(solar) + np.array(wind) + np.array(hydro) + np.array(geo) + np.array(bio), label='Ocean', color='#1ABC9C')

ax1.set_title("Energy Trends (2010-20)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Yr", fontsize=12)
ax1.set_ylabel("Usage (TWh)", fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(title='Source', loc='upper right')
ax1.grid(True, axis='y', linestyle='-.', alpha=0.5)

ax2.plot(years, total, marker='s', linestyle='--', color='teal', label='Total Usage')
ax2.set_title("Total Usage/Year", fontsize=16, fontweight='bold')
ax2.set_xlabel("Yr", fontsize=12)
ax2.set_ylabel("Usage (TWh)", fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.legend(loc='upper left')
ax2.grid(False)

plt.tight_layout()
plt.show()