import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
average_production = np.array([300, 320, 340, 350, 365, 375, 390, 405, 420, 430, 445])
error = np.array([15, 18, 20, 22, 19, 21, 20, 18, 17, 16, 15])

percent_change = np.diff(average_production) / average_production[:-1] * 100

fig, axs = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

# First subplot (now): Bar chart showing percentage change
axs[0].bar(years[1:], percent_change, color='navy', alpha=0.7)
axs[0].set_xticks(years[1:])
axs[0].set_xticklabels(years[1:], rotation=45)
axs[0].grid(True, linestyle='--', alpha=0.6)

# Second subplot (now): Line chart with error bars
axs[1].errorbar(
    years, average_production, yerr=error, fmt='-o', color='teal', ecolor='lightcoral',
    linestyle='-', capsize=5, capthick=2, markerfacecolor='navy', alpha=0.8
)
axs[1].set_xticks(years)
axs[1].set_xticklabels(years, rotation=45)
axs[1].set_yticks(np.arange(280, 470, 20))
axs[1].grid(True, linestyle='--', alpha=0.6)

plt.show()