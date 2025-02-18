import matplotlib.pyplot as plt
import numpy as np

regions = ['N', 'S', 'E', 'W']
reusable_bags = [1200, 950, 1100, 800]
solar_chargers = [750, 850, 920, 700]
bamboo_toothbrushes = [530, 610, 720, 580]
eco_water_bottles = [1020, 870, 990, 760]

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.2
y_pos = np.arange(len(regions))

colors = ['#e7298a', '#1b9e77', '#d95f02', '#7570b3']

ax.barh(y_pos - 1.5 * bar_width, reusable_bags, bar_width, label='Bags', color=colors[0], hatch='/')
ax.barh(y_pos - 0.5 * bar_width, solar_chargers, bar_width, label='Chargers', color=colors[1], hatch='\\')
ax.barh(y_pos + 0.5 * bar_width, bamboo_toothbrushes, bar_width, label='Brushes', color=colors[2], hatch='.')
ax.barh(y_pos + 1.5 * bar_width, eco_water_bottles, bar_width, label='Bottles', color=colors[3], hatch='x')

ax.set_yticks(y_pos)
ax.set_yticklabels(regions, fontsize=12)
ax.set_xlabel('Units', fontsize=12)
ax.set_title('EcoTrendz Campaign Q1 2023', fontsize=14, fontweight='bold', pad=20)

# Changed legend location and added shadow
ax.legend(title='Products', loc='lower center', fontsize=10, shadow=True)

# Modified grid to show on y-axis with different style
plt.grid(visible=True, which='major', axis='y', linestyle='-.', linewidth=0.7, color='blue', alpha=0.6)

# Added different border style to the axes
ax.spines['top'].set_linestyle('dotted')
ax.spines['right'].set_linestyle('dashed')
ax.spines['bottom'].set_linestyle('solid')
ax.spines['left'].set_linestyle('dashdot')

for i in range(len(regions)):
    ax.text(reusable_bags[i] + 10, i - 1.5 * bar_width, str(reusable_bags[i]), va='center', color='black', fontsize=10)
    ax.text(solar_chargers[i] + 10, i - 0.5 * bar_width, str(solar_chargers[i]), va='center', color='black', fontsize=10)
    ax.text(bamboo_toothbrushes[i] + 10, i + 0.5 * bar_width, str(bamboo_toothbrushes[i]), va='center', color='black', fontsize=10)
    ax.text(eco_water_bottles[i] + 10, i + 1.5 * bar_width, str(eco_water_bottles[i]), va='center', color='black', fontsize=10)

plt.tight_layout()
plt.show()