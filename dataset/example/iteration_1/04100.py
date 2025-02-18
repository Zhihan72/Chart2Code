import matplotlib.pyplot as plt
import numpy as np

# Backstory: A local community organized an annual planting event for the past five years.
# The chart shows the number of different types of trees planted each year.

# Data: Types of trees and the number planted each year
years = ['2018', '2019', '2020', '2021', '2022']
tree_types = ['Oak', 'Pine', 'Maple', 'Birch', 'Cherry']
planting_data = [
    [50, 60, 45, 70, 80],  # Oak
    [80, 90, 100, 85, 95],  # Pine
    [40, 50, 55, 65, 70],  # Maple
    [30, 45, 60, 40, 50],  # Birch
    [20, 25, 30, 35, 45]   # Cherry
]

# Transposing the planting_data for easier plotting
planting_data_t = np.array(planting_data).T

# Colors for the different types of trees
colors = plt.cm.viridis(np.linspace(0, 1, len(tree_types)))

fig, ax = plt.subplots(figsize=(12, 8))

# Create stacked bar plots
for i, (tree_type, color) in enumerate(zip(tree_types, colors)):
    if i == 0:
        bars = ax.bar(years, planting_data_t[:, i], color=color, edgecolor='black', label=tree_type)
    else:
        bars = ax.bar(years, planting_data_t[:, i], bottom=np.sum(planting_data_t[:, :i], axis=1), color=color, edgecolor='black', label=tree_type)

# Add labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Trees Planted', fontsize=12)
ax.set_title('Annual Community Planting Event: 2018-2022\nNumber of Trees Planted by Type', fontsize=16, fontweight='bold')

# Adding a legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12, title="Tree Types", title_fontsize='13')

# Add annotations for total trees planted each year
totals = planting_data_t.sum(axis=1)
for year, total in zip(years, totals):
    ax.text(year, total + 5, f'{total}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adding grid for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to ensure elements fit well
plt.tight_layout()

# Show plot
plt.show()