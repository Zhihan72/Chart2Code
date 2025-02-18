import matplotlib.pyplot as plt
import numpy as np

art_movements = ['Impression', 'Deco', 'Minimal', 'Surreal']

influence_matrix = np.array([
    [7, 5, 3, 4, 6], 
    [4, 7, 5, 3, 6], 
    [3, 4, 9, 8, 5], 
    [5, 6, 4, 7, 8], 
])

avg_influence = np.mean(influence_matrix, axis=1)

fig, ax = plt.subplots(figsize=(10, 8))

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
bar = ax.barh(art_movements, avg_influence, color=colors, edgecolor=['#e0e0e0', '#c0c0c0', '#a0a0a0', '#808080'], )

ax.set_title("Avg Influence of Art Movements", fontsize=18, fontstyle='italic', pad=20)
ax.set_xlabel("Avg Influence", fontsize=13, labelpad=15, color='darkblue')
ax.set_ylabel("Art Movements", fontsize=13, labelpad=15, color='darkgreen')

for rect in bar:
    width = rect.get_width()
    ax.annotate(f'{width:.1f}',
                xy=(width, rect.get_y() + rect.get_height() / 2),
                xytext=(5, 0),  # adjusted for consistency
                textcoords="offset points",
                ha='left', va='center', fontsize=11, color='darkblue', fontstyle='italic')

# Add a legend with marker shapes to illustrate influence
ax.legend(['Light', 'Medium', 'Strong', 'Very Strong'], loc='lower right', title='Legend', fontsize=11, title_fontsize='13', markerscale=1.2)

# Add a grid for better readability
ax.xaxis.grid(True, color='grey', linestyle='--', linewidth=0.5)

plt.show()