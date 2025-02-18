import matplotlib.pyplot as plt
import numpy as np

# Data
locations = ['North', 'South', 'Central']
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

north_trees = [22, 15, 18, 31, 32, 28, 25, 30, 29, 24, 27, 26]
south_trees = [18, 13, 10, 35, 34, 25, 32, 33, 29, 27, 30, 22]
central_trees = [28, 30, 11, 31, 32, 24, 19, 34, 33, 8, 35, 15]

# Sorting the data in descending order
north_sorted = sorted(zip(north_trees, months), reverse=True)
south_sorted = sorted(zip(south_trees, months), reverse=True)
central_sorted = sorted(zip(central_trees, months), reverse=True)

north_trees_sorted, months_sorted_north = zip(*north_sorted)
south_trees_sorted, months_sorted_south = zip(*south_sorted)
central_trees_sorted, months_sorted_central = zip(*central_sorted)

fig, ax = plt.subplots(figsize=(14, 8))

width = 0.25
x = np.arange(len(months))

# Use shortened region names
bars1 = ax.bar(x - width, north_trees_sorted, width, color='teal', edgecolor='navy', linestyle=':', label='North')
bars2 = ax.bar(x, south_trees_sorted, width, color='limegreen', edgecolor='forestgreen', linestyle='--', label='South')
bars3 = ax.bar(x + width, central_trees_sorted, width, color='crimson', edgecolor='darkred', linestyle='-.', label='Central')

# Shorter title & labels
ax.set_title('Tree Data', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Trees (1000s)', fontsize=14)

ax.set_xticks(x)
ax.set_xticklabels(months_sorted_north, fontsize=12, rotation=45, ha='right')

def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                    xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', fontsize=9, color='darkred')

annotate_bars(bars1)
annotate_bars(bars2)
annotate_bars(bars3)

ax.legend(title='Region', title_fontsize='13', fontsize='12', loc='upper right')

plt.tight_layout()
plt.show()