import matplotlib.pyplot as plt

# Neighborhoods and their corresponding volunteering hours
neighborhoods = ['Greenfield', 'Rivertown', 'Sunnydale', 'Hillcrest', 'Brookside']
volunteering_hours = [
    [2, 4, 6, 8, 12, 14, 16, 18, 20, 25],  # Greenfield
    [1, 3, 5, 10, 12, 14, 16, 19, 22],     # Rivertown
    [3, 5, 7, 10, 11, 13, 15, 17, 21, 23], # Sunnydale
    [2, 4, 9, 11, 12, 15, 17, 18, 19, 22], # Hillcrest
    [1, 5, 8, 10, 12, 14, 17, 18, 21]      # Brookside
]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Generate horizontal box plot with altered style elements
bp = ax.boxplot(volunteering_hours, vert=False, patch_artist=True, notch=False,
                meanline=False, showmeans=True, meanprops=dict(marker='s', markerfacecolor='cyan', markersize=10))

# Customizing the appearance of the box plots
colors = ['#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FF9999']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color, alpha=0.5)

# Customize whiskers, caps, medians, means with varied styles
for whisker in bp['whiskers']:
    whisker.set(color='darkred', linewidth=2, linestyle="-.")

for cap in bp['caps']:
    cap.set(color='darkred', linewidth=2)

for median in bp['medians']:
    median.set(color='green', linewidth=3)

for mean in bp['means']:
    mean.set(marker='s', markerfacecolor='cyan', markersize=10)

# Alter title and labels
ax.set_title('Community Volunteering Hours by Neighborhood', fontsize=18, fontweight='normal', pad=30)
ax.set_xlabel('Volunteering Hours', fontsize=14)
ax.set_yticklabels(neighborhoods, fontsize=13)

# Change grid style
ax.xaxis.grid(True, linestyle='-', alpha=0.3)

# Add legend with altered style
mean_legend = plt.Line2D([], [], color='cyan', marker='s', linestyle='None', markersize=10, label='Mean')
median_legend = plt.Line2D([], [], color='green', linestyle='-', linewidth=3, label='Median')
ax.legend(handles=[mean_legend, median_legend], loc='upper left')

plt.tight_layout()
plt.show()