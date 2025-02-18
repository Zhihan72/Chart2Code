import matplotlib.pyplot as plt
import numpy as np

# Defining the data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
north_trees = [15, 18, 22, 25, 28, 30, 32, 31, 29, 27, 26, 24]
south_trees = [10, 13, 18, 22, 27, 29, 33, 35, 34, 32, 30, 25]
central_trees = [8, 11, 15, 19, 24, 28, 30, 32, 33, 35, 34, 31]

# Sorting the data
sorted_indices_north = np.argsort(north_trees)
sorted_indices_south = np.argsort(south_trees)
sorted_indices_central = np.argsort(central_trees)

# Sorting the months and tree data for each region accordingly
sorted_months_north = months[sorted_indices_north]
sorted_north_trees = np.array(north_trees)[sorted_indices_north]

sorted_months_south = months[sorted_indices_south]
sorted_south_trees = np.array(south_trees)[sorted_indices_south]

sorted_months_central = months[sorted_indices_central]
sorted_central_trees = np.array(central_trees)[sorted_indices_central]

# Plotting the sorted bar chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(sorted_months_north, sorted_north_trees, width=0.25, label='Northern Woods', color='forestgreen', align='center')
ax.bar(sorted_months_south, sorted_south_trees, width=0.25, label='Southern Plains', color='limegreen', align='edge')
ax.bar(sorted_months_central, sorted_central_trees, width=0.25, label='Heartland', color='darkgreen', align='edge')

ax.set_title('Eco Warriors: Tree Plantation Journey\nTrees Planted Monthly in 2023 (in k)', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Trees Planted (Thousands)', fontsize=14)

ax.legend(title='Plantation Areas', title_fontsize='13', fontsize='12', loc='upper left', bbox_to_anchor=(1, 1))

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()