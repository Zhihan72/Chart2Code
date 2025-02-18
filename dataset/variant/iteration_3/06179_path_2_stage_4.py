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

# Using a single color for all bars in the bar chart
single_color = '#66b3ff'
average_bmi = [np.mean(bmi) for bmi in bmi_data]

# Change barh to bar for vertical bars
axs[0].bar(age_groups, average_bmi, color=single_color, alpha=0.8, edgecolor='black')

box = axs[1].boxplot(bmi_data, vert=False, patch_artist=True, notch=True)
for patch in box['boxes']:
    patch.set_facecolor(single_color)

axs[1].grid(True, linestyle='--', alpha=0.6, axis='x')

plt.tight_layout()
plt.show()