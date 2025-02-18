import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

north_region_temp = np.array([15, 15.2, 15.1, 15.5, 15.6, 16, 16.2, 16.5, 16.8, 17, 17.3, 17.5, 18, 18.2, 18.4, 18.6, 18.8, 19, 19.2, 19.4, 19.6])
south_region_temp = np.array([25, 25.2, 25.1, 25.4, 25.5, 25.7, 25.9, 26, 26.3, 26.5, 26.6, 26.8, 27, 27.2, 27.4, 27.6, 27.8, 28, 28.2, 28.3, 28.5])
central_region_temp = np.array([20, 20.1, 20.2, 20.4, 20.5, 20.6, 20.8, 21, 21.2, 21.3, 21.5, 21.7, 22, 22.2, 22.4, 22.5, 22.7, 22.9, 23, 23.1, 23.3])

fig, ax = plt.subplots(figsize=(14, 8))

# Shuffled colors
ax.plot(years, north_region_temp, 'o-', label='North Region', color='green', linewidth=2.5)
ax.plot(years, south_region_temp, 's-', label='South Region', color='blue', linewidth=2.5)
ax.plot(years, central_region_temp, '^-', label='Central Region', color='red', linewidth=2.5)

ax.set_title("Average Temperature Changes in Fictional Country\n(2000-2020)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Average Temperature (°C)", fontsize=14)

ax.legend(title="Regions", fontsize=12, title_fontsize=14, loc='upper left')

important_years = [2012, 2016, 2020]
annotations = [
    (2012, north_region_temp[years == 2012][0], 'Pacific Cyclone Impact'),
    (2016, south_region_temp[years == 2016][0], 'Record-High Summer'),
    (2020, central_region_temp[years == 2020][0], 'Drought Year')
]

for year, value, note in annotations:
    ax.annotate(note, 
                xy=(year, value), 
                xytext=(year, value + 1), 
                textcoords='data',
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=10, 
                color='black')

for year, n_temp, s_temp, c_temp in zip(years, north_region_temp, south_region_temp, central_region_temp):
    ax.annotate(f'{n_temp:.1f}', xy=(year, n_temp), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='green')
    ax.annotate(f'{s_temp:.1f}', xy=(year, s_temp), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='blue')
    ax.annotate(f'{c_temp:.1f}', xy=(year, c_temp), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='red')

ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(1999, 2021)
ax.set_ylim(14, 30)

plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()