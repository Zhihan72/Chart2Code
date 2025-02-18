import matplotlib.pyplot as plt
import numpy as np

# Define the age groups
age_groups = ['8-12', '13-17', '18-25', '26-35', '36-50', '51-65']

# Construct the BMI data for each age group
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

# Create box plot without stylistic features
axs[0].boxplot(bmi_data, vert=False, labels=age_groups)

axs[0].set_xlabel("BMI (kg/m^2)")
axs[0].set_ylabel("Age Group")

# Calculate the average BMI for each age group for the bar chart
average_bmi = [np.mean(bmi) for bmi in bmi_data]

# Create horizontal bar chart without stylistic features
axs[1].barh(age_groups, average_bmi)

axs[1].set_xlabel("Average BMI (kg/m^2)")
axs[1].set_ylabel("Age Group")

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()