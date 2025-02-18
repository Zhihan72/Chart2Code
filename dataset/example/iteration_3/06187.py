import matplotlib.pyplot as plt
import numpy as np

# Backstory: A fictional study on "Impact of City Noise Levels on Human Sleep Quality"
# Sleep quality index data from different neighborhoods in a city with varying noise levels

# Data representing sleep quality index (higher is better) in five different neighborhoods
neighborhood_a_sleep_quality = [75, 78, 80, 82, 76, 79, 83, 85, 77, 81, 82, 79]
neighborhood_b_sleep_quality = [68, 70, 65, 72, 74, 66, 67, 71, 69, 73, 70, 68]
neighborhood_c_sleep_quality = [55, 57, 60, 58, 54, 56, 53, 59, 61, 55, 57, 60]
neighborhood_d_sleep_quality = [45, 47, 50, 48, 44, 46, 43, 49, 51, 45, 47, 50]
neighborhood_e_sleep_quality = [30, 32, 35, 33, 29, 31, 28, 34, 36, 30, 32, 35]

# Combine data in a list
all_sleep_quality_data = [
    neighborhood_a_sleep_quality,
    neighborhood_b_sleep_quality,
    neighborhood_c_sleep_quality,
    neighborhood_d_sleep_quality,
    neighborhood_e_sleep_quality
]

# Labels for each neighborhood
neighborhood_labels = ["Neighborhood A", "Neighborhood B", "Neighborhood C", "Neighborhood D", "Neighborhood E"]

# Create the figure and axis object with subplots
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 8))

# Creating the boxplot
box = ax.boxplot(
    all_sleep_quality_data,
    patch_artist=True,
    notch=True,
    vert=True,
    labels=neighborhood_labels,
    widths=0.6
)

# Customizing the boxplot colors and appearance
colors = ['#FF6347', '#FFD700', '#32CD32', '#87CEFA', '#EE82EE']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

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

# Adding a legend for the boxplot colors
for label, color in zip(neighborhood_labels, colors):
    plt.plot([], [], color=color, label=label, linewidth=10)
plt.legend(title="Neighborhoods", loc='upper right')

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()