import matplotlib.pyplot as plt
import numpy as np

# Daily coffee consumption data (cups per day)
young_adults_coffee = [2, 3, 2, 1, 4, 2, 3, 2, 3, 3]
adults_coffee = [3, 4, 3, 5, 4, 3, 4, 3, 5, 4]
middle_aged_coffee = [2, 3, 3, 2, 4, 3, 2, 4, 3, 3]
seniors_coffee = [1, 1, 2, 1, 2, 1, 1, 0, 2, 1]

monthly_avg_coffee = [np.mean(young_adults_coffee) * 30, 
                      np.mean(adults_coffee) * 30, 
                      np.mean(middle_aged_coffee) * 30, 
                      np.mean(seniors_coffee) * 30]

coffee_data = [young_adults_coffee, adults_coffee, middle_aged_coffee, seniors_coffee]
age_groups = ['Young Adults (20-29)', 'Adults (30-49)', 'Middle-Aged (50-64)', 'Seniors (65+)']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

boxes = axes[0].boxplot(coffee_data, vert=False, patch_artist=True, notch=True,
                        boxprops=dict(facecolor='#00CC99', color='black'),
                        whiskerprops=dict(color='black'),
                        capprops=dict(color='black'),
                        medianprops=dict(color='darkred'))

# New set of colors for the boxes
new_colors = ['#FF9999', '#FFCC99', '#FFFF99', '#99FF99']
for patch, color in zip(boxes['boxes'], new_colors):
    patch.set_facecolor(color)

axes[0].set_title("Caffeine Trends:\nDaily Coffee Consumption Across Age Groups", fontsize=14, weight='bold', pad=20)
axes[0].set_xlabel('Daily Coffee Consumption (cups)', fontsize=12)
axes[0].set_yticklabels(age_groups, fontsize=10)
axes[0].grid(True, linestyle='--', alpha=0.7)

bar_positions = np.arange(len(monthly_avg_coffee))
axes[1].barh(bar_positions, monthly_avg_coffee, color=new_colors)
axes[1].set_yticks(bar_positions)
axes[1].set_yticklabels(age_groups, fontsize=10)
axes[1].set_title("Monthly Average Coffee Consumption\nAcross Age Groups", fontsize=14, weight='bold', pad=20)
axes[1].set_xlabel('Monthly Coffee Consumption (cups)', fontsize=12)

for i, v in enumerate(monthly_avg_coffee):
    axes[1].text(v + 3, i, f"{int(v)} cups", color='black', va='center')

plt.tight_layout()
plt.show()