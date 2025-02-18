import numpy as np
import matplotlib.pyplot as plt

cities = ['Town1', 'District2', 'Metropolis3', 'Capital5', 'Borough6', 'Hamlet7', 'Region8', 'Locality9', 'Urban10']
populations = [50000, 150000, 300000, 600000, 850000, 1200000, 1500000, 2000000, 3000000]
park_counts = [20, 35, 50, 90, 150, 200, 250, 300, 350]

fig, ax = plt.subplots(figsize=(12, 8))

# Set custom colors manually to shuffle the originally assigned colors
custom_colors = ['red', 'purple', 'blue', 'orange', 'yellow', 'green', 'cyan', 'magenta', 'black']

# Scatter plot with altered markers and edgecolors
scatter = ax.scatter(populations, park_counts, s=populations, alpha=0.6, edgecolors='r', marker='^', c=custom_colors, label='Urban Areas')

# Annotate with altered font size for a few cities
for i, city in enumerate(cities):
    ax.annotate(city, (populations[i], park_counts[i]), fontsize=8, ha='left')

# Regression line with altered style
coefficients = np.polyfit(populations, park_counts, 1)
polynomial = np.poly1d(coefficients)
trendline = polynomial(populations)
ax.plot(populations, trendline, color='green', linestyle='-', linewidth=2, label='Regression Line')

# Title and labels with altered fonts
ax.set_title('Size vs. Parks: A Visual Exploration', fontsize=16, fontweight='normal')
ax.set_xlabel('Population Size', fontsize=14)
ax.set_ylabel('Number of Parks', fontsize=14)

# Updated legend and grid style
ax.legend(facecolor='lightyellow', edgecolor='gray')
ax.grid(True, linestyle='-.', alpha=0.5)

plt.tight_layout()
plt.show()