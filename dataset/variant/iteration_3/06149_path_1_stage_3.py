import matplotlib.pyplot as plt

# Sleep hours for basketball athletes
basketball_sleep_hours = [7.5, 8, 8.1, 7.9, 8.3, 8, 7.8, 8.2, 8.3, 8.1, 7.9, 8, 7.5, 8, 8.2, 8.4, 8.6, 7.8, 8.1, 7.9]

# Create the box plot for a single group of data
fig, ax = plt.subplots(figsize=(6, 8))
single_color = 'blue'
ax.boxplot(basketball_sleep_hours, patch_artist=True,
           boxprops=dict(facecolor=single_color, color=single_color),
           whiskerprops=dict(color=single_color),
           capprops=dict(color=single_color),
           flierprops=dict(marker='o', color=single_color, markersize=8, alpha=0.6),
           medianprops=dict(color=single_color, linewidth=2))

# Set labels
ax.set_ylabel('Sleep Hours per Night', fontsize=12)
ax.set_xticklabels(['Basketball'], fontsize=11, fontweight='bold')

# Adjust layout and show plot
plt.tight_layout()
plt.show()