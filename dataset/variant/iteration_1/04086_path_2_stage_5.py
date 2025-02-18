import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

crews = ["Beta", "Delta", "Epsilon", "Gamma", "Alpha", "Theta", "Eta"]
epochs = np.arange(2015, 2022)

efficiency_data = np.array([
    [72, 78, 81, 85, 88, 90, 93],
    [70, 75, 78, 82, 84, 86, 90],
    [65, 68, 72, 75, 79, 82, 85],
    [68, 73, 72, 76, 79, 83, 88],
    [65, 70, 75, 80, 78, 82, 87],
    [66, 70, 73, 76, 79, 81, 84],
    [67, 70, 74, 78, 81, 83, 87]
]).T 

mask = np.tril(np.ones_like(efficiency_data, dtype=bool), k=-1)

fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(1, 1)

ax = plt.subplot(gs[0, 0])
lower_triangle_data = np.ma.array(efficiency_data, mask=~mask)
heatmap = ax.imshow(lower_triangle_data, cmap='coolwarm', aspect='auto', interpolation='bilinear')

ax.set_title("Crew Efficiency Over Time", fontsize=18, fontweight='light', pad=15)
ax.set_xlabel('Crews', fontsize=14)
ax.set_ylabel('Epoch', fontsize=14)
ax.set_xticks(np.arange(len(crews)))
ax.set_xticklabels(crews, rotation=60, ha='right', fontstyle='italic')
ax.set_yticks(np.arange(len(epochs)))
ax.set_yticklabels(epochs, fontstyle='italic')

cbar = plt.colorbar(heatmap, ax=ax, orientation='horizontal', pad=0.2)
cbar.set_label('Efficiency Score', fontsize=14)

for i in range(len(epochs)):
    for j in range(len(crews)):
        if mask[i, j]:
            ax.text(j, i, efficiency_data[i, j], ha='center', va='center', color='blue', fontsize=10, fontweight='bold')

ax.grid(True, linestyle=':', linewidth=0.5)
plt.tight_layout()
plt.show()