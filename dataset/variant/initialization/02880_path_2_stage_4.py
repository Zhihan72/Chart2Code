import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2024)
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

visitors_spring = np.array([30, 34, 36, 38])
visitors_summer = np.array([50, 55, 60, 62])
visitors_autumn = np.array([25, 27, 28, 30])
visitors_winter = np.array([15, 18, 16, 14])

temps_spring = np.array([12, 13, 14, 15])
temps_summer = np.array([25, 26, 27, 28])
temps_autumn = np.array([14, 13, 13, 12])
temps_winter = np.array([2, 3, 4, 3])

fig, axs = plt.subplots(2, 1, figsize=(10, 8), constrained_layout=True)

axs[0].stackplot(years, visitors_spring, visitors_summer, visitors_autumn, visitors_winter,
                 labels=seasons, colors=['#4682B4'], alpha=0.7)
axs[0].set_title('Seasonal Visitor Trends\nEvergreen National Park (2020-2023)', fontsize=14, fontweight='bold', pad=10)
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Visitors (Thousands)', fontsize=12)
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45, ha='right')
axs[0].grid(True, linestyle='-.', linewidth=0.75)
axs[0].legend(loc='lower right', title='Legend', fontsize=9)
axs[0].annotate('Summer Peak', xy=(2023, 62), xytext=(2022.3, 70),
                arrowprops=dict(arrowstyle='->', color='gray'),
                fontsize=9, color='navy')

bar_width = 0.25
x_indices = np.arange(len(years))

for i, season in enumerate(seasons):
    axs[1].barh(x_indices + i * bar_width, 
                [temps_spring[i], temps_summer[i], temps_autumn[i], temps_winter[i]], 
                bar_width, label=season, color='#4682B4', alpha=0.8, hatch=['/', '\\', '|', '-'][i])

axs[1].set_title('Average Seasonal Temperatures (°C)', fontsize=14, fontweight='bold', pad=10)
axs[1].set_xlabel('Temperature (°C)', fontsize=12)
axs[1].set_ylabel('Year', fontsize=12)
axs[1].set_yticks(x_indices + bar_width * 1.5)
axs[1].set_yticklabels(years, rotation=45, ha='right')
axs[1].legend(loc='lower left', title='Weather Periods', fontsize=9)
axs[1].grid(False)

plt.show()