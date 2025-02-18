import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2024)
seasons = ['Spring', 'Summer', 'Autumn', 'Winter', 'Stormy']

# Visitor data
visitors_spring = np.array([30, 34, 36, 38])
visitors_summer = np.array([50, 55, 60, 62])
visitors_autumn = np.array([25, 27, 28, 30])
visitors_winter = np.array([15, 18, 16, 14])
visitors_stormy = np.array([10, 12, 11, 15])  # New data

# Temperature data
temps = [
    [12, 13, 14, 15],  # Spring
    [25, 26, 27, 28],  # Summer
    [14, 13, 13, 12],  # Autumn
    [2, 3, 4, 3],      # Winter
    [8, 7, 9, 10],     # Stormy
]

fig, axs = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

# Stackplot for visitors
axs[0].stackplot(years, visitors_spring, visitors_summer, visitors_autumn, visitors_winter, visitors_stormy,
                 labels=seasons, colors=['#FF6347', '#FFD700', '#98FB98', '#4682B4', '#8B008B'], alpha=0.8)

axs[0].set_title('Seasonal Visitor Trends\nEvergreen National Park (2020-2023)', fontsize=14, fontweight='bold', pad=10)
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Visitors (Thousands)', fontsize=12)
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45, ha='right')
axs[0].grid(True, linestyle='-', alpha=0.3)
axs[0].legend(loc='best', title='Seasons', fontsize=10)
axs[0].annotate('Summer Peak', xy=(2023, 62), xytext=(2022.5, 70),
                arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=7),
                fontsize=10, color='darkred')

# Bar plot for temperatures
bar_width = 0.15
x_indices = np.arange(len(years))

markers = ['o', 's', '^', 'd', 'x']  # Markers for each season
for i, season in enumerate(seasons):
    axs[1].bar(x_indices + i * bar_width, temps[i], bar_width, label=season, alpha=0.8, hatch=markers[i])

axs[1].set_title('Average Seasonal Temperatures (°C)', fontsize=14, fontweight='bold', pad=10)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Temperature (°C)', fontsize=12)
axs[1].set_xticks(x_indices + bar_width * 2)
axs[1].set_xticklabels(years, rotation=45, ha='right')
axs[1].legend(loc='upper right', title='Seasons', fontsize=10)
axs[1].grid(False)

plt.show()