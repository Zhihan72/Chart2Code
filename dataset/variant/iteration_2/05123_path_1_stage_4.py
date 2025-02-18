import matplotlib.pyplot as plt
import numpy as np

age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
happiness_data = [
    [7, 8, 7, 6, 8, 8, 7, 9, 7, 6, 7, 8, 7, 8, 7],
    [6, 7, 6, 6, 7, 7, 6, 6, 6, 7, 6, 6, 5, 6, 6],
    [5, 6, 5, 6, 6, 5, 6, 6, 5, 5, 5, 5, 5, 6, 5],
    [6, 6, 5, 4, 5, 6, 5, 4, 4, 5, 6, 5, 4, 5, 5],
    [7, 6, 7, 6, 7, 7, 7, 6, 6, 7, 8, 7, 8, 7, 7]
]

fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal boxplot without stylistic elements
box = ax.boxplot(happiness_data, vert=False, patch_artist=True, notch=True, meanline=True, showmeans=True)

new_colors = ['#FF4500', '#32CD32', '#4682B4', '#800080', '#FF69B4']
for patch, color in zip(box['boxes'], new_colors):
    patch.set_facecolor(color)

plt.setp(box['means'], color='blue')
plt.setp(box['medians'], color='red')

# Scatter plot of medians for horizontal boxplot
medians = [np.median(group) for group in happiness_data]
ax.scatter(medians, range(1, len(age_groups) + 1), color='purple', marker='D', zorder=3)

ax.set_yticklabels(age_groups)

# Remove grid, axis background, and borders
ax.set_facecolor('white')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()