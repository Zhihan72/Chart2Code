import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

north_region_temp = np.array([15, 15.2, 15.1, 15.5, 15.6, 16, 16.2, 16.5, 16.8, 17, 17.3, 17.5, 18, 18.2, 18.4, 18.6, 18.8, 19, 19.2, 19.4, 19.6])
south_region_temp = np.array([25, 25.2, 25.1, 25.4, 25.5, 25.7, 25.9, 26, 26.3, 26.5, 26.6, 26.8, 27, 27.2, 27.4, 27.6, 27.8, 28, 28.2, 28.3, 28.5])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, north_region_temp, 'x--', label='North Region', color='blue', linewidth=2)
ax.plot(years, south_region_temp, 'd:', label='South Region', color='green', linewidth=2)

ax.set_title("Climatic Changes in Different Regions\n2000 to 2020", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Average Temperature (°C)", fontsize=14)

ax.legend(title="Regions", fontsize=12, title_fontsize=14, loc='lower right')

important_years = [2012, 2016]
annotations = [
    (2012, north_region_temp[years == 2012][0], 'Cyclone Effects'),
    (2016, south_region_temp[years == 2016][0], 'Summer Peak')
]

for year, value, note in annotations:
    ax.annotate(note, 
                xy=(year, value), 
                xytext=(year, value + 0.5), 
                textcoords='data',
                arrowprops=dict(facecolor='darkgray', shrink=0.05),
                fontsize=10, 
                color='black')

ax.grid(True, linestyle='-', alpha=0.7)
ax.set_xlim(1999, 2021)
ax.set_ylim(14, 30)

plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()