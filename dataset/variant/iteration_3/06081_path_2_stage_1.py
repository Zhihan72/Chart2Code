import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2021)
asia_temp = [-0.2, 0.1, 0.3, 0.5, 0.4, 0.6, 0.7, 0.8, 0.9, 1.2, 1.3]
europe_temp = [-0.1, 0.0, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.0, 1.1, 1.2]
africa_temp = [0.0, 0.1, 0.3, 0.4, 0.4, 0.6, 0.7, 0.9, 1.0, 1.2, 1.3]
north_america_temp = [-0.3, -0.2, 0.1, 0.3, 0.2, 0.5, 0.6, 0.8, 0.9, 1.0, 1.1]
south_america_temp = [0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.3, 1.4]

fig, ax = plt.subplots(figsize=(14, 7))

# Plot each continent's temperature change with random markers and line styles
lines = ax.plot(years, asia_temp, marker='x', linestyle=':', label='Asia', linewidth=1.5)
lines += ax.plot(years, europe_temp, marker='+', linestyle='-', label='Europe', linewidth=1.5)
lines += ax.plot(years, africa_temp, marker='1', linestyle='-.', label='Africa', linewidth=1.5)
lines += ax.plot(years, north_america_temp, marker='2', linestyle='--', label='North America', linewidth=1.5)
lines += ax.plot(years, south_america_temp, marker='3', linestyle='-', label='South America', linewidth=1.5)

# Highlight specific events on plots (includes annotations)
highlight_years = {'2015': [asia_temp[5], europe_temp[5], africa_temp[5], north_america_temp[5], south_america_temp[5]],
                   '2020': [asia_temp[10], europe_temp[10], africa_temp[10], north_america_temp[10], south_america_temp[10]]}

for year, temps in highlight_years.items():
    for i, temp in enumerate(temps):
        ax.annotate(year, xy=(int(year), temp), xytext=(5, (5 if i % 2 == 0 else -10)),
                    textcoords='offset points', fontsize=9, color=lines[i].get_color())

# Plot customization with altered properties
ax.set_title("Average Temperature Change (2010-2020) Across Different Continents", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12, weight='bold')
ax.set_ylabel("Temperature Change (°C)", fontsize=12, weight='bold')
ax.legend(loc='upper right', title='Continents', fontsize=10, title_fontsize=12)
ax.grid(visible=False, which='both')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()