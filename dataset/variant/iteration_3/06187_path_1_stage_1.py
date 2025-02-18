import matplotlib.pyplot as plt

# Data representing sleep quality index in five different neighborhoods
all_sleep_quality_data = [
    [75, 78, 80, 82, 76, 79, 83, 85, 77, 81, 82, 79],
    [68, 70, 65, 72, 74, 66, 67, 71, 69, 73, 70, 68],
    [55, 57, 60, 58, 54, 56, 53, 59, 61, 55, 57, 60],
    [45, 47, 50, 48, 44, 46, 43, 49, 51, 45, 47, 50],
    [30, 32, 35, 33, 29, 31, 28, 34, 36, 30, 32, 35]
]

# Labels for each neighborhood
neighborhood_labels = ["Neighborhood A", "Neighborhood B", "Neighborhood C", "Neighborhood D", "Neighborhood E"]

# Create the figure and axis object
fig, ax = plt.subplots(figsize=(14, 8))

# Creating the boxplot
box = ax.boxplot(
    all_sleep_quality_data,
    patch_artist=True,
    notch=True,
    vert=True,
    labels=neighborhood_labels,
    widths=0.6
)

# Customizing the boxplot with a single color (e.g., 'skyblue')
single_color = 'skyblue'
for patch in box['boxes']:
    patch.set_facecolor(single_color)

# Customizing the medians, whiskers, caps, and fliers
plt.setp(box['medians'], color='darkblue', linewidth=2)
plt.setp(box['whiskers'], color='gray', linewidth=1.5, linestyle='-')
plt.setp(box['caps'], color='grey', linewidth=1.5)
plt.setp(box['fliers'], marker='o', color='black', alpha=0.5)

# Add title, labels, and grid for readability
ax.set_title("Impact of City Noise Levels on Human Sleep Quality\nA Neighborhood Analysis", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Neighborhood", fontsize=12)
ax.set_ylabel("Sleep Quality Index", fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Additional customization for tick labels
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()