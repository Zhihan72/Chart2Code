import matplotlib.pyplot as plt
import numpy as np

# Backstory: The Health & Fitness Monitor Society wants to analyze the body mass index (BMI) distribution
# across different age groups to understand the prevalence of healthy, overweight, and obese categories.

# Define the age groups
age_groups = ['8-12', '13-17', '18-25', '26-35', '36-50', '51-65']

# Construct the BMI data for each age group (in kg/m^2)
# Data is constructed with consideration of known BMI statistics for different age groups
bmi_data = [
    [15, 16, 17, 18, 19, 20, 21, 22],          # Age 8-12
    [18, 20, 21, 22, 23, 24, 25, 27, 28],      # Age 13-17
    [19, 20, 22, 23, 24, 25, 26, 27, 29, 30],  # Age 18-25
    [22, 24, 26, 27, 28, 30, 32, 33],          # Age 26-35
    [25, 27, 29, 30, 32, 34, 35],              # Age 36-50
    [27, 28, 30, 32, 33, 34, 36, 38, 40]       # Age 51-65
]

# Create a Matplotlib figure
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Customize the plot title and overall layout
fig.suptitle("BMI Distribution Across Various Age Groups in 2023", fontsize=16, fontweight='bold', y=1.04)

# Create box plot on the first subplot
box = axs[0].boxplot(bmi_data, vert=False, patch_artist=True, labels=age_groups, notch=True)

# Apply custom colors to each box for better distinction
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize the box plot
axs[0].set_title("BMI Distribution", fontsize=14)
axs[0].set_xlabel("BMI (kg/m^2)")
axs[0].set_ylabel("Age Group")

# Add a custom grid
axs[0].grid(True, linestyle='--', alpha=0.6, axis='x')

# Add legend for the box plot
colors_legend = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
labels_legend = age_groups
axs[0].legend(colors_legend, labels_legend, title="Age Groups", loc='upper right', fontsize=10)

# Calculate the average BMI for each age group for the bar chart
average_bmi = [np.mean(bmi) for bmi in bmi_data]

# Create horizontal bar chart on the second subplot
bars = axs[1].barh(age_groups, average_bmi, color=colors, alpha=0.8, edgecolor='black')

# Annotate the bar chart with average values
for bar in bars:
    axs[1].text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2, f"{bar.get_width():.2f}", 
                va='center', ha='left', fontweight='bold')

# Customize the bar chart
axs[1].set_title("Average BMI Per Age Group", fontsize=14)
axs[1].set_xlabel("Average BMI (kg/m^2)")
axs[1].set_ylabel("Age Group")

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()