import matplotlib.pyplot as plt
import numpy as np

# Data
locations = ['North Region', 'South Region', 'Central Region']
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

north_trees = [22, 15, 18, 31, 32, 28, 25, 30, 29, 24, 27, 26]
south_trees = [18, 13, 10, 35, 34, 25, 32, 33, 29, 27, 30, 22]
central_trees = [28, 30, 11, 31, 32, 24, 19, 34, 33, 8, 35, 15]

# Sorting the data in descending order
north_sorted = sorted(zip(north_trees, months), reverse=True)
south_sorted = sorted(zip(south_trees, months), reverse=True)
central_sorted = sorted(zip(central_trees, months), reverse=True)

# Unzipping sorted data
north_trees_sorted, months_sorted_north = zip(*north_sorted)
south_trees_sorted, months_sorted_south = zip(*south_sorted)
central_trees_sorted, months_sorted_central = zip(*central_sorted)

# Creating subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Bar placement
width = 0.25  # Width of the bars
x = np.arange(len(months))

# Drawing bars using sorted data with new colors
bars1 = ax.bar(x - width, north_trees_sorted, width, color='teal', edgecolor='navy', linestyle=':', label='North Region')
bars2 = ax.bar(x, south_trees_sorted, width, color='limegreen', edgecolor='forestgreen', linestyle='--', label='South Region')
bars3 = ax.bar(x + width, central_trees_sorted, width, color='crimson', edgecolor='darkred', linestyle='-.', label='Central Region')

# Title & labels
ax.set_title('Sorted Tree Planting Data (Descending)\n Trees Planted (in thousands)', fontsize=16, fontweight='bold')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Number of Trees (in thousands)', fontsize=14)

# Xticks using sorted month data
ax.set_xticks(x)
ax.set_xticklabels(months_sorted_north, fontsize=12, rotation=45, ha='right')

# Annotation function
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                    xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', fontsize=9, color='darkred')

# Annotate each set of bars
annotate_bars(bars1)
annotate_bars(bars2)
annotate_bars(bars3)

# Legend
ax.legend(title='Regions', title_fontsize='13', fontsize='12', loc='upper right')

plt.tight_layout()
plt.show()