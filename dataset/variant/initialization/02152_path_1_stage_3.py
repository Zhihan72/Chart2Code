import matplotlib.pyplot as plt
import numpy as np

categories = ['Creativity', 'Emotional Depth', 'Social Commentary', 'Humor', 'Style']
modern_writers = ['Morrison', 'Atwood', 'Toni', 'Murakami', 'Rushdie']

modern_data = {
    'Morrison': [8, 9, 8, 5, 7],
    'Atwood': [7, 8, 7, 6, 8],
    'Toni': [6, 7, 9, 6, 7],
    'Murakami': [7, 7, 6, 8, 8],
    'Rushdie': [8, 8, 9, 4, 6],
    'Gaiman': [7, 8, 6, 7, 9]
}

num_vars = len(categories)

def create_radar_chart(ax, data, label, color='blue'):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    ax.fill(angles, data, color=color, alpha=0.35)
    ax.plot(angles, data, color=color, linestyle='--', marker='o')
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9, fontstyle='italic')
    ax.grid(visible=True, linewidth=0.5, color='gray', linestyle='-.')

fig, axs = plt.subplots(1, 2, figsize=(16, 8), subplot_kw=dict(polar=True))
ax_radar, ax_heatmap = axs

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Radar chart plotting remains unchanged
ax_radar.set_title('The Literary Prowess\nof Historical Writers', size=16, weight='bold', position=(0.5, 1.1))

# Creating the lower triangle mask for the heatmap
heatmap_data = np.array([modern_data[writer] for writer in modern_writers + ['Gaiman']])
mask = np.triu(np.ones_like(heatmap_data, dtype=bool))

ax_heatmap.remove()
ax_heatmap = fig.add_subplot(122)

# Apply mask to heatmap data
masked_data = np.ma.masked_where(mask, heatmap_data)

cax = ax_heatmap.matshow(masked_data, cmap='Greens', aspect='auto')

ax_heatmap.set_xticks(np.arange(len(categories)))
ax_heatmap.set_yticks(np.arange(len(modern_writers) + 1))
ax_heatmap.set_xticklabels(categories, rotation=45, ha='right', fontsize=9)
ax_heatmap.set_yticklabels(modern_writers + ['Gaiman'], fontsize=9)

for i in range(heatmap_data.shape[0]):
    for j in range(heatmap_data.shape[1]):
        if i >= j:  # Only place text in the lower triangle
            ax_heatmap.text(j, i, f"{heatmap_data[i, j]:.1f}", ha='center', va='center', color='navy')

ax_heatmap.set_title('Literary Scores of Modern Writers', size=16, weight='bold', pad=20)

fig.colorbar(cax, ax=ax_heatmap, orientation='vertical', fraction=0.046, pad=0.04)

plt.tight_layout()
plt.show()