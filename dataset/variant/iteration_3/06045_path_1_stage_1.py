import matplotlib.pyplot as plt
import numpy as np

# Monthly running distance data (in km) for each type of athlete
amateur_distances = [30, 45, 50, 60, 35, 40, 50, 55, 45, 50, 60, 55]
semi_pro_distances = [70, 80, 85, 90, 75, 80, 85, 95, 90, 85, 90, 95]
professional_distances = [100, 110, 115, 120, 105, 110, 115, 125, 120, 115, 120, 125]
marathoner_distances = [200, 210, 220, 230, 205, 210, 220, 230, 220, 215, 220, 230]
sprinter_distances = [60, 70, 75, 80, 65, 70, 75, 85, 80, 75, 80, 85]

# Group all distance data into a list for plotting
all_distances = [
    amateur_distances,
    semi_pro_distances,
    professional_distances,
    marathoner_distances,
    sprinter_distances
]

# Athlete labels for the box plot
athlete_labels = ["Amateur", "Semi-Professional", "Professional", "Marathoner", "Sprinter"]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Plot the boxplots
box = ax.boxplot(all_distances, labels=athlete_labels, patch_artist=True, notch=True, vert=True, showmeans=True)

# Customize the box plots with different colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CC99FF']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize plot elements
ax.set_xlabel("Types of Athletes", fontsize=14)
ax.set_ylabel("Running Distance (km)", fontsize=14)

# Further customize the box plots
for element in ['whiskers', 'caps', 'medians', 'means']:
    plt.setp(box[element], color='black')
plt.setp(box['fliers'], marker='o', color='red', markersize=5, alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()