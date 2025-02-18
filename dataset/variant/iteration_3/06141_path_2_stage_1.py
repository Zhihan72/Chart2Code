import matplotlib.pyplot as plt
import numpy as np

# Define the data for the sorted bar chart
years = ['2012', '2014', '2016', '2018', '2020', '2022']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Bioenergy']

# Adoption data in percentage (rows: years, columns: energy sources)
adoption_data = np.array([
    [5, 10, 30, 5, 3],   # 2012
    [10, 15, 35, 6, 5],  # 2014
    [20, 30, 40, 7, 7],  # 2016
    [30, 40, 45, 8, 10], # 2018
    [40, 50, 50, 9, 12], # 2020
    [50, 60, 55, 10, 15] # 2022
])

# Sort the data according to the adoption rates in 2022
latest_year_adoption = adoption_data[-1]
sorted_indices = np.argsort(latest_year_adoption)[::-1]
sorted_sources = [energy_sources[i] for i in sorted_indices]
sorted_data = adoption_data[:, sorted_indices]

# Prepare the figure
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each energy source's sorted adoption data
bar_positions = np.arange(len(energy_sources))

ax.bar(bar_positions, sorted_data[-1], color='skyblue')

# Set axis labels and title
ax.set_xlabel('Energy Source', fontsize=12, labelpad=10)
ax.set_ylabel('Adoption Rate (%) in 2022', fontsize=12, labelpad=10)
ax.set_title('Sorted Adoption Rates of Renewable Energy Sources in 2022', fontsize=16, fontweight='bold', pad=20)

# Set x-ticks positions and labels
ax.set_xticks(bar_positions)
ax.set_xticklabels(sorted_sources)

# Add grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate bars with their respective values
for i in range(len(sorted_sources)):
    ax.text(bar_positions[i], sorted_data[-1, i] + 1, str(sorted_data[-1, i]), ha='center', va='bottom')

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()