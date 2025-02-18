import matplotlib.pyplot as plt
import numpy as np

# Data for hydration levels as percentage of body weight across different age groups
teens_hydration = [66, 67, 68, 65, 70, 69, 68, 67, 66, 69]
young_adults_hydration = [60, 62, 61, 59, 63, 64, 62, 61, 60, 63]
adults_hydration = [55, 56, 58, 54, 57, 56, 55, 58, 54, 57]
seniors_hydration = [50, 52, 51, 49, 53, 54, 51, 50, 49, 53]

data = [teens_hydration, young_adults_hydration, adults_hydration, seniors_hydration]
age_groups = ["Teens", "Young Adults", "Adults", "Seniors"]

fig, ax = plt.subplots(figsize=(12, 8))

# Create the horizontal box plot
boxplot = ax.boxplot(data, patch_artist=True, vert=False, labels=age_groups, notch=True, widths=0.6)

# Apply a single color to all box plots
single_color = '#66B3FF'
for patch in boxplot['boxes']:
    patch.set_facecolor(single_color)
    patch.set_alpha(0.7)

# Customizing whiskers, caps, medians, and outliers
plt.setp(boxplot['whiskers'], color='gray', linewidth=1.5, linestyle="--")
plt.setp(boxplot['caps'], color='black', linewidth=1.5)
plt.setp(boxplot['medians'], color='blue', linewidth=2)
plt.setp(boxplot['fliers'], marker='o', color='red', alpha=0.6)

ax.set_title("Hydration Levels Across Different Age Groups\n(As a Percentage of Body Weight)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Hydration Level (%)", fontsize=14)
ax.set_ylabel("Age Groups", fontsize=14)

ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

for i, median in enumerate(boxplot['medians']):
    y_median = median.get_ydata()[1]
    x_median = median.get_xdata()[0]
    ax.annotate(f'{x_median:.0f}%', xy=(x_median, y_median), xytext=(10, 0),
                textcoords='offset points', color='blue', fontsize=10, va='center')

plt.tight_layout()
plt.show()