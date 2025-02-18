import matplotlib.pyplot as plt

# Quest durations for knights from different kingdoms
avalon = [30, 45, 40, 38, 60, 72, 55, 48, 63, 35]
camelot = [50, 65, 62, 58, 80, 95, 82, 75, 78, 67]
gondor = [45, 50, 55, 52, 48, 65, 60, 58, 53, 47]

# Combine data into a list for box plot
data = [avalon, camelot, gondor]

# Altered labels for the kingdoms
kingdoms = ['Gondor', 'Avalon', 'Camelot']

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create the boxplot
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, labels=kingdoms, widths=0.6)

# Customizing boxplot appearance
colors = ['#d6a0f6', '#9fc5e8', '#f9cb9c']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Styling whiskers, caps, and medians
for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=1.5, linestyle="--")
for cap in bp['caps']:
    cap.set(color='black', linewidth=1.5)
for median in bp['medians']:
    median.set(color='darkblue', linewidth=2)

# Adding grid, new title, and altered axis labels
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_title('Duration of Quests in the Middle Ages\nPer Kingdom', fontsize=14)
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Days on Quest', fontsize=12)

# Adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()