import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

biodiversity_data = np.array([
    [0.85, 0.75, 0.60, 0.70, 0.65],
    [0.78, 0.50, 0.55, 0.68, 0.60],
    [0.82, 0.55, 0.58, 0.75, 0.68],
    [0.80, 0.65, 0.62, 0.72, 0.66]
])

ecosystems = ["Trop. Forest", "Desert", "Temp. Forest", "Coral Reef", "Wetland"]
regions = ["S. America", "Africa", "Asia", "Oceania"]

region_avg = biodiversity_data.mean(axis=1)

fig, ax1 = plt.subplots(figsize=(10, 8))

# Heatmap
cax = ax1.imshow(biodiversity_data, cmap='coolwarm', aspect='auto', interpolation='bilinear')
cbar = fig.colorbar(cax, ax=ax1, fraction=0.046, pad=0.04)
cbar.set_label('Biodiv.', rotation=270, labelpad=15)

ax1.set_xticks(np.arange(len(ecosystems)))
ax1.set_yticks(np.arange(len(regions)))
ax1.set_xticklabels(ecosystems, rotation=30, ha="right", fontsize=11, fontweight='bold')
ax1.set_yticklabels(regions, fontsize=11, fontstyle='italic')
ax1.set_title('Biodiversity Index\nby Eco & Reg', pad=10, fontsize=14)

# Annotate cells
for i in range(len(regions)):
    for j in range(len(ecosystems)):
        value = biodiversity_data[i, j]
        color = 'black' if value < 0.65 else 'white'
        ax1.text(j, i, f'{value:.2f}', ha='center', va='center', color=color, fontweight='bold')

highlight_index = np.argmax(biodiversity_data)
highlight_x, highlight_y = np.unravel_index(highlight_index, biodiversity_data.shape)
highlight_patch = mpatches.Rectangle((highlight_y - 0.5, highlight_x - 0.5), 1, 1, fill=False, edgecolor='darkgreen', linewidth=3, linestyle=':')
ax1.add_patch(highlight_patch)

ax1.grid(visible=True, color='gray', linestyle='--', linewidth=0.5)

plt.tight_layout()

plt.show()