import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
tree_types = ['Oak', 'Pine', 'Maple', 'Birch']
planting_data = [
    [50, 60, 45, 70, 80],  # Oak
    [80, 90, 100, 85, 95],  # Pine
    [40, 50, 55, 65, 70],  # Maple
    [30, 45, 60, 40, 50]   # Birch
]

# Convert data to a numpy array for easier indexing
planting_data_np = np.array(planting_data)

# Parameters for bar chart
num_years = len(years)
num_tree_types = len(tree_types)
bar_width = 0.2  # Width of each bar
x = np.arange(num_years)  # The x locations for the groups

fig, ax = plt.subplots(figsize=(12, 8))

# Plot each type of tree's data as a separate group of bars
for i, tree_type in enumerate(tree_types):
    offset = i * bar_width  # Calculate offset for bar placement
    ax.bar(x + offset, planting_data_np[i], bar_width, label=tree_type)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Trees Planted', fontsize=12)
ax.set_title('Tree Planting: 2018-2022', fontsize=16, fontweight='bold')
ax.set_xticks(x + bar_width * (num_tree_types - 1) / 2)  # Center x-ticks under groups
ax.set_xticklabels(years)
ax.legend()

plt.tight_layout()
plt.show()