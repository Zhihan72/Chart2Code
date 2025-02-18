import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Comparing hydration levels (as percentage of body weight) across different age groups (Teens, Young Adults, Adults, Seniors) in a community
# The study aims to observe hydration variability within and across these groups, conducted over several months.

# Data for hydration levels (as percentage of body weight) across different age groups
teens_hydration = [66, 67, 68, 65, 70, 69, 68, 67, 66, 69]
young_adults_hydration = [60, 62, 61, 59, 63, 64, 62, 61, 60, 63]
adults_hydration = [55, 56, 58, 54, 57, 56, 55, 58, 54, 57]
seniors_hydration = [50, 52, 51, 49, 53, 54, 51, 50, 49, 53]

# Aggregate the data into a list of lists
data = [teens_hydration, young_adults_hydration, adults_hydration, seniors_hydration]

# Labels for the age groups
age_groups = ["Teens", "Young Adults", "Adults", "Seniors"]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create the box plot
boxplot = ax.boxplot(data, patch_artist=True, vert=True, labels=age_groups, notch=True, widths=0.6)

# Adding custom colors for the boxes to differentiate age groups
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Customizing whiskers, caps, medians, and outliers
plt.setp(boxplot['whiskers'], color='gray', linewidth=1.5, linestyle="--")
plt.setp(boxplot['caps'], color='black', linewidth=1.5)
plt.setp(boxplot['medians'], color='blue', linewidth=2)
plt.setp(boxplot['fliers'], marker='o', color='red', alpha=0.6)

# Adding title and labels
ax.set_title("Hydration Levels Across Different Age Groups\n(As a Percentage of Body Weight)", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Hydration Level (%)", fontsize=14)
ax.set_xlabel("Age Groups", fontsize=14)

# Adding a grid for better visual comparison
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Highlighting medians with annotations
for i, median in enumerate(boxplot['medians']):
    x_median = median.get_xdata()[1]
    y_median = median.get_ydata()[1]
    ax.annotate(f'{y_median:.0f}%', xy=(x_median, y_median), xytext=(0, 10),
                textcoords='offset points', color='blue', fontsize=10, ha='center')

# Ensure no overlap and improve layout
plt.tight_layout()

# Display the chart
plt.show()