import matplotlib.pyplot as plt

# Altered group of data
screen_time_6_12 = [130, 110, 115, 145, 120, 150, 105, 140, 125, 100]

fig, ax = plt.subplots(figsize=(7, 7))
box = ax.boxplot(screen_time_6_12, vert=True, patch_artist=True, notch=False, showmeans=True)

# Apply different color to the box
colors = ['#33ffad']
box['boxes'][0].set_facecolor(colors[0])

# Customize mean and median lines with different styles
box['means'][0].set(marker='o', color='magenta', markersize=7)
box['medians'][0].set(color='green', linewidth=3)

# Set titles and labels
ax.set_title('Screen Time for Students', fontsize=14, style='italic')
ax.set_ylabel('Hours (Per Month)', fontsize=11)
ax.set_xticklabels(['Students'], fontsize=9)

# Modify grid style
ax.yaxis.grid(True, linestyle='-.', alpha=0.5)

# Adjust border style
for spine in ax.spines.values():
    spine.set_edgecolor('grey')
    spine.set_linewidth(2)

plt.tight_layout()
plt.show()