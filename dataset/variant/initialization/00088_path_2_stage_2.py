import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Hydropower', 'Nuclear', 'Coal', 'Natural Gas', 'Other Renewables', 'Fusion']
percentages_2050 = [25, 20, 15, 10, 10, 15, 3, 2]
percentages_2020 = [3, 6, 15, 10, 27, 34, 4, 1]

# Manually shuffled list of colors
colors = ['#32CD32', '#A9A9A9', '#FFD700', '#FF4500', '#9370DB', '#8A2BE2', '#1E90FF', '#FFA07A']

fig, axs = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1.5, 1]})

bars = axs[0].barh(energy_sources, percentages_2050, color=colors)
axs[0].xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
axs[0].bar_label(bars, fmt='%.1f%%')
axs[0].set_title('Projected Global Energy Source Composition\nfor Sustainability in 2050', fontsize=16, pad=20)
axs[0].set_xlabel('Percentage of Total Energy Consumption', fontsize=12)
axs[0].set_xlim(0, 30)
axs[0].set_yticklabels(energy_sources, fontsize=11)

axs[1].pie(percentages_2020, labels=energy_sources, autopct='%1.1f%%',
           startangle=90, colors=colors)
axs[1].set_title('Energy Source Composition in 2020', fontsize=14, pad=20)

plt.tight_layout()
plt.show()