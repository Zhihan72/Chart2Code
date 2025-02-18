import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2021)
asia_temp = [-0.2, 0.1, 0.3, 0.5, 0.4, 0.6, 0.7, 0.8, 0.9, 1.2, 1.3]
europe_temp = [-0.1, 0.0, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.0, 1.1, 1.2]
africa_temp = [0.0, 0.1, 0.3, 0.4, 0.4, 0.6, 0.7, 0.9, 1.0, 1.2, 1.3]
north_america_temp = [-0.3, -0.2, 0.1, 0.3, 0.2, 0.5, 0.6, 0.8, 0.9, 1.0, 1.1]
south_america_temp = [0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.3, 1.4]

# Plot
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(years, asia_temp, marker='o', label='Asia', linewidth=2, color='cyan')
ax.plot(years, europe_temp, marker='v', label='Eur', linewidth=2, color='magenta')
ax.plot(years, africa_temp, marker='s', label='Afr', linewidth=2, color='yellow')
ax.plot(years, north_america_temp, marker='D', label='N. Am', linewidth=2, color='green')
ax.plot(years, south_america_temp, marker='*', label='S. Am', linewidth=2, color='blue')

highlight_years = {'2015': [asia_temp[5], europe_temp[5], africa_temp[5], 
                            north_america_temp[5], south_america_temp[5]],
                   '2020': [asia_temp[10], europe_temp[10], africa_temp[10], 
                            north_america_temp[10], south_america_temp[10]]}

for year, temps in highlight_years.items():
    ax.annotate(year, xy=(int(year), temps[0]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='cyan')
    ax.annotate(year, xy=(int(year), temps[1]), xytext=(5, -10), textcoords='offset points', fontsize=9, color='magenta')
    ax.annotate(year, xy=(int(year), temps[2]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='yellow')
    ax.annotate(year, xy=(int(year), temps[3]), xytext=(5, -10), textcoords='offset points', fontsize=9, color='green')
    ax.annotate(year, xy=(int(year), temps[4]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='blue')

# Customization
ax.set_title("Avg. Temp Change (2010-20)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Yr", fontsize=12, weight='bold')
ax.set_ylabel("Temp Change (°C)", fontsize=12, weight='bold')
ax.legend(loc='upper left', fontsize=10, title='Cont', title_fontsize=12)
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()