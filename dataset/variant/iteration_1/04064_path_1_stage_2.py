import matplotlib.pyplot as plt
import numpy as np

locations = ['North Region', 'South Region', 'Central Region']
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

north_trees = [22, 15, 18, 31, 32, 28, 25, 30, 29, 24, 27, 26]
south_trees = [18, 13, 10, 35, 34, 25, 32, 33, 29, 27, 30, 22]
central_trees = [28, 30, 11, 31, 32, 24, 19, 34, 33, 8, 35, 15]

x = np.arange(len(months))
width = 0.25

fig, ax = plt.subplots(figsize=(14, 8))

bars1 = ax.bar(x - width, north_trees, width, color='skyblue', edgecolor='blue', linestyle=':', label='North Region')
bars2 = ax.bar(x, south_trees, width, color='gold', edgecolor='orange', linestyle='--', label='South Region')
bars3 = ax.bar(x + width, central_trees, width, color='salmon', edgecolor='red', linestyle='-.', label='Central Region')

ax.set_title('GreenEarth Guardians: Tree Planting Campaign 2023\n Trees Planted (in thousands)', fontsize=16, fontweight='bold')
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Number of Trees (in thousands)', fontsize=14)

ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=12, rotation=45, ha='right')

def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                    xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', fontsize=9, color='darkred')
        
annotate_bars(bars1)
annotate_bars(bars2)
annotate_bars(bars3)

# Removed gridlines and relocated the legend
ax.legend(title='Regions', title_fontsize='13', fontsize='12', loc='upper right')

plt.tight_layout()
plt.show()