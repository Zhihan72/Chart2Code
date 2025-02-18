import matplotlib.pyplot as plt

# A single group of volunteering hours
volunteering_hours = [2, 4, 6, 8, 12, 14, 16, 18, 20, 25]  # Example group

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Generate vertical box plot
bp = ax.boxplot(volunteering_hours, vert=True, patch_artist=True, notch=False,
                meanline=False, showmeans=True, meanprops=dict(marker='s', markerfacecolor='cyan', markersize=10))

# Customizing the appearance of the box plots
bp['boxes'][0].set(facecolor='#66B3FF', alpha=0.5)

# Customize whiskers, caps, medians, means styles
for whisker in bp['whiskers']:
    whisker.set(color='darkred', linewidth=2, linestyle="-.")

for cap in bp['caps']:
    cap.set(color='darkred', linewidth=2)

for median in bp['medians']:
    median.set(color='green', linewidth=3)

for mean in bp['means']:
    mean.set(marker='s', markerfacecolor='cyan', markersize=10)

# Alter title and labels
ax.set_title('Volunteering Hours - Example Group', fontsize=18, fontweight='normal', pad=20)
ax.set_ylabel('Volunteering Hours', fontsize=14)
ax.set_xticklabels(['Example Group'], fontsize=13)

# Change grid style
ax.yaxis.grid(True, linestyle='-', alpha=0.3)

# Add legend
mean_legend = plt.Line2D([], [], color='cyan', marker='s', linestyle='None', markersize=10, label='Mean')
median_legend = plt.Line2D([], [], color='green', linestyle='-', linewidth=3, label='Median')
ax.legend(handles=[mean_legend, median_legend], loc='upper right')

plt.tight_layout()
plt.show()