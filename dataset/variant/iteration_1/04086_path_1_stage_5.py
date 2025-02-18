import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.colors import ListedColormap

teams = ["Theta", "Eta", "Beta", "Delta", "Zeta", "Alpha"]
years = np.array([2020, 2019, 2015, 2018, 2016, 2021])

productivity_data = np.array([
    [65, 70, 75, 78, 82, 87],
    [68, 73, 72, 79, 83, 88],
    [70, 75, 78, 84, 86, 90],
    [72, 78, 81, 88, 90, 93],
    [65, 68, 72, 79, 82, 85],
    [68, 72, 76, 83, 86, 88],
]).T

fig, ax = plt.subplots(figsize=(10, 6))

mask = np.triu(np.ones_like(productivity_data, dtype=bool))
masked_data = np.ma.masked_where(mask, productivity_data)

# Creating a shuffled color map
cmap_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A833FF', '#33FFF5']
shuffled_cmap = ListedColormap(cmap_colors)

heatmap = ax.imshow(masked_data, cmap=shuffled_cmap, aspect='auto', interpolation='nearest')

ax.set_title("Innovation Dynamics Across Myriad Epochs", fontsize=14, fontweight='normal', pad=15)
ax.set_xlabel('Innovation Units', fontsize=10)
ax.set_ylabel('Project Cycle', fontsize=10)

ax.set_xticks(np.arange(len(teams)))
ax.set_xticklabels(teams, rotation=0, ha='center')
ax.set_yticks(np.arange(len(years)))
ax.set_yticklabels(years[::-1])

cbar = plt.colorbar(heatmap, ax=ax, orientation='horizontal')
cbar.set_label('Efficiency Index', fontsize=10, style='italic')

ax.grid()

for i in range(len(years)):
    for j in range(len(teams)):
        if not mask[i, j]:
            ax.text(j, i, productivity_data[i, j], ha='center', va='center', color='white', fontsize=8, fontweight='bold')

plt.tight_layout()
plt.show()