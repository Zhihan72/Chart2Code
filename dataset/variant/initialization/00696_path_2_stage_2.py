import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
average_production = np.array([300, 320, 340, 350, 365, 375, 390, 405, 420, 430, 445])
error = np.array([15, 18, 20, 22, 19, 21, 20, 18, 17, 16, 15])

percent_change = np.diff(average_production) / average_production[:-1] * 100

fig, axs = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

# First subplot: Line chart with error bars
axs[0].errorbar(
    years, average_production, yerr=error, fmt='-o', color='navy', ecolor='lightblue',
    linestyle='-', capsize=5, capthick=2, markerfacecolor='lightcoral', alpha=0.8, label='Avg. Production'
)
axs[0].set_title('Solar Energy: 2010-2020', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Yr', fontsize=12, fontweight='bold')
axs[0].set_ylabel('Avg. (GWh)', fontsize=12, fontweight='bold')
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45)
axs[0].set_yticks(np.arange(280, 470, 20))
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper left', fontsize=10)
axs[0].text(2010.5, 440, 'Weather impact', fontsize=10, style='italic', bbox={'facecolor': 'lightblue', 'alpha': 0.5, 'pad': 5})

# Second subplot: Bar chart showing percentage change
axs[1].bar(years[1:], percent_change, color='teal', alpha=0.7, label='Yearly Change')
axs[1].set_title('% Change in Production', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Yr', fontsize=12, fontweight='bold')
axs[1].set_ylabel('% Change', fontsize=12, fontweight='bold')
axs[1].set_xticks(years[1:])
axs[1].set_xticklabels(years[1:], rotation=45)
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].legend(loc='upper right', fontsize=10)

plt.show()