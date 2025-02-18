import matplotlib.pyplot as plt
import numpy as np

modern_writers = ['Morrison', 'Atwood', 'Toni', 'Murakami', 'Rushdie']
modern_data = {
    'Morrison': [8, 9, 8, 5, 7],
    'Atwood': [7, 8, 7, 6, 8],
    'Toni': [6, 7, 9, 6, 7],
    'Murakami': [7, 7, 6, 8, 8],
    'Rushdie': [8, 8, 9, 4, 6]
}

categories = ['Creativity', 'Emotional Depth', 'Social Commentary', 'Humor', 'Style']

fig, ax_heatmap = plt.subplots(figsize=(8, 8))
cax = ax_heatmap.matshow(np.array([modern_data[writer] for writer in modern_writers]), cmap='Blues', aspect='auto')

ax_heatmap.set_xticks(np.arange(len(categories)))
ax_heatmap.set_yticks(np.arange(len(modern_writers)))
ax_heatmap.set_xticklabels([])
ax_heatmap.set_yticklabels([])

for i in range(len(modern_writers)):
    for j in range(len(categories)):
        ax_heatmap.text(j, i, f"{modern_data[modern_writers[i]][j]:.1f}", ha='center', va='center', color='black')

plt.tight_layout()
plt.show()