import matplotlib.pyplot as plt

# A single group of data
screen_time_6_12 = [120, 130, 110, 115, 145, 150, 100, 105, 140, 125]

fig, ax = plt.subplots(figsize=(6, 8))
box = ax.boxplot(screen_time_6_12, vert=True, patch_artist=True, notch=False, showmeans=True)

# Applying color to the box
colors = ['#ff5733']  # Single color since there's only one box
box['boxes'][0].set_facecolor(colors[0])

# Customize mean and median lines
box['means'][0].set(marker='D', color='blue', markersize=5)
box['medians'][0].set(color='red', linewidth=2)

# Set titles and labels
ax.set_title('Digital Time for Grade Schoolers', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Time (Hours/Month)', fontsize=12)
ax.set_xticklabels(['Grade Schoolers'], fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()