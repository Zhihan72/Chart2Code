import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
average_production = np.array([300, 320, 340, 350, 365, 375, 390, 405, 420, 430, 445])
error = np.array([15, 18, 20, 22, 19, 21, 20, 18, 17, 16, 15])

percent_change = np.diff(average_production) / average_production[:-1] * 100

fig, axs = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

# Swapped positions: Bar chart is now axs[0] and Line chart is now axs[1]

# First subplot (now): Bar chart showing percentage change
axs[0].bar(years[1:], percent_change, color='navy', alpha=0.7, label='Yearly % Change')
axs[0].set_title('Yearly Percentage Change\nin Solar Production', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12, fontweight='bold')
axs[0].set_ylabel('Percentage Change (%)', fontsize=12, fontweight='bold')
axs[0].set_xticks(years[1:])
axs[0].set_xticklabels(years[1:], rotation=45)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper right', fontsize=10)

# Second subplot (now): Line chart with error bars
axs[1].errorbar(
    years, average_production, yerr=error, fmt='-o', color='teal', ecolor='lightcoral',
    linestyle='-', capsize=5, capthick=2, markerfacecolor='navy', alpha=0.8, label='Avg. Solar Production'
)
axs[1].set_title('Decadal Trends in Solar Energy Production:\n2010-2020', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12, fontweight='bold')
axs[1].set_ylabel('Average Production (GWh)', fontsize=12, fontweight='bold')
axs[1].set_xticks(years)
axs[1].set_xticklabels(years, rotation=45)
axs[1].set_yticks(np.arange(280, 470, 20))
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].legend(loc='upper left', fontsize=10)
axs[1].text(2010.5, 440, 'Variability due to weather conditions', fontsize=10, style='italic', bbox={'facecolor': 'lightblue', 'alpha': 0.5, 'pad': 5})

plt.show()