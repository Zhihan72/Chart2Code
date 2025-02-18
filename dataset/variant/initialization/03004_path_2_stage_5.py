import matplotlib.pyplot as plt
import numpy as np

genres = ['FPS', 'RTS', 'Sports']

fps_data = [
    [58, 61, 59, 62, 70, 65, 56, 60, 63, 67],
    [72, 75, 73, 72, 76, 73, 78, 71, 79, 74],
    [66, 69, 71, 67, 65, 69, 70, 68, 72, 70]
]

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(fps_data, vert=False, patch_artist=True, notch=True, showmeans=True)

ax.set_xlabel('FPS', fontsize=12, labelpad=10)
ax.set_ylabel('Genres', fontsize=12, labelpad=10)

ax.set_yticks(np.arange(1, len(genres) + 1))
ax.set_yticklabels(genres, fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()