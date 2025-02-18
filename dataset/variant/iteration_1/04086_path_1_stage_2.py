import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# Randomized team names and years
teams = ["Theta", "Eta", "Beta", "Gamma", "Delta", "Zeta", "Alpha", "Epsilon"]
years = np.array([2020, 2019, 2015, 2018, 2016, 2021, 2017])

productivity_data = np.array([
    [65, 70, 75, 80, 78, 82, 87],
    [68, 73, 72, 76, 79, 83, 88],
    [70, 75, 78, 82, 84, 86, 90],
    [72, 78, 81, 85, 88, 90, 93],
    [65, 68, 72, 75, 79, 82, 85],
    [68, 72, 76, 80, 83, 86, 88],
    [67, 70, 74, 78, 81, 83, 87],
    [66, 70, 73, 76, 79, 81, 84]
]).T

fig, ax = plt.subplots(figsize=(10, 6))

# Mask out the upper triangle
mask = np.triu(np.ones_like(productivity_data, dtype=bool))

# Apply the mask to the data
masked_data = np.ma.masked_where(mask, productivity_data)

heatmap = ax.imshow(masked_data, cmap='YlOrRd', aspect='auto', interpolation='nearest')

# Changed titles and labels
ax.set_title("Innovation Dynamics Across Myriad Epochs", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Innovation Units', fontsize=12)
ax.set_ylabel('Project Cycle', fontsize=12)
ax.set_xticks(np.arange(len(teams)))
ax.set_xticklabels(teams, rotation=45, ha='right')
ax.set_yticks(np.arange(len(years)))
ax.set_yticklabels(years)

cbar = plt.colorbar(heatmap, ax=ax, orientation='vertical')
cbar.set_label('Efficiency Index', fontsize=12)

for i in range(len(years)):
    for j in range(len(teams)):
        if not mask[i, j]:
            ax.text(j, i, productivity_data[i, j], ha='center', va='center', color='black', fontsize=8)

plt.tight_layout()
plt.show()