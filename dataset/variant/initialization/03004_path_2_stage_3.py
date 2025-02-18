import matplotlib.pyplot as plt
import numpy as np

# Define game genres excluding 'RPG: Role-Playing Game'
genres = ['FPS: First-Person Shooter', 'RTS: Real-Time Strategy', 'Sports Game']

# FPS data excluding RPG
fps_data = [
    [58, 61, 59, 62, 70, 65, 56, 60, 63, 67],
    [72, 75, 73, 72, 76, 73, 78, 71, 79, 74],
    [66, 69, 71, 67, 65, 69, 70, 68, 72, 70]
]

# Initiate a plot
fig, ax = plt.subplots(figsize=(10, 6))

# Generate horizontal box plots
boxplots = ax.boxplot(fps_data, vert=False, patch_artist=True, notch=True, showmeans=True)

# Define custom colors for box plot fill
colors = ['#66B2FF', '#FFCC99', '#FF9999']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

# Configure title and axis labels
ax.set_title('Frame Rate Analysis Across Game Genres\n(Frames Per Second - FPS)', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Frames Per Second (FPS)', fontsize=12, labelpad=10)
ax.set_ylabel('Game Genres', fontsize=12, labelpad=10)

# Customize y-tick labels
ax.set_yticks(np.arange(1, len(genres) + 1))
ax.set_yticklabels(genres, fontsize=10, fontweight='bold')

# Legend to explain color coding
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, [genre.split(':')[0] for genre in genres], title="Genre", loc='upper right', bbox_to_anchor=(1.15, 1), fontsize=10)

# Ensure layout is tight
plt.tight_layout()

# Display the plot
plt.show()