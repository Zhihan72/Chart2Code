import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
average_production = np.array([300, 320, 340, 350, 365, 375, 390, 405, 420, 430, 445])
error = np.array([15, 18, 20, 22, 19, 21, 20, 18, 17, 16, 15])

percent_change = np.diff(average_production) / average_production[:-1] * 100

fig, axs = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

# First subplot: Line chart with error bars
axs[0].errorbar(
    years, average_production, yerr=error, fmt='-s', color='orange', ecolor='darkseagreen',
    linestyle='-.', capsize=4, capthick=1, markerfacecolor='yellowgreen', alpha=0.6, label='Avg. Production'
)
axs[0].set_title('Renewable Energy: 2010-2020', fontsize=13, fontweight='normal')
axs[0].set_xlabel('Year', fontsize=11, fontweight='normal', color='darkred')
axs[0].set_ylabel('Avg. Production (GWh)', fontsize=11, fontweight='normal', color='darkred')
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=60)
axs[0].set_yticks(np.arange(300, 460, 25))
axs[0].grid(False)
axs[0].legend(loc='lower right', fontsize=9)
axs[0].text(2011, 410, 'Impact note', fontsize=9, style='italic', bbox={'facecolor': 'darkseagreen', 'alpha': 0.3, 'pad': 4})

# Second subplot: Bar chart showing percentage change
axs[1].bar(years[1:], percent_change, color='darkcyan', alpha=0.8, label='Annual Change')
axs[1].set_title('% Yearly Change', fontsize=13, fontweight='normal')
axs[1].set_xlabel('Year', fontsize=11, fontweight='normal', color='darkred')
axs[1].set_ylabel('% Change', fontsize=11, fontweight='normal', color='darkred')
axs[1].set_xticks(years[1:])
axs[1].set_xticklabels(years[1:], rotation=60)
axs[1].grid(False)
axs[1].legend(loc='best', fontsize=9)

plt.show()