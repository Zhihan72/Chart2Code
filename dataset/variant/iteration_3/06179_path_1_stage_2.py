import matplotlib.pyplot as plt

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
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 7))

# Create vertical box plot
ax.boxplot(bmi_data, vert=True, labels=age_groups)

ax.set_xlabel("Age Group")
ax.set_ylabel("BMI (kg/m^2)")

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()