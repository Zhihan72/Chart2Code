import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

north_region_temp = np.array([15, 15.2, 15.1, 15.5, 15.6, 16, 16.2, 16.5, 16.8, 17, 17.3, 17.5, 18, 18.2, 18.4, 18.6, 18.8, 19, 19.2, 19.4, 19.6])
south_region_temp = np.array([25, 25.2, 25.1, 25.4, 25.5, 25.7, 25.9, 26, 26.3, 26.5, 26.6, 26.8, 27, 27.2, 27.4, 27.6, 27.8, 28, 28.2, 28.3, 28.5])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, north_region_temp, 'o-', color='blue', linewidth=2.5)
ax.plot(years, south_region_temp, 's-', color='red', linewidth=2.5)

ax.set_title("Climate Trends in Imaginary Land\n(2000-2020)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Timeline", fontsize=14)
ax.set_ylabel("Temperature (°C)", fontsize=14)

important_years = [2012, 2016]
annotations = [
    (2012, north_region_temp[years == 2012][0], 'Storm Surge Event'),
    (2016, south_region_temp[years == 2016][0], 'Extreme Heatwave')
]

for year, value, note in annotations:
    ax.annotate(note, 
                xy=(year, value), 
                xytext=(year, value + 1), 
                textcoords='data',
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=10, 
                color='black')

for year, n_temp, s_temp in zip(years, north_region_temp, south_region_temp):
    ax.annotate(f'{n_temp:.1f}', xy=(year, n_temp), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='blue')
    ax.annotate(f'{s_temp:.1f}', xy=(year, s_temp), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='red')

ax.set_xlim(1999, 2021)
ax.set_ylim(14, 30)

plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()