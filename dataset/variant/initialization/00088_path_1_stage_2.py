import matplotlib.pyplot as plt
import numpy as np

# Data: Projected Energy Mix in 2050 (altered values)
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Nuclear', 'Coal', 'Natural Gas', 'Other Renewables']
percentages_2050 = [20, 25, 15, 5, 15, 10, 10]

# Sort the data for the 2050 projection
sorted_indices = np.argsort(percentages_2050)
sorted_energy_sources = [energy_sources[i] for i in sorted_indices]
sorted_percentages_2050 = [percentages_2050[i] for i in sorted_indices]

# Historical Data: Energy Mix in 2020 (altered values)
percentages_2020 = [6, 3, 27, 5, 15, 10, 34]

# Create figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1.5, 1]})

# Sorted bar chart for 2050
bars = axs[0].barh(sorted_energy_sources, sorted_percentages_2050, color=['#FFD700', '#1E90FF', '#32CD32', '#FFA07A', '#A9A9A9', '#FF4500', '#9370DB'])
axs[0].xaxis.grid(True, linestyle='--', color='grey', alpha=0.5)
axs[0].bar_label(bars, fmt='%.1f%%')
axs[0].set_title('Projected Global Energy Source Composition\nfor Sustainability in 2050', fontsize=16, pad=20)
axs[0].set_xlabel('Percentage of Total Energy Consumption', fontsize=12)
axs[0].set_xlim(0, 30)
axs[0].set_yticklabels(sorted_energy_sources, fontsize=11)

# Pie chart for 2020
axs[1].pie(percentages_2020, labels=energy_sources, autopct='%1.1f%%',
           startangle=90, colors=['#FFD700', '#1E90FF', '#32CD32', '#FFA07A', '#A9A9A9', '#FF4500', '#9370DB'])
axs[1].set_title('Energy Source Composition in 2020', fontsize=14, pad=20)

plt.tight_layout()
plt.show()