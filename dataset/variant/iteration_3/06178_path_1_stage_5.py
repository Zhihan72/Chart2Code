import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
sources = ['Sol', 'Wnd', 'Hyd', 'Bio']

energy_production = np.array([
    [90, 65, 50, 100, 80],   # Solar
    [95, 80, 110, 70, 85],   # Wind
    [115, 110, 100, 120, 105],  # Hydropower
    [45, 50, 35, 30, 40]     # Biomass
])

# Calculate the total production for each source to sort them
total_production = np.sum(energy_production, axis=1)

# Sort indices based on total production in ascending order
sorted_indices = np.argsort(total_production)

# Sort sources and energy_production based on determined indices
sorted_sources = [sources[i] for i in sorted_indices]
sorted_energy_production = energy_production[sorted_indices]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#1E90FF', '#8B4513', '#FFD700', '#32CD32']

# Create a sorted bar chart based on total production
for i, source in enumerate(sorted_sources):
    ax.bar(years, sorted_energy_production[i], label=source, color=colors[i], width=0.2, alpha=0.7)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Production (TWh)', fontsize=12)
ax.set_title('Sorted Renewable Energy Production by Source in EU (2018-22)', fontsize=14, fontweight='bold')
ax.legend()
plt.tight_layout()
plt.show()