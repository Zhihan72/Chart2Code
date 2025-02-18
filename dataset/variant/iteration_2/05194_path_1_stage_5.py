import matplotlib.pyplot as plt
import numpy as np

sectors = ['Tidal Power', 'Geothermal Energy', 'Bioenergy']
power_sources = ['Tidal Generators', 'Hydrothermal Vents', 'Hydrogen Cells', 'Biomass']

energy_data = [
    [50, 10, 20, 20],
    [10, 60, 20, 10],
    [20, 10, 20, 50]
]

efficiency_ratios = [0.8, 0.6, 0.7]

# Shuffled colors manually
colors = ['#FFD54F', '#81C784', '#FF8A65']

fig, ax = plt.subplots(2, 2, figsize=(16,16))
plt.subplots_adjust(top=0.85)

# Convert pie charts to sorted bar charts
for i in range(len(sectors)):
    data = energy_data[i]
    sorted_indices = np.argsort(data)  # Sorting indices of the data for ascending order
    sorted_data = np.array(data)[sorted_indices]
    sorted_power_sources = np.array(power_sources)[sorted_indices]
    
    ax.flatten()[i].bar(sorted_power_sources, sorted_data, color=colors[i])

# Sorted bar chart for efficiency ratios
sorted_indices_eff = np.argsort(efficiency_ratios)
sorted_eff_ratios = np.array(efficiency_ratios)[sorted_indices_eff]
sorted_sectors = np.array(sectors)[sorted_indices_eff]

ax_eff = fig.add_subplot(224)
ax_eff.bar(sorted_sectors, sorted_eff_ratios, color=colors)

plt.tight_layout(rect=[0, 0, 0.85, 0.95])
plt.show()