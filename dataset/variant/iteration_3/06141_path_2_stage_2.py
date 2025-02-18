import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
years = ['2012', '2014', '2016', '2018', '2020', '2022']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geo', 'Bio']

# Adoption data in percentage
adoption_data = np.array([
    [5, 10, 30, 5, 3],
    [10, 15, 35, 6, 5],
    [20, 30, 40, 7, 7],
    [30, 40, 45, 8, 10],
    [40, 50, 50, 9, 12],
    [50, 60, 55, 10, 15]
])

# Sort data by 2022 adoption rates
latest_year_adoption = adoption_data[-1]
sorted_indices = np.argsort(latest_year_adoption)[::-1]
sorted_sources = [energy_sources[i] for i in sorted_indices]
sorted_data = adoption_data[:, sorted_indices]

# Plot
fig, ax = plt.subplots(figsize=(14, 8))
bar_positions = np.arange(len(sorted_sources))
ax.bar(bar_positions, sorted_data[-1], color='skyblue')

# Labels and title adjustments
ax.set_xlabel('Source', fontsize=12)
ax.set_ylabel('Rate (%) ' + years[-1], fontsize=12)
ax.set_title('Renewable Energy Adoption ' + years[-1], fontsize=16, fontweight='bold')

# Set x-ticks
ax.set_xticks(bar_positions)
ax.set_xticklabels(sorted_sources)

# Grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate bars
for i in range(len(sorted_sources)):
    ax.text(bar_positions[i], sorted_data[-1, i] + 1, str(sorted_data[-1, i]), ha='center', va='bottom')

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()