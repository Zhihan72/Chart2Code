import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

genres = ['FPS', 'RPG', 'RTS', 'Sports']

fps_data = [
    [61, 56, 70, 62, 67, 65, 58, 60, 63, 59],  # shuffled
    [50, 45, 49, 47, 54, 51, 48, 44, 53, 50],  # shuffled
    [72, 71, 78, 73, 75, 76, 74, 79, 72, 73],  # shuffled
    [69, 72, 70, 71, 66, 67, 70, 65, 69, 68]   # shuffled
]

fig, ax = plt.subplots(figsize=(10, 6))

ax.boxplot(fps_data, vert=False, patch_artist=True, notch=True, showmeans=True)

colors = ['#FF6347', '#4682B4', '#32CD32', '#B8860B']
for patch, color in zip(ax.boxplot(fps_data, vert=False)['boxes'], colors):
    patch = mpatches.PathPatch(patch.get_path(), color=color)
    patch.set_facecolor(color)

ax.set_yticks(np.arange(1, len(genres) + 1))
ax.set_yticklabels(genres, fontsize=10)

plt.show()