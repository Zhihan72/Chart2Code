import matplotlib.pyplot as plt

volunteering_hours = [2, 4, 6, 8, 12, 14, 16, 18, 20, 25]

fig, ax = plt.subplots(figsize=(8, 6))

# New color scheme for box plot
bp = ax.boxplot(volunteering_hours, vert=True, patch_artist=True, notch=False,
                meanline=False, showmeans=True, meanprops=dict(marker='o', markerfacecolor='orange', markersize=10))

# Applying new colors to the box plot components
bp['boxes'][0].set(facecolor='lightgreen', alpha=0.7)

for whisker in bp['whiskers']:
    whisker.set(color='purple', linewidth=2, linestyle="--")

for cap in bp['caps']:
    cap.set(color='purple', linewidth=2)

for median in bp['medians']:
    median.set(color='darkblue', linewidth=3)

for mean in bp['means']:
    mean.set(marker='o', markerfacecolor='orange', markersize=10)

ax.set_title('Volunteering Hours - Example Group', fontsize=18, fontweight='normal', pad=20)
ax.set_ylabel('Volunteering Hours', fontsize=14)
ax.set_xticklabels(['Example Group'], fontsize=13)

ax.yaxis.grid(True, linestyle='-', alpha=0.3)

mean_legend = plt.Line2D([], [], color='orange', marker='o', linestyle='None', markersize=10, label='Mean')
median_legend = plt.Line2D([], [], color='darkblue', linestyle='-', linewidth=3, label='Median')
ax.legend(handles=[mean_legend, median_legend], loc='upper right')

plt.tight_layout()
plt.show()