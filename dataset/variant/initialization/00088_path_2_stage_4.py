import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Hydropower', 'Nuclear', 'Coal', 'Natural Gas', 'Other Renewables', 'Fusion']
percentages_2050 = [25, 20, 15, 10, 10, 15, 3, 2]
percentages_2020 = [3, 6, 15, 10, 27, 34, 4, 1]

# Manually shuffled list of colors
colors = ['#32CD32', '#A9A9A9', '#FFD700', '#FF4500', '#9370DB', '#8A2BE2', '#1E90FF', '#FFA07A']

# Sort indices based on percentages_2050 values in descending order
sorted_indices_2050 = np.argsort(percentages_2050)[::-1]
sorted_energy_sources_2050 = [energy_sources[i] for i in sorted_indices_2050]
sorted_percentages_2050 = [percentages_2050[i] for i in sorted_indices_2050]
sorted_colors_2050 = [colors[i] for i in sorted_indices_2050]

# Sort indices based on percentages_2020 values in descending order
sorted_indices_2020 = np.argsort(percentages_2020)[::-1]
sorted_percentages_2020 = [percentages_2020[i] for i in sorted_indices_2020]
sorted_colors_2020 = [colors[i] for i in sorted_indices_2020]

fig, axs = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1.5, 1]})

# Draw sorted horizontal bar chart
bars = axs[0].barh(sorted_energy_sources_2050, sorted_percentages_2050, color=sorted_colors_2050)
axs[0].xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
axs[0].set_xlim(0, 30)
axs[0].set_yticklabels([])

# Draw sorted pie chart
axs[1].pie(sorted_percentages_2020, labels=None, startangle=90, colors=sorted_colors_2020)

plt.tight_layout()
plt.show()