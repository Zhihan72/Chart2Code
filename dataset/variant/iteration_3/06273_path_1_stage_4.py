import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

friends = ['Alice', 'Bob', 'Charlie', 'Diana']
alice_hours = [50, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 120]
bob_hours = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
charlie_hours = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
diana_hours = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

genres = ['RPG', 'FPS', 'MOBA', 'Sports', 'Puzzle']
alice_genres = [30, 25, 20, 15, 10]
bob_genres = [25, 30, 20, 10, 15]
charlie_genres = [20, 20, 30, 10, 20]
diana_genres = [15, 25, 25, 20, 15]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

# Multiple colors for different groups
colors = ['lightsalmon', 'lightgreen', 'lightblue', 'plum']

# Create grouped bar chart
X = np.arange(len(genres))
bar_width = 0.2

ax1.bar(X, alice_genres, width=bar_width, label='Alice', color=colors[0], hatch='/')
ax1.bar(X + bar_width, bob_genres, width=bar_width, label='Bob', color=colors[1], hatch='\\')
ax1.bar(X + 2 * bar_width, charlie_genres, width=bar_width, label='Charlie', color=colors[2], hatch='-')
ax1.bar(X + 3 * bar_width, diana_genres, width=bar_width, label='Diana', color=colors[3], hatch='x')

ax1.set_title("Favorite Gaming Genres", fontsize=14, fontweight='bold')
ax1.set_xlabel("Genres", fontsize=12)
ax1.set_ylabel("Percentage of Total Gaming Time", fontsize=12)
ax1.set_xticks(X + 1.5 * bar_width)
ax1.set_xticklabels(genres)
ax1.legend(loc='upper right', fontsize=10)

# Create box plot
data = [alice_hours, bob_hours, charlie_hours, diana_hours]
box = ax2.boxplot(data, vert=True, patch_artist=True, labels=friends, showmeans=True)

# Different colors for each box
colors_box = ['mistyrose', 'honeydew', 'lavender', 'thistle']
for i, patch in enumerate(box['boxes']):
    patch.set_facecolor(colors_box[i])

ax2.set_title("Monthly Gaming Hours Distribution", fontsize=14, fontweight='bold')
ax2.set_xlabel("Friends", fontsize=12)
ax2.set_ylabel("Hours", fontsize=12)

# Customizing whiskers, caps, medians, and means; altering styles
plt.setp(box['whiskers'], color='navy', linestyle='dashed', linewidth=1.5)
plt.setp(box['caps'], color='darkorange', linestyle=':', linewidth=1.5)
plt.setp(box['medians'], color='crimson', linestyle='-', linewidth=2)
plt.setp(box['means'], marker='D', markerfacecolor='gold', markeredgecolor='black', markersize=8)

# Adding grid and removing border lines for aesthetic purpose
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()