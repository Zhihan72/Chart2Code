import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data collection for monthly gaming hours
friends = ['Alice', 'Bob', 'Charlie', 'Diana']

# Monthly gaming hours over the past year
alice_hours = [50, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 120]
bob_hours = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
charlie_hours = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
diana_hours = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

# Favorite gaming genres data
genres = ['RPG', 'FPS', 'MOBA', 'Sports', 'Puzzle']
alice_genres = [30, 25, 20, 15, 10]
bob_genres = [25, 30, 20, 10, 15]
charlie_genres = [20, 20, 30, 10, 20]
diana_genres = [15, 25, 25, 20, 15]

# Create figure and axes for subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

# Create stacked bar chart for favorite gaming genres
X = np.arange(len(genres))
bar_width = 0.2
offset = bar_width * np.arange(len(friends))

ax1.bar(X + offset[0], alice_genres, width=bar_width, label='Alice', color='lightcoral')
ax1.bar(X + offset[1], bob_genres, width=bar_width, label='Bob', color='lightblue')
ax1.bar(X + offset[2], charlie_genres, width=bar_width, label='Charlie', color='lightgreen')
ax1.bar(X + offset[3], diana_genres, width=bar_width, label='Diana', color='lightyellow')

ax1.set_title("Favorite Gaming Genres\nAmong Friends", fontsize=14, fontweight='bold')
ax1.set_xlabel("Genres", fontsize=12)
ax1.set_ylabel("Percentage of Total Gaming Time", fontsize=12)
ax1.set_xticks(X + bar_width)
ax1.set_xticklabels(genres)
ax1.legend(title='Friends', fontsize=10)

# Create box plot for monthly gaming hours
data = [alice_hours, bob_hours, charlie_hours, diana_hours]
box = ax2.boxplot(data, vert=True, patch_artist=True, labels=friends, showmeans=True)

# Customizing the box plot
colors = ['lightcoral', 'lightblue', 'lightgreen', 'lightyellow']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
ax2.set_title("Monthly Gaming Hours Distribution\nAmong Friends", fontsize=14, fontweight='bold')
ax2.set_xlabel("Friends", fontsize=12)
ax2.set_ylabel("Hours", fontsize=12)

# Customizing whiskers, caps, medians, and means
plt.setp(box['whiskers'], color='darkgrey', linewidth=1.5)
plt.setp(box['caps'], color='darkgreen', linewidth=1.5)
plt.setp(box['medians'], color='black', linewidth=2)
plt.setp(box['means'], marker='o', markerfacecolor='purple', markeredgecolor='black', markersize=8)

# Adding a legend to box plot manually
legend_elements = [Patch(facecolor=color, label=friend) for color, friend in zip(colors, friends)]
ax2.legend(handles=legend_elements, title='Friends', loc='upper left', fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Display the plots
plt.show()