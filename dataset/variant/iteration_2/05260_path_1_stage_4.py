import matplotlib.pyplot as plt
import numpy as np

regions = ['NA', 'EU', 'AS', 'SA', 'AF']
# Manually shuffled values for Italian cuisine popularity
italian_cuisine = [50, 60, 85, 70, 80]
colors = '#32CD32'

fig, ax = plt.subplots(figsize=(14, 8))
positions = np.arange(len(regions))

# Drawing the bar chart with the manually shuffled data
ax.bar(positions, italian_cuisine, color=colors, edgecolor='black', alpha=0.9, hatch='//')

ax.set_title("Italian Cuisine Popularity 2023", fontsize=18, fontweight='light', pad=10)
ax.set_xlabel("Regions", fontsize=12, fontweight='bold')
ax.set_ylabel("Popularity", fontsize=12, fontstyle='italic')

ax.set_xticks(positions)
ax.set_xticklabels(regions, fontsize=14, fontweight='light')

ax.grid(axis='y', linestyle='-.', color='gray', alpha=0.5)
ax.yaxis.set_ticks(np.arange(0, 101, 20))

plt.tight_layout()
plt.show()