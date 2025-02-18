import matplotlib.pyplot as plt

# Use a single group's data for a vertical box plot
volunteering_hours_single_group = [value for sublist in [
    [2, 4, 6, 8, 12, 14, 16, 18, 20, 25],  # Greenfield
    [3, 5, 7, 10, 11, 13, 15, 17, 21, 23], # Sunnydale
    [2, 4, 9, 11, 12, 15, 17, 18, 19, 22]  # Hillcrest
] for value in sublist]

fig, ax = plt.subplots(figsize=(8, 6))

# Plot a vertical single group boxplot
bp = ax.boxplot(volunteering_hours_single_group, vert=True, patch_artist=True, notch=False,
                meanline=True, showmeans=True, meanprops=dict(linestyle='-', linewidth=2, color='darkorange'))

# Set color for the box
single_color = '#99CCFF'
for patch in bp['boxes']:
    patch.set(facecolor=single_color, alpha=0.7)

# Set styles for whiskers, caps, medians, and means
for whisker in bp['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle="--")

for cap in bp['caps']:
    cap.set(color='gray', linewidth=1.5)

for median in bp['medians']:
    median.set(color='blue', linewidth=2)

for mean in bp['means']:
    mean.set(marker='o', markerfacecolor='darkorange', markersize=8)

ax.set_ylabel('Hours', fontsize=13)

plt.tight_layout()
plt.show()