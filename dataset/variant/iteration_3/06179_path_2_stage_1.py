import matplotlib.pyplot as plt
import numpy as np

# Define the age groups
age_groups = ['8-12', '13-17', '18-25', '26-35', '36-50', '51-65']

# Construct the BMI data for each age group (in kg/m^2)
bmi_data = [
    [15, 16, 17, 18, 19, 20, 21, 22],
    [18, 20, 21, 22, 23, 24, 25, 27, 28],
    [19, 20, 22, 23, 24, 25, 26, 27, 29, 30],
    [22, 24, 26, 27, 28, 30, 32, 33],
    [25, 27, 29, 30, 32, 34, 35],
    [27, 28, 30, 32, 33, 34, 36, 38, 40]
]

# Create a Matplotlib figure
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Create box plot on the first subplot
box = axs[0].boxplot(bmi_data, vert=False, patch_artist=True, notch=True)

# Apply custom colors to each box for better distinction
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add a custom grid
axs[0].grid(True, linestyle='--', alpha=0.6, axis='x')

# Calculate the average BMI for each age group for the bar chart
average_bmi = [np.mean(bmi) for bmi in bmi_data]

# Create horizontal bar chart on the second subplot
axs[1].barh(age_groups, average_bmi, color=colors, alpha=0.8, edgecolor='black')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()