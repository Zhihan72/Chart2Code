import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
average_production = np.array([300, 320, 340, 350, 365, 375, 390, 405, 420, 430, 445])
error = np.array([15, 18, 20, 22, 19, 21, 20, 18, 17, 16, 15])

percent_change = np.diff(average_production) / average_production[:-1] * 100

# Sorting percent_change in ascending order and reordering years accordingly
sorted_indices = np.argsort(percent_change)
sorted_percent_change = percent_change[sorted_indices]
sorted_years = years[1:][sorted_indices]

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# First subplot: Sorted bar chart showing percentage change
axs[0].bar(sorted_years, sorted_percent_change, color='darkorange', alpha=0.7)
axs[0].set_xticks(sorted_years)
axs[0].set_xticklabels(sorted_years, rotation=45)

# Second subplot: Line chart with error bars (original)
axs[1].errorbar(
    years, average_production, yerr=error, fmt='-o', color='forestgreen', ecolor='crimson',
    linestyle='-', capsize=5, capthick=2, markerfacecolor='darkorange', alpha=0.8
)
axs[1].set_xticks(years)
axs[1].set_xticklabels(years, rotation=45)
axs[1].set_yticks(np.arange(280, 470, 20))

plt.show()