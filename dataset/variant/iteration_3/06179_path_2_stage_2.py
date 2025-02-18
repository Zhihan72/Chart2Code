import matplotlib.pyplot as plt
import numpy as np

age_groups = ['8-12', '13-17', '18-25', '26-35', '36-50', '51-65']

bmi_data = [
    [15, 16, 17, 18, 19, 20, 21, 22],
    [18, 20, 21, 22, 23, 24, 25, 27, 28],
    [19, 20, 22, 23, 24, 25, 26, 27, 29, 30],
    [22, 24, 26, 27, 28, 30, 32, 33],
    [25, 27, 29, 30, 32, 34, 35],
    [27, 28, 30, 32, 33, 34, 36, 38, 40]
]

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Using a single color for all boxes in the box plot
single_color = '#66b3ff'
box = axs[0].boxplot(bmi_data, vert=False, patch_artist=True, notch=True)
for patch in box['boxes']:
    patch.set_facecolor(single_color)

axs[0].grid(True, linestyle='--', alpha=0.6, axis='x')

average_bmi = [np.mean(bmi) for bmi in bmi_data]

# Using the same single color for the bar chart
axs[1].barh(age_groups, average_bmi, color=single_color, alpha=0.8, edgecolor='black')

plt.tight_layout()
plt.show()