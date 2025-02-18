import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

genres = ['FPS', 'RPG', 'RTS', 'Sports']

fps_data = [
    [58, 61, 59, 62, 70, 65, 56, 60, 63, 67],
    [44, 50, 47, 51, 49, 54, 45, 48, 53, 50],
    [72, 75, 73, 72, 76, 73, 78, 71, 79, 74],
    [66, 69, 71, 67, 65, 69, 70, 68, 72, 70]
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