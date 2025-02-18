import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
north_trees = [18, 22, 26, 15, 30, 24, 27, 32, 31, 29, 25, 28]
south_trees = [22, 27, 30, 10, 35, 18, 29, 34, 25, 33, 32, 13]
central_trees = [24, 15, 19, 11, 28, 33, 35, 8, 32, 31, 30, 34]

# Sorting the data
sorted_indices_north = np.argsort(north_trees)
sorted_indices_south = np.argsort(south_trees)
sorted_indices_central = np.argsort(central_trees)

sorted_months_north = months[sorted_indices_north]
sorted_north_trees = np.array(north_trees)[sorted_indices_north]

sorted_months_south = months[sorted_indices_south]
sorted_south_trees = np.array(south_trees)[sorted_indices_south]

sorted_months_central = months[sorted_indices_central]
sorted_central_trees = np.array(central_trees)[sorted_indices_central]

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