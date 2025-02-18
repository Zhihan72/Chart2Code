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
axs[0].set_xlim(0, 30)
axs[0].set_yticklabels([])

axs[1].pie(percentages_2020, labels=None, startangle=90, colors=colors)

plt.tight_layout()
plt.show()