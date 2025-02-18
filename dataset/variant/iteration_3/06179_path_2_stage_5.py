import matplotlib.pyplot as plt
import numpy as np

# Age groups to be used as labels on the x-axis
age_groups = ['8-12', '13-17', '18-25', '26-35', '36-50', '51-65']

# Shuffled BMI data within each age group, preserving the structure
bmi_data = [
    [18, 16, 21, 15, 22, 17, 19, 20],
    [28, 25, 24, 18, 27, 22, 21, 23, 20],
    [20, 23, 19, 29, 22, 30, 24, 26, 27, 25],
    [33, 32, 22, 28, 26, 27, 30, 24],
    [34, 35, 32, 29, 30, 25, 27],
    [38, 27, 36, 28, 30, 32, 34, 33, 40]
]

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Calculate average BMI for each group for the bar chart
average_bmi = [np.mean(bmi) for bmi in bmi_data]

# Bar chart using average BMI values
axs[0].bar(age_groups, average_bmi, color='#66b3ff', alpha=0.8, edgecolor='black')

# Box plot using shuffled bmi_data
box = axs[1].boxplot(bmi_data, vert=False, patch_artist=True, notch=True)
for patch in box['boxes']:
    patch.set_facecolor('#66b3ff')

axs[1].grid(True, linestyle='--', alpha=0.6, axis='x')

plt.tight_layout()
plt.show()