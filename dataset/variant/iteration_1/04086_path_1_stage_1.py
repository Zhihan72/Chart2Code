import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

teams = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta"]
years = np.arange(2015, 2022)

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

ax.set_title("Team Productivity Over the Years at Tech Innovations Inc.", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Teams', fontsize=12)
ax.set_ylabel('Year', fontsize=12)
ax.set_xticks(np.arange(len(teams)))
ax.set_xticklabels(teams, rotation=45, ha='right')
ax.set_yticks(np.arange(len(years)))
ax.set_yticklabels(years)

cbar = plt.colorbar(heatmap, ax=ax, orientation='vertical')
cbar.set_label('Monthly Productivity Score', fontsize=12)

for i in range(len(years)):
    for j in range(len(teams)):
        if not mask[i, j]:
            ax.text(j, i, productivity_data[i, j], ha='center', va='center', color='black', fontsize=8)

plt.tight_layout()
plt.show()