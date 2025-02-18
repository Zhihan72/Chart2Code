import matplotlib.pyplot as plt
import numpy as np

young_adults_coffee = [2, 3, 2, 1, 4, 2, 3, 2, 3, 3]
adults_coffee = [3, 4, 3, 5, 4, 3, 4, 3, 5, 4]
middle_aged_coffee = [2, 3, 3, 2, 4, 3, 2, 4, 3, 3]
seniors_coffee = [1, 1, 2, 1, 2, 1, 1, 0, 2, 1]

monthly_avg_coffee = [np.mean(young_adults_coffee) * 30, 
                      np.mean(adults_coffee) * 30, 
                      np.mean(middle_aged_coffee) * 30, 
                      np.mean(seniors_coffee) * 30]

coffee_data = [young_adults_coffee, adults_coffee, middle_aged_coffee, seniors_coffee]

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

boxes = axes[0].boxplot(coffee_data, vert=False, patch_artist=True, notch=True,
                        boxprops=dict(facecolor='skyblue', color='navy'),
                        whiskerprops=dict(color='navy', linestyle='-.'),
                        capprops=dict(color='navy', linestyle='-.'),
                        medianprops=dict(color='orange', linewidth=2),
                        flierprops=dict(marker='o', color='red', alpha=0.5))

new_colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']
for patch, color in zip(boxes['boxes'], new_colors):
    patch.set_facecolor(color)

axes[0].set_yticklabels(['Young Adults', 'Adults', 'Middle-Aged', 'Seniors'])
axes[0].grid(False)

# Retained horizontal bar chart style
bar_positions = np.arange(len(monthly_avg_coffee))
bars = axes[1].barh(bar_positions, monthly_avg_coffee, color=new_colors, edgecolor='black', linestyle='--', linewidth=1.5)
axes[1].set_yticks(bar_positions)
axes[1].set_yticklabels(['Young Adults', 'Adults', 'Middle-Aged', 'Seniors'])

# Alter border for subplots
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()