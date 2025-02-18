import matplotlib.pyplot as plt
import numpy as np

# Data setup
countries = ['Region X', 'Region Y']
energy_types = ['Geothermal', 'Nuclear', 'Biomass']
percentage_distributions = np.array([
    [40, 35, 25],  # Region X
    [30, 40, 30],  # Region Y
])

# Calculate totals for sorting
totals = percentage_distributions.sum(axis=0)
sorted_indices = np.argsort(totals)[::-1]  # Sort in descending order

# Sort energy_types and percentage_distributions
sorted_energy_types = [energy_types[i] for i in sorted_indices]
sorted_distributions = percentage_distributions[:, sorted_indices]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35

# Plot bars for each region
bar_positions = np.arange(len(sorted_energy_types))
for i, (region, color) in enumerate(zip(countries, ['#99ff99', '#66b3ff'])):
    ax.bar(bar_positions + i * bar_width, sorted_distributions[i], bar_width,
           label=region, color=color, edgecolor='grey', alpha=0.7)

# Labeling
ax.set_xlabel('Energy Sources', fontsize=12)
ax.set_ylabel('Usage Percentage (%)', fontsize=12)
ax.set_title('Sorted Energy Use By Region (2023)', fontsize=16)
ax.set_xticks(bar_positions + bar_width / 2)
ax.set_xticklabels(sorted_energy_types)
ax.legend(title='Regions')

plt.tight_layout()
plt.show()