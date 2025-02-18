import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

friends = ['Alice', 'Bob', 'Charlie']
alice_hours = [50, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 120]
bob_hours = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
charlie_hours = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
genres = ['RPG', 'FPS', 'MOBA', 'Sports', 'Puzzle']
alice_genres = [30, 25, 20, 15, 10]
bob_genres = [25, 30, 20, 10, 15]
charlie_genres = [20, 20, 30, 10, 20]

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(15, 8))

data = [alice_hours, bob_hours, charlie_hours]
box = ax2.boxplot(data, vert=True, patch_artist=True, labels=friends, showmeans=True)

new_colors = ['lightpink', 'lightblue', 'lightgreen']
for patch, color in zip(box['boxes'], new_colors):
    patch.set_facecolor(color)

ax2.set_title("Monthly Gaming Hours Distribution\nAmong Friends", fontsize=14, fontweight='bold')
ax2.set_xlabel("Friends", fontsize=12)
ax2.set_ylabel("Hours", fontsize=12)

plt.setp(box['whiskers'], color='black', linestyle='dotted', linewidth=1.5)
plt.setp(box['caps'], color='darkblue', linestyle='dashed', linewidth=1)
plt.setp(box['medians'], color='red', linewidth=2, linestyle='-.')
plt.setp(box['means'], marker='^', markerfacecolor='orange', markeredgecolor='black', markersize=8)

legend_elements = [Patch(facecolor=color, label=friend) for color, friend in zip(new_colors, friends)]
ax2.legend(handles=legend_elements, title='Friends', loc='upper right', fontsize=10)

X = np.arange(len(genres))
bar_width = 0.25
offset = bar_width * np.arange(len(friends))

ax1.bar(X + offset[0], alice_genres, width=bar_width, label='Alice', color=new_colors[0])
ax1.bar(X + offset[1], bob_genres, width=bar_width, label='Bob', color=new_colors[1])
ax1.bar(X + offset[2], charlie_genres, width=bar_width, label='Charlie', color=new_colors[2])

ax1.set_title("Favorite Gaming Genres\nAmong Friends", fontsize=14, fontweight='bold')
ax1.set_xlabel("Genres", fontsize=12)
ax1.set_ylabel("Percentage of Total Gaming Time", fontsize=12)
ax1.set_xticks(X + bar_width)
ax1.set_xticklabels(genres)

ax1.legend(title='Friends', fontsize=10)
ax1.grid(axis='y', linestyle='--', color='grey', linewidth=0.7)

plt.tight_layout()
plt.show()